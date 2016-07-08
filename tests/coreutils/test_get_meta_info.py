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
from ucsmsdk.ucscoreutils import get_meta_info


def test_known_class():
    meta = get_meta_info(class_id="OrGoRg")
    xml_attribute = meta.xml_attribute
    assert_equal(xml_attribute, "orgOrg")


def test_unknown_class():
    meta = get_meta_info(class_id="unknown")
    assert_equal(meta, None)


def test_known_class_props():
    meta = get_meta_info(class_id="OrGoRg")
    properties = len(meta.props)
    assert_not_equal(properties, 0)


def test_known_class_props_meta():
    meta = get_meta_info(class_id="OrGoRg")
    xml_attribute = meta.props['name'].xml_attribute
    assert_equal(xml_attribute, 'name')


def test_include_prop_false():
    meta = get_meta_info(class_id="OrGoRg", include_prop=False)
    properties = len(meta.props)
    assert_equal(properties, 0)
