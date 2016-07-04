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

import logging

from . import ucsgenutils
from . import ucscoreutils

try:
    import xml.etree.cElementTree as ET
    from xml.etree.cElementTree import Element, SubElement
except ImportError:
    import cElementTree as ET
    from cElementTree import Element, SubElement

log = logging.getLogger('ucs')


class UcsBase(object):
    """
    This class acts as the base class for ManagedObject, ExternalMethod
    and AbstractFilter and BaseObject classes.
    """

    def __init__(self, class_id):
        self._class_id = class_id
        self._child = []
        self._handle = None

    @property
    def child(self):
        """Getter Method of UcsBase Class"""
        return self._child

    @property
    def dirty_mask(self):
        """Getter Method of UcsBase Class"""
        return self._dirty_mask

    def get_class_id(self):
        return self._class_id

    def get_handle(self):
        return self._handle

    def child_add(self, obj):
        """Method adds the child managed object."""
        self._child.append(obj)

    def child_remove(self, obj):
        """Method removes the child managed object."""
        self._child.remove(obj)

    def child_count(self):
        """Method returns the child managed object count."""
        return len(self._child)

    def child_to_xml(self, xml_doc, option=None):
        """Method writes the xml representation for the object."""
        for child in self._child:
            child.to_xml(xml_doc, option)

    def child_is_dirty(self):
        """Method checks whether the child object is dirty or not."""
        for child in self._child:
            if child.is_dirty():
                return True
        return False

    def child_mark_clean(self):
        """Method Method cleans the dirty mask of child managed object."""
        for child in self._child:
            child.mark_clean()

    def mark_clean(self):
        """Method cleans the dirty mask of the managed object."""
        self._dirty_mask = 0

    def is_dirty(self):
        """Method checks whether the object is dirty or not."""
        return self.child_is_dirty()

    def write_object(self):
        """Method writes the string representation of the object."""
        for child in self._child:
            if child is not None:
                child.write_object()

    def clone(self):
        """ Method returns the clone of the Managed Object. """
        import copy

        return copy.deepcopy(self)

    def __deepcopy__(self, memo):
        """ Overridden method to support deepcopy of Managed Object. """
        import copy

        clone = copy.copy(self)
        clone_child = []
        for child in clone._child:
            clone_child.append(copy.deepcopy(child))
        clone._child = clone_child
        return clone

    def attr_set(self, key, value):
        """This method sets attribute value of the Method object."""
        self.__dict__[key] = value

    def attr_get(self, key):
        """This method gets attribute value of the Method object."""
        return self.__dict__[key]

    def elem_create(self, class_tag, xml_doc=None, override_tag=None):
        if xml_doc is None:
            xml_obj = Element(class_tag)
        else:
            if override_tag:
                xml_obj = SubElement(xml_doc, override_tag)
            else:
                xml_obj = SubElement(xml_doc, class_tag)
        return xml_obj

    def _not_mo_prop(self, prop):
        pass

    def __get_prop_dict(self):

        prop_dict = {}
        for prop, prop_value in sorted(ucsgenutils.iteritems(self.__dict__)):
            if self._not_mo_prop(prop):
                continue
            prop_dict[prop] = prop_value

        return prop_dict

    def to_dict(self, include_children=True, depth=None, level=0):

        mo_dict = {self._class_id: None}
        prop_dict = self.__get_prop_dict()

        if not self._child or not include_children:
            mo_dict[self._class_id] = prop_dict
            return mo_dict

        level += 1
        if depth is None or level < depth:
            prop_dict['child'] = []
            for ch in self._child:
                prop_dict['child'].append(ch.to_dict(include_children,
                                                     depth,
                                                     level))

        mo_dict[self._class_id] = prop_dict
        return mo_dict

    def to_json(self, include_children=True, depth=None):
        import json

        return json.dumps(self.to_dict(include_children, depth),
                          indent=2,
                          sort_keys=True)


class AbstractFilter(UcsBase):
    """class AbstractFilter."""

    def __init__(self, class_id, tag_name=None):
        self._tag_name = tag_name
        UcsBase.__init__(self, class_id)

    def to_xml(self, xml_doc=None, option=None, elem_name=None):
        """This method writes the xml representation of the Method object."""
        xml_obj = self.elem_create(class_tag=self._tag_name,
                                   xml_doc=xml_doc,
                                   override_tag=elem_name)
        for key in self.__dict__:
            if key.startswith("_"):
                continue
            elif key == "class_":
                xml_obj.set("class", self.attr_get(key))
            else:
                xml_obj.set(key, self.attr_get(key))

        self.child_to_xml(xml_obj, option)
        return xml_obj


class BaseObject(UcsBase):
    """class BaseObject."""

    def __init__(self, class_id, tag_name=None):
        self._tag_name = tag_name
        UcsBase.__init__(self, class_id)

    def to_xml(self, xml_doc=None, option=None, elem_name=None):
        """This method writes the xml representation of the Method object."""
        xml_obj = self.elem_create(class_tag=self._tag_name,
                                   xml_doc=xml_doc,
                                   override_tag=elem_name)
        for key in self.__dict__:
            if key.startswith("_"):
                continue
            else:
                xml_obj.set(key, self.attr_get(key))

        self.child_to_xml(xml_obj, option)
        return xml_obj

    def from_xml(self, elem, handle=None):
        """This method creates the object from the xml representation
        of the Method object."""

        self._handle = handle
        if elem.attrib:
            for attr_name, attr_value in ucsgenutils.iteritems(elem.attrib):
                self.attr_set(ucsgenutils.convert_to_python_var_name(
                    attr_name), str(attr_value))

        child_elems = elem.getchildren()
        if child_elems:
            for child_elem in child_elems:
                if not ET.iselement(child_elem):
                    continue

                cln = ucsgenutils.word_u(child_elem.tag)
                child = ucscoreutils.get_ucs_obj(cln, child_elem)
                self._child.append(child)
                child.from_xml(child_elem, handle)
