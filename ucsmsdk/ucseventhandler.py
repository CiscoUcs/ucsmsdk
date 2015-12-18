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

from threading import Condition, Lock, Thread
from Queue import Queue
import datetime
import urllib2
import logging
import signal

import ucsgenutils
import ucsmo
import ucscoreutils
import ucsxmlcodec as xc
from ucsexception import UcsWarning
from ucsexception import UcsValidationException

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
                log.debug("queue error:" + self.error_code)
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
        print "\n"
        print 'EventId'.ljust(tab_size * 2) + ':' + str(mce.event_id)
        print 'ChangeList'.ljust(tab_size * 2) + ':' + str(mce.change_list)
        print 'ClassId'.ljust(tab_size * 2) + ':' + str(mce.mo._class_id)


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
            self.__event_chan_resp = self.__handle.post_xml(xml_str=xml_query,
                                                            read=False)
        except Exception:
            return

        try:
            while self.__event_chan_resp and len(self.__wbs):
                # log.debug('waiting to acquire lock on %s' %
                #           self.__enqueue_thread.name)
                self.__condition.acquire()
                # log.debug('condition acquired by %s' %
                #           self.__enqueue_thread.name)

                if self.__handle.cookie is None:
                    break
                if self.__event_chan_resp is None:
                    break

                resp = self.__event_chan_resp.readline()
                resp = self.__event_chan_resp.read(int(resp))
                for mo_elem in self.__get_mo_elem(resp):
                    gmo = ucsmo.generic_mo_from_xml_elem(mo_elem[0])
                    mce = MoChangeEvent(
                                event_id=mo_elem[1],
                                mo=gmo.to_mo(),
                                change_list=gmo.properties.keys())

                    for watch_block in self.__wbs:
                        if watch_block.fmce(mce):
                            watch_block.enqueue(mce)
                            # log.debug('condition notified by %s' %
                            #           self.__enqueue_thread.name)
                            self.__condition.notify()

                # log.debug('condition released by %s' %
                #           self.__enqueue_thread.name)
                self.__condition.release()

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
        # self.__enqueue_thread.daemon = True
        self.__enqueue_thread.start()

    # def __thread_enqueue_stop(self):
    #     """
    #     Internal method to stop the enqueue thread.
    #     """
    #
    #     #self.__enqueue_thread = None
    #     self.__event_chan_resp = None

    def __dequeue_function(self):
        """
        Internal method to dequeue to events.
        """

        while len(self.__wbs):
            # log.debug('waiting to acquire lock on %s' %
            #               self.__dequeue_thread.name)
            self.__condition.acquire()
            # log.debug('condition acquired by %s' %
            #           self.__dequeue_thread.name)

            lowest_timeout = None
            wb_to_remove = []

            for watch_block in self.__wbs:
                poll_sec = watch_block.params["poll_sec"]
                managed_object = watch_block.params["managed_object"]
                timeout_sec = watch_block.params["timeout_sec"]
                transient_value = watch_block.params["transient_value"]
                success_value = watch_block.params["success_value"]
                failure_value = watch_block.params["failure_value"]
                prop = watch_block.params["prop"]
                start_time = watch_block.params["start_time"]

                gmo = None
                pmo = None
                mce = None

                if poll_sec is not None and managed_object is not None:
                    pmo = self.__handle.query_dn(managed_object.dn)
                    if pmo is None:
                        UcsWarning('Mo ' +
                                   managed_object.dn +
                                   ' not found.')
                        continue
                    elem = pmo.to_xml()
                    xml_str = xc.to_xml_str(elem)
                    gmo = ucsmo.generic_mo_from_xml(xml_str)
                else:
                    time_diff = datetime.datetime.now() - start_time
                    timeout_ms = 0
                    if timeout_sec is not None:
                        if time_diff.seconds >= timeout_sec:  # TimeOut
                            wb_to_remove.append(watch_block)
                            continue
                        timeout_ms = (timeout_sec - time_diff.seconds)

                        if lowest_timeout is None:
                            lowest_timeout = timeout_ms
                        else:
                            if lowest_timeout > timeout_ms:
                                lowest_timeout = timeout_ms

                    if timeout_ms > 0:
                        mce = watch_block.dequeue(timeout_ms)
                    else:
                        mce = watch_block.dequeue(2147483647)
                        # print mce
                    if mce is None:
                        continue

                # Means parameter set is not Mo
                if managed_object is None:
                    if watch_block.callback is not None:
                        watch_block.callback(mce)
                    continue

                if mce is not None:
                    elem = mce.mo.to_xml()
                    xml_str = xc.to_xml_str(elem)
                    gmo = ucsmo.generic_mo_from_xml(xml_str)

                attributes = []
                if mce is None:
                    attributes = gmo.properties.keys()
                else:
                    attributes = mce.change_list

                attributes_dict = {}
                for attr in attributes:
                    attributes_dict[
                        ucsgenutils.to_python_propname(attr)] = attr

                nprop = prop.lower()
                if prop in attributes_dict:
                    prop_val = gmo.properties[attributes_dict[nprop]]
                    if mce is None:
                        mce = MoChangeEvent(event_id=0, mo=pmo,
                                            change_list=prop)

            # check if any of the conditional checks match
            # if so, call the callback specified by the application
            # and remove the watch_block (deferred to outside the loop)
                    if (
                        (len(success_value) > 0 and
                                    prop_val in success_value) or
                        (len(failure_value) > 0 and
                                    prop_val in failure_value) or
                        (len(transient_value) > 0 and
                                    prop_val in transient_value)):
                        if watch_block.callback:
                            watch_block.callback(mce)
                        wb_to_remove.append(watch_block)
                        continue

                if poll_sec is not None:
                    poll_ms = poll_sec
                    if timeout_sec is not None:
                        pts = datetime.datetime.now() - start_time
                        if pts.seconds >= timeout_sec:  # TimeOut
                            break
                        timeout_ms = timeout_sec - pts.seconds

                        if timeout_ms < poll_sec:
                            poll_ms = pts.seconds

                    # time.sleep(poll_ms)
                    if lowest_timeout is None:
                        lowest_timeout = poll_ms
                    else:
                        if lowest_timeout > poll_ms:
                            lowest_timeout = poll_ms

            if len(wb_to_remove):
                self.__wbs_lock.acquire()

                for wb in wb_to_remove:
                    self.watch_block_remove(wb)
                wb_to_remove = []

                self.__wbs_lock.release()

            # There is a possibility that all the watchblocks
            # were deleted in the above loop.
            # In that case, no need to wait for more events
            if len(self.__wbs):
                # log.debug('condition wait by %s' %
                #           self.__dequeue_thread.name)
                self.__condition.wait(lowest_timeout)

            # log.debug('condition released by %s' %
            #           self.__dequeue_thread.name)
            self.__condition.release()

        return

    def __thread_dequeue_start(self):
        """
        Internal method to start dequeue thread.
        """

        self.__dequeue_thread = Thread(name="dequeue_thread",
                                       target=self.__dequeue_function)
        # self.__dequeue_thread.daemon = True
        self.__dequeue_thread.start()

    # def __thread_dequeue_stop(self):
    #     """
    #     Internal method to stop dequeue thread.
    #     """
    #     self.__dequeue_thread = None

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

        # if len(self.__wbs) == 0:
        #     self.__thread_enqueue_stop()
        #     self.__thread_dequeue_stop()

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
            class_id (str) - specifies the class name for which events should be monitored.
            managed_object (object) - specifies a particular managed object that
                user wants to monitor. prop specifies the the property of the
                managed object which will be monitored.
            success_value - specifies the success values of a ManagedObject Prop
            failure_value - specifies the failure values of a ManagedObject Prop
            transient_value - specifies transient values of a ManagedObject Prop 
            poll_sec - specifies the time in seconds for polling event.
            timeout_sec - specifies the time after which method should stop 
                            polling or timeOut.
            call_back - specifies the call Back Method or operation that can be
                            given to this method
        """

        if class_id is not None and managed_object is None:
            if ucscoreutils.find_class_id_in_mo_meta_ignore_case(class_id) \
                    is None:
                raise UcsValidationException(
                    "Invalid ClassId %s specified." % class_id)
        elif managed_object is not None and class_id is None:
            if ucscoreutils.find_class_id_in_mo_meta_ignore_case(
                    managed_object._class_id) is None:
                raise UcsValidationException(
                    "Object of unknown ClassId %s provided." %
                    managed_object._class_id)

            if prop is None:
                raise UcsValidationException(
                    "prop parameter is not provided.")

            mo_property_meta = ucscoreutils.get_mo_property_meta(
                managed_object._class_id, prop)
            if mo_property_meta is None:
                raise UcsValidationException(
                    "Unknown Property %s provided." % prop)

            if not success_value:
                raise UcsValidationException(
                    "success_value parameter is not provided.")
        elif class_id is not None and managed_object is not None:
            raise UcsValidationException(
                "Specify either class_id or managedObject, not both")

        watch_block = None
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
        # log.debug(param_dict)
        if class_id is None and managed_object is None:
            def watch_all_filter(mce):
                """
                Callback method to work on all events.
                """
                return True

            watch_block = self.watch_block_add(
                                    params=param_dict,
                                    filter_callback=watch_all_filter,
                                    callback=call_back)
        elif class_id is not None and managed_object is None:
            def watch__type_filter(mce):
                """
                Callback method to work on events with a specific class_id.
                """
                if mce.mo._class_id.lower() == class_id.lower():
                    return True
                return False

            watch_block = self.watch_block_add(
                                    params=param_dict,
                                    filter_callback=watch__type_filter,
                                    callback=call_back)
        elif class_id is None and managed_object is not None:
            if poll_sec is None:
                def watch_mo_filter(mce):
                    """
                    Callback method to work on events specific to respective
                    managed object.
                    """
                    # log.debug(mce.mo.dn)
                    # log.debug(managed_object.dn)
                    if mce.mo.dn == managed_object.dn:
                        return True
                    return False

                watch_block = self.watch_block_add(
                                    params=param_dict,
                                    filter_callback=watch_mo_filter,
                                    callback=call_back)
            else:
                def watch_none_filter(mce):
                    """
                    Callback method to ignore all events.
                    """
                    return False

                watch_block = self.watch_block_add(
                                    params=param_dict,
                                    filter_callback=watch_none_filter,
                                    callback=call_back)

        if watch_block is None:
            raise UcsValidationException("Error adding WatchBlock...")

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
