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

handle = None
sp = None
dn = "org-root/ls-eventhandle"
event_flag = False
ueh = None


def setup_module():
    from ucsmsdk.ucseventhandler import UcsEventHandle
    from ucsmsdk.mometa.ls.LsServer import LsServer

    global handle, sp, ueh
    handle = custom_setup()
    ueh = UcsEventHandle(handle)
    org = handle.query_dn("org-root")

    sp = LsServer(org, name="eventhandle", descr="")
    handle.add_mo(sp, True)
    handle.commit()


def teardown_module():
    if sp is not None:
        handle.remove_mo(sp)
        handle.commit()
    custom_teardown(handle)


def watch_mo(mce):
    global event_flag
    print("Inside watch_mo")
    event_flag = True


def test_watch_mo():
    mo = handle.query_dn(dn)
    if mo is None:
        raise ValueError("Mo does no exist")
    wb_mo = ueh.add(managed_object=mo, call_back=watch_mo)
    time.sleep(2)

    mo.descr = "watch_mo"
    handle.set_mo(mo)
    handle.commit()

    time.sleep(2)

    assert event_flag


def test_watch_mo_remove():
    mo = handle.query_dn(dn)
    if mo is None:
        raise ValueError("Mo does no exist")
    wb_mo_remove = ueh.add(managed_object=mo)
    time.sleep(2)
    print(wb_mo_remove)

    print(ueh.get())
    handle.remove_mo(mo)
    handle.commit()
    time.sleep(2)
    print(ueh.get())

    assert wb_mo_remove not in ueh.get()
