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

from nose.tools import *
from ..connection.info import custom_setup, custom_teardown
import threading

handle = None
sp = None
dn = "org-root/ls-eventhandle-test"
finished = False


def setup_module():
    from ucsmsdk.ucseventhandler import UcsEventHandle
    from ucsmsdk.mometa.ls.LsServer import LsServer

    global handle, sp, ueh
    handle = custom_setup()
    ueh = UcsEventHandle(handle)
    org = handle.query_dn("org-root")

    sp = LsServer(org, name="eventhandle-test", descr="")
    handle.add_mo(sp, True)
    handle.commit()


def teardown_module():
    if sp is not None:
        handle.remove_mo(sp)
        handle.commit()
    custom_teardown(handle)


def user_callback(mce):
    global finished
    finished = True


def wait_method(poll_sec=0):
    # Always clear the label
    sp.usr_lbl = ""
    handle.add_mo(sp, modify_present=True)
    handle.commit()

    handle.wait_for_event(
        mo=sp,
        prop="usr_lbl",
        value="trigger",
        cb=user_callback,
        timeout=20,
        poll_sec=poll_sec
    )


def wait_method_for_multiple_values(poll_sec=0):
    handle.wait_for_event(
        mo=sp,
        prop="usr_lbl",
        value=["trigger", "another_trigger"],
        cb=user_callback,
        timeout=20,
        poll_sec=poll_sec
    )


def trigger_method(label=None):
    sp.usr_lbl = label
    handle.set_mo(sp)
    handle.commit()


def test_wait_for_event_mo():
    global finished
    finished = False

    t1 = threading.Thread(name="wait", target=wait_method)
    t2 = threading.Thread(name="trigger", target=trigger_method, args=("trigger",))

    t1.start()
    time.sleep(1)
    t2.start()

    t1.join()
    t2.join()

    assert_equal(finished, True)


def test_wait_for_poll_mo():
    global finished
    finished = False

    t1 = threading.Thread(name="wait", target=wait_method, args=(5,))
    t2 = threading.Thread(name="trigger", target=trigger_method, args=("trigger",))

    t1.start()
    time.sleep(1)
    t2.start()

    t1.join()
    t2.join()

    assert_equal(finished, True)


def test_wait_for_event_timeout():
    global finished
    finished = False

    t1 = threading.Thread(name="wait", target=wait_method)
    t2 = threading.Thread(name="trigger", target=trigger_method, args=("invalid_trigger",))

    t1.start()
    time.sleep(1)
    t2.start()

    t1.join()
    t2.join()

    assert_equal(finished, False)


def test_wait_for_poll_timeout():
    global finished
    finished = False

    t1 = threading.Thread(name="wait", target=wait_method, args=(2,))
    t2 = threading.Thread(name="trigger", target=trigger_method, args=("invalid_trigger",))

    t1.start()
    time.sleep(1)
    t2.start()

    t1.join()
    t2.join()

    assert_equal(finished, False)


@raises(Exception)
def test_wait_for_event_invalid_mo():

    other_mo = handle.query_dn("capabilities")

    handle.wait_for_event(
        mo=other_mo,
        prop="usr_lbl",
        value="trigger",
        cb=user_callback,
        timeout=20
    )


@raises(Exception)
def test_wait_for_poll_invalid_mo():
    other_mo = handle.query_dn("capabilities")

    handle.wait_for_event(
        mo=other_mo,
        prop="usr_lbl",
        value="trigger",
        cb=user_callback,
        timeout=20,
        poll_sec=5
    )


def test_wait_for_event_multiple():
    global finished
    finished = False

    t1 = threading.Thread(name="wait", target=wait_method_for_multiple_values)
    t2 = threading.Thread(name="trigger", target=trigger_method, args=("trigger",))

    t1.start()
    time.sleep(1)
    t2.start()

    t1.join()
    t2.join()

    assert_equal(finished, True)


def test_wait_for_poll_multiple():
    global finished
    finished = False

    t1 = threading.Thread(name="wait", target=wait_method_for_multiple_values, args=(2,))
    t3 = threading.Thread(name="another_trigger", target=trigger_method, args=("another_trigger",))

    t1.start()
    time.sleep(1)
    t3.start()

    t1.join()
    t3.join()

    assert_equal(finished, True)
