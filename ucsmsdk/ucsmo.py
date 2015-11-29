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
import os

import ucsgenutils
import ucscoreutils
import ucscoremeta

try:
    import xml.etree.cElementTree as ET
    from xml.etree.cElementTree import Element, SubElement
except ImportError:
    import cElementTree as ET
    from cElementTree import Element, SubElement

from ucscoremeta import WriteXmlOption
from ucsexception import UcsValidationException, UcsWarning
from ucscore import UcsBase

log = logging.getLogger('ucs')


class GenericProp():
    def __init__(self, name, value, is_dirty):
        self.name = name
        self.value = value
        self.is_dirty = is_dirty


class ManagedObject(UcsBase):
    """This class structures/represents all the managed objects."""
    DUMMY_DIRTY = "0x1L"
    __internal_prop = frozenset(
        ["_dirty_mask", "_class_id", "_child", ''])

    def __init__(self, class_id, parent_mo_or_dn=None, **kwargs):
        self.__parent_mo = None
        self.__status = None
        self.__parent_dn = None
        self.__xtra_props = {}
        self.__xtra_props_dirty_mask = 0x1L

        self._rn_set()
        self._dn_set(parent_mo_or_dn)
        xml_attribute = self.mo_meta.xml_attribute

        UcsBase.__init__(self, ucsgenutils.word_u(xml_attribute))
        # self.mark_dirty()

        if self.__parent_mo:
            self.__parent_mo.child_add(self)

        if kwargs:
            for prop_name, prop_value in kwargs.iteritems():
                if prop_name not in self.prop_meta:
                    log.debug("Unknown property %s" % prop_name)
                self.__set_prop(prop_name, prop_value)

    @property
    def parent_mo(self):
        return self.__parent_mo

    def _rn_set(self):
        if "prop_meta" in dir(self) and "rn" in self.prop_meta:
            self.rn = self.make_rn()
        else:
            self.rn = ""

    def _dn_set(self, pmo_or_dn):
        if pmo_or_dn:
            if isinstance(pmo_or_dn, ManagedObject):
                self.__parent_mo = pmo_or_dn
                self.__parent_dn = self.__parent_mo.dn
            elif isinstance(pmo_or_dn, str):
                self.__parent_dn = pmo_or_dn
            else:
                raise ValueError('parent mo or dn must be specified')

        if "prop_meta" in dir(self) and "dn" in self.prop_meta:
            if self.__parent_dn:
                self.dn = self.__parent_dn + '/' + self.rn
            else:
                self.dn = self.rn
        else:
            self.dn = ""

    def __setattr__(self, name, value):
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
            self.__xtra_props[name] = GenericProp(name, value, True)
            self._dirty_mask |= self.__xtra_props_dirty_mask
            object.__setattr__(self, name, value)

    def __set_prop(self, name, value, mark_dirty=True, forced=False):
        if not forced:
            prop_meta = self.prop_meta[name]
            if prop_meta.access != ucscoremeta.MoPropertyMeta.READ_WRITE:
                raise ValueError("%s is not a read-write property." % name)
            if not prop_meta.validate_property_value(value):
                raise ValueError("Invalid Value Exception - "
                                 "[%s]: Prop <%s>, Value<%s>. "
                                 % (self.__class__.__name__,
                                    name,
                                    value))
                # return False
            if prop_meta.mask and mark_dirty:
                self._dirty_mask |= prop_meta.mask
        object.__setattr__(self, name, value)

    def __str__(self):
        """ Method to return string representation of a managed object. """
        ts = 8
        out_str = "\n"
        out_str += "Managed Object\t\t\t:\t" + str(self._class_id) + "\n"
        out_str += "-" * len("Managed Object") + "\n"
        for prop, prop_value in sorted(self.__dict__.iteritems()):
            if prop in ManagedObject.__internal_prop or prop.startswith(
                    "_ManagedObject__"):
                continue
            if prop in self.__xtra_props:
                prop = "[X]" + str(prop)
            out_str += str(prop).ljust(ts * 4) + ':' + str(
                prop_value) + "\n"
        # print unknown properties
        # for prop, prop_value in self.__xtra_props.iteritems():
        #     prop = "[X]" + str(prop)
        #     out_str += str(prop).ljust(ts * 4) + ':' + str(
        #         prop_value) + "\n"

        out_str += "\n"
        return out_str

    def mark_dirty(self):
        """ This method marks the managed object dirty. """
        if self.__class__.__name__ == "ManagedObject" and not self.is_dirty():
            self._dirty_mask = ManagedObject.DUMMY_DIRTY
        elif "mo_meta" in dir(self):
            self._dirty_mask = self.mo_meta.mask

    def is_dirty(self):
        """ This method checks if managed object is dirty. """
        return self._dirty_mask != 0 or self.child_is_dirty()

    # Ideally an rn should never change across ucsm releases.
    # but we do have some of these cases
    # These cause an issue, because we cannot parse them
    # the below is a special case to handle these cases
    def rn_is_special_case(self):
        if self.__class__.__name__ == "StorageLocalDiskPartition":
            return True
        return False

    def rn_get_special_case(self):
        if self.__class__.__name__ == "StorageLocalDiskPartition":
            # some version of ucs have rn "partition" instead of "partition-id"
            return "partition"

    def make_rn(self):
        """ This method returns the Rn for a managed object. """
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

    def to_xml(self, xml_doc=None, option=None, element_name=None):
        """ Method writes the xml representation of the managed object. """
        if option == WriteXmlOption.DIRTY and not self.is_dirty():
            log.debug("Object is not dirty")
            return

        xml_obj = self.elem_create(class_tag=self.mo_meta.xml_attribute,
                                   xml_doc=xml_doc,
                                   override_tag=element_name)

        for key in self.__dict__:
            if key != 'rn' and key in self.prop_meta:
                mo_prop_meta = self.prop_meta[key]
                if (option != WriteXmlOption.DIRTY or (
                            mo_prop_meta.mask is not None and
                            self._dirty_mask & mo_prop_meta.mask != 0)):
                    value = getattr(self, key)
                    if value:
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
                    if value:
                        xml_obj.set(key, value)

        if 'dn' not in xml_obj.attrib:
            xml_obj.set('dn', self.dn)

        self.child_to_xml(xml_obj, option)
        return xml_obj

    def from_xml(self, element):
        """ Method updates the object from the xml representation of
         the managed object. """
        if element.attrib:
            if self.__class__.__name__ != "ManagedObject":
                for attr_name, attr_value in element.attrib.iteritems():
                    if attr_name in self.prop_map:
                        attr_name = self.prop_map[attr_name]
                    else:
                        self.__xtra_props[attr_name] = GenericProp(
                            attr_name,
                            attr_value,
                            False)
                    object.__setattr__(self, attr_name, attr_value)
            else:
                for attr_name, attr_value in element.attrib.iteritems():
                    object.__setattr__(self, attr_name, attr_value)

        self.mark_clean()

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue

                if self.__class__.__name__ != "ManagedObject" and (
                            child_element.tag in self.mo_meta.field_names):
                    pass

                class_id = ucsgenutils.word_u(child_element.tag)
                child_obj = ucscoreutils.get_ucs_obj(class_id, child_element,
                                                     self)
                self.child_add(child_obj)
                child_obj.from_xml(child_element)

    def sync_mo(self, mo):  # TODO - Check with Rahul
        """ Method to return string representation of a managed object. """
        for prop, prop_value in sorted(self.__dict__.iteritems()):
            if prop in ManagedObject.__internal_prop or prop.startswith(
                    "_ManagedObject__"):
                continue
            mo.__dict__[prop] = prop_value
        return None

    def show_tree(self, level=0):
        """ Method to return string representation of a managed object. """
        indent = "  "
        level_indent = "%s%s)" % (indent * level, level)
        # level_key_dn = "level_%s_dn" % (str(level))
        print "%s %s[%s]" % (level_indent, self._class_id, self.dn)
        for ch_ in self.children:
            level += 1
            ch_.show_tree(level)
            level -= 1
        return None

    def show_hierarchy(self, level=0, break_level=None, show_level=[]):
        """ Method to return string representation of a managed object. """
        from ucscoreutils import print_mo_hierarchy

        print_mo_hierarchy(self._class_id, level, break_level,
                           show_level)


