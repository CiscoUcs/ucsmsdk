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

from __future__ import print_function

from nose.tools import assert_equal 
import ucsmsdk.ucsxmlcodec as xc
from ucsmsdk.ucscoremeta import WriteXmlOption


def test_001_knownmo_unknownprop():
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
    expected = b'<lsServer agentPolicyName="" dn="ls-ra11" name="ra11" type="instance" unknownProps="known" usrLbl="b" />'
    result_str = xc.to_xml_str(xml_element)
    assert_equal(result_str, expected)


def test_002_knownmo_unknownprop():
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
