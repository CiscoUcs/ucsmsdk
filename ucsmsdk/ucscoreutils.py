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

import os
import sys
import re
import logging

import ucsgenutils
import mometa
import methodmeta
import ucsmethod
import ucsmo
from ucsmeta import MO_CLASS_ID, METHOD_CLASS_ID, OTHER_TYPE_CLASS_ID, \
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

    if class_id in METHOD_CLASS_ID:
        return ucsmethod.ExternalMethod(class_id)
    elif class_id in MO_CLASS_ID:
        mo_class = load_class(class_id)
        mo_class_params = inspect.getargspec(mo_class.__init__)[0][2:]
        mo_class_param_dict = {}
        for param in mo_class_params:
            mo_param = mo_class.prop_meta[param].xml_attribute
            if mo_param not in elem.attrib:
                mo_class_param_dict[param] = ""
                continue
            mo_class_param_dict[param] = elem.attrib[mo_param]

        p_dn = ""
        if "dn" in elem.attrib:
            p_dn = os.path.dirname(elem.attrib["dn"])
        elif "rn" in elem.attrib and mo_obj:
            p_dn = mo_obj.dn

        if 'topRoot' in mo_class.mo_meta.parents:
            mo_obj = mo_class(**mo_class_param_dict)
        else:
            mo_obj = mo_class(parent_mo_or_dn=p_dn, **mo_class_param_dict)
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

    mo_obj = ucsmo.GenericMo(class_id=elem.tag, parent_mo_or_dn=p_dn, **elem.attrib)
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
                                   [module_name])
        return module_import


def load_class(class_id):
    """
    This loads the class into the current name space

    Args:
        class_id (str): class_id

    Returns:
        MangedObject or ExtenalMethod Object or None
    """

    class_id = ucsgenutils.word_u(class_id)
    if class_id and class_id in MO_CLASS_ID:
        mod_class_id = ucsgenutils.word_l(class_id)
        class_id_sub_pkg = re.match("([a-z])+", mod_class_id).group()
        mo_pkg = mometa.__name__ + ".%s.%s" % (class_id_sub_pkg, class_id)
        mo_module = __import__(mo_pkg, globals(), locals(), [class_id])
        mo_class = getattr(mo_module, class_id)
        return mo_class
    elif class_id and class_id in METHOD_CLASS_ID:
        mo_import = methodmeta.__name__ + ".%sMeta" % (class_id)
        method_meta = __import__(mo_import, globals(), locals(),
                                 [class_id])
        return getattr(method_meta, class_id)
    return None


def load_mo(elem):
    """
    This loads the managed object  into the current name space

    Args:
        class_id (str): class_id

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
            mo_class.PROPERTY_MAP[param]]

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
    # print class_id
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

    if isinstance(mo_or_list, ucsmethod.ExternalMethod):
        if hasattr(mo_or_list, "out_configs"):
            for child in mo_or_list.out_configs.child:
                if isinstance(child, ucsmo.ManagedObject):
                    write_object(child)
    elif isinstance(mo_or_list, list) and len(mo_or_list) > 0:
        for mo in mo_or_list:
            if (isinstance(mo, ucsmo.ManagedObject) or
                    isinstance(mo, ucsmo.GenericMo)):
                print mo
    elif (isinstance(mo_or_list, ucsmo.ManagedObject) or
            isinstance(mo_or_list, ucsmo.GenericMo)):
        print mo_or_list


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
        molist = extract_molist_from_method_response(method_response=response, in_hierarchical=True)
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


def write_mo_tree(mo, level=0, break_level=None, show_level=[],
                  print_tree=True, tree_dict={}, dn=None):
    """
    Prints tree structure of any managed object

    Args:
        mo (object): ManagedObject
        level (int): by default zero
        break_level (int or None): last level to process
        show_level (int list): levels to display
        print_tree (bool): if True, print mo tree
        tree_dict (dict): by default {}
        dn (str): dn

    Returns:
        dictionary

    Example:
        mo=handle.query_dn("org-root")\n
        tree_dict = write_mo_tree(mo, break_level=3, show_level=[1, 3])\n
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

    # print tree_dict

    if print_tree:
        if not show_level:
            print "%s %s (%s)" % (level_indent, mo.dn, mo.class_id)
        elif level in show_level:
            print "%s %s (%s)" % (level_indent, mo.dn, mo.class_id)

    for child in mo.child:
        child.mark_clean()
        level += 1
        if break_level is None:
            tree_dict = write_mo_tree(child, level, break_level,
                                      show_level, print_tree,
                                      tree_dict, dn)
        elif level <= break_level:
            tree_dict = write_mo_tree(child, level, break_level,
                                      show_level, print_tree,
                                      tree_dict, dn)
        level -= 1

    return tree_dict



def extract_mo_tree_from_config_method_response(method_response,
                                                break_level=None,
                                                show_level=[],
                                                print_tree=False,
                                                tree_dict={}):
    """
    extracts tree structure of any managed object from config method response

    Args:
        method_response (object): ExternalMethod
        break_level (int or None): last level to process
        show_level (int list): levels to display
        print_tree (bool): if True, print mo tree
        tree_dict (dict): by default {}

    Returns:
        dictionary

    Example:
        response=handle.query_dn("org-root", need_response=True)\n
        tree_dict = write_mo_tree(response, break_level=3, show_level=[1, 3])\n
    """

    current_mo_list = method_response.out_configs.child
    for current_mo in current_mo_list:
        level = 0
        tree_dict = write_mo_tree(current_mo, level, break_level,
                                  show_level, print_tree,
                                  tree_dict)
    return tree_dict


def print_mo_hierarchy(class_id, level=0, break_level=None, show_level=[]):
    """
    print hierarchy of class_id

    Args:
        class_id (str): class id
        level (int): by default zero
        break_level (int or None): last level to process
        show_level (int list): levels to display

    Returns:
        dictionary

    Example:
        response=handle.query_dn("org-root", need_response=True)\n
        tree_dict = write_mo_tree(response, break_level=3, show_level=[1, 3])\n
    """

    indent = " "
    level_indent = "%s%s)" % (indent * level, level)
    class_id = ucsgenutils.word_u(class_id)

    if level == 0:
        parents = [ucsgenutils.word_u(parent) for parent in
                   MO_CLASS_META[class_id].parents]
        print "[%s]" % (", ".join(sorted(parents)))

    if level == 0 or not show_level or level in show_level:
        print "%s%s" % (level_indent, ucsgenutils.word_u(class_id))

    children = sorted(MO_CLASS_META[class_id].children)

    level += 1
    if break_level is None or level <= break_level:
        for ch_ in children:
            child = ucsgenutils.word_u(ch_)
            if child == class_id:
                continue
            print_mo_hierarchy(child, level, break_level,
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
        naming_props = get_naming_props(rn_str="ls-test_sp", rn_pattern="ls-[name]")
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
