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

try:
    from Queue import Queue
except:
    from queue import Queue

from threading import Condition, Lock, Thread
import datetime
import logging

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
        self.error_code = 0  # TODO:error_code to call notify as per PowerTool
        self.event_q = Queue()  # infinite size Queue

    def dequeue(self, miliseconds_timeout):
        """Internal method to dequeue the events."""
        while True:
            if self.error_code != 0:
                log.debug("queue error:" + str(self.error_code))
                return None
            if not self.event_q.empty():
                mo_chg_event = self.event_q.get()
                return mo_chg_event
            else:
                return None

    def enqueue(self, cmce):
        """Internal method to enqueue the events."""
        if self.event_q.maxsize < self.capacity:
            self.event_q.put(cmce)
        else:
            self.overflow = True

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
        self.__handle = handle
        self.__lock_object = None
        self.__wbs = []
        self.__wbs_lock = Lock()
        self.__enqueue_thread = None
        self.__condition = Condition()
        self.__event_chan_resp = None
        self.__dequeue_thread = None
        self.__lowest_timeout = None
        self.__wb_to_remove = []

    def __get_mo_elem(self, xml_str):
        """
        Internal method to extract mo elements from xml string
        """

        root = xc.extract_root_elem(xml_str)
        mo_elems = []
        if root.tag == "methodVessel":
            for in_stimuli in root:
                for cmce in in_stimuli:
                    for in_config in cmce:
                        for mo_elem in in_config:
                            mo_elems.append(
                                (mo_elem, cmce.attrib.get('inEid')))
        elif root.tag == "configMoChangeEvent":
            for in_config in root:
                for mo_elem in in_config:
                    mo_elems.append(mo_elem)
        return mo_elems

    def __enqueue_function(self):
        """
        Internal method used by add_event_handler.
        Provides functionality of enqueue/dequeue of the events and
        triggering callbacks.
        """

        try:
            xml_query = '<eventSubscribe cookie="%s"/>' % self.__handle.cookie
            self.__event_chan_resp = self.__handle.post_xml(
                xml_str=xml_query.encode(), read=False)
        except Exception:
            raise

        try:
            while self.__event_chan_resp and len(self.__wbs):

                if self.__handle.cookie is None or \
                        self.__event_chan_resp is None:
                    break

                resp = self.__event_chan_resp.readline()
                resp = self.__event_chan_resp.read(int(resp))
                for mo_elem in self.__get_mo_elem(resp):
                    gmo = ucsmo.generic_mo_from_xml_elem(mo_elem[0])
                    mce = MoChangeEvent(event_id=mo_elem[1],
                                        mo=gmo.to_mo(),
                                        change_list=gmo.properties.keys())

                    for watch_block in self.__wbs:
                        if watch_block.fmce(mce):
                            watch_block.enqueue(mce)
                            with self.__condition:
                                self.__condition.notify()

            if len(self.__wbs) == 0:
                self.__condition.acquire()
                self.__condition.notify()
                self.__condition.release()
        except:
            raise

    def __thread_enqueue_start(self):
        """
        Internal method to start the enqueue thread which adds the events in
        an internal queue.
        """

        self.__enqueue_thread = Thread(name="enqueue_thread",
                                       target=self.__enqueue_function)
        self.__enqueue_thread.daemon = True
        self.__enqueue_thread.start()

    def __time_left(self, watch_block):
        timeout_sec = watch_block.params["timeout_sec"]
        start_time = watch_block.params["start_time"]
        time_diff = datetime.datetime.now() - start_time
        if time_diff.seconds < timeout_sec:
            return timeout_sec - time_diff.seconds
        else:
            return 0
        # return 2147483647

    def __dequeue_mce(self, time_left, watch_block):
        if time_left and time_left > 0:
            if self.__lowest_timeout is None or \
                    self.__lowest_timeout > time_left:
                self.__lowest_timeout = time_left
            mce = watch_block.dequeue(time_left)
        else:
            mce = watch_block.dequeue(2147483647)

        return mce

    def __prop_val_exist(self, mo, prop, success_value,
                         failure_value, transient_value,
                         change_list=None):
        if isinstance(mo, ucsmo.GenericMo):
            n_prop = prop
            n_prop_val = mo.properties[n_prop]
        elif prop not in mo.prop_meta:
            n_prop = prop
            n_prop_val = getattr(mo, n_prop)
        else:
            n_prop = mo.prop_meta[prop].xml_attribute
            n_prop_val = getattr(mo, n_prop)

        if change_list and n_prop not in change_list:
            return False

        if (len(success_value) > 0 and n_prop_val in success_value) or \
                (len(failure_value) > 0 and n_prop_val in failure_value) or \
                (len(transient_value) > 0 and n_prop_val in transient_value):
            return True
        return False

    def __dequeue_mo_prop_poll(self, mo, prop, poll_sec, watch_block,
                               timeout_sec=None, time_left=None):

        success_value = watch_block.params["success_value"]
        failure_value = watch_block.params["failure_value"]
        transient_value = watch_block.params["transient_value"]

        if not success_value or len(success_value) < 1:
            raise ValueError("success_value is missing.")

        pmo = self.__handle.query_dn(mo.dn)
        if pmo is None:
            UcsWarning('Mo ' + pmo.dn + ' not found.')
            return

        if timeout_sec is not None and time_left is not None and time_left > 0:
            if time_left < poll_sec:
                poll_sec = timeout_sec - time_left

        if self.__lowest_timeout is None or self.__lowest_timeout > poll_sec:
            self.__lowest_timeout = poll_sec

        if self.__prop_val_exist(pmo, prop, success_value,
                                 failure_value, transient_value):
            log.info("Successful")
            self.__wb_to_remove.append(watch_block)

    def __dequeue_mo_prop_event(self, prop, watch_block, time_left=None):

        success_value = watch_block.params["success_value"]
        failure_value = watch_block.params["failure_value"]
        transient_value = watch_block.params["transient_value"]

        if not success_value or len(success_value) < 1:
            raise ValueError("success_value is missing.")

        # dequeue mce
        mce = self.__dequeue_mce(time_left, watch_block)
        if mce is None:
            return

        # checks if prop value exist in success or failure or transient values
        attributes = mce.change_list
        if self.__prop_val_exist(mce.mo, prop, success_value, failure_value,
                                 transient_value, attributes):
            if watch_block.callback:
                watch_block.callback(mce)
            self.__wb_to_remove.append(watch_block)

    def __dequeue_mo_until_removed(self, watch_block, time_left=None):

        # dequeue mce
        mce = self.__dequeue_mce(time_left, watch_block)
        if mce is None:
            return

        if watch_block.callback is not None:
            watch_block.callback(mce)

        # watch mo until gets deleted
        if mce.mo.status == "deleted":
            self.__wb_to_remove.append(watch_block)

    def __dequeue_all_class_id(self, watch_block, time_left=None):

        # dequeue mce
        mce = self.__dequeue_mce(time_left, watch_block)
        if mce is not None and watch_block.callback is not None:
            watch_block.callback(mce)

    def __dequeue_function(self):
        """
        Internal method to dequeue to events.
        """

        while len(self.__wbs):
            self.__lowest_timeout = None
            self.__wb_to_remove = []

            try:
                for watch_block in self.__wbs:
                    mo = watch_block.params["managed_object"]
                    prop = watch_block.params["prop"]
                    poll_sec = watch_block.params["poll_sec"]
                    timeout_sec = watch_block.params["timeout_sec"]

                    # checks if watch_block is not timed out, else remove
                    time_left = None
                    if timeout_sec is not None:
                        time_left = self.__time_left(watch_block)
                        if time_left <= 0:
                            self.__wb_to_remove.append(watch_block)
                            continue

                    # poll for mo. Not to monitor event.
                    if poll_sec is not None and mo is not None:
                        self.__dequeue_mo_prop_poll(mo, prop, poll_sec,
                                                    watch_block, timeout_sec,
                                                    time_left)
                    elif mo is not None:
                        # watch mo until prop_val changed to desired value
                        if prop is not None:
                            self.__dequeue_mo_prop_event(prop, watch_block,
                                                         time_left)
                        # watch mo until it is removed
                        else:
                            self.__dequeue_mo_until_removed(watch_block,
                                                            time_left)
                    elif mo is None:
                        # watch all event or specific to class_id
                        self.__dequeue_all_class_id(watch_block, time_left)
            except Exception as e:
                log.info(str(e))
                self.__wb_to_remove.append(watch_block)

            # removing watch_block
            if len(self.__wb_to_remove):
                self.__wbs_lock.acquire()

                for wb in self.__wb_to_remove:
                    self.watch_block_remove(wb)
                self.__wb_to_remove = []

                self.__wbs_lock.release()

            # wait for more events only if watch_block exists
            if len(self.__wbs):
                with self.__condition:
                    self.__condition.wait(self.__lowest_timeout)
        return

    def __thread_dequeue_start(self):
        """
        Internal method to start dequeue thread.
        """

        self.__dequeue_thread = Thread(name="dequeue_thread",
                                       target=self.__dequeue_function)
        self.__dequeue_thread.daemon = True
        self.__dequeue_thread.start()

    def watch_block_add(self, params,
                        filter_callback,
                        capacity=500,
                        callback=None):
        """
        Internal method to add a watch block for starting event monitoring.
        """

        if self.__handle.cookie is None:
            return None

        self.__wbs_lock.acquire()
        watch_block = WatchBlock(params,
                                 filter_callback,
                                 capacity,
                                 callback)  # Add a List of Watchers

        if watch_block is not None and watch_block.callback is None:
            watch_block.callback = watch_block.dequeue_default_callback

        self.__wbs.append(watch_block)
        self.__wbs_lock.release()
        return watch_block

    def watch_block_remove(self, watch_block):
        """
        Internal method to remove a watch block for
        stopping event monitoring.
        """
        if watch_block in self.__wbs:
            self.__wbs.remove(watch_block)

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
            failure_value=[],
            transient_value=[],
            poll_sec=None,
            timeout_sec=None,
            call_back=None):
        """
        Adds an event handler.

        An event handler can be added using this method where an user can
        subscribe for the event channel from UCS and can monitor those events
        for any specific success value or failure value for a managed object.

        Args:
            class_id (str): managed object class id
            managed_object (ManagedObject)
            prop (str) - property of the managed object to monitor
            success_value (list) - success values of a prop
            failure_value (list) - failure values of a prop
            transient_value (list) - transient values of a prop
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
                      'failure_value': failure_value,
                      'transient_value': transient_value,
                      'poll_sec': poll_sec,
                      'timeout_sec': timeout_sec,
                      'call_back': call_back,
                      'start_time': datetime.datetime.now()}

        if filter_callback is None:
            raise UcsValidationException("Error adding WatchBlock...")

        watch_block = self.watch_block_add(params=param_dict,
                                           filter_callback=filter_callback,
                                           callback=call_back)

        if watch_block is not None and len(self.__wbs) == 1:
            if poll_sec is None:
                self.__thread_enqueue_start()
            self.__thread_dequeue_start()

        return watch_block

    def remove(self, watch_block):
        """
        Removes an event handler.
        """

        self.__wbs_lock.acquire()
        if watch_block in self.__wbs:
            self.watch_block_remove(watch_block)
        else:
            UcsWarning("Event handler not found")
        self.__wbs_lock.release()

    def clean(self):
        """
        Removes all the watch blocks from the event handler
        """

        self.__wbs_lock.acquire()
        for each in self.__wbs:
            self.watch_block_remove(each)
        self.__wbs_lock.release()

    def get(self):
        """
        Returns the list of event handlers.
        """
        return self.__wbs