# class GenericMo(ManagedObject):
#     """ This class handles the exceptional behaviour of
#      Generic managed object. """
#
#     def __init__(self, mo, option):
#         ManagedObject.__init__(self, mo.class_id)
#         self._exclude_prop_list = []
#         xml_doc = mo.write_xml(option=option)
#         doc = ET.tostring(xml_doc)
#         root_element = ET.fromstring(doc)
#         self.load_from_xml(root_element, mo.handle)


def generic_mo_from_xml(xml_str):
    import ucsxmlcodec as xc
    # xml_str = xc.to_xml_str(elem)
    # # gmo = xc.from_xml_str(xml_str)
    root_element = ET.fromstring(xml_str)
    class_id = root_element.tag
    gmo = GenericMo(class_id)
    gmo.from_xml(root_element)
    return gmo

def generic_mo_from_xml_element(element):
    import ucsxmlcodec as xc
    xml_str = xc.to_xml_str(element)
    gmo = generic_mo_from_xml(xml_str)
    return gmo

class GenericMo(UcsBase):
    """
        This class implements a Generic Managed Object.

        Ex:
            args = {"a": 1, "b": 2, "c":3}
            GenericMo("test", "org-root", **args)
            GenericMo("test", "org-root", a = 1, b = 2, c = 3, d = 4)

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
            for key, value in kwargs.iteritems():
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

            # if 'rn' not in dir(self):
            #     if 'dn' in dir(self):
            #         self.rn = os.path.basename(self.dn)
            #     else:
            #         self.rn = ""
            #
            # if 'dn' not in dir(self):
            #     self.dn = self.__parent_dn + '/' + self.rn

    def to_xml(self, xml_doc=None, option=None):
        """
        This method returns the xml element node for the current object
        with it's hierarchy.

        Attributes:
            xml_doc: document to which the Mo attributes are added.
                    Can be None.
            option: not required for Generic Mo class object

        Example:
            from ucsmsdk.ucsmo import GenericMo
            args = {"a": 1, "b": 2, "c":3}
            obj = GenericMo("testLsA", "org-root", **args)
            obj1 = GenericMo("testLsB", "org-root", **args)
            obj.add_child(obj1)
            elem = obj.write_xml()

            import ucsmsdk.ucsxmlcodec as xc
            xc.to_xml_str(elem)

        Output:
            '<testLsA a="1" b="2" c="3" dn="org-root/" rn="">
                <testLsB a="1" b="2" c="3" dn="org-root/" rn="" />
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

    def from_xml(self, element):
        """
            This method is form objects out of xml element.
            This is called internally from ucsxmlcode.from_xml_str
            method.

            Example:
                xml = '<testLsA a="1" b="2" c="3" dn="org-root/" rn="">
                <testLsB a="1" b="2" c="3" dn="org-root/" rn="" /></testLsA>'
                obj = xc.from_xml_str(xml)

                print type(obj)
                print type(obj.

            Outputs:
                <class 'ucsmsdk.ucsmo.GenericMo'>
        """
        if element is None:
            return None

        self._class_id = element.tag
        if element.attrib:
            for name, value in element.attrib.iteritems():
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

        children = element.getchildren()
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
                child_obj.from_xml(child)

    def __get_mo_obj(self, class_id):
        import inspect

        mo_class = ucscoreutils.load_class(class_id)
        mo_class_params = inspect.getargspec(mo_class.__init__)[0][2:]
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
        # if "dn" in xml_element.attrib:
        #     p_dn = os.path.dirname(xml_element.attrib["dn"])
        # elif "rn" in xml_element.attrib and mo_obj:
        #     p_dn = mo_obj.dn

        if 'topRoot' in mo_class.mo_meta.parents:
            mo_obj = mo_class(**mo_class_param_dict)
        else:
            mo_obj = mo_class(parent_mo_or_dn=p_dn, **mo_class_param_dict)
        return mo_obj

    def to_mo(self):
        import ucsmeta

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
            for key in self.__dict__:
                if key.startswith('_'):
                    continue
                out_str += str(key).ljust(ts * 4) + ':' + str(
                    getattr(self, key)) + "\n"

            return out_str


