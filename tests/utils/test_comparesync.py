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

from ucsmsdk.utils.comparesyncmo import compare_ucs_mo, write_mo_diff

ref_handle = None
diff_handle = None


def static_setup():
    from ucsmsdk.ucshandle import UcsHandle
    from ucsmsdk.ucscoremeta import UcsVersion

    global ref_handle
    global diff_handle

    ref_handle = UcsHandle("192.168.1.1", "admin", "password")
    diff_handle = UcsHandle("192.168.1.2", "admin", "password")

    ref_handle.__dict__['_UcsSession__version'] = UcsVersion("2.2(5a)")
    diff_handle.__dict__['_UcsSession__version'] = UcsVersion("2.2(2c)")


def test_compare_same_obj_with_diff_props():
    from ucsmsdk.mometa.ls.LsServer import LsServer
    static_setup()

    ref_mo = LsServer(parent_mo_or_dn="org-root", name="same", usr_lbl="")
    ref_mo.__dict__['config_state'] = "applied"
    ref_mo._handle = ref_handle
    ref_mos = [ref_mo]

    diff_mo = LsServer(parent_mo_or_dn="org-root", name="same", usr_lbl="xxx")
    diff_mo.__dict__['config_state'] = "applying"
    diff_mo._handle = diff_handle
    diff_mos = [diff_mo]

    difference = compare_ucs_mo(ref_mos, diff_mos)
    write_mo_diff(difference)
    assert_equal(len(difference), 1)
    assert_equal(len(difference[0].diff_property), 1)


def test_compare_same_obj_with_diff_props_include_operational():
    from ucsmsdk.mometa.ls.LsServer import LsServer
    static_setup()

    ref_mo = LsServer(parent_mo_or_dn="org-root", name="same", usr_lbl="")
    ref_mo.__dict__['config_state'] = "applied"
    ref_mo._handle = ref_handle
    ref_mos = [ref_mo]

    diff_mo = LsServer(parent_mo_or_dn="org-root", name="same", usr_lbl="xxx")
    diff_mo.__dict__['config_state'] = "applying"
    diff_mo._handle = diff_handle
    diff_mos = [diff_mo]

    difference = compare_ucs_mo(ref_mos, diff_mos, include_operational=True)
    write_mo_diff(difference)
    assert_equal(len(difference), 1)
    assert_equal(len(difference[0].diff_property), 2)


def test_compare_add_obj_to_ref_exist_only_in_diff():
    from ucsmsdk.mometa.ls.LsServer import LsServer
    static_setup()

    ref_mos = []

    diff_mo = LsServer(parent_mo_or_dn="org-root", name="add_to_ref",
                       usr_lbl="xxx")
    diff_mo._handle = diff_handle
    diff_mos = [diff_mo]

    difference = compare_ucs_mo(ref_mos, diff_mos)
    write_mo_diff(difference)
    assert_equal(len(difference), 1)


def test_compare_remove_obj_from_ref_exist_only_in_ref():
    from ucsmsdk.mometa.ls.LsServer import LsServer
    static_setup()

    ref_mo = LsServer(parent_mo_or_dn="org-root", name="remove_from_ref",
                      usr_lbl="")
    ref_mo._handle = ref_handle
    ref_mos = [ref_mo]

    diff_mos = []

    difference = compare_ucs_mo(ref_mos, diff_mos)
    write_mo_diff(difference)
    assert_equal(len(difference), 1)


def test_compare_org_hierarchy():
    from ucsmsdk.mometa.org.OrgOrg import OrgOrg
    from ucsmsdk.mometa.ls.LsServer import LsServer
    static_setup()

    ref_org = OrgOrg(parent_mo_or_dn="org-root", name="org_same", descr="")
    ref_org._handle = ref_handle
    ref_same_sp = LsServer(ref_org, name="same")
    ref_same_sp._handle = ref_handle
    ref_remove = LsServer(ref_org, name="remove_from_ref")
    ref_remove._handle = ref_handle
    ref_mos = [ref_org, ref_same_sp, ref_remove]

    diff_org = OrgOrg(parent_mo_or_dn="org-root", name="org_same",
                      descr="diff")
    diff_org._handle = diff_handle
    diff_same_sp = LsServer(diff_org, name="same", usr_lbl="diff")
    diff_same_sp._handle = diff_handle
    diff_add = LsServer(diff_org, name="add_to_ref")
    diff_add._handle = diff_handle
    diff_mos = [diff_org, diff_same_sp, diff_add]

    difference = compare_ucs_mo(ref_mos, diff_mos)
    write_mo_diff(difference)
    assert_equal(len(difference), 4)


def test_unknown_property():
    from ucsmsdk.mometa.ls.LsServer import LsServer
    static_setup()

    ref_mo = LsServer(parent_mo_or_dn="org-root", name="ra_ref", usr_lbl="")
    ref_mo._handle = ref_handle
    ref_mo.unknown = ""
    ref_mos = [ref_mo]

    diff_mo = LsServer(parent_mo_or_dn="org-root", name="ra_ref",
                       usr_lbl="xxx")
    diff_mo._handle = diff_handle
    diff_mo.unknown = "yyy"
    diff_mos = [diff_mo]

    difference = compare_ucs_mo(ref_mos, diff_mos)
    write_mo_diff(difference)
    assert_equal(len(difference), 1)
    assert_equal(len(difference[0].diff_property), 1)


def test_unknown_property_noversionfilter():
    from ucsmsdk.mometa.ls.LsServer import LsServer
    static_setup()

    ref_mo = LsServer(parent_mo_or_dn="org-root", name="ra_ref", usr_lbl="")
    ref_mo._handle = ref_handle
    ref_mo.unknown = ""
    ref_mos = [ref_mo]

    diff_mo = LsServer(parent_mo_or_dn="org-root", name="ra_ref",
                       usr_lbl="xxx")
    diff_mo._handle = diff_handle
    diff_mo.unknown = "yyy"
    diff_mos = [diff_mo]

    difference = compare_ucs_mo(ref_mos, diff_mos, version_filter=False)
    write_mo_diff(difference)
    assert_equal(len(difference), 1)
    assert_equal(len(difference[0].diff_property), 2)


def test_unknown_mo():
    from ucsmsdk.ucsmo import GenericMo
    static_setup()

    ref_mo = GenericMo(class_id="unknown", parent_mo_or_dn="parent_dn",
                       dn="sys/unknown", unknown="")
    ref_mo._handle = ref_handle
    ref_mos = [ref_mo]

    diff_mo = GenericMo(class_id="unknown", parent_mo_or_dn="parent_dn",
                        dn="sys/unknown", unknown="yyy")
    diff_mo._handle = diff_handle
    diff_mos = [diff_mo]

    difference = compare_ucs_mo(ref_mos, diff_mos)
    write_mo_diff(difference)
    assert_equal(len(difference), 0)


def test_unknown_mo_noversionfilter():
    from ucsmsdk.ucsmo import GenericMo
    static_setup()

    ref_mo = GenericMo(class_id="unknown", parent_mo_or_dn="parent_dn",
                       dn="sys/unknown", unknown="")
    ref_mo._handle = ref_handle
    ref_mos = [ref_mo]

    diff_mo = GenericMo(class_id="unknown", parent_mo_or_dn="parent_dn",
                        dn="sys/unknown", unknown="yyy")
    diff_mo._handle = diff_handle
    diff_mos = [diff_mo]

    difference = compare_ucs_mo(ref_mos, diff_mos, version_filter=False)
    write_mo_diff(difference)
    assert_equal(len(difference), 1)
    assert_equal(len(difference[0].diff_property), 1)
