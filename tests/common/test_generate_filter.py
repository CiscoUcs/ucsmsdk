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
from ucsmsdk.ucsfilter import generate_infilter
from ucsmsdk.ucsxmlcodec import to_xml_str


def test_001_not_filter():

    expected = b'<filter><not><eq class="lsServer" property="dn" value="org-root/ls-C1_B1" /></not></filter>'

    filter_str = 'not (dn,"org-root/ls-C1_B1", type="eq")'
    filter_xml = generate_infilter(class_id="LsServer",
                                   filter_str=filter_str,
                                   is_meta_class_id=True)

    xml_str = to_xml_str(filter_xml.to_xml())

    assert_equal(xml_str, expected)
