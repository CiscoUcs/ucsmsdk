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

import unittest
import xml.etree.ElementTree as ET

import ucsmsdk.ucsxmlcodec as xc
import ucsmsdk.ucsmo as ucsmo


class TestUcsgMo(unittest.TestCase):
    def test_001_create_gmo_from_xml(self):
        xml = '''
        <testLsA a="1" b="2" c="3" dn="org-root/" rn="">
         <testLsB a="1" b="2" c="3" dn="org-root/" rn="" />
         <testLsC a="1" b="2" c="3" dn="org-root/" rn="" >
          <testLsD a="1" b="2" c="3" dn="org-root/" rn="" />
         </testLsC>
        </testLsA>'''
        obj = xc.from_xml_str(xml)
        self.assertEqual(obj.__class__.__name__, 'GenericMo')

    def test_002_create_gmo_using_param_dict(self):
        args = {"a": 1, "b": 2, "c":3}
        obj = ucsmo.GenericMo("testLsA", "org-root", **args)
        obj1 = ucsmo.GenericMo("testLsB", "org-root", **args)
        obj.child_add(obj1)
        elem = obj.to_xml()
        xml_str = xc.to_xml_str(elem)

        expected = b'<testLsA a="1" b="2" c="3" rn="" dn=""><testLsB a="1" b="2" c="3" rn="" dn="" /></testLsA>'
        expected_xml_str = xc.to_xml_str(ET.fromstring(expected))
        self.assertEqual(xml_str, expected_xml_str)

    def test_003_create_gmo_using_param_dict(self):
        args = {"a": 1, "b": 2, "c":3, "rn": "parent"}
        obj = ucsmo.GenericMo("testLsA", "org-root", **args)
        obj1 = ucsmo.GenericMo("testLsB", obj.dn, rn="child")
        obj.child_add(obj1)
        elem = obj.to_xml()
        xml_str = xc.to_xml_str(elem)

        expected = b'<testLsA a="1" b="2" c="3" rn="parent" dn="org-root/parent"><testLsB rn="child" dn="org-root/parent/child" /></testLsA>'
        expected_xml_str = xc.to_xml_str(ET.fromstring(expected))
        self.assertEqual(xml_str, expected_xml_str)

    def test_004_create_gmo_using_parent_mo(self):
        args = {"a": 1, "b": 2, "c":3, "rn": "parent"}
        obj = ucsmo.GenericMo("testLsA", "org-root", **args)
        obj1 = ucsmo.GenericMo("testLsB", obj, rn="child")
        elem = obj.to_xml()
        xml_str = xc.to_xml_str(elem)

        expected = b'<testLsA a="1" b="2" c="3" rn="parent" dn="org-root/parent"><testLsB rn="child" dn="org-root/parent/child" /></testLsA>'
        expected_xml_str = xc.to_xml_str(ET.fromstring(expected))
        self.assertEqual(xml_str, expected_xml_str)
       

    def test_005_create_gmo_from_xml(self):
        xml_str = '''
        <faultInst descr="TCA: etherTxStats totalBytesDelta = 1005,
        raised above 0" dn="sys/chassis-1/slot-1/host/port-2/fault-F35275"
        status="modified"/>
        '''
        gmo = ucsmo.generic_mo_from_xml(xml_str)
        xml_element = gmo.to_xml()
        to_xml_str = xc.to_xml_str(xml_element)

    def test_006_gmo_to_mo(self):
        xml_str = '''
        <faultInst descr="TCA: etherTxStats totalBytesDelta = 1005,
        raised above 0" dn="sys/chassis-1/slot-1/host/port-2/fault-F35275"
        status="modified"/>
        '''

        gmo = ucsmo.generic_mo_from_xml(xml_str)
        mo = gmo.to_mo()
        self.assertEqual(mo.code, "F35275")

