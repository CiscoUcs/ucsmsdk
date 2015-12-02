# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    import xml.etree.cElementTree as ET
    from xml.etree.cElementTree import Element, SubElement
except ImportError:
    import cElementTree as ET
    from cElementTree import Element, SubElement

import ucsgenutils
import ucscoreutils
import ucsexception as ex


def to_xml_str(elem):
    return ET.tostring(elem)

def extract_root_elem(xml_str):
    root_elem = ET.fromstring(xml_str)
    return root_elem

def from_xml_str(xml_str):
    root_elem = ET.fromstring(xml_str)
    if root_elem.tag == "error":
        error_code = root_elem.attrib['errorCode']
        error_descr = root_elem.attrib['errorDescr']
        raise ex.UcsException(error_code, error_descr)

    class_id = ucsgenutils.word_u(root_elem.tag)
    response = ucscoreutils.get_ucs_obj(class_id, root_elem)
    response.from_xml(root_elem)
    return response
