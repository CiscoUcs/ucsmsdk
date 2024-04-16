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

import ucsmsdk.ucsxmlcodec as xc
from ucsmsdk.ucscoremeta import WriteXmlOption
import xml.etree.ElementTree as ET

class TestUnknownProps(unittest.TestCase):
    def test_001_knownmo_unknownprop(self):
        xml_str = '''
        <lsServer agentPolicyName=""
        name="ra11"
        type="instance"
        usrLbl="b"
        rn = "ls-ra11"
        unknownProps="unknown"/>'''

        obj = xc.from_xml_str(xml_str)
        obj.unknownProps = "known"
        xml_element = obj.to_xml()
        expected = b'<lsServer name="ra11" agentPolicyName="" type="instance" usrLbl="b" unknownProps="known" dn="ls-ra11" />'
        result_str = xc.to_xml_str(xml_element)
        expected_xml_str = xc.to_xml_str(ET.fromstring(expected))
        self.assertEqual(result_str, expected_xml_str)

    def test_002_knownmo_unknownprop(self):
        xml_str = '''
        <lsServer agentPolicyName=""
        name="ra11"
        type="instance"
        usrLbl="b"
        rn = "ls-ra11"
        unknownProps="unknown"/>'''

        obj = xc.from_xml_str(xml_str)
        obj.unknownProps = "known"
        xml_element = obj.to_xml(option=WriteXmlOption.DIRTY)
        print(xc.to_xml_str(xml_element))
