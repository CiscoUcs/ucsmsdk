# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License prop
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module contains the UcsSdk Core classes.
"""

from __future__ import absolute_import
from .ucscore import UcsBase
from . import ucscoreutils
from . import ucsgenutils


try:
    import xml.etree.cElementTree as ET
    from xml.etree.cElementTree import Element, SubElement
except ImportError:
    import cElementTree as ET
    from cElementTree import Element, SubElement

import logging

log = logging.getLogger('ucs')


class ExternalMethod(UcsBase):
    """
    This class represents the UCS Central Xml api's query/configuration
    methods.
    """

    _external_method_attrs = {'errorCode': 'error_code',
                              'errorDescr': 'error_descr',
                              'invocationResult': 'invocation_result',
                              'response': 'response'}

    def __init__(self, method_id):
        # """ __init__ of the UcsBase class """
        UcsBase.__init__(self, method_id)

        meta_module = ucscoreutils.load_module(method_id)
        self.__method_meta = getattr(meta_module, "method_meta")
        self.__property_meta = getattr(meta_module, "prop_meta")
        self.__property_map = getattr(meta_module, "prop_map")

        # """ instantiate class variables """
        # for prop in CoreUtils.get_property_list(self._class_id):
        #     if prop != "Meta":
        #         self.__dict__[prop] = None
        for prop in self.__property_meta:
            self.__dict__[prop] = None

        self.error_code = 0
        self.error_descr = None
        self.invocation_result = None
        self.response = None
        self.mark_clean()

    def child_add(self, mo):
        """ This method adds child external method object to a
        external method object. """
        self._child.append(mo)

    def set_attr(self, key, value):
        """ This method sets the attribute of external method object."""
        if key in self.__property_meta:
            self.__dict__[key] = value
        elif key == 'error_code':
            self.error_code = value
        elif key == 'error_descr':
            self.error_descr = value
        elif key == 'invocation_result':
            self.invocation_result = value
        elif key == 'response':
            self.response = value
        else:
            # """ no such property """
            return None
            # raise AttributeError

    def get_error_response(self, error_code, error_descr):
        """ This methods sets error attributes of an external
         method object. """
        self.error_code = error_code
        self.error_descr = error_descr
        self.response = "yes"
        # return self

    def to_xml(self, xml_doc=None, option=None, elem_name=None):
        """ Method writes the xml representation of the external
        method object. """
        xml_obj = self.elem_create(
            class_tag=self.__method_meta.xml_attribute, xml_doc=xml_doc,
            override_tag=elem_name)

        for prop in self.__property_meta:
            if xml_obj.tag == "aaaLogout" and prop == "in_delay_secs" \
               and int(getattr(self, prop)) > 300:
                continue
            prop_meta = self.__property_meta[prop]
            if prop_meta.inp_out == "Output":
                continue
            if prop_meta.is_complex_type:
                if getattr(self, prop) is not None:
                    self.__dict__[prop].to_xml(xml_obj, option,
                                               prop_meta.xml_attribute)
            elif getattr(self, prop) is not None:
                xml_obj.set(prop_meta.xml_attribute, getattr(self, prop))

        self.child_to_xml(xml_obj, option)
        return xml_obj

    # , handle, modify_self=False, mo=None):
    def from_xml(self, elem, handle=None):
        """Method updates/fills the object from the xml representation
        of the external method object. """

        self._handle = handle
        if elem.attrib:
            for attr_name, attr_value in ucsgenutils.iteritems(elem.attrib):
                if attr_name in self.__property_map:
                    attr = self.__property_map[attr_name]
                    method_prop_meta = self.__property_meta[attr]
                    if method_prop_meta.inp_out == "Input" or (
                            method_prop_meta.is_complex_type):
                        continue
                    self.set_attr(attr, str(attr_value))
                elif attr_name in ExternalMethod._external_method_attrs:
                    self.set_attr(
                        ExternalMethod._external_method_attrs[attr_name],
                        str(attr_value))

        child_elems = list(elem)
        if child_elems:
            for child_elem in child_elems:
                if not ET.iselement(child_elem):
                    continue
                child_name = child_elem.tag
                if child_name in self.__property_map:
                    child_name = self.__property_map[child_name]
                    method_prop_meta = self.__property_meta[
                        child_name]
                    if method_prop_meta.inp_out == "Output" and \
                            (method_prop_meta.is_complex_type):
                        child_obj = ucscoreutils.get_ucs_obj(
                            method_prop_meta.field_type,
                            child_elem)
                        if child_obj is not None:
                            self.set_attr(child_name,
                                          child_obj)
                            child_obj.from_xml(child_elem, handle)

    def __str__(self):
        tab_size = 8
        out_str = "\n"
        out_str += "External Method\t\t\t:\t" + str(self._class_id) + "\n"
        out_str += "-" * len("External Method") + "\n"
        for prop, prop_value in sorted(ucsgenutils.iteritems(self.__dict__)):
            if "ExternalMethod" in prop:
                continue
            out_str += str(prop).ljust(tab_size * 4) + ':' + str(
                prop_value) + "\n"

        return out_str
