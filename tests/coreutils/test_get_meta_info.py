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

from ucsmsdk.ucscoreutils import get_meta_info


class TestGetMetaInfo(unittest.TestCase):
    def test_known_class(self):
        meta = get_meta_info(class_id="OrGoRg")
        xml_attribute = meta.xml_attribute
        self.assertEqual(xml_attribute, "orgOrg")

    def test_unknown_class(self):
        meta = get_meta_info(class_id="unknown")
        self.assertIsNone(meta)

    def test_known_class_props(self):
        meta = get_meta_info(class_id="OrGoRg")
        properties = len(meta.props)
        self.assertNotEqual(properties, 0)

    def test_known_class_props_meta(self):
        meta = get_meta_info(class_id="OrGoRg")
        xml_attribute = meta.props['name'].xml_attribute
        self.assertEqual(xml_attribute, 'name')

    def test_include_prop_false(self):
        meta = get_meta_info(class_id="OrGoRg", include_prop=False)
        properties = len(meta.props)
        self.assertEqual(properties, 0)

