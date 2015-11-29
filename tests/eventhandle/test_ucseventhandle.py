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

from nose.tools import with_setup
from ..connection.info import custom_setup, custom_teardown


from ucsmsdk.mometa.ls.LsServer import LsServer, LsServerConsts

handle = None
sp_name = "test_sp_ucsmsdk_testing"
sp = LsServer("org-root", name=sp_name)

def setup():
    global handle, sp
    print handle, sp
    handle = custom_setup()
    handle.add_mo(mo=sp, modify_present=True)
    handle.commit()
    print "create"

def teardown():
    global handle, sp
    print handle, sp
    handle.remove_mo(sp)
    handle.commit()
    custom_teardown(handle)
    print "delete"


def test_001_watch_all():
    import ucsmsdk.ucseventhandler as eh
    ueh = eh.UcsEventHandle(handle)
    ueh.add()

    wb_list = ueh.get()
    print wb_list

    time.sleep(30)

    for wb in wb_list:
        ueh.remove(wb)

    wb_list = ueh.get()
    print wb_list

def test_002_watch_class():
    import ucsmsdk.ucseventhandler as eh
    ueh = eh.UcsEventHandle(handle)
    print sp.rn
    ueh.add(class_id="LsServer")

    wb_list = ueh.get()
    print wb_list

    time.sleep(10)
    sp.descr = "class"
    handle.set_mo(sp)
    handle.commit()
    time.sleep(30)

    for wb in wb_list:
        ueh.remove(wb)

    wb_list = ueh.get()
    print wb_list

def test_003_watch_mo_success():
    import ucsmsdk.ucseventhandler as eh
    ueh = eh.UcsEventHandle(handle)
    print sp.rn
    ueh.add(managed_object=sp,
                              prop="usr_lbl",
                              success_value=['success'],
                              poll_sec=15)

    wb_list = ueh.get()
    print wb_list

    time.sleep(10)
    sp.usr_lbl = "success"
    handle.set_mo(sp)
    handle.commit()
    time.sleep(30)

    for wb in wb_list:
        ueh.remove(wb)

    wb_list = ueh.get()
    print wb_list

def test_004_watch_mo_failure():
    import ucsmsdk.ucseventhandler as eh
    ueh = eh.UcsEventHandle(handle)
    print sp.rn
    ueh.add(managed_object=sp,
                              prop="usr_lbl",
                              success_value=['success'],
                              failure_value=['failure'],
                              poll_sec=15)

    wb_list = ueh.get()
    print wb_list

    time.sleep(10)
    sp.usr_lbl = "failure"
    handle.set_mo(sp)
    handle.commit()
    time.sleep(30)

    for wb in wb_list:
        ueh.remove(wb)

    wb_list = ueh.get()
    print wb_list

def test_005_watch_mo_transient():
    import ucsmsdk.ucseventhandler as eh
    ueh = eh.UcsEventHandle(handle)
    print sp.rn
    ueh.add(managed_object=sp,
                              prop="usr_lbl",
                              success_value=['success'],
                              transient_value=['transient'],
                              poll_sec=15)

    wb_list = ueh.get()
    print wb_list

    time.sleep(10)
    sp.usr_lbl = "transient"
    handle.set_mo(sp)
    handle.commit()
    time.sleep(30)
    sp.usr_lbl = "success"
    handle.set_mo(sp)
    handle.commit()
    time.sleep(30)

    for wb in wb_list:
        ueh.remove(wb)

    wb_list = ueh.get()
    print wb_list

def test_006_watch_class_timeout():
    import ucsmsdk.ucseventhandler as eh
    ueh = eh.UcsEventHandle(handle)

    ueh.add(class_id="LsServer", timeout_sec=30)

    wb_list = ueh.get()
    print wb_list

    time.sleep(30)
    sp.usr_lbl = "success"
    handle.set_mo(sp)
    handle.commit()
    time.sleep(20)

    for wb in wb_list:
        ueh.remove(wb)

    wb_list = ueh.get()
    print wb_list
