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
This module contains the ManagedObject and GenericManagedObject Class.
"""

from __future__ import print_function

import logging
import os

from . import ucsgenutils
from . import ucscoreutils
from . import ucscoremeta
import six

try:
    import xml.etree.cElementTree as ET
    from xml.etree.cElementTree import Element, SubElement
except ImportError:
    import cElementTree as ET
    from cElementTree import Element, SubElement

from .ucscoremeta import WriteXmlOption
from .ucsexception import UcsValidationException, UcsWarning
from .ucscore import UcsBase

log = logging.getLogger('ucs')


class _GenericProp():
    """
    Internal class to handle the unknown property.
    """

    def __init__(self, name, value, is_dirty):
        self.name = name
        self.value = value
        self.is_dirty = is_dirty


class ManagedObject(UcsBase):
    """
    This class structures/represents all the managed objects.
    """

    DUMMY_DIRTY = "0x1"
    __internal_prop = frozenset(
        ["_dirty_mask", "_class_id", "_child", "_handle", ''])

    def __init__(
            self,
            class_id,
            parent_mo_or_dn=None,
            from_xml_response=False,
            **kwargs):
        self.__parent_mo = None
        self.__status = None
        self.__parent_dn = None
        self.__xtra_props = {}
        self.__xtra_props_dirty_mask = 0x1

        self._set_parent_mo_or_dn(parent_mo_or_dn)

        self._rn_set(from_xml_response)
        self._dn_set(from_xml_response)

        UcsBase.__init__(self, ucsgenutils.word_u(self.mo_meta.xml_attribute))

        self._set_child_of_parent_mo()
        self._set_mo_prop_value(kwargs)

    def _set_parent_mo_or_dn(self, parent_mo_or_dn):
        if not parent_mo_or_dn:
            return

        if isinstance(parent_mo_or_dn, ManagedObject):
            self.__parent_mo = parent_mo_or_dn
            self.__parent_dn = parent_mo_or_dn.dn
        elif isinstance(parent_mo_or_dn, str) or isinstance(parent_mo_or_dn, six.text_type):
            self.__parent_dn = str(parent_mo_or_dn)
        else:
            raise ValueError('parent mo or dn must be specified')

    def _set_child_of_parent_mo(self):
        if self.__parent_mo:
            self.__parent_mo.child_add(self)

    def _set_mo_prop_value(self, kwargs):
        if kwargs:
            for prop_name, prop_value in ucsgenutils.iteritems(kwargs):
                if self._is_unknown_property(prop_name):
                    log.debug("Unknown property %s" % prop_name)
                if prop_value is not None:
                    self.__set_prop(prop_name, prop_value)

    def _is_unknown_property(self, prop):
        return prop not in self.prop_meta

    def check_prop_match(self, **kwargs):
        for prop_name in kwargs:
            if self._is_unknown_property(prop_name):
                raise ValueError("Unknown Property Name Exception - "
                                 "Class [%s]: Prop <%s> "
                                 % (self.__class__.__name__, prop_name))

            if kwargs[prop_name] is not None and \
                    kwargs[prop_name] != getattr(self, prop_name):
                return False
        return True

    def set_prop_multiple(self, **kwargs):
        for prop_name in kwargs:
            if self._is_unknown_property(prop_name):
                UcsWarning("Unknown Property Name for "
                           "Class [%s]: Prop <%s>, setting it forcefully"
                           % (self.__class__.__name__, prop_name))
                self.__set_prop(prop_name, kwargs[prop_name], forced=True)
            else:
                self.__set_prop(prop_name, kwargs[prop_name])

    @property
    def parent_mo(self):
        """Getter method of ManagedObject Class"""

        return self.__parent_mo

    def _rn_set(self, from_xml_response=False):
        """
        Internal method to set rn
        """

        if from_xml_response:
            return

        if "prop_meta" in dir(self) and "rn" in self.prop_meta:
            self.rn = self.make_rn()
        else:
            self.rn = ""

    def _dn_set(self, from_xml_response=False):
        """
        Internal method to set dn
        """

        if from_xml_response:
            return

        if "prop_meta" in dir(self) and "dn" in self.prop_meta:
            if self.__parent_dn:
                self.dn = self.__parent_dn + '/' + self.rn
            else:
                self.dn = self.rn
        else:
            self.dn = ""

    def __setattr__(self, name, value):
        """
        overridden setattr method
        """

        if "prop_meta" in dir(self) and name in self.prop_meta:
            if name in dir(self):
                self.__set_prop(name, value)
            else:
                if value:
                    if not self.prop_meta[name].validate_property_value(value):
                        raise ValueError("Invalid Value Exception - "
                                         "[%s]: Prop <%s>, Value<%s>. "
                                         % (self.__class__.__name__,
                                            name,
                                            value))
                object.__setattr__(self, name, value)
                if self.prop_meta[name].mask is not None:
                    self._dirty_mask |= self.prop_meta[name].mask
        elif name.startswith("_"):
            object.__setattr__(self, name, value)
        else:
            # These are properties which the current version of ucsmsdk
            # does not know of.
            # The code will come here lot often, when using older version of
            # ucsmsdk with newer releases on the UCS.
            # This needs to be handled so that the same sdk can work across
            # multiple ucs releases
            self.__xtra_props[name] = _GenericProp(name, value, True)
            self._dirty_mask |= self.__xtra_props_dirty_mask
            object.__setattr__(self, name, value)

    def __set_prop(self, name, value, mark_dirty=True, forced=False):
        """
        Internal method to set the properties after validation

        Args:
            name (str): property name
            value (str): property value
            mark_dirty (bool): if True, property will be part of xml request
            forced (bool): if True, set the value without validation

        Returns:
            None
        """

        if not forced:
            prop_meta = self.prop_meta[name]
            if prop_meta.access != ucscoremeta.MoPropertyMeta.READ_WRITE:
                if getattr(self, name) is not None or \
                        prop_meta.access != \
                        ucscoremeta.MoPropertyMeta.CREATE_ONLY:
                    raise ValueError("%s is not a read-write property." % name)
            if value and not prop_meta.validate_property_value(value):
                raise ValueError("Invalid Value Exception - "
                                 "[%s]: Prop <%s>, Value<%s>. "
                                 % (self.__class__.__name__,
                                    name,
                                    value))
                # return False
            if prop_meta.mask and mark_dirty:
                self._dirty_mask |= prop_meta.mask
        object.__setattr__(self, name, value)

    def __json__(self):
        # return the json dict
        dict = {'class_id': self._class_id}
        for prop, prop_value in sorted(ucsgenutils.iteritems(self.__dict__)):
            if prop in ManagedObject.__internal_prop or prop.startswith(
                    "_ManagedObject__"):
                continue
            if prop in self.__xtra_props:
                prop = "[X]" + str(prop)
                dict[prop] = prop_value
            else:
                dict[prop] = prop_value

        return dict

    def __str__(self):
        """
        Method to return string representation of a managed object.
        """

        ts = 8
        out_str = "\n"
        out_str += "Managed Object\t\t\t:\t" + str(self._class_id) + "\n"
        out_str += "-" * len("Managed Object") + "\n"

        for prop, prop_value in ucsgenutils.iteritems(self.__json__()):
            out_str += str(prop).ljust(ts * 4) + ':' + str(
                prop_value) + "\n"
        # print unknown properties
        # for prop, prop_value in six.iteritems(self.__xtra_props):
        #     prop = "[X]" + str(prop)
        #     out_str += str(prop).ljust(ts * 4) + ':' + str(
        #         prop_value) + "\n"

        out_str += "\n"
        return out_str

    def mark_dirty(self):
        """
        This method marks the managed object dirty.
        """

        if self.__class__.__name__ == "ManagedObject" and not self.is_dirty():
            self._dirty_mask = ManagedObject.DUMMY_DIRTY
        elif "mo_meta" in dir(self):
            self._dirty_mask = self.mo_meta.mask

    def is_dirty(self):
        """
        This method checks if managed object is dirty.
        """

        return self._dirty_mask != 0 or self.child_is_dirty()

    # Ideally an rn should never change across ucsm releases.
    # but we do have some of these cases
    # These cause an issue, because we cannot parse them
    # the below is a special case to handle these cases
    def rn_is_special_case(self):
        """
        Method to handle if rn pattern is different across UCS Version
        """

        if self.__class__.__name__ == "StorageLocalDiskPartition":
            return True
        return False

    def rn_get_special_case(self):
        """
        Method to handle if rn pattern is different across UCS Version
        """

        if self.__class__.__name__ == "StorageLocalDiskPartition":
            # some version of ucs have rn "partition" instead of "partition-id"
            return "partition"

    def make_rn(self):
        """
        This method returns the Rn for a managed object.
        """

        import re

        rn_pattern = self.mo_meta.rn
        for prop in re.findall(r"""\[([^\]]*)\]""", rn_pattern):
            if prop in self.prop_meta:
                if getattr(self, prop):
                    rn_pattern = re.sub(r"""\[%s\]""" % prop,
                                        '%s' % getattr(self, prop), rn_pattern)
                else:
                    log.debug('Property "%s" was None in make_rn' % prop)
                    if self.rn_is_special_case():
                        return self.rn_get_special_case()
                    raise UcsValidationException(
                        'Property "%s" was None in make_rn' % prop)
            else:
                log.debug(
                    'Property "%s" was not found in make_rn arguments' % prop)
                if self.rn_is_special_case():
                    return self.rn_get_special_case()
                raise UcsValidationException(
                    'Property "%s" was not found in make_rn arguments' % prop)

        return rn_pattern

    def to_xml(self, xml_doc=None, option=None, elem_name=None):
        """
        Method writes the xml representation of the managed object.
        """

        if option == WriteXmlOption.DIRTY and not self.is_dirty():
            log.debug("Object is not dirty")
            return

        xml_obj = self.elem_create(class_tag=self.mo_meta.xml_attribute,
                                   xml_doc=xml_doc,
                                   override_tag=elem_name)

        for key in self.__dict__:
            if key != 'rn' and key in self.prop_meta:
                mo_prop_meta = self.prop_meta[key]
                if (option != WriteXmlOption.DIRTY or (
                    mo_prop_meta.mask is not None and
                        self._dirty_mask & mo_prop_meta.mask != 0)):
                    value = getattr(self, key)
                    if value is not None:
                        xml_obj.set(mo_prop_meta.xml_attribute, value)
            else:
                if key not in self.__xtra_props:
                    # This is an internal property
                    # This should not be a part of the xml
                    continue

                # This is an unknown property
                # This should be a part of the xml
                # The server might understand this property, even though
                # the sdk does not
                if option != WriteXmlOption.DIRTY or \
                        self.__xtra_props[key].is_dirty:
                    value = self.__xtra_props[key].value
                    if value is not None:
                        xml_obj.set(key, value)

        if 'dn' not in xml_obj.attrib:
            xml_obj.set('dn', self.dn)

        self.child_to_xml(xml_obj, option)
        return xml_obj

    def from_xml(self, elem, handle=None):
        """
        Method updates the object from the xml representation of the managed
        object.
        """

        self._handle = handle
        if elem.attrib:
            if self.__class__.__name__ != "ManagedObject":
                for attr_name, attr_value in ucsgenutils.iteritems(
                        elem.attrib):
                    if attr_name in self.prop_map:
                        attr_name = self.prop_map[attr_name]
                    else:
                        self.__xtra_props[attr_name] = _GenericProp(
                            attr_name,
                            attr_value,
                            False)
                    object.__setattr__(self, attr_name, attr_value)
            else:
                for attr_name, attr_value in ucsgenutils.iteritems(
                        elem.attrib):
                    object.__setattr__(self, attr_name, attr_value)

        if hasattr(self, 'rn') and not hasattr(self, 'dn'):
            self._dn_set()
        elif not hasattr(self, 'rn') and hasattr(self, 'dn'):
            self.__set_prop("rn", os.path.basename(self.dn), forced=True)
        self.mark_clean()

        child_elems = list(elem)
        if child_elems:
            for child_elem in child_elems:
                if not ET.iselement(child_elem):
                    continue

                if self.__class__.__name__ != "ManagedObject" and (
                        child_elem.tag in self.mo_meta.field_names):
                    pass

                class_id = ucsgenutils.word_u(child_elem.tag)
                child_obj = ucscoreutils.get_ucs_obj(class_id, child_elem,
                                                     self)
                self.child_add(child_obj)
                child_obj.from_xml(child_elem, handle)

    def sync_mo(self, mo):
        """
        Method to return string representation of a managed object.
        """

        for prop, prop_value in sorted(ucsgenutils.iteritems(self.__dict__)):
            if prop in ManagedObject.__internal_prop or prop.startswith(
                    "_ManagedObject__"):
                continue
            mo.__dict__[prop] = prop_value
        return None

    def show_tree(self, level=0):
        """
        Method to return string representation of a managed object.
        """

        indent = "  "
        level_indent = "%s%s)" % (indent * level, level)
        # level_key_dn = "level_%s_dn" % (str(level))
        print("%s %s[%s]" % (level_indent, self._class_id, self.dn))
        for ch_ in self.children:
            level += 1
            ch_.show_tree(level)
            level -= 1
        return None

    def show_hierarchy(self, level=0, depth=None, show_level=[]):
        """
        Method to return string representation of a managed object.
        """

        from .ucscoreutils import print_mo_hierarchy

        print_mo_hierarchy(self._class_id, level, depth,
                           show_level)


def generic_mo_from_xml(xml_str):
    """
    create GenericMo object from xml string
    """
    root_elem = ET.fromstring(xml_str)
    class_id = root_elem.tag
    gmo = GenericMo(class_id)
    gmo.from_xml(root_elem)
    return gmo


def generic_mo_from_xml_elem(elem):
    """
    create GenericMo object from xml element
    """

    from . import ucsxmlcodec as xc
    xml_str = xc.to_xml_str(elem)
    gmo = generic_mo_from_xml(xml_str)
    return gmo


class GenericMo(UcsBase):
    """
    This class implements a Generic Managed Object.

    Args:
        class_id (str): class id of managed object
        parent_mo_or_dn (ManagedObject or str): parent managed object or dn
    """

    # Every variable that should not be a part of the final xml
    # should start with a underscore in this class
    def __init__(self, class_id, parent_mo_or_dn=None, **kwargs):

        self.__properties = {}

        if isinstance(parent_mo_or_dn, GenericMo):
            self.__parent_mo = parent_mo_or_dn
            self.__parent_dn = parent_mo_or_dn.dn
        elif isinstance(parent_mo_or_dn, str):
            # if (parent_mo_or_dn == "") and ("dn" in kwargs):
            #     parent_mo_or_dn = kwargs["dn"]
            self.__parent_dn = parent_mo_or_dn
            self.__parent_mo = None
        elif parent_mo_or_dn is None:
            self.__parent_dn = ""
            self.__parent_mo = None
        else:
            raise ValueError("parent_mo_or_dn should be an instance of str or "
                             "GenericMo")

        UcsBase.__init__(self, class_id)

        if kwargs:
            for key, value in ucsgenutils.iteritems(kwargs):
                self.__dict__[key] = str(value)
                self.__properties[key] = str(value)

        if 'rn' in dir(self) and 'dn' in dir(self):
            pass
        elif 'rn' in dir(self) and 'dn' not in dir(self):
            if self.__parent_dn is not None and self.__parent_dn != "":
                self.dn = self.__parent_dn + '/' + self.rn
                self.__properties['dn'] = self.dn
            else:
                self.dn = self.rn
                self.__properties['dn'] = self.dn
        elif 'rn' not in dir(self) and 'dn' in dir(self):
            self.rn = os.path.basename(self.dn)
            self.__properties['rn'] = self.rn
        else:
            self.rn = ""
            self.dn = ""

        if self.__parent_mo:
            self.__parent_mo.child_add(self)

    def to_xml(self, xml_doc=None, option=None):
        """
        This method returns the xml element node for the current object
        with it's hierarchy.

        Args:
            xml_doc: document to which the Mo attributes are added.
                    Can be None.
            option: not required for Generic Mo class object

        Example:
            from ucsmsdk.ucsmo import GenericMo\n
            args = {"a": 1, "b": 2, "c":3}\n
            obj = GenericMo("testLsA", "org-root", **args)\n
            obj1 = GenericMo("testLsB", "org-root", **args)\n
            obj.add_child(obj1)\n
            elem = obj.write_xml()\n

            import ucsmsdk.ucsxmlcodec as xc\n
            xc.to_xml_str(elem)\n

        Output:
            '<testLsA a="1" b="2" c="3" dn="org-root/" rn="">\n
                <testLsB a="1" b="2" c="3" dn="org-root/" rn="" />\n
            </testLsA>'
        """

        if xml_doc is None:
            xml_obj = Element(ucsgenutils.word_l(self._class_id))
        else:
            xml_obj = SubElement(xml_doc, ucsgenutils.word_l(self._class_id))
        for key in self.__dict__:
            if not key.startswith('_'):
                xml_obj.set(key, getattr(self, key))
        self.child_to_xml(xml_obj)
        return xml_obj

    @property
    def properties(self):
        """Getter Method of GenericMO Class"""
        return self.__properties

    def from_xml(self, elem, handle=None):
        """
        This method is form objects out of xml element.
        This is called internally from ucsxmlcode.from_xml_str
        method.

        Example:
            xml = '<testLsA a="1" b="2" c="3" dn="org-root/" rn="">
            <testLsB a="1" b="2" c="3" dn="org-root/" rn="" /></testLsA>'\n
            obj = xc.from_xml_str(xml)\n

            print type(obj)\n

        Outputs:
            <class 'ucsmsdk.ucsmo.GenericMo'>
        """

        if elem is None:
            return None

        self._handle = handle
        self._class_id = elem.tag
        if elem.attrib:
            for name, value in ucsgenutils.iteritems(elem.attrib):
                self.__dict__[name] = value
                self.__properties[name] = str(value)

        if self.rn and self.dn:
            pass
        elif self.rn and not self.dn:
            if self.__parent_dn is not None and self.__parent_dn != "":
                self.dn = self.__parent_dn + '/' + self.rn
                self.__properties['dn'] = self.dn
            else:
                self.dn = self.rn
                self.__properties['dn'] = self.dn
        elif not self.rn and self.dn:
            self.rn = os.path.basename(self.dn)
            self.__properties['rn'] = self.rn
        # else:
        #     raise ValueError("Both rn and dn does not present.")

        children = list(elem)
        if children:
            for child in children:
                if not ET.iselement(child):
                    continue
                class_id = ucsgenutils.word_u(child.tag)
                # child_obj = ucscoreutils.get_ucs_obj(class_id, child, self)
                pdn = None
                if 'dn' in dir(self):
                    pdn = self.dn
                child_obj = GenericMo(class_id, parent_mo_or_dn=pdn)
                self.child_add(child_obj)
                child_obj.from_xml(child, handle)

    def __get_mo_obj(self, class_id):
        """
        Internal methods to create managed object from class_id
        """

        import inspect

        mo_class = ucscoreutils.load_class(class_id)
        mo_class_params = inspect.getfullargspec(mo_class.__init__)[0][2:]
        mo_class_param_dict = {}
        for param in mo_class_params:
            mo_param = mo_class.prop_meta[param].xml_attribute
            if mo_param not in self.__properties:
                if 'rn' in self.__properties:
                    rn_str = self.__properties['rn']
                elif 'dn' in self.__properties:
                    rn_str = os.path.basename(self.__properties['dn'])

                rn_pattern = mo_class.mo_meta.rn
                np_dict = ucscoreutils.get_naming_props(rn_str, rn_pattern)
                if param not in np_dict:
                    mo_class_param_dict[param] = ""
                else:
                    mo_class_param_dict[param] = np_dict[param]
            else:
                mo_class_param_dict[param] = self.__properties[mo_param]

        p_dn = ""

        if 'topRoot' in mo_class.mo_meta.parents:
            mo_obj = mo_class(**mo_class_param_dict)
        else:
            mo_obj = mo_class(parent_mo_or_dn=p_dn, **mo_class_param_dict)
        return mo_obj

    def to_mo(self):
        """
        Converts GenericMo to ManagedObject
        """

        from . import ucsmeta

        class_id = ucsgenutils.word_u(self._class_id)
        if class_id not in ucsmeta.MO_CLASS_ID:
            return None

        mo = self.__get_mo_obj(class_id)
        if not mo:  # or not isinstance(mo, ManagedObject):
            return None

        for prop in self.__properties:
            if prop in mo.prop_map:
                mo.__dict__[mo.prop_map[prop]] = self.__properties[prop]
            else:
                UcsWarning("Property %s Not Exist in MO %s" % (
                    ucsgenutils.word_u(prop), class_id))

        if len(self.child):
            for ch_ in self.child:
                mo_ch = ch_.to_mo()
                mo.child_add(mo_ch)

        return mo

    def __str__(self):
        ts = 8
        if isinstance(self, GenericMo):
            out_str = "\n"
            out_str += 'GenericMo'.ljust(ts * 4) + ':' + str(
                self._class_id) + "\n"
            out_str += "-" * len("GenericMo") + "\n"
            for prop, prop_val in sorted(ucsgenutils.iteritems(self.__dict__)):
                if prop.startswith('_'):
                    continue
                out_str += str(prop).ljust(ts * 4) + ':' + str(prop_val) + "\n"

            return out_str
