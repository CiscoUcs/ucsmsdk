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

import ucsmsdk.ucsxmlcodec as xc
import ucsmsdk.ucsmo as ucsmo

handle = None

fault_inst_xml_str='''
<faultInst descr="TCA: etherTxStats totalBytesDelta = 6480,
raised above 0" dn="sys/switch-A/slot-1/switch-ether/port-3/fault-F35275"
status="modified"/>
'''

def setup():
    pass
    # global handle
    # handle = custom_setup()
    # print "create"


def teardown():
    pass
    # custom_teardown(handle)
    # print "delete"


def test_001_create_gmo_from_xml():
    xml = '''
    <testLsA a="1" b="2" c="3" dn="org-root/" rn="">
     <testLsB a="1" b="2" c="3" dn="org-root/" rn="" />
     <testLsC a="1" b="2" c="3" dn="org-root/" rn="" >
      <testLsD a="1" b="2" c="3" dn="org-root/" rn="" />
     </testLsC>
    </testLsA>'''
    obj = xc.from_xml_str(xml)
    assert_equal(obj.__class__.__name__, 'GenericMo')


def test_002_create_gmo_using_param_dict():
    args = {"a": 1, "b": 2, "c":3}
    obj = ucsmo.GenericMo("testLsA", "org-root", **args)
    obj1 = ucsmo.GenericMo("testLsB", "org-root", **args)
    obj.child_add(obj1)
    elem = obj.to_xml()
    xml_str = xc.to_xml_str(elem)

    expected = b'<testLsA a="1" b="2" c="3" dn="" rn=""><testLsB a="1" b="2" c="3" dn="" rn="" /></testLsA>'

    assert_equal(xml_str, expected)

def test_003_create_gmo_using_param_dict():
    args = {"a": 1, "b": 2, "c":3, "rn": "parent"}
    obj = ucsmo.GenericMo("testLsA", "org-root", **args)
    obj1 = ucsmo.GenericMo("testLsB", obj.dn, rn="child")
    obj.child_add(obj1)
    elem = obj.to_xml()
    xml_str = xc.to_xml_str(elem)

    expected = b'<testLsA a="1" b="2" c="3" dn="org-root/parent" rn="parent"><testLsB dn="org-root/parent/child" rn="child" /></testLsA>'

    assert_equal(xml_str, expected)

def test_004_create_gmo_using_parent_mo():
    args = {"a": 1, "b": 2, "c":3, "rn": "parent"}
    obj = ucsmo.GenericMo("testLsA", "org-root", **args)
    obj1 = ucsmo.GenericMo("testLsB", obj, rn="child")
    elem = obj.to_xml()
    xml_str = xc.to_xml_str(elem)

    expected = b'<testLsA a="1" b="2" c="3" dn="org-root/parent" rn="parent"><testLsB dn="org-root/parent/child" rn="child" /></testLsA>'

    assert_equal(xml_str, expected)

def test_005_create_gmo_from_xml():
    xml_str = '''
    <faultInst descr="TCA: etherTxStats totalBytesDelta = 1005,
    raised above 0" dn="sys/chassis-1/slot-1/host/port-2/fault-F35275"
    status="modified"/>
    '''
    gmo = ucsmo.generic_mo_from_xml(xml_str)
    xml_element = gmo.to_xml()
    to_xml_str = xc.to_xml_str(xml_element)

def test_006_gmo_to_mo():
    xml_str = '''
    <faultInst descr="TCA: etherTxStats totalBytesDelta = 1005,
    raised above 0" dn="sys/chassis-1/slot-1/host/port-2/fault-F35275"
    status="modified"/>
    '''

    gmo = ucsmo.generic_mo_from_xml(xml_str)
    mo = gmo.to_mo()
    assert_equal(mo.code, "F35275")




