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

from . import ucsgenutils
from . import ucscoreutils
from . import ucsexception as ex


def to_xml_str(elem):
    """
    Converts xml element to xml string.

    Args:
        elem (xml element)

    Returns:
        xml string

    Example:
        xml_str = to_xml_str(elem=xml_element)
    """

    return ET.tostring(elem)


def extract_root_elem(xml_str=None, xml_file=None):
    """
    extracts root xml element from xml string or file.

    Args:
        xml_str (str): xml string or None
        xml_file (str): xml file full path or None

    Returns:
        xml element

    Example:
        xml_str='''
        <lsClone dn="org-root/ls-testsp" inHierarchical="false"
        inServerName="test" inTargetOrg="">
        </lsClone>
        '''
        root_element = extract_root_elem(xml_str)
    """

    if xml_str:
        return ET.fromstring(xml_str)
    elif xml_file:
        tree = ET.parse(xml_file)
        return tree.getroot()


def from_xml_str(xml_str, handle=None):
    """
    Generates response object from the given xml string.

    Args:
        xml_str (str): xml string

    Returns:
        object (external method or managed object or generic managed object)

    Example:
        xml_str='''\n
        <lsServer dn="org-root/ls-testsp" dynamicConPolicyName="test"\n
        extIPPoolName="ext-mgmt" name="testsp" />\n
        '''\n
        root_element = extract_root_elem(xml_str)\n
    """

    root_elem = ET.fromstring(xml_str)
    if root_elem.tag == "error":
        error_code = root_elem.attrib['errorCode']
        error_descr = root_elem.attrib['errorDescr']
        raise ex.UcsException(error_code, error_descr)

    class_id = ucsgenutils.word_u(root_elem.tag)
    response = ucscoreutils.get_ucs_obj(class_id, root_elem)
    response.from_xml(root_elem, handle)
    return response


def convert_dict_to_xml(tag, **attrs):
    """
    Converts dict to xml string.

    Args:
        tag (xml element tag)

    Returns:
        xml string

    Example:
        xml_str = convert_dict_to_xml(tag='ucselement', **dict)
    """

    root = Element(tag, **attrs)
    return ET.tostring(root)
