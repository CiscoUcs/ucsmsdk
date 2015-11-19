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
import ucsmethod
import ucsmo
import ucsexception as ex
from ucsmeta import MO_CLASS_ID, METHOD_CLASS_ID



def to_xml_str(xml_element):
    return ET.tostring(xml_element)


def extract_root_element(xml_str):
    root_element = ET.fromstring(xml_str)
    return root_element


def from_xml_str(xml_str):
    root_element = ET.fromstring(xml_str)
    if root_element.tag == "error":
        error_code = root_element.attrib['errorCode']
        error_descr = root_element.attrib['errorDescr']
        raise ex.UcsException(error_code, error_descr)

    class_id = ucsgenutils.word_u(root_element.tag)
    response = ucscoreutils.get_ucs_obj(class_id, root_element)
    # if class_id in METHOD_CLASS_ID:
    #     response = ucsmethod.ExternalMethod(class_id)
    # elif class_id in MO_CLASS_ID:
    #     response = ucsmo.ManagedObject(class_id)
    # else:
    #     response = ucsmo.GenericMo(class_id)
    response.from_xml(root_element)
    return response
