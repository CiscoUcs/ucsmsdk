# Copyright 2013 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module is responsible for event handling of the events exposed by
UCSM server.
"""

from __future__ import print_function

from six.moves import queue


from threading import Condition, Lock, Thread
import datetime
import logging
import time

from . import ucsmo
from . import ucscoreutils
from . import ucsxmlcodec as xc
from .ucsexception import UcsWarning
from .ucsexception import UcsValidationException

log = logging.getLogger('ucs')


class MoChangeEvent(object):
    """
    This class provides structure to save an event generated for any change,
    its associated managed object and property change list.
    This functionality is used during add_event_handler.
    """

    def __init__(self, event_id=None, mo=None, change_list=None):
        self.event_id = event_id
        self.mo = mo
        self.change_list = change_list


class WatchBlock(object):
    """
    This class handles the functionality about the Event Handling/Watch block.
    enqueue/dequeue fuctionality of events is handled by this class.
    This functionality is used during add_event_handler.
    """

    def __init__(self, params, fmce, capacity, callback):
        self.fmce = fmce
        self.callback = callback
        self.capacity = capacity
        self.params = params
        self.overflow = False
        self.error_code = 0
        self.event_q = queue.Queue()  # infinite size Queue

    def dequeue(self, miliseconds_timeout):
        """Internal method to dequeue the events."""
        while True:
            if self.error_code != 0:
                log.debug("queue error:" + str(self.error_code))
                return None
            if not self.event_q.empty():
                mo_chg_event = self.event_q.get_nowait()
                return mo_chg_event
            else:
                return None

    def enqueue(self, cmce):
        """Internal method to enqueue the events."""
        if self.event_q.maxsize < self.capacity:
            self.event_q.put(cmce)
        else:
            self.overflow = True

    def queue_size(self):
        return self.event_q.qsize()

    def dequeue_default_callback(self, mce):
        """Default callback method."""
        tab_size = 8
        print("\n")
        print('EventId'.ljust(tab_size * 2) + ':' + str(mce.event_id))
        print('ChangeList'.ljust(tab_size * 2) + ':' + str(mce.change_list))
        print('ClassId'.ljust(tab_size * 2) + ':' + str(mce.mo.get_class_id()))
        print('MoDn'.ljust(tab_size * 2) + ':' + str(mce.mo.dn))


class UcsEventHandle(object):
    """This class provides api to add and remove event handler."""

    def __init__(self, handle):
        self._handle = handle
        self._lock_object = None
        self._wbs = []
        self._wbs_lock = Lock()
        self._enqueue_thread = None
        self._condition = Condition()
        self._event_chan_resp = None
        self._dequeue_thread = None
        self._lowest_timeout = None
        self._wb_to_remove = []

    def _process_method_vessel(self, root, elems):
        for in_stimuli in root:
            for cmce in in_stimuli:
                for in_config in cmce:
                    for mo_elem in in_config:
                        elems.append(
                            (mo_elem, cmce.attrib.get('inEid')))
        return elems

    def _process_mo_change_event(self, root, elems):
        for in_config in root:
            for mo_elem in in_config:
                elems.append(mo_elem)
        return elems

    def _get_mo_elem(self, xml_str):
        """
        Internal method to extract mo elements from xml string
        """

        root = xc.extract_root_elem(xml_str)
        mo_elems = []
        if root.tag == "methodVessel":
            mo_elems = self._process_method_vessel(root, mo_elems)
        elif root.tag == "configMoChangeEvent":
            mo_elems = self._process_mo_change_event(root, mo_elems)
        return mo_elems

    def _can_enqueue(self):
        return self._event_chan_resp and len(
            self._wbs) and (
            self._handle.cookie is not None)

    def _notify_to_dequeue(self):
        with self._condition:
            self._condition.notify()

    def _process_event_channel_resp(self, resp):
        enqueued = False

        for mo_elem in self._get_mo_elem(resp):
            gmo = ucsmo.generic_mo_from_xml_elem(mo_elem[0])
            mce = MoChangeEvent(event_id=mo_elem[1],
                                mo=gmo.to_mo(),
                                change_list=gmo.properties.keys())

            for watch_block in self._wbs:
                if watch_block.fmce(mce):
                    watch_block.enqueue(mce)
                    enqueued = True

        if enqueued:
            self._notify_to_dequeue()

    def _enqueue_function(self):
        """
        Internal method used by add_event_handler.
        Provides functionality of enqueue/dequeue of the events and
        triggering callbacks.
        """

        try:
            xml_query = '<eventSubscribe cookie="%s"/>' % self._handle.cookie
            self._event_chan_resp = self._handle.post_xml(
                xml_str=xml_query.encode(), read=False)
        except Exception:
            raise

        try:
            while self._can_enqueue():
                resp = self._event_chan_resp.readline()
                resp = self._event_chan_resp.read(int(resp))
                self._process_event_channel_resp(resp)

            if len(self._wbs) == 0:
                self._condition.acquire()
                self._condition.notify()
                self._condition.release()
        except:
            raise

    def _thread_enqueue_start(self):
        """
        Internal method to start the enqueue thread which adds the events in
        an internal queue.
        """

        self._enqueue_thread = Thread(name="enqueue_thread",
                                      target=self._enqueue_function)
        self._enqueue_thread.daemon = True
        self._enqueue_thread.start()

    def _time_left(self, watch_block):
        timeout_sec = watch_block.params["timeout_sec"]
        start_time = watch_block.params["start_time"]
        time_diff = datetime.datetime.now() - start_time
        if time_diff.seconds < timeout_sec:
            return timeout_sec - time_diff.seconds
        else:
            return 0
        # return 2147483647

    def _dequeue_mce(self, time_left, watch_block):
        if time_left and time_left > 0:
            if self._lowest_timeout is None or \
                    self._lowest_timeout > time_left:
                self._lowest_timeout = time_left
            mce = watch_block.dequeue(time_left)
        else:
            mce = watch_block.dequeue(2147483647)

        return mce

    def _get_ucs_prop_name(self, mo, python_prop):
        if isinstance(mo, ucsmo.GenericMo):
            return python_prop
        elif python_prop in mo.prop_meta:
            # return the Ucs equivalent of this property
            # so `usr_lbl` will be returned as `usrLbl`
            return mo.prop_meta[python_prop].xml_attribute
        else:
            # we do not know about this property
            # return the same back - no other option
            return python_prop

    def _get_prop_value(self, mo, python_prop):
        if isinstance(mo, ucsmo.GenericMo):
            return mo.properties[python_prop]
        elif python_prop in mo.prop_meta:
            return getattr(mo, python_prop)
        elif python_prop in vars(mo):
            # we do not know about this property
            # but the property seems to be available
            # in the mo. so return mo[prop]
            return getattr(mo, python_prop)
        else:
            # Not sure what we can do!!
            return None

    def _should_skip_prop_match(self, prop, change_list):
        # if prop is not a part of change_list
        # skip processing the property
        return change_list and prop not in change_list

    def _is_property_in_success_values(self, value, success_values):
        return len(success_values) > 0 and (value in success_values)

    def _prop_val_match(self, mo, prop, success_values,
                        change_list=None):
        ucs_prop = self._get_ucs_prop_name(mo, prop)
        prop_val = self._get_prop_value(mo, prop)

        if self._should_skip_prop_match(ucs_prop, change_list):
            return False

        return self._is_property_in_success_values(prop_val, success_values)

    def _invoke_callback_and_set_done(self, wb, mce):
        if wb.callback:
            ctxt = wb.params['context']
            if ctxt:
                ctxt["done"] = True
            wb.callback(mce)

    def _dequeue_mo_prop_poll(self, mo, prop, poll_sec, watch_block,
                              timeout_sec=None, time_left=None):

        success_value = watch_block.params["success_value"]

        if not success_value or len(success_value) < 1:
            raise ValueError("success_value is missing.")

        pmo = self._handle.query_dn(mo.dn)
        if pmo is None:
            UcsWarning('Mo ' + pmo.dn + ' not found.')
            return

        if timeout_sec is not None and time_left is not None and time_left > 0:
            if time_left < poll_sec:
                poll_sec = timeout_sec - time_left

        if self._lowest_timeout is None or self._lowest_timeout > poll_sec:
            self._lowest_timeout = poll_sec

        if self._prop_val_match(pmo, prop, success_value):
            mce = MoChangeEvent(mo=pmo)
            self._invoke_callback_and_set_done(watch_block, mce)
            self._wb_to_remove.append(watch_block)

    def _dequeue_mo_prop_event(self, prop, watch_block, time_left=None):

        success_value = watch_block.params["success_value"]

        if not success_value or len(success_value) < 1:
            raise ValueError("success_value is missing.")

        # dequeue mce
        mce = self._dequeue_mce(time_left, watch_block)
        if mce is None:
            return

        # checks if prop value exist in success value(s)
        attributes = mce.change_list
        if self._prop_val_match(mce.mo, prop, success_value, attributes):
            self._invoke_callback_and_set_done(watch_block, mce)
            self._wb_to_remove.append(watch_block)

    def _dequeue_mo_until_removed(self, watch_block, time_left=None):

        # dequeue mce
        mce = self._dequeue_mce(time_left, watch_block)
        if mce is None:
            return

        if watch_block.callback is not None:
            watch_block.callback(mce)

        # watch mo until gets deleted
        if mce.mo.status == "deleted":
            self._wb_to_remove.append(watch_block)

    def _dequeue_all_class_id(self, watch_block, time_left=None):

        # dequeue mce
        mce = self._dequeue_mce(time_left, watch_block)
        if mce is not None and watch_block.callback is not None:
            watch_block.callback(mce)

    def _dequeue_function(self):
        """
        Internal method to dequeue to events.
        """
        while len(self._wbs):
            self._lowest_timeout = None
            self._wb_to_remove = []

            try:
                for watch_block in self._wbs:
                    mo = watch_block.params["managed_object"]
                    prop = watch_block.params["prop"]
                    poll_sec = watch_block.params["poll_sec"]
                    timeout_sec = watch_block.params["timeout_sec"]

                    # checks if watch_block is not timed out, else remove
                    time_left = None
                    if timeout_sec is not None:
                        time_left = self._time_left(watch_block)
                        if time_left <= 0:
                            self._wb_to_remove.append(watch_block)
                            continue
                    if self._lowest_timeout is None:
                        self._lowest_timeout = time_left
                    elif self._lowest_timeout < time_left:
                        self._lowest_timeout = time_left


                    # Dequeue any change events for a specified watch_block
                    # poll for mo. Not to monitor event.
                    if poll_sec is not None and mo is not None:
                        self._dequeue_mo_prop_poll(mo, prop, poll_sec,
                                                   watch_block, timeout_sec,
                                                   time_left)
                    elif mo is not None:
                        while watch_block.queue_size() > 0:
                            # watch mo until prop_val changed to desired value
                            if prop is not None:
                                self._dequeue_mo_prop_event(prop, watch_block,
                                                            time_left)
                            # watch mo until it is removed
                            else:
                                self._dequeue_mo_until_removed(watch_block,
                                                               time_left)
                    elif mo is None:
                        while watch_block.queue_size() > 0:
                            # watch all event or specific to class_id
                            self._dequeue_all_class_id(watch_block, time_left)
            except Exception as e:
                log.info(str(e))
                self._wb_to_remove.append(watch_block)

            # remove any watch blocks in to_remove list
            self._process_wb_remove_list()

            # wait for more events only if watch_block exists
            if len(self._wbs):
                with self._condition:
                    self._condition.wait(self._lowest_timeout)
        return

    def _process_wb_remove_list(self):
        if len(self._wb_to_remove) == 0:
            return

        self._wbs_lock.acquire()

        for wb in self._wb_to_remove:
            if "context" in wb.params:
                ctxt = wb.params['context']
                if ctxt:
                    ctxt["done"] = True
            self.watch_block_remove(wb)
        self._wb_to_remove = []

        self._wbs_lock.release()

    def _thread_dequeue_start(self):
        """
        Internal method to start dequeue thread.
        """

        self._dequeue_thread = Thread(name="dequeue_thread",
                                      target=self._dequeue_function)
        self._dequeue_thread.daemon = True
        self._dequeue_thread.start()

    def watch_block_add(self, params,
                        filter_callback,
                        capacity=500,
                        callback=None):
        """
        Internal method to add a watch block for starting event monitoring.
        """

        if self._handle.cookie is None:
            return None

        self._wbs_lock.acquire()
        watch_block = WatchBlock(params,
                                 filter_callback,
                                 capacity,
                                 callback)  # Add a List of Watchers

        if watch_block is not None and watch_block.callback is None:
            watch_block.callback = watch_block.dequeue_default_callback

        self._wbs.append(watch_block)
        self._wbs_lock.release()
        return watch_block

    def watch_block_remove(self, watch_block):
        """
        Internal method to remove a watch block for
        stopping event monitoring.
        """
        if watch_block in self._wbs:
            self._wbs.remove(watch_block)

    def _add_class_id_watch(self, class_id):
        if ucscoreutils.find_class_id_in_mo_meta_ignore_case(class_id) is None:
            raise UcsValidationException(
                "Invalid ClassId %s specified." % class_id)

        def watch__type_filter(mce):
            """
            Callback method to work on events with a specific class_id.
            """
            if mce.mo.get_class_id().lower() == class_id.lower():
                return True
            return False

        return watch__type_filter

    def _add_mo_watch(self, managed_object, prop=None, success_value=[],
                      poll_sec=None):
        if ucscoreutils.find_class_id_in_mo_meta_ignore_case(
                managed_object.get_class_id()) is None:
            raise UcsValidationException(
                "Unknown ClassId %s provided." %
                managed_object.get_class_id())

        if prop is not None:
            mo_property_meta = ucscoreutils.get_mo_property_meta(
                managed_object.get_class_id(), prop)
            if mo_property_meta is None:
                raise UcsValidationException(
                    "Unknown Property %s provided." % prop)

            if not success_value:
                raise UcsValidationException(
                    "success_value parameter is not provided.")

        if poll_sec is None:
            def watch_mo_filter(mce):
                """
                Callback method to work on events specific to respective
                managed object.
                """
                if mce.mo.dn == managed_object.dn:
                    return True
                return False
            return watch_mo_filter
        else:
            def watch_none_filter(mce):
                """
                Callback method to ignore all events.
                """
                return False
            return watch_none_filter

    def add(self,
            class_id=None,
            managed_object=None,
            prop=None,
            success_value=[],
            poll_sec=None,
            timeout_sec=None,
            call_back=None,
            context=None):
        """
        Adds an event handler.

        An event handler can be added using this method where an user can
        subscribe for the event channel from UCS and can monitor those events
        for any specific success value for a managed object.

        Args:
            class_id (str): managed object class id
            managed_object (ManagedObject)
            prop (str) - property of the managed object to monitor
            success_value (list) - success values of a prop
            poll_sec - specifies the time in seconds for polling event.
            timeout_sec - time after which method should stop monitoring.
            call_back - call back method
        """

        if class_id is not None and managed_object is not None:
            raise UcsValidationException(
                "Specify either class_id or managedObject, not both")

        if class_id is not None:
            filter_callback = self._add_class_id_watch(class_id)
        elif managed_object is not None:
            filter_callback = self._add_mo_watch(managed_object, prop,
                                                 success_value, poll_sec)
        else:
            def watch_all_filter(mce):
                """
                Callback method to work on all events.
                """
                return True
            filter_callback = watch_all_filter

        param_dict = {'class_id': class_id,
                      'managed_object': managed_object,
                      'prop': prop,
                      'success_value': success_value,
                      'poll_sec': poll_sec,
                      'timeout_sec': timeout_sec,
                      'call_back': call_back,
                      'start_time': datetime.datetime.now(),
                      'context': context}

        if filter_callback is None:
            raise UcsValidationException("Error adding WatchBlock...")

        watch_block = self.watch_block_add(params=param_dict,
                                           filter_callback=filter_callback,
                                           callback=call_back)

        if watch_block is not None and len(self._wbs) == 1:
            if poll_sec is None:
                self._thread_enqueue_start()
            self._thread_dequeue_start()

        return watch_block

    def remove(self, watch_block):
        """
        Removes an event handler.
        """

        self._wbs_lock.acquire()
        if watch_block in self._wbs:
            self.watch_block_remove(watch_block)
        else:
            UcsWarning("Event handler not found")
        self._wbs_lock.release()

    def clean(self):
        """
        Removes all the watch blocks from the event handler
        """

        self._wbs_lock.acquire()
        for each in self._wbs:
            self.watch_block_remove(each)
        self._wbs_lock.release()

    def get(self):
        """
        Returns the list of event handlers.
        """
        return self._wbs


def wait(handle, mo, prop, value, cb, timeout_sec=None, poll_sec=None):
    """
    Waits for `mo.prop == value`

    Args:
        handle(UcsHandle): connection handle to the server
        mo (Managed Object): managed object to watch
        prop (str): property to watch
        value (str): property value to wait for
        cb(function): callback on success
        timeout_sec (int): timeout
        poll_sec (int): polling interval in seconds

    Returns:
        None

    Example:
        This method is called from UcsHandle class,
        wait_for_event method
    """

    if mo is None:
        return

    # create a new event handler
    ueh = UcsEventHandle(handle)

    context = {}
    context["done"] = False

    if isinstance(value, list):
        success_value = value
    else:
        success_value = [value]

    # create a watch block
    ueh.add(
        managed_object=mo,
        prop=prop,
        success_value=success_value,
        call_back=cb,
        timeout_sec=timeout_sec,
        poll_sec=poll_sec,
        context=context)

    # wait for the event to occur
    while not context["done"]:
        time.sleep(1)
