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
This module contains the UcsSdk Core utilities.
"""

from __future__ import print_function

import os
import re
import logging
import sys

from . import ucsgenutils
from . import mometa
from . import methodmeta
from . ucsmeta import MO_CLASS_ID, METHOD_CLASS_ID, OTHER_TYPE_CLASS_ID, \
    MO_CLASS_META


log = logging.getLogger('ucs')


def get_ucs_obj(class_id, elem, mo_obj=None):
    """
    This creates object of type ExternalMethod or ManagedObject or GenericMo
    depending on element tag

    Args:
        class_id (str): class id
        elem (xml element): xml element
        mo_obj : parent managed object

    Returns:
        object of type ExternalMethod or ManagedObject or GenericMo
    """

    import inspect

    from . import ucsmethod
    from . import ucsmo

    if class_id in METHOD_CLASS_ID:
        return ucsmethod.ExternalMethod(class_id)
    elif class_id in MO_CLASS_ID:
        mo_class = load_class(class_id)
        if sys.version_info > (3, 0):
            # Python 3 code in this block
            mo_class_params = inspect.getfullargspec(mo_class.__init__)[0][2:]
        else:
            # Python 2 code in this block
            mo_class_params = inspect.getargspec(mo_class.__init__)[0][2:]
        mo_class_param_dict = {}
        for param in mo_class_params:
            mo_class_param_dict[param] = None

        p_dn = ""
        if "dn" in elem.attrib:
            p_dn = os.path.dirname(elem.attrib["dn"])
        elif "rn" in elem.attrib and mo_obj:
            p_dn = mo_obj.dn

        if 'topRoot' in mo_class.mo_meta.parents:
            mo_obj = mo_class(from_xml_response=True, **mo_class_param_dict)
        else:
            mo_obj = mo_class(parent_mo_or_dn=p_dn,
                              from_xml_response=True, **mo_class_param_dict)
        return mo_obj
    elif class_id in OTHER_TYPE_CLASS_ID:
        module_ = load_module(class_id)
        return getattr(module_, class_id)()

    # This case handles object types that are not known to this version
    # of the SDK. This case can arise when the UCS server has higher
    # version with more objects and the SDK is not at the latest
    # version yet.

    p_dn = ""
    if "dn" in elem.attrib:
        p_dn = os.path.dirname(elem.attrib["dn"])
    elif mo_obj:
        p_dn = mo_obj.dn

    mo_obj = ucsmo.GenericMo(
        class_id=elem.tag, parent_mo_or_dn=p_dn, **elem.attrib)
    return mo_obj


def load_module(module_name):
    """
    This loads the module into the current name space

    Args:
        module_name (str): module_name

    Returns:
        None
    """

    module_name = ucsgenutils.word_u(module_name)
    if module_name and module_name in MO_CLASS_ID:
        fq_module_name = mometa.__name__ + ".%s" % module_name
        module_import = __import__(fq_module_name, globals(), locals(),
                                   [module_name])
        return module_import
    elif module_name and module_name in METHOD_CLASS_ID:
        fq_module_name = methodmeta.__name__ + ".%sMeta" % module_name
        module_import = __import__(fq_module_name, globals(), locals(),
                                   [module_name])
        return module_import
    elif module_name and module_name in OTHER_TYPE_CLASS_ID:
        fq_module_name = OTHER_TYPE_CLASS_ID[module_name]
        module_import = __import__(fq_module_name, globals(), locals(),
                                   [module_name], level=1)
        return module_import


def get_import_str(class_id):
    """
    Returns the complete import string for a given class/method

    Args:
        class_id (str): class_id

    Returns:
        equivalent import string for the class_id
    """

    class_id = ucsgenutils.word_u(class_id)
    if class_id and class_id in MO_CLASS_ID:
        mod_class_id = ucsgenutils.word_l(class_id)
        class_id_sub_pkg = re.match("([a-z])+", mod_class_id).group()
        return mometa.__name__ + ".%s.%s" % (class_id_sub_pkg, class_id)
    elif class_id and class_id in METHOD_CLASS_ID:
        return methodmeta.__name__ + ".%sMeta" % (class_id)
    return None


def load_class(class_id):
    """
    This loads the class into the current name space

    Args:
        class_id (str): class_id

    Returns:
        MangedObject or ExtenalMethod Object or None
    """
    class_id = ucsgenutils.word_u(class_id)
    import_str = get_import_str(class_id)
    if import_str is None:
        return None

    imported_module = __import__(import_str, globals(), locals(), [class_id])
    imported_class = getattr(imported_module, class_id)
    return imported_class


def load_mo(elem):
    """
    This loads the managed object  into the current name space

    Args:
        elem (xml element): xml element representation of the class and
                            it's attributes

    Returns:
        MangedObject
    """

    import inspect

    mo_class_id = elem.tag
    mo_class = load_class(mo_class_id)
    mo_class_params = inspect.getargspec(mo_class.__init__)[0][2:]
    mo_class_param_dict = {}
    for param in mo_class_params:
        mo_class_param_dict[param] = elem.attrib[
            mo_class.prop_map[param]]

    mo_obj = mo_class(parent_mo_or_dn="", **mo_class_param_dict)
    return mo_obj


def is_valid_class_id(class_id):
    """
    Methods checks whether the provided class_id is valid or not."""

    if class_id in MO_CLASS_ID or class_id in METHOD_CLASS_ID:
        return True
    return False


def find_class_id_in_mo_meta_ignore_case(class_id):
    """
    Methods whether class_id is valid or not . Given class is case insensitive.
    """

    if not class_id:
        return None
    if class_id in MO_CLASS_ID:
        return class_id
    l_class_id = class_id.lower()
    for key in MO_CLASS_ID:
        if key.lower() == l_class_id:
            return key
    return None


def find_class_id_in_method_meta_ignore_case(class_id):
    """
    Methods whether class_id is valid or not . Given class is case insensitive.
    """

    if class_id in METHOD_CLASS_ID:
        return class_id
    l_class_id = class_id.lower()
    for key in METHOD_CLASS_ID:
        if key.lower() == l_class_id:
            return key
    return None


def get_mo_property_meta(class_id, key):
    """
    Methods returns the mo property meta of the provided key for the given
    class_id.

    Args:
        class_id (str): class_id of mo
        key (str): prop of class_id

    Returns:
        Object of type MoPropertyMeta

    Example:
        prop_meta = get_mo_property_meta(class_id="LsServer", key="usr_lbl")
    """

    class_obj = load_class(class_id)
    if key == "mo_meta":
        return class_obj.mo_meta

    prop_meta = class_obj.prop_meta
    prop_map = class_obj.prop_map
    if key in prop_map:
        return prop_meta[prop_map[key]]
    elif key in prop_meta:
        return prop_meta[key]
    return None


def write_object(mo_or_list):
    """
    This prints the managed object on the standard output.
    """

    from . import ucsmethod
    from . import ucsmo

    if isinstance(mo_or_list, ucsmethod.ExternalMethod):
        if hasattr(mo_or_list, "out_configs"):
            for child in mo_or_list.out_configs.child:
                if isinstance(child, ucsmo.ManagedObject):
                    write_object(child)
    elif isinstance(mo_or_list, list) and len(mo_or_list) > 0:
        for mo in mo_or_list:
            if (isinstance(mo, ucsmo.ManagedObject) or
                    isinstance(mo, ucsmo.GenericMo)):
                print(mo)
    elif (isinstance(mo_or_list, ucsmo.ManagedObject) or
            isinstance(mo_or_list, ucsmo.GenericMo)):
        print(mo_or_list)


def extract_molist_from_method_response(method_response,
                                        in_hierarchical=False):
    """
    Methods extracts mo list from response received from ucs server i.e.
    external method object

    Args:
        method_response (ExternalMethod Object): response
        in_hierarchical (bool): if True, return all the hierarchical child of
                                    managed objects

    Returns:
        List of ManagedObjects

    Example:
        response = handle.query_dn("org-root", need_response=True)\n
        molist = extract_molist_from_method_response(method_response=response,
                                                     in_hierarchical=True)
    """

    mo_list = []
    if len(method_response.out_configs.child) == 0:
        return mo_list
    if in_hierarchical:
        current_mo_list = method_response.out_configs.child
        while len(current_mo_list) > 0:
            child_mo_list = []
            for mo in current_mo_list:
                mo_list.append(mo)
                while mo.child_count() > 0:
                    for child in mo.child:
                        mo.child_remove(child)
                        child.mark_clean()
                        child_mo_list.append(child)
                        break
            current_mo_list = child_mo_list
    else:
        mo_list = method_response.out_configs.child

    return mo_list


def write_mo_tree(mo, level=0, depth=None, show_level=[],
                  print_tree=True, tree_dict={}, dn=None):
    """
    Prints tree structure of any managed object

    Args:
        mo (object): ManagedObject
        level (int): by default zero
        depth (int or None): last level to process
        show_level (int list): levels to display
        print_tree (bool): if True, print mo tree
        tree_dict (dict): by default {}
        dn (str): dn

    Returns:
        dictionary

    Example:
        mo=handle.query_dn("org-root")\n
        tree_dict = write_mo_tree(mo, depth=3, show_level=[1, 3])\n
    """

    if not mo.dn:
        mo.dn = dn
    indent = "    "

    level_indent = "%s%s)" % (indent * level, level)

    level_key_dn = "level_%s_dn" % (str(level))
    if level_key_dn not in tree_dict:
        tree_dict[level_key_dn] = {mo.dn: mo}
    else:
        tree_dict[level_key_dn][mo.dn] = mo

    level_key_mo = "level_%s_mo" % (str(level))
    if level_key_mo not in tree_dict:
        tree_dict[level_key_mo] = {mo.class_id: [mo]}
    else:
        if mo.class_id not in tree_dict[level_key_mo]:
            tree_dict[level_key_mo][mo.class_id] = [mo]
        else:
            tree_dict[level_key_mo][mo.class_id].append(mo)

    key_all_mo = "all_mo"
    if key_all_mo not in tree_dict:
        tree_dict[key_all_mo] = {mo.class_id: [mo]}
    else:
        if mo.class_id not in tree_dict[key_all_mo]:
            tree_dict[key_all_mo][mo.class_id] = [mo]
        else:
            tree_dict[key_all_mo][mo.class_id].append(mo)


    if print_tree:
        if not show_level:
            print("%s %s (%s)" % (level_indent, mo.dn, mo.class_id))
        elif level in show_level:
            print("%s %s (%s)" % (level_indent, mo.dn, mo.class_id))

    for child in mo.child:
        child.mark_clean()
        level += 1
        if depth is None:
            tree_dict = write_mo_tree(child, level, depth,
                                      show_level, print_tree,
                                      tree_dict, dn)
        elif level <= depth:
            tree_dict = write_mo_tree(child, level, depth,
                                      show_level, print_tree,
                                      tree_dict, dn)
        level -= 1

    return tree_dict


def extract_mo_tree_from_config_method_response(method_response,
                                                depth=None,
                                                show_level=[],
                                                print_tree=False,
                                                tree_dict={}):
    """
    extracts tree structure of any managed object from config method response

    Args:
        method_response (object): ExternalMethod
        depth (int or None): last level to process
        show_level (int list): levels to display
        print_tree (bool): if True, print mo tree
        tree_dict (dict): by default {}

    Returns:
        dictionary

    Example:
        response=handle.query_dn("org-root", need_response=True)\n
        tree_dict = write_mo_tree(response, depth=3, show_level=[1, 3])\n
    """

    current_mo_list = method_response.out_configs.child
    for current_mo in current_mo_list:
        level = 0
        tree_dict = write_mo_tree(current_mo, level, depth,
                                  show_level, print_tree,
                                  tree_dict)
    return tree_dict


def print_mo_hierarchy(class_id, level=0, depth=None, show_level=[]):
    """
    print hierarchy of class_id

    Args:
        class_id (str): class id
        level (int): by default zero
        depth (int or None): last level to process
        show_level (int list): levels to display

    Returns:
        dictionary

    Example:
        response=handle.query_dn("org-root", need_response=True)\n
        tree_dict = write_mo_tree(response, depth=3, show_level=[1, 3])\n
    """

    indent = " "
    level_indent = "%s%s)" % (indent * level, level)
    class_id = ucsgenutils.word_u(class_id)

    if level == 0:
        parents = [ucsgenutils.word_u(parent) for parent in
                   MO_CLASS_META[class_id].parents]
        print("[%s]" % (", ".join(sorted(parents))))

    if level == 0 or not show_level or level in show_level:
        print("%s%s" % (level_indent, ucsgenutils.word_u(class_id)))

    children = sorted(MO_CLASS_META[class_id].children)

    level += 1
    if depth is None or level <= depth:
        for ch_ in children:
            child = ucsgenutils.word_u(ch_)
            if child == class_id:
                continue
            print_mo_hierarchy(child, level, depth,
                               show_level)
    level -= 1


def get_naming_props(rn_str, rn_pattern):
    """
    extract naming property and its value from a given rn and its pattern

    Args:
        rn_str (str): rn value
        rn_pattern (str): rn pattern from mo_meta

    Returns:
        dictionary

    Example:
        naming_props = get_naming_props(rn_str="ls-test_sp",
                                        rn_pattern="ls-[name]")
    """

    rn_regex = re.sub(r"\[(.+?)\]", r"(?P<\1>.+)", rn_pattern)
    rn_regex_pat = re.compile(rn_regex)
    match_obj = re.match(rn_regex_pat, rn_str)
    if match_obj is None:
        log.debug("Error getting naming props. rn_str: %s rn_pattern %s" %
                  (rn_str, rn_pattern))
        return {}
    naming_prop_dict = match_obj.groupdict()
    return naming_prop_dict


class ClassIdMeta(object):

    def __init__(
            self,
            class_id,
            include_prop=True,
            show_tree=True,
            depth=None):
        self.__mo_meta = MO_CLASS_META[class_id]
        self.class_id = class_id
        self.xml_attribute = self.__mo_meta.xml_attribute
        self.rn = self.__mo_meta.rn
        self.min_version = self.__mo_meta.version
        self.access = self.__mo_meta.inp_out
        self.access_privilege = self.__mo_meta.access
        self.parents = self.__mo_meta.parents
        self.children = self.__mo_meta.children
        self.props = {}

        self._str_tree = "\n"
        self._str_props = "\n"

        if show_tree:
            self._str_tree = _show_tree(class_id, depth)

        if include_prop:
            class_obj = load_class(self.class_id)
            self.props = class_obj.prop_meta
            for prop in sorted(self.props):
                self._str_props += str(self.props[prop]) + "\n"

    def __str__(self):
        """
        Method to return string representation.
        """
        ts = 8
        out_str = ""

        out_str += self._str_tree

        out_str += "\n"
        out_str += str("ClassId").ljust(ts * 4) + str(self.class_id) + "\n"
        out_str += ("-" * len("ClassId")).ljust(ts * 4) + "-" * len(
            self.class_id) + "\n"
        out_str += str("xml_attribute").ljust(ts * 4) + ':' + str(
            self.xml_attribute) + "\n"
        out_str += str("rn").ljust(ts * 4) + ':' + str(
            self.rn) + "\n"
        out_str += str("min_version").ljust(ts * 4) + ':' + str(
            self.min_version) + "\n"
        out_str += str("access").ljust(ts * 4) + ':' + str(self.access) + "\n"
        out_str += str("access_privilege").ljust(ts * 4) + ':' + str(
            self.access_privilege) + "\n"
        out_str += str("parents").ljust(ts * 4) + ':' + str(self.parents) + \
            "\n"
        out_str += str("children").ljust(ts * 4) + ':' + str(self.children)

        out_str += self._str_props

        return out_str


def _show_tree(class_id, depth=None, level=0, ancestor_str="",
               ancestor=[], last_child=True):

    meta_class_id = ucsgenutils.word_u(class_id)

    out_str = ""
    if not ancestor:
        for parent in sorted(MO_CLASS_META[meta_class_id].parents):
            out_str += "[" + ucsgenutils.word_u(parent) + "]" + "\n"

    index = len(ancestor) + 1

    level += 1

    if meta_class_id in ancestor:
        out_str += ancestor_str + "  |-" + meta_class_id + "\n"
    else:
        ancestor.append(meta_class_id)
        out_str += ancestor_str + "  |-" + meta_class_id + "\n"
        children = sorted(MO_CLASS_META[meta_class_id].children)
        total = len(children)
        count = 0
        if depth is None or level < depth + 1:
            for child in children:
                count += 1

                if last_child:
                    ancestor_str_ = ancestor_str + "   "
                else:
                    ancestor_str_ = ancestor_str + "  |"

                out_str += _show_tree(child, depth, level,
                                      ancestor_str_, ancestor, total == count)

        ancestor.pop(index - 1)
    return out_str


def search_class_id(class_id):
    """
    case insensitive search for class_id in meta.
    if unable to find exact class_id, this will also suggest matching class_id.

    Args:
        class_id (str): string matching class_id.(case insensitive)

    Returns:
        (str) or None

    Example:
        class_ids = search_class_id(class_id="ls")
    """

    from . import ucsmeta

    meta_class_id = find_class_id_in_mo_meta_ignore_case(class_id=class_id)

    if meta_class_id is not None:
        return meta_class_id

    # if class_id not exists in meta
    l_class_id = class_id.lower()
    class_ids = sorted([cid for cid in ucsmeta.MO_CLASS_ID
                        if re.search(l_class_id, cid, re.IGNORECASE)])
    if class_ids:
        log.info('"%s" did not match any available Class Ids.\n'
                 'Related Class Ids are:\n%s\n%s' %
                 (class_id,
                  "-" * len("Related Class Ids are:"),
                  "\n".join(class_ids)))
    else:
        log.info('"%s" did not match any available Class Ids.' % class_id)


def get_meta_info(class_id, include_prop=True,
                  show_tree=True, depth=None):
    """
    Gets class id meta information

    Args:
        class_id (str): string matching class_id.(case insensitive)
        include_prop (bool): by default True. If False, excludes property.
        show_tree (bool): by default True. If False will not display mo tree.
        depth (int): depth to which hierarchy is displayed.

    Returns:
        None: If class_id is not present in meta.
        Or
        ClassIdMeta Object: class_id
                            xml_attribute
                            rn
                            min_version
                            access
                            access_privilege
                            parents : parent list
                            children : children list
                            properties : property list
                            props : {property_name : MoPropertyMeta Object}

    Example:
        meta = get_meta_info(class_id="lsserver")
        meta = get_meta_info(class_id="lsserver", depth=2)
        meta = get_meta_info(class_id="lsserver", include_prop=False)
        meta = get_meta_info(class_id="lsserver", show_tree=False)

        print(meta.xml_attribute)
        print(meta.children)
        print(meta.props["name"])
    """

    meta_class_id = search_class_id(class_id)
    if not meta_class_id:
        return

    return ClassIdMeta(meta_class_id, include_prop, show_tree, depth)
