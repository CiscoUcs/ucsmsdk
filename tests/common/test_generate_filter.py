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

from ucsmsdk.ucsfilter import generate_infilter
from ucsmsdk.ucsxmlcodec import to_xml_str


class TestGenerateFilter(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.success = True

    def ls_filter(self):
        filter_ = generate_infilter(class_id="lsServer",
                                    filter_str='(type, "instance", type="eq")',
                                    is_meta_class_id=True)
        expected = b'<filter><eq class="lsServer" property="type" ' \
                   b'value="instance" /></filter>'
        if to_xml_str(filter_.to_xml()) != expected:
            self.success = False

    def org_filter(self):
        filter_ = generate_infilter(class_id="orgOrg",
                                    filter_str='(descr, "oroorg", type="eq")',
                                    is_meta_class_id=True)
        expected = b'<filter><eq class="orgOrg" property="descr" ' \
                   b'value="oroorg" /></filter>'
        if to_xml_str(filter_.to_xml()) != expected:
            self.success = False

    def test_001_not_filter(self):
        expected = b'<filter><not><eq class="lsServer" property="dn" ' \
                    b'value="org-root/ls-C1_B1" /></not></filter>'

        filter_str = 'not (dn,"org-root/ls-C1_B1", type="eq")'
        filter_xml = generate_infilter(class_id="LsServer",
                                       filter_str=filter_str,
                                       is_meta_class_id=True)

        xml_str = to_xml_str(filter_xml.to_xml())

        self.assertEqual(xml_str, expected)

    def test_002_multi_thread_filter(self):
        import threading
        import time

        for i in range(1, 50):
            if i % 2 != 0:
                target = self.ls_filter
            else:
                target = self.org_filter

            thread = threading.Thread(name=i, target=target)
            thread.start()

        while len(threading.enumerate()) > 1:
            time.sleep(1)

        self.assertTrue(self.success)

    def test_003_mixed_filter(self):
        expected = b'<filter>' \
                   b'<not>' \
                   b'<or>' \
                   b'<eq class="lsServer" property="type" value="instance" />' \
                   b'<and><eq class="lsServer" property="usrLbl" ' \
                   b'value="lsserver" />' \
                   b'<not><wcard class="lsServer" property="descr" ' \
                   b'value="description" />' \
                   b'</not>' \
                   b'</and>' \
                   b'</or>' \
                   b'</not>' \
                   b'</filter>'

        filter_str = 'not(' \
                     '(type, "instance", type="eq") or ' \
                     '(usr_lbl, "lsserver", type="eq") and ' \
                     'not(descr, "description", type="re"))'
        filter_xml = generate_infilter(class_id="LsServer",
                                       filter_str=filter_str,
                                       is_meta_class_id=True)

        xml_str = to_xml_str(filter_xml.to_xml())

        self.assertEqual(xml_str, expected)

