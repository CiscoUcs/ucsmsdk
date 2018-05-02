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

from nose import SkipTest
from nose.tools import *
from ..connection.info import custom_setup, custom_teardown, get_skip_msg

handle = None
obj = None


def setup_module():
    from ucsmsdk.mometa.ls.LsServer import LsServer
    global obj
    global handle

    handle = custom_setup()
    if not handle:
        msg = get_skip_msg()
        raise SkipTest(msg)

    obj = LsServer("org-root", "test", usr_lbl="sample")

    handle.add_mo(obj, True)
    handle.commit()


def teardown_module():
    if handle:
        handle.remove_mo(obj)
        handle.commit()
    custom_teardown(handle)


@raises(Exception)
def test_001_set_ro_property():
    # This is a read only property
    # Should fail with an exception
    obj.oper_state = "up"


def test_002_set_rw_property():
    # This is a read write property.
    # Should happen without any issues
    obj.descr = "test_description"


@raises(Exception)
def test_003_set_naming_property():
    # This is a naming property. so, it is create only
    # Should fail with an exception
    obj.name = "test1"


def test_004_check_existing_prop_match():
    # Checking property aginst existing property
    bool_var = obj.check_prop_match(usr_lbl="sample")
    assert_equal(bool_var, True)


@raises(Exception)
def test_005_check_nonexisting_prop_match():
    # Checking property aginst non-existing property
    bool_var = obj.check_prop_match(usr_lbl="new_label")
    assert_equal(bool_var, True)


def test_006_set_prop_multiple():
    # Setting multiple property of object
    obj.set_prop_multiple(usr_lbl="new_label",
                          vmedia_policy_name="test_vmedia_pol")
    handle.set_mo(obj)
    handle.commit()

    new_obj = handle.query_dn(obj.dn)
    assert_equal(new_obj.usr_lbl, "new_label")
    assert_equal(new_obj.vmedia_policy_name, "test_vmedia_pol")