# class _GenericMo(ManagedObject):
#     """ This class provides the functionality to create
#     Generic managed objects. """
#
#     def __init__(self, xml_element=None, mo=None,
#                  option=WriteXmlOption.ALL_CONFIG):
#         ManagedObject.__init__(self, "GMO")
#         self.__class_id = None
#         self.dn = None
#         self.rn = None
#         self.properties = {}
#         self.load_xml = xml_element
#         self.mo = mo
#         self.option = option
#
#         if xml_element:
#             self.get_root_node(xml_element)
#         if mo:
#             self.from_managed_object()
#
#     def get_root_node(self, xml_string):
#         """Convert XML to _GenericMO object"""
#         root_element = ET.fromstring(xml_string)
#         self.load_from_xml(root_element)
#
#     def get_attribute(self, attr):
#         """Get Attribute of Generic Managed Object"""
#         if attr in self.properties:
#             return self.properties[attr]
#         return None
#
#     def write_to_attributes(self, element):
#         """Set Attribute of Generic Managed Object"""
#         if element.attrib:
#             for attr_name, attr_value in element.attrib.iteritems():
#                 self.properties[attr_name] = attr_value
#
#     def load_from_xml(self, element):
#         """Populate object using Xml Document Node"""
#         self._class_id = element.tag
#         meta_class_id = ucscoreutils.find_class_id_in_mo_meta_ignore_case(
#             self._class_id)
#
#         if meta_class_id:
#             self.__class_id = meta_class_id
#
#         if NamingPropertyId.DN in element.attrib:
#             self.dn = element.attrib[NamingPropertyId.DN]
#
#         if self.dn:
#             self.rn = os.path.basename(self.dn)
#
#         # Write the attribute and value to dictionary properties, as it is .
#         self.write_to_attributes(element)
#
#         # Run the load_from_xml for each child_node recursively and
#         # populate child list too.
#         child_elements = element.getchildren()
#         if child_elements:
#             for child_element in child_elements:
#                 if not ET.iselement(child_element):
#                     continue
#                 child = _GenericMo()
#                 self.child.append(child)
#                 child.load_from_xml(child_element)
#
#     def write_xml(self, xml_doc=None, option=None, element_name=None):
#         """create Xml Document Node using object attributes"""
#         if xml_doc is None:
#             xml_obj = Element(self.__class_id)
#         else:
#             if element_name is None:
#                 xml_obj = SubElement(xml_doc, self.__class_id)
#             else:
#                 xml_obj = SubElement(xml_doc, element_name)
#
#         for prop in self.__dict__['properties']:
#             xml_obj.set(ucsgenutils.word_l(prop),
#                         self.__dict__['properties'][prop])
#         self.child_write_xml(xml_obj, option)
#         return xml_obj
#
#     def to_managed_object(self):
#         """
#         Method creates and returns an object of ManagedObject class using
#         the class_id and information from the Generic managed object.
#         """
#         from ucs import class_factory
#
#         cln = ucsgenutils.word_u(self.__class_id)
#         mo = class_factory(cln)
#         if mo and isinstance(mo, ManagedObject):
#             meta_class_id = ucscoreutils.find_class_id_in_mo_meta_ignore_case(
#                 self.__class_id)
#             # mo.handle = self.__handle
#             for prop in self.properties:
#                 if ucsgenutils.word_u(prop) in ucscoreutils.get_property_list(
#                         meta_class_id):
#                     mo.set_attr(ucsgenutils.word_u(prop),
#                                 self.properties[prop])
#                 else:
#                     UcsWarning("Property %s Not Exist in MO %s" % (
#                         ucsgenutils.word_u(prop), meta_class_id))
#
#             if len(self.child):
#                 for child in self.child:
#                     moch = child.to_managed_object()
#                     mo.child.append(moch)
#             return mo
#         else:
#             return None
#
#     def from_managed_object(self):
#         """
#         Method creates and returns an object of _GenericMO class using
#         the class_id and other information from the managed object.
#         """
#         if isinstance(self.mo, ManagedObject):
#             self.__class_id = self.mo.class_id
#             self.__handle = self.mo.handle
#
#             if self.mo.get_attr('Dn'):
#                 self.dn = self.mo.get_attr('Dn')
#
#             if self.mo.get_attr('Rn'):
#                 self.rn = self.mo.get_attr('Rn')
#             elif self.dn:
#                 self.rn = os.path.basename(self.dn)
#
#             for prop in ucscoreutils.get_property_list(self.mo.class_id):
#                 self.properties[prop] = self.mo.get_attr(prop)
#
#             if len(self.mo.child):
#                 for child in self.mo.child:
#                     if not child.getattr('dn'):
#                         _dn = self.mo.getattr('dn') + "/" + child.getattr('Rn')
#                         child.setattr('dn', _dn)
#                     gmo = _GenericMo(mo=child)
#                     self.__child.append(gmo)
#
#     def __str__(self):
#         tab_size = 8
#         if isinstance(self, _GenericMo):
#             out_str = "\n"
#             out_str += 'class_id'.ljust(tab_size * 4) + ':' + str(
#                 self.__dict__['__class_id']) + "\n"
#             out_str += 'dn'.ljust(tab_size * 4) + ':' + str(
#                 self.__dict__['dn']) + "\n"
#             out_str += 'rn'.ljust(tab_size * 4) + ':' + str(
#                 self.__dict__['rn']) + "\n"
#             for key, value in self.__dict__['properties'].items():
#                 out_str += key.ljust(tab_size * 4) + ':' + str(value) + "\n"
#             for child in self.__child:
#                 out_str += str(child) + "\n"
#
#             return out_str
#
#     def get_child_class_id(self, class_id):
#         """
#         Method extracts and returns the child object list same as
#         the given class_id
#         """
#         child_list = []
#         for child in self.child:
#             if child.class_id.lower() == class_id.lower():
#                 child_list.append(child)
#         return child_list
#
#     def get_child(self):
#         """ Method returns the child object. """
#         return self.child
