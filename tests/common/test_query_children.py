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

from nose.tools import *
from ..connection.info import custom_setup, custom_teardown

handle = None
sp_list = []


def setup_module():
    from ucsmsdk.mometa.ls.LsServer import LsServer

    global handle
    handle = custom_setup()
    org = handle.query_dn("org-root")

    sp_TEST = LsServer(org, name="TEST", usr_lbl="TEST")
    handle.add_mo(sp_TEST, True)
    sp_list.append(sp_TEST)

    sp_test = LsServer(org, name="test", usr_lbl="test", descr="test")
    handle.add_mo(sp_test, True)
    sp_list.append(sp_test)

    sp_test11 = LsServer(org, name="test11", usr_lbl="test11")
    handle.add_mo(sp_test11, True)
    sp_list.append(sp_test11)

    sp_test12 = LsServer(org, name="test12", usr_lbl="test12")
    handle.add_mo(sp_test12, True)
    sp_list.append(sp_test12)

    handle.commit()


def teardown_module():
    for sp in sp_list:
        handle.remove_mo(sp)
    handle.commit()
    custom_teardown(handle)


def test_default_filter():
    mos = handle.query_children(in_dn="org-root", class_id="LsServer",
                                filter_str="(usr_lbl, 'test')")
    assert_equal(len(mos), 3)


def test_default_case_insensitive():
    mos = handle.query_children(in_dn="org-root", class_id="LsServer",
                                filter_str="(usr_lbl, 'test', flag='I')")
    assert_equal(len(mos), 4)


def test_type_eq():
    mos = handle.query_children(in_dn="org-root", class_id="LsServer",
                                filter_str="(usr_lbl, 'test', type='eq')")
    assert_equal(len(mos), 1)


def test_type_eq_prop_without_underscore():
    mos = handle.query_children(in_dn="org-root", class_id="LsServer",
                                filter_str="(descr, 'test', type='eq')")
    assert_equal(len(mos), 1)


def test_type_re():
    mos = handle.query_children(in_dn="org-root", class_id="LsServer",
                                filter_str="(usr_lbl, 'test.*1.*', type='re')")
    assert_equal(len(mos), 2)
