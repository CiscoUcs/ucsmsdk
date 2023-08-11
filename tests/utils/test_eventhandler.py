# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import threading

from tests.base import BaseTest


class TestEventHandler(BaseTest):
    def setUp(self):
        super().setUp()
        from ucsmsdk.ucseventhandler import UcsEventHandle
        from ucsmsdk.mometa.ls.LsServer import LsServer

        self.ueh = UcsEventHandle(self.handle)
        self.org = self.handle.query_dn("org-root")

        self.sp = LsServer(org, name="eventhandle-test", descr="")
        self.handle.add_mo(sp, True)
        self.handle.commit()
        self.finished = False

    def tearDown(self):
        if self.sp is not None:
            self.handle.remove_mo(self.sp)
            self.handle.commit()
        super().tearDown()

    def user_callback(self, mce):
        self.finished = True

    def wait_method(self, poll_sec=None):
        # Always clear the label
        self.sp.usr_lbl = ""
        self.handle.add_mo(self.sp, modify_present=True)
        self.handle.commit()

        self.handle.wait_for_event(
            mo=self.sp,
            prop="usr_lbl",
            value="trigger",
            cb=self.user_callback,
            timeout=20,
            poll_sec=poll_sec
        )

    def wait_method_for_multiple_values(self, poll_sec=None):
        self.handle.wait_for_event(
            mo=self.sp,
            prop="usr_lbl",
            value=["trigger", "another_trigger"],
            cb=self.user_callback,
            timeout=20,
            poll_sec=poll_sec
        )

    def trigger_method(self, label=None):
        self.sp.usr_lbl = label
        self.handle.set_mo(self.sp)
        self.handle.commit()

    def test_wait_for_event_mo(self):
        self.finished = False

        t1 = threading.Thread(name="wait", target=self.wait_method)
        t2 = threading.Thread(name="trigger", target=self.trigger_method, args=("trigger",))

        t1.start()
        time.sleep(1)
        t2.start()

        t1.join()
        t2.join()

        self.assertTrue(self.finished)

    def test_wait_for_poll_mo(self):
        self.finished = False

        t1 = threading.Thread(name="wait", target=self.wait_method, args=(5,))
        t2 = threading.Thread(name="trigger", target=self.trigger_method, args=("trigger",))

        t1.start()
        time.sleep(1)
        t2.start()

        t1.join()
        t2.join()

        self.assertTrue(self.finished)

    def test_wait_for_event_timeout(self):
        self.finished = False

        t1 = threading.Thread(name="wait", target=self.wait_method)
        t2 = threading.Thread(name="trigger", target=self.trigger_method, args=("invalid_trigger",))

        t1.start()
        time.sleep(1)
        t2.start()

        t1.join()
        t2.join()

        self.assertFalse(self.finished)

    def test_wait_for_poll_timeout(self):
        self.finished = False

        t1 = threading.Thread(name="wait", target=self.wait_method, args=(2,))
        t2 = threading.Thread(name="trigger", target=self.trigger_method, args=("invalid_trigger",))

        t1.start()
        time.sleep(1)
        t2.start()

        t1.join()
        t2.join()

        self.assertFalse(self.finished)

    def test_wait_for_event_invalid_mo(self):
        other_mo = self.handle.query_dn("capabilities")
        with self.assertRaises(Exception):
            self.handle.wait_for_event(
                mo=other_mo,
                prop="usr_lbl",
                value="trigger",
                cb=self.user_callback,
                timeout=20
            )

    def test_wait_for_poll_invalid_mo(self):
        other_mo = self.handle.query_dn("capabilities")

        with self.assertRaises(Exception):
            handle.wait_for_event(
                mo=other_mo,
                prop="usr_lbl",
                value="trigger",
                cb=self.user_callback,
                timeout=20,
                poll_sec=5
            )

    def test_wait_for_event_multiple(self):
        self.finished = False

        t1 = threading.Thread(name="wait", target=self.wait_method_for_multiple_values)
        t2 = threading.Thread(name="trigger", target=self.trigger_method, args=("trigger",))

        t1.start()
        time.sleep(1)
        t2.start()

        t1.join()
        t2.join()

        self.assertTrue(self.finished)

    def test_wait_for_poll_multiple(self):
        self.finished = False

        t1 = threading.Thread(name="wait", target=self.wait_method_for_multiple_values, args=(2,))
        t3 = threading.Thread(name="another_trigger", target=self.trigger_method, args=("another_trigger",))

        t1.start()
        time.sleep(1)
        t3.start()

        t1.join()
        t3.join()

        self.assertTrue(self.finished)

    def test_wait_for_event_timeout_noenqueue(self):
        self.handle.wait_for_event(
            mo=sp,
            prop="usr_lbl",
            value="trigger",
            cb=self.user_callback,
            timeout=5
        )

