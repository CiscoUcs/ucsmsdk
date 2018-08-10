# Copyright 2013 Cisco Systems, Inc.
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

"""
This module generated the python script using UCS GUI, GUI logs and xml
request.
"""

from __future__ import print_function

import os
import sys
import time
import glob
import re
import xml.dom
import xml.dom.minidom
from os.path import dirname
from .. import ucsgenutils
from .. import ucscoreutils
from ..ucsconstants import Status, NamingPropertyId, YesOrNo
from ..ucsexception import UcsValidationException

import logging

log = logging.getLogger('ucs')

# variable declaration
_display_xml = False
_outfile_flag = False
_outfile_path = None
_outfile = None
_and_count = 0
_or_count = 0
_not_count = 0
_multi_line_method = ["<configConfMo", "<lsInstantiateNNamedTemplate",
                      "<statsClearInterval", "<lsClone", "<lsTemplatise",
                      "<lsInstantiateTemplate", "<lsInstantiateNTemplate",
                      "<configConfRename"]
_single_line_method = ["</configConfMo", "</lsInstantiateNNamedTemplate",
                       "</statsClearInterval", "</lsClone", "</lsTemplatise",
                       "</lsInstantiateTemplate", "</lsInstantiateNTemplate",
                       "/>", "</configConfRename"]


# class declaration
class _ClassStatus:
    """enum for mo status."""
    NONE_ = 0
    CREATED = 1
    MODIFIED = 2
    REMOVED = 4
    DELETED = 8
    GET = 16


# Function Definition
# ---- START - OF - GENERIC - FUCNTION ----
def _get_class_id_for_dn(dn):
    """
    Internal method to get the class id for a given dn
    """

    rns = dn.split('/')
    class_id = None
    parent_class_id = None

    for rn in rns:
        class_id = _get_class_id_for_rn(rn, parent_class_id)
        if class_id is None:
            break
        parent_class_id = class_id

    return class_id


def _get_class_id_for_rn(rn, prev_class_id=None):
    """
    Internal method to get the class id for a given rn
    """

    if not prev_class_id:
        prev_class_id = "TopRoot"

    meta_class_id = ucscoreutils.find_class_id_in_mo_meta_ignore_case(
        prev_class_id)
    if meta_class_id is None:
        raise UcsValidationException(
            '[Error]: class_id [%s] is not valid' % (
                prev_class_id))

    mo_meta = ucscoreutils.get_mo_property_meta(meta_class_id, "mo_meta")
    if mo_meta is None:
        raise UcsValidationException(
            '[Error]: mo_meta for class_id [%s] is not valid'
            % prev_class_id)

    for child_class_id in mo_meta.children:
        # 1.If Rn does not contain [, then there is no naming property.
        #   Check directly.
        # 2. If Rn contains [,
        # 2.1) Check if the Rn contains a "-" and ChildClassId.Rn does not,
        #      then proceed to next child_class_id.
        #      substitute \[[^\]]*\] with .* and do a regex match
        # 2.2) If Rn does not contain a "-",
        #      then probably the child_class_id has only the naming property
        #      without any suffix or prefix. Check for "[*]".
        #      Need to see, if there is a possibility of more than one [*]
        #      directly under a ClassId

        # child_class_id = "orgorg"
        child_class_id = ucscoreutils.find_class_id_in_mo_meta_ignore_case(
            child_class_id)
        child_mo_meta = ucscoreutils.get_mo_property_meta(child_class_id,
                                                          "mo_meta")
        if child_mo_meta is None:
            continue

        # 2. Check if there is a naming property
        match = re.search(r"(\[[^\]]+\])", child_mo_meta.rn)
        if not match:
            if child_mo_meta.rn == rn:
                return child_mo_meta.name
            continue

        # 2.1 Check if it has a prefix or suffix
        match = re.search(r"(([^\]]\[)|(\][^\[]))", child_mo_meta.rn)
        if match:
            mod_meta_rn = re.sub(r"\[([^\]]+)\]", r"(?P<\1>.*?)",
                                 child_mo_meta.rn)
            if re.match(r"\|", mod_meta_rn):
                mod_meta_rn = re.sub(r"\|", r"\|", mod_meta_rn)
            pattern = "^" + mod_meta_rn + "$"
            if re.match(pattern, rn):
                return child_mo_meta.name
        else:
            continue

    for child_class_id in mo_meta.children:
        child_mo_meta = ucscoreutils.get_mo_property_meta(child_class_id,
                                                          "mo_meta")
        if child_mo_meta is None:
            continue
        match = re.match(r"^(\[[^\]]+\])+$", child_mo_meta.rn)
        if match:
            return child_mo_meta.name

    return None


def _get_prop_name(prop):
    """
    Internal method to modify property name as python convention
    """

    new_prop = re.sub('_+', '_',
                      re.sub('^_', '',
                             re.sub(r'[/\-: +]', '_',
                                    re.sub(r'([a-z0-9])([A-Z])',
                                           r'\g<1>_\g<2>', prop)))).upper()
    return new_prop


def _first_capital(string):
    """
    Internal method to make first letter capital
    """

    string = string[:1].upper() + string[1:]
    return string


def _is_root_node(dom, tag_name):
    """
    Internal method to check if it root xml node
    """

    root_node_tag_name = dom.documentElement.tag_name
    if root_node_tag_name == tag_name:
        return True
    else:
        return False


def _get_pair_nodes(root_node):
    """
    Internal method to get "pair" nodes under root_node
    """

    method_elem = root_node
    in_configs_elem_list = method_elem.getElementsByTagName("inConfigs")
    in_configs_elem = in_configs_elem_list[0]
    pair_elems_list = in_configs_elem.getElementsByTagName("pair")
    return pair_elems_list


def _get_only_elem_child_node(node):
    """
    Internal method to return only first element child node
    """

    child_list = [child_node for child_node in node.childNodes
                  if child_node.nodeType == child_node.ELEMENT_NODE]
    return child_list[0]


def _get_elem_child_nodes(node):
    """
    Internal method to return all element child nodes
    """

    child_list = [child_node for child_node in node.childNodes if
                  child_node.nodeType == child_node.ELEMENT_NODE]
    return child_list


def _dump_xml_on_screen(doc):
    """
    Internal method to display xml extracted to generate sdk code.
    """

    global _outfile_path, _outfile_flag
    xml_new = doc.toprettyxml(indent=" ")
    xml_new = re.sub(r"^.*?xml version.*\n", "", xml_new)
    xml_new = re.sub(r"\n[\s]*\n", "\n", xml_new)
    multiline_pattern = re.compile(r"^(.*)", flags=re.MULTILINE)
    xml_new = re.sub(multiline_pattern, r"#\1", xml_new)
    if _outfile_flag:
        _outfile = open(_outfile_path, 'a')
        _outfile.write("\n##### Start-Of-XML #####\n")
        _outfile.write("%s" % xml_new)
        _outfile.write("\n##### End-Of-XML #####\n")
        _outfile.close()
    else:
        print("\n##### Start-Of-XML #####\n")
        print(xml_new)
        print("\n##### End-Of-XML #####\n")


def _check_if_any_list_value_in_string(listx, line):
    """
    Internal method to test if any of the list value present in a line.
    """

    flag = False
    for value in listx:
        if value in line:
            flag = True
            break
    return flag


def _create_property_map_from_node(class_node, class_status):
    gmo_flag = False
    property_map = {}

    if ucscoreutils.find_class_id_in_mo_meta_ignore_case(
            class_node.localName) is None:
        gmo_flag = True

    if not gmo_flag:
        peer_class_id = _first_capital(class_node.localName)
        peer_class_ref = ucscoreutils.load_class(peer_class_id)
        peer_class_naming_props = peer_class_ref.naming_props
        peer_class_prop_map = peer_class_ref.prop_map
        peer_class_prop_meta = peer_class_ref.prop_meta
        peer_class_mo_meta = peer_class_ref.mo_meta

    # create property map for attributes
    attributes_dict = dict(class_node.attributes.items())
    if "dn" in attributes_dict:
        prop_dn = attributes_dict["dn"]
        prop_rn = os.path.basename(prop_dn)
    elif "rn" in attributes_dict:
        prop_rn = attributes_dict["rn"]

    naming_props_py_from_rn = ucscoreutils.get_naming_props(
        prop_rn, peer_class_mo_meta.rn)

    for attr, val in class_node.attributes.items():
        name = attr
        value = val

        if name in ['dn', 'rn', 'status']:
            continue

        # prop_ucs : ucs naming convention
        # prop_py  : python naming convention
        # if name.lower() == "Filter".lower():
        #     prop_ucs = "FilterValue"
        # else:
        #     prop_ucs = name
        prop_ucs = name

        if not gmo_flag and prop_ucs in peer_class_prop_map:
            prop_py = peer_class_prop_map[prop_ucs]
            prop_meta = peer_class_prop_meta[prop_py]
            prop_access = prop_meta.access
            if prop_access in [2, 4]:
                continue
            elif prop_access in [0, 1]:
                if class_status & _ClassStatus.CREATED != \
                        _ClassStatus.CREATED:
                    continue
            if not prop_meta.validate_property_value(val):
                continue
        else:
            prop_py = prop_ucs

        if "\\" in val:
            value = 'r"' + str(val) + '"'
        else:
            value = '"' + str(val) + '"'

        property_map[prop_py] = value

    if class_status & _ClassStatus.CREATED == _ClassStatus.CREATED:
        for naming_prop_ucs in peer_class_naming_props:
            naming_prop_py = peer_class_prop_map[naming_prop_ucs]
            if naming_prop_py not in property_map:
                val = naming_props_py_from_rn[naming_prop_py]
                if peer_class_prop_meta[naming_prop_py]. \
                        validate_property_value(val):
                    if "\\" in val:
                        value = 'r"' + str(val) + '"'
                    else:
                        value = '"' + str(val) + '"'

                    property_map[naming_prop_py] = value

    return property_map


# ---- END - OF - GENERIC - FUCNTION ----

# ---- START - OF - METHOD SPECIFIC - FUNCTION ----
def _get_config_conf_cmdlet(node, is_pair_node):
    """
    Internal method to process configConf request.
    """

    cmdlet = ""
    if node is None:
        return None
    class_node = None
    key = ""

    if is_pair_node:
        key = node.getAttribute(NamingPropertyId.KEY)
        class_node = _get_only_elem_child_node(node)
        if class_node is None:
            return None
    else:
        key = node.getAttribute(NamingPropertyId.DN)
        class_node = node

    dn = ""
    mo_tag = ""
    if class_node.hasAttribute(NamingPropertyId.DN):
        dn = class_node.getAttribute(NamingPropertyId.DN)

    if class_node.hasAttribute(
        NamingPropertyId.STATUS) and \
            class_node.getAttribute(NamingPropertyId.STATUS) is not \
            None:
        mo_tag = "mo"
    else:
        if class_node.hasChildNodes() and len(
                _get_elem_child_nodes(class_node)) > 0:
            mo_tag = "obj"
        else:
            mo_tag = "mo"

    import_list = []
    obj_flag = False

    top_cmdlet, op_flag, import_list = _form_configconf_cmdlet(
        class_node=class_node,
        key=key,
        tag=mo_tag,
        import_list=import_list)

    if class_node.hasChildNodes() and \
            len(_get_elem_child_nodes(class_node)) > 0:
        call_count = 1
        cmdlet = ""
        for child_node in _get_elem_child_nodes(class_node):
            sub_cmdlet, import_list, obj_flag = _get_config_conf_sub_cmdlet(
                child_node,
                dn, mo_tag,
                call_count,
                import_list,
                obj_flag)

            call_count += 1
            if sub_cmdlet is not None:
                cmdlet += "\n" + sub_cmdlet
            else:
                call_count -= 1

    if op_flag in ["add", "addmodify", "set", "remove"] and mo_tag == "mo":
        if op_flag == "add":
            cmdlet += "\n" + "handle.add_mo(mo)\n"
        elif op_flag == "addmodify":
            cmdlet += "\n" + "handle.add_mo(mo, True)\n"
        elif op_flag == "set":
            cmdlet += "\n" + "handle.set_mo(mo)\n"
        elif op_flag == "remove":
            cmdlet += "handle.remove_mo(mo)"

    import_cmdlet = ""
    for mo in import_list:
        mo_folder = re.match("([a-z])+", ucsgenutils.word_l(mo)).group()
        import_cmdlet += "from ucsmsdk.mometa.%s.%s import %s\n" % (
            mo_folder, mo, mo)

    main_cmdlet = ""
    if import_cmdlet:
        main_cmdlet += "\n" + import_cmdlet
    if mo_tag == "obj" and not obj_flag:
        top_cmdlet = ""

    main_cmdlet += "\n" + top_cmdlet
    main_cmdlet += cmdlet

    return main_cmdlet


def _get_config_conf_sub_cmdlet(class_node, parent_dn, parent_mo_tag,
                                parent_call_count, import_list, obj_flag):
    """
    Internal method to process configConf request.
    """

    cmdlet = ""
    dn = ""
    # use_parent_mo = False ##if the parent mo should be used at this level

    if class_node.hasAttribute(NamingPropertyId.DN):
        dn = class_node.getAttribute(NamingPropertyId.DN)
    elif class_node.hasAttribute(NamingPropertyId.RN):
        dn = parent_dn + "/" + class_node.getAttribute(NamingPropertyId.RN)

    count = 1
    if parent_mo_tag == "obj":
        tag = "mo"
    else:
        tag = parent_mo_tag + "_" + str(parent_call_count)

    cmdlet, op_flag, import_list = _form_configconf_cmdlet(
        class_node=class_node,
        key=dn,
        tag=tag,
        import_list=import_list,
        parent_tag=parent_mo_tag,
        sub_cmdlet=True)

    # Recursively cater to subnodes
    for child_node in _get_elem_child_nodes(class_node):
        sub_cmdlet, import_list, obj_flag = _get_config_conf_sub_cmdlet(
            child_node,
            dn,
            tag,
            count,
            import_list,
            obj_flag)
        count += 1
        if sub_cmdlet is not None:
            cmdlet += "\n" + sub_cmdlet
        else:
            count -= 1

    # if op_flag in ["add", "addmodify", "set", "remove"] and tag == "mo":
    if op_flag == "add" and tag == "mo":
        cmdlet += "\n" + "handle.add_mo(mo)\n"
    if op_flag == "addmodify" and tag == "mo":
        cmdlet += "\n" + "handle.add_mo(mo, True)\n"
    if op_flag == "set":
        cmdlet += "\n" + "handle.set_mo(mo)\n"
    if op_flag == "remove":
        cmdlet += "handle.remove_mo(%s)\n" % tag

    if not obj_flag:
        if parent_mo_tag == "obj" and op_flag in ["add", "addmodify", "set"]:
            obj_flag = True

    return cmdlet, import_list, obj_flag


def _form_configconf_cmdlet(class_node, key, tag, import_list, parent_tag=None,
                            sub_cmdlet=False):
    """
    Internal method to process configConf request.
    """

    cmdlet = ""
    class_status = _ClassStatus.NONE_
    op_flag = None
    parent_dn = dirname(key)
    peer_class_id = _first_capital(class_node.localName)

    parent_class_id = _get_class_id_for_dn(parent_dn)
    if parent_class_id is None:
        parent_class_id = ""

    if class_node.hasAttribute(
        NamingPropertyId.STATUS) and \
            class_node.getAttribute(NamingPropertyId.STATUS) is not \
            None:
        cs_list = []
        cs_list = class_node.getAttribute(NamingPropertyId.STATUS).split(',')
        cs_list = [x.strip() for x in cs_list]
        if Status.CREATED in cs_list:
            class_status |= _ClassStatus.CREATED
        if Status.MODIFIED in cs_list:
            class_status |= _ClassStatus.MODIFIED
        if Status.DELETED in cs_list:
            class_status |= _ClassStatus.DELETED
        if Status.REMOVED in cs_list:
            class_status |= _ClassStatus.REMOVED
    else:
        if sub_cmdlet:
            class_status = _ClassStatus.CREATED | _ClassStatus.MODIFIED
        else:
            if class_node.hasChildNodes() and \
                    len(_get_elem_child_nodes(class_node)) > 0:
                class_status = _ClassStatus.GET
            else:
                class_status = _ClassStatus.CREATED | _ClassStatus.MODIFIED

    property_map = _create_property_map_from_node(class_node, class_status)

    parent_mo_or_dn = '"' + str(parent_dn) + '"'
    if sub_cmdlet:
        parent_mo_or_dn = parent_tag

    # make cmdlet
    if class_status & _ClassStatus.GET == _ClassStatus.GET:
        op_flag = "get"
        cmdlet = "%s = handle.query_dn(\"%s\")" % (tag, key)
    elif class_status & _ClassStatus.DELETED == _ClassStatus.DELETED or \
            class_status & \
            _ClassStatus.REMOVED == _ClassStatus.REMOVED:
        op_flag = "remove"
        cmdlet = "%s = handle.query_dn(\"%s\")\n" % (tag, key)
    elif class_status & _ClassStatus.CREATED == _ClassStatus.CREATED:
        op_flag = "add"
        if peer_class_id not in import_list:
            import_list.append(peer_class_id)
        if class_status & _ClassStatus.MODIFIED == _ClassStatus.MODIFIED:
            op_flag = "addmodify"
            add_prop_map = ", ".join(
                [k + "=" + v for k, v in ucsgenutils.iteritems(property_map)])
            cmdlet = '%s = %s(parent_mo_or_dn=%s, %s)' % (
                tag, peer_class_id, parent_mo_or_dn, add_prop_map)
        else:
            add_prop_map = ", ".join(
                [k + "=" + v for k, v in ucsgenutils.iteritems(property_map)])
            cmdlet = '%s = %s(parent_mo_or_dn=%s, %s)' % (
                tag, peer_class_id, parent_mo_or_dn, add_prop_map)
    elif class_status & _ClassStatus.MODIFIED == _ClassStatus.MODIFIED:
        op_flag = "set"
        set_prop_map = "\n".join(
            [tag + "." + k + " = " + v for k, v in ucsgenutils.iteritems(property_map)])
        cmdlet = "%s = handle.query_dn(\"%s\")\n%s\n" % (
            tag, key, set_prop_map)
    else:
        print("Throw Exception XML request status (%s) is invalid." % (
            class_node.getAttribute(NamingPropertyId.STATUS)))

    return cmdlet, op_flag, import_list


def _generate_config_conf_cmdlets(xml_string):
    """
    Internal method which takes xmlstring, and generate script for configConfMo
    and configConfMos methods.
    """

    doc = xml.dom.minidom.parseString(xml_string)
    top_node = doc.documentElement

    if top_node is None:
        return

    cmdlet = ""

    if len(top_node.getElementsByTagName("inConfigs")) != 0:
        pair_nodes = _get_elem_child_nodes(
            top_node.getElementsByTagName("inConfigs")[0])
    else:
        pair_nodes = None

    if pair_nodes is None or len(pair_nodes) < 1:
        node = top_node.getElementsByTagName("inConfig")[0]
        if node is None:
            return

        node = _get_only_elem_child_node(node)
        if node is None:
            return
        cmdlet = _get_config_conf_cmdlet(node, False)
    elif len(pair_nodes) > 1:
        temp_cmdlet = ""
        temp_dn = ""
        temp_mo = ""
        count = 0
        dict_mos = {}

        # cmdlet = "handle.start_ucs_transaction()" + "\n"
        for node in pair_nodes:
            temp_dn = node.getAttribute(NamingPropertyId.KEY)
            temp_mo = "mo"
            if count > 0:
                temp_mo += str(count)
            if temp_dn not in dict_mos:
                dict_mos[temp_dn] = temp_mo

            # check if parent is already there in dictionary
            child_dn = os.path.basename(temp_dn)
            parent_dn = os.path.dirname(temp_dn)
            if parent_dn in dict_mos:
                node.setAttribute(NamingPropertyId.KEY, child_dn)
                temp_cmdlet = _get_config_conf_cmdlet(node, True)
                cmdlet += temp_mo + " = " + dict_mos[
                    parent_dn] + " | " + temp_cmdlet + "\n"
            else:
                temp_cmdlet = _get_config_conf_cmdlet(node, True)
                cmdlet += temp_cmdlet + "\n"

            count += 1

            # cmdlet += "handle.complete_ucs_transaction()"
    else:
        cmdlet = _get_config_conf_cmdlet(pair_nodes[0], True)

    cmdlet += "\nhandle.commit()"

    if cmdlet is not None:
        return cmdlet


def _generate_config_resolve_cmdlet(xml_string, method):
    """
    Internal method which takes xmlstring, and generate script for
    configResolveDn, configResolveDns, configResolveClass and
    configResolveClasses methods.
    """

    doc = xml.dom.minidom.parseString(xml_string)
    cmdlet = ""
    if not _is_root_node(doc, method):
        return

    # <configResolveDn>
    if method == "configResolveDn":
        top_node = doc.documentElement
        if top_node is None:
            return
        dn = top_node.getAttribute(NamingPropertyId.DN)
        in_hierarchical = ""
        if top_node.hasAttribute("in_hierarchical"):
            in_hierarchical = top_node.getAttribute("in_hierarchical")
        if in_hierarchical.lower() == "true":
            in_hierarchical_value = YesOrNo.TRUE
        else:
            in_hierarchical_value = YesOrNo.FALSE

        cmdlet = 'handle.config_resolve_dn("%s", "%s")' % (
            dn, in_hierarchical_value)
    # <configResolveDns>
    elif method == "configResolveDns":
        top_node = doc.documentElement
        if top_node is None:
            return
        in_hierarchical = ""
        if top_node.hasAttribute("in_hierarchical"):
            in_hierarchical = top_node.getAttribute("in_hierarchical")

        dn_nodes = _get_elem_child_nodes(
            top_node.getElementsByTagName("inDns")[0])
        if dn_nodes is None:
            return

        cmdlet = "dn_set = DnSet()" + "\n"
        temp_dn = ""

        for node in dn_nodes:
            temp_dn = node.getAttribute(NamingPropertyId.VALUE)
            cmdlet += "dn = Dn()\ndn.attr_set(\"value\"," \
                      "\"%s\")\ndn_set.child_add(dn)\n" % temp_dn

        if in_hierarchical.lower() == "true":
            in_hierarchical_value = YesOrNo.TRUE
        else:
            in_hierarchical_value = YesOrNo.FALSE

        cmdlet += 'handle.config_resolve_dns(dn_set, "%s")' % \
                  in_hierarchical_value
    # <configResolveClass>
    elif method == "configResolveClass":
        _and_count = 0
        _or_count = 0
        _not_count = 0
        top_node = doc.documentElement
        filter_node = _get_only_elem_child_node(top_node)
        print(filter_node)
        if top_node is None or filter_node is None:
            return

        in_hierarchical = ""
        if top_node.hasAttribute("in_hierarchical") is not None:
            in_hierarchical = top_node.getAttribute("in_hierarchical")

        class_id = ""
        if top_node.hasAttribute("class_id") is not None:
            class_id = top_node.getAttribute("class_id")

        if in_hierarchical.lower() == "true":
            in_hierarchical_value = YesOrNo.TRUE
        else:
            in_hierarchical_value = YesOrNo.FALSE

        cmdlet = "in_filter = FilterFilter()\n" + _create_python_filter_code(
            filter_node,
            "inFilter") + 'handle.config_resolve_class(' \
                          '"%s", in_filter, "%s")' % (class_id,
                                                      in_hierarchical_value)
    # <configResolveClasses>
    elif method == "configResolveClasses":
        top_node = doc.documentElement
        if top_node is None:
            return

        in_hierarchical = ""
        if top_node.hasAttribute("in_hierarchical") is not None:
            in_hierarchical = top_node.getAttribute("in_hierarchical")

        class_id_nodes = _get_elem_child_nodes(
            top_node.getElementsByTagName("inIds")[0])

        cmdlet = '\nfrom ucsmsdk.ucsbasetype import ClassIdSet, ClassId\n'
        cmdlet += "id_set = ClassIdSet()" + "\n"
        temp_class_id = ""
        for node in class_id_nodes:
            temp_class_id = node.getAttribute(NamingPropertyId.VALUE)
            cmdlet += "class_id = ClassId()\nclass_id.attr_set(\"value\"," \
                      "\"%s\")\nidSet.child_add(class_id)\n" % temp_class_id

        if in_hierarchical.lower() == "true":
            in_hierarchical_value = YesOrNo.TRUE
        else:
            in_hierarchical_value = YesOrNo.FALSE

        cmdlet += 'handle.config_resolve_classes(id_set, "%s")' % \
                  in_hierarchical_value

    return cmdlet


def _create_python_filter_code(parent_node, parent_filter_name):
    """
    Internal method to provide filter support.
    """

    cmdlet = ""
    filter_name = ""
    temp_name = ""

    for node in _get_elem_child_nodes(parent_node):
        if node.localName == "and":
            temp_name = "andFilter" + str(_and_count)
            _and_count += 1
            cmdlet = temp_name
            cmdlet += " = AndFilter()\n"
            cmdlet += _create_python_filter_code(node, temp_name)
            cmdlet += parent_filter_name
            cmdlet += ".child_add(" + temp_name + ")\n"
            continue

        if node.localName == "or":
            temp_name = "orFilter" + str(_or_count)
            _or_count += 1
            cmdlet = temp_name
            cmdlet += " = OrFilter()\n"
            cmdlet += _create_python_filter_code(node, temp_name)
            cmdlet += parent_filter_name
            cmdlet += ".child_add(" + temp_name + ")\n"
            continue

        if node.localName == "not":
            temp_name = "notFilter" + str(_not_count)
            _not_count += 1
            cmdlet = temp_name
            cmdlet += " = NotFilter()\n"
            cmdlet += _create_python_filter_code(node, temp_name)
            cmdlet += parent_filter_name
            cmdlet += ".child_add(" + temp_name + ")\n"
            continue

        if node.localName == "eq":
            filter_name = "eqFilter"
        if node.localName == "ne":
            filter_name = "neFilter"
        if node.localName == "gt":
            filter_name = "gtFilter"
        if node.localName == "lt":
            filter_name = "ltFilter"
        if node.localName == "le":
            filter_name = "leFilter"
        if node.localName == "wcard":
            filter_name = "wcardFilter"
        if node.localName == "anybit":
            filter_name = "anybitFilter"
        if node.localName == "allbits":
            filter_name = "allbitsFilter"
        if node.localName == "bw":
            filter_name = "bwFilter"

        cmdlet += filter_name + " = " + _first_capital(filter_name) + "()\n"

        for name, value in node.attributes.items():
            cmdlet += "%s.%s = \"%s\"\n" % (
                filter_name, _first_capital(name), value)

        cmdlet += parent_filter_name + ".child_add(" + filter_name + ")\n"

    return cmdlet


def _generate_single_clone_cmdlets(xml_string, is_template):
    """
    Internal method which takes xmlstring, and generate script for
    lsClone and lsInstantiateTemplate methods.
    """

    doc = xml.dom.minidom.parseString(xml_string)
    node = None
    top_node = doc.documentElement
    if top_node is None:
        return

    if is_template:
        if top_node.localName == "lsInstantiateTemplate":
            node = top_node
    else:
        if top_node.localName == "lsClone":
            node = top_node

    dn = ""
    if node.hasAttribute(NamingPropertyId.DN):
        dn = node.getAttribute(NamingPropertyId.DN)
    else:
        print("Attribute 'Dn' not available")  # writewarning in dotnet
        return

    sp_new_name = ""
    if node.hasAttribute("inServerName"):
        sp_new_name = node.getAttribute("inServerName")
    else:
        print("Attribute 'inServerName' not available")
        return

    dest_org = ""
    if node.hasAttribute("inTargetOrg"):
        dest_org = node.getAttribute("inTargetOrg")

    match_object = re.match(
        r"^(org-[\-\.:_a-zA-Z0-9]{1,16}/)*org-[\-\.:_a-zA-Z0-9]{1,16}", dn)
    if match_object is not None:
        # source_org = match_object.group(0)
        pass
    else:
        print("Attribute 'Dn' is corrupt")
        return

    cmdlet = ""
    in_hierarchical = ""
    if node.hasAttribute("in_hierarchical") is not None:
        in_hierarchical = node.getAttribute("in_hierarchical")

    if in_hierarchical.lower() == "true":
        in_hierarchical_value = YesOrNo.TRUE
    else:
        in_hierarchical_value = YesOrNo.FALSE

    in_error_on_existing = ""
    if node.hasAttribute("inErrorOnExisting") is not None:
        in_error_on_existing = node.getAttribute("inErrorOnExisting")

    if is_template:
        cmdlet = '\nfrom ucsmsdk.ucsmethodfactory ' \
                 'import ls_instantiate_template\n'
        cmdlet += 'elem = ls_instantiate_template(cookie=' \
                  'handle.cookie, dn="%s", in_error_on_existing=' \
                  '"%s", in_server_name="%s", in_target_org=' \
                  '"%s", in_hierarchical="%s")' % (dn,
                                                   in_error_on_existing,
                                                   sp_new_name,
                                                   dest_org,
                                                   in_hierarchical_value)
        cmdlet += '\nmo_list = handle.process_xml_elem(elem)\n'
    else:
        cmdlet = '\nfrom ucsmsdk.ucsmethodfactory import ls_clone\n'
        cmdlet += 'elem = ls_clone(cookie=handle.cookie, dn=' \
                  '"%s", in_server_name="%s", in_target_org=' \
                  '"%s", in_hierarchical="%s")' % (dn,
                                                   sp_new_name,
                                                   dest_org,
                                                   in_hierarchical_value)
        cmdlet += '\nmo_list = handle.process_xml_elem(elem)\n'

    return cmdlet


def _generate_ls_templatise_cmdlets(xml_string):
    """
    Internal method which takes xmlstring, and generate script for
    lsTemplatise method.
    """

    doc = xml.dom.minidom.parseString(xml_string)
    node = None
    top_node = doc.documentElement
    if top_node is None:
        return

    if top_node.localName == "lsTemplatise":
        node = top_node
    else:
        print("Check if Method is <lsTemplatise>")
        return

    dn = ""
    if node.hasAttribute(NamingPropertyId.DN):
        dn = node.getAttribute(NamingPropertyId.DN)
    else:
        print("Attribute 'Dn' not available")  # writewarning in dotnet
        return

    sp_new_name = ""
    if node.hasAttribute("inTemplateName"):
        sp_new_name = node.getAttribute("inTemplateName")
    else:
        print("Attribute 'inTemplateName' not available")
        return

    template_type = ""
    if node.hasAttribute("inTemplateType"):
        template_type = node.getAttribute("inTemplateType")
    else:
        print("Attribute 'inTemplateType' not available")
        return

    dest_org = ""
    if node.hasAttribute("inTargetOrg"):
        dest_org = node.getAttribute("inTargetOrg")

    match_object = re.match(
        r"^(org-[\-\.:_a-zA-Z0-9]{1,16}/)*org-[\-\.:_a-zA-Z0-9]{1,16}", dn)
    if match_object is not None:
        # source_org = match_object.group(0)
        pass
    else:
        print("Attribute 'Dn' is corrupt")
        return

    cmdlet = ""
    in_hierarchical = ""
    if node.hasAttribute("in_hierarchical") is not None:
        in_hierarchical = node.getAttribute("in_hierarchical")
    if in_hierarchical.lower() == "true":
        in_hierarchical_value = YesOrNo.TRUE
    else:
        in_hierarchical_value = YesOrNo.FALSE

    if dest_org is not None:
        cmdlet = '\nfrom ucsmsdk.ucsmethodfactory import ls_templatise\n'
        cmdlet += 'elem = ls_templatise(cookie=handle.cookie,' \
                  'dn="%s", in_target_org="%s", in_template_name="%s", ' \
                  'in_template_type="%s", in_hierarchical="%s")' % (dn,
                                                                    dest_org,
                                                                    sp_new_name,
                                                                    template_type,
                                                                    in_hierarchical_value)
        cmdlet += '\nmo_list = handle.process_xml_elem(elem)\n'
    else:
        cmdlet = '\nfrom ucsmsdk.ucsmethodfactory import ls_templatise\n'
        cmdlet += 'elem = ls_templatise(cookie=handle.cookie,' \
                  'dn="%s", in_target_org="org-root", ' \
                  'in_template_name="%s", ' \
                  'in_template_type="%s", ' \
                  'in_hierarchical=%s)' % (dn,
                                           sp_new_name,
                                           template_type,
                                           in_hierarchical_value)
        cmdlet += '\nmo_list = handle.process_xml_elem(elem)\n'

    return cmdlet


def _generate_multiple_clone_cmdlets(xml_string, is_prefix_based):
    """
    Internal method which takes xmlstring, and generate script for
    lsInstantiateNTemplate and  lsInstantiateNNamedTemplate methods.
    """

    doc = xml.dom.minidom.parseString(xml_string)
    node = None
    top_node = doc.documentElement
    if top_node is None:
        return

    if is_prefix_based:
        if top_node.localName == "lsInstantiateNTemplate":
            node = top_node
    else:
        if top_node.localName == "lsInstantiateNNamedTemplate":
            node = top_node

    dn = ""
    if node.hasAttribute(NamingPropertyId.DN):
        dn = node.getAttribute(NamingPropertyId.DN)
    else:
        print("Attribute 'Dn' not available")  # writewarning in dotnet
        return

    dest_org = ""
    if node.hasAttribute("inTargetOrg"):
        dest_org = node.getAttribute("inTargetOrg")

    sp_name = re.sub(
        r"^(org-[\-\.:_a-zA-Z0-9]{1,16}/)*org-[\-\.:_a-zA-Z0-9]{1,16}/ls-", "",
        dn)

    # source_org = ""
    match_object = re.match(
        r"^(org-[\-\.:_a-zA-Z0-9]{1,16}/)*org-[\-\.:_a-zA-Z0-9]{1,16}", dn)
    if match_object is not None:
        # source_org = match_object.group(0)
        pass
    else:
        print("Attribute 'Dn' is corrupt")
        return

    cmdlet = ""
    in_hierarchical = ""
    if node.hasAttribute("in_hierarchical") is not None:
        in_hierarchical = node.getAttribute("in_hierarchical")

    in_error_on_existing = ""
    if node.hasAttribute("inErrorOnExisting") is not None:
        in_error_on_existing = node.getAttribute("inErrorOnExisting")

    if is_prefix_based:
        # prefix = ""
        if node.hasAttribute("inServerNamePrefixOrEmpty") is not None:
            # prefix = node.getAttribute("inServerNamePrefixOrEmpty")
            pass
        else:
            print("Attribute 'inServerNamePrefixOrEmpty' not available")
            return

        count = 0
        if node.hasAttribute("inNumberOf") is not None:
            count = node.getAttribute("inNumberOf")
        else:
            print("Attribute 'inNumberOf' not available")
            return

        if in_hierarchical.lower() == "true":
            in_hierarchical_value = YesOrNo.TRUE
        else:
            in_hierarchical_value = YesOrNo.FALSE

        cmdlet = '\nfrom ucsmsdk.ucsmethodfactory import ' \
                 'ls_instantiate_n_template\n'
        cmdlet += 'elem = ls_instantiate_n_template(' \
                  'cookie=handle.cookie, dn=\%s", in_number_of=%s, ' \
                  'in_server_name_prefix_or_empty="%s", in_target_org="%s", ' \
                  'in_hierarchical=%s)' % (dn, count, sp_name, dest_org,
                                           in_hierarchical_value)
        cmdlet += '\nmo_list = handle.process_xml_elem(elem)\n'
    else:
        dn_nodes = _get_elem_child_nodes(
            node.getElementsByTagName("inNameSet")[0])
        if dn_nodes is None or len(dn_nodes) < 1:
            print("Xml is corrupt. New names not available")
            return

        new_names = "@("
        new_name_exists = False
        temp_dn = ""
        cmdlet = '\nfrom ucsmsdk.ucsmethodfactory import ' \
                 'ls_instantiate_n_named_template\n'
        cmdlet += 'from ucsmsdk.ucsbasetype import DnSet, Dn\n\n'
        cmdlet += "dn_set = DnSet()" + "\n"

        for dn_node in dn_nodes:
            if dn_node.hasAttribute("value"):
                new_name_exists = True
                temp_dn = dn_node.getAttribute("value")
                new_names += "\"" + temp_dn + "\","
                cmdlet += "dn = Dn()\ndn.attr_set(\"value\"," \
                          "\"%s\")\ndn_set.child_add(dn)\n" % temp_dn
            else:
                print("Xml is corrupt. New names not available")
                return

        if not new_name_exists:
            print("Xml is corrupt. New names not available")
            return

        new_names = new_names.rstrip(',')
        new_names += ")"

        if in_hierarchical.lower() == "true":
            in_hierarchical_value = YesOrNo.TRUE
        else:
            in_hierarchical_value = YesOrNo.FALSE

        cmdlet += 'elem = ls_instantiate_n_named_template(' \
                  'cookie=handle.cookie, dn="%s", in_error_on_existing=' \
                  '"%s", in_name_set=dn_set, in_target_org' \
                  '="%s", in_hierarchical="%s")' % (dn,
                                                    in_error_on_existing,
                                                    dest_org,
                                                    in_hierarchical_value)
        cmdlet += '\nmo_list = handle.process_xml_elem(elem)\n'
    return cmdlet


def _generate_clear_interval_cmdlet(xml_string):
    """
    Internal method which takes xmlstring, and generate script for
    statsClearInterval method.
    """

    doc = xml.dom.minidom.parseString(xml_string)
    node = None
    top_node = doc.documentElement
    if top_node is None:
        return

    if top_node.localName == "statsClearInterval":
        node = top_node
    else:
        print("Check if Method is <statsClearInterval>")
        return

    cmdlet = ""
    dn_nodes = _get_elem_child_nodes(node.getElementsByTagName("inDns")[0])

    if dn_nodes is None or len(dn_nodes) < 0:
        return

    cmdlet = "dn_set = DnSet()" + "\n"
    temp_dn = ""

    for dn_node in dn_nodes:
        temp_dn = dn_node.getAttribute(NamingPropertyId.VALUE)
        cmdlet += "dn = Dn()\ndn.attr_set(\"value\", " \
                  "\"%s\")\ndn_set.child_add(dn)\n" % temp_dn
    cmdlet += "handle.config_resolve_dns(dn_set)"

    return cmdlet


def _generate_config_conf_rename_cmdlet(xml_string):
    """
    Internal method which takes xmlstring, and generate script for
    configConfRename method.
    """

    doc = xml.dom.minidom.parseString(xml_string)
    node = None
    top_node = doc.documentElement
    if top_node is None:
        return

    if top_node.localName == "configConfRename":
        node = top_node
    else:
        print("Check if Method is <configConfRename>")
        return

    if node.hasAttribute('dn'):
        dn = node.getAttribute('dn')
    if node.hasAttribute('inNewName'):
        in_new_name = node.getAttribute('inNewName')
    if node.hasAttribute('inHierarchical'):
        in_hierarchical = node.getAttribute('inHierarchical')
    cmdlet = "\nfrom ucsmsdk.ucsmethodfactory import config_conf_rename\n\n"
    cmdlet += 'elem = config_conf_rename(' \
              'cookie=handle.cookie, dn="%s", ' \
              'in_new_name="%s", ' \
              'in_hierarchical="%s")' % (dn, in_new_name, in_hierarchical)
    cmdlet += '\nmo_list = handle.process_xml_elem(elem)\n'
    return cmdlet


# ---- END - OF - METHOD SPECIFIC - FUNCTION ----

def _generate_cmdlets(xml_string):
    """
    Internal method which takes xmlstring, and identify which method to call
    for a specific method.
    """

    doc = xml.dom.minidom.parseString(xml_string)
    cmdlet = ""
    global _display_xml, _outfile_path
    if _display_xml:
        # doc = xml.dom.minidom.parseString(xml_string)
        _dump_xml_on_screen(doc)

    category = ""
    match_found = re.match(r"^[\s]*<[\s]*([\S]+)", xml_string)
    if match_found:
        method_name = match_found.group(1)
        category = method_name
    else:
        return

    if category == "configConfMos" or category == "configConfMo":
        cmdlet = _generate_config_conf_cmdlets(xml_string)
    elif category in ["configResolveDn", "configResolveDns",
                      "configResolveClass", "configResolveClasses"]:
        cmdlet = _generate_config_resolve_cmdlet(xml_string, category)
    elif category == "lsClone":
        cmdlet = _generate_single_clone_cmdlets(xml_string, False)
    elif category == "lsInstantiateTemplate":
        cmdlet = _generate_single_clone_cmdlets(xml_string, True)
    elif category == "lsTemplatise":
        cmdlet = _generate_ls_templatise_cmdlets(xml_string)
    elif category == "lsInstantiateNTemplate":
        cmdlet = _generate_multiple_clone_cmdlets(xml_string, True)
    elif category == "lsInstantiateNNamedTemplate":
        cmdlet = _generate_multiple_clone_cmdlets(xml_string, False)
    elif category == "statsClearInterval":
        cmdlet = _generate_clear_interval_cmdlet(xml_string)
    elif category == "configConfRename":
        cmdlet = _generate_config_conf_rename_cmdlet(xml_string)
    # support for redirecting script output to respective file
    if _outfile_flag:
        _outfile = open(_outfile_path, 'a')
        _outfile.write('##### Start-Of-PythonScript #####')
        _outfile.write(cmdlet)
        _outfile.write('\n##### End-Of-PythonScript #####\n\n')
        _outfile.close()
    else:
        print("##### Start-Of-PythonScript #####")
        print(cmdlet)
        print("##### End-Of-PythonScript #####")
    return


def _extract_xml(file_stream, line):
    """
    Internal method which extracts xmlstring from the file stream and calls the
    _generate_cmdlets() on this xmlstring.
    """

    read_flag = False
    request_string = ""
    line_count = 0
    while line != "":
        if read_flag and not re.search(r"^\s*$", line):
            request_string += line + "\n"
            line_count += 1
        if _check_if_any_list_value_in_string(_multi_line_method, line):
            request_string += line + "\n"
            read_flag = True
            line_count += 1
        if read_flag and _check_if_any_list_value_in_string(
                _single_line_method, line):
            if line_count > 1 and '/>' in line:
                line = file_stream.readline()
                continue
            read_flag = False
            _generate_cmdlets(request_string)
            request_string = ""
            break

        line = file_stream.readline()


def _find_xml_requests_in_file(file_stream, gui_log):
    """
    Internal method which depending on gui_log flag, calls the _extract_xml()
    internally.
    """

    line = file_stream.readline()
    while line != "":
        if not gui_log:
            _extract_xml(file_stream, line)
        elif "[------------- Sending Request to Server ------------" in line:
            line = file_stream.readline()
            if line is not None and _check_if_any_list_value_in_string(
                    _multi_line_method,line):
                # print "[%s]" %(line)
                _extract_xml(file_stream, line)
        line = file_stream.readline()


def _if_path_or_literal_path(path, literal_path, gui_log):
    """
    Internal method which checks if path or literal_path present for the
    respective parameter set and if exists then
    call _find_xml_requests_in_file().
    """

    if path:
        if literal_path:
            print("Parameter <path> takes precedence over <literal_path>")
        file_path = path
    elif literal_path:
        file_path = literal_path
    else:
        print("Please provide path or literal_path")
        return

    file_stream = open(file_path, 'r')
    _find_xml_requests_in_file(file_stream, gui_log)
    file_stream.close()


def _get_ucs_default_logpath_windows():
    """
    Internal method to find ucsm logs path on windows os.
    """

    if 'APPDATA' in os.environ.keys():
        log_file_path = os.getenv('APPDATA')
    else:
        print(os.name)
        raise Exception('Not windows OS')

    if sys.getwindowsversion()[0] == 6:  # in case OS is Win 2008 or above
        log_file_path = os.path.join(dirname(log_file_path), "LocalLow")
    log_file_path += r"\Sun\Java\Deployment\log\.ucsm" + "\\"
    return log_file_path


def _get_ucs_default_logpath_linux():
    """
    Internal method to find ucsm logs path on linux os.
    """

    log_file_path = os.getenv('HOME')
    log_file_path += r"/.java/deployment/log/.ucsm/"
    return log_file_path


def _get_ucs_default_logpath_osx():
    """
    Internal method to find ucsm logs path on osx os.
    """

    log_file_path = os.getenv('HOME')
    # log_file_path += r"/Library/Caches/Java/log/.ucsm"
    path = r"/Library/Application Support/Oracle/Java/Deployment/log/.ucsm"
    log_file_path += path
    return log_file_path


def _get_ucs_default_logpath_cygwin():
    """
    Internal method to find ucsm logs path on cygwin os.
    """

    log_file_path = os.getenv('APPDATA')
    log_file_path = log_file_path.replace("\\", "/")
    # TODO:
    # if OSMajorVersion == 6:
    log_file_path = dirname(log_file_path) + "/LocalLow"
    log_file_path += r"/Sun/Java/Deployment/log/.ucsm/"
    return log_file_path


def convert_to_ucs_python(log_path=None, xml=False, request=None,
                          gui_log=False, path=None, literal_path=None,
                          dump_to_file=False, dump_file_path=None,
                          dump_xml=False):
    """
    This operation generates python script from ucsm gui using ucsm logs
    or directly from ucs logfile or xml request.

    Args:
        log_path (str): ucsm guilog path, if code unable to find the ucsm
              guilog path you can specify the path using this parameter.
        xml (bool): if True, generates python script using xml request.
        request (str): xml request
        gui_log (bool): if True, generates python script using ucsm logfile
        path (str): path of the file containing xml request or ucsm logfile
        literal_path (str): path of the file containing xml request or
              ucsm logfile
        dump_to_file (bool): if True, dump the code to file
        dump_file_path (str): path of file where to dump generated code.
        dump_xml (bool): if True, display the xml extracted for generating
              code

    Examples:
        * Optional in all param set - dump_to_file, dump_file_path, dump_xml

        * param set 1:
            convert_to_ucs_python()\n
            convert_to_ucs_python(dump_xml=True)\n
            file_path = r"/home/user/pythoncode.py"\n
            convert_to_ucs_python(dump_to_file=True,
                              dump_file_path=file_path,
                              dump_xml=True)\n

        * param set 2:
            xml_str='''
             <configConfRename
             dn="org-root/ls-ra1"
             inNewName="ra2"
             inHierarchical="false">
             </configConfRename>'''\n
            convert_to_ucs_python(xml=True, request=xml_str)\n

            file_path = '/home/user/ucsmxml/configrequest.xml'\n
            convert_to_ucs_python(xml=True, path=file_path)\n

        * param set 3:
            file_path = '/home/user/ucsmlog/centrale_14804.log'\n
            convert_to_ucs_python(gui_log=True, path=file_path)\n
    """

    print("### Please review the generated cmdlets before deployment.\n")
    global _display_xml, _outfile_flag, _outfile_path, _outfile
    _display_xml = dump_xml
    _outfile_flag = dump_to_file
    _outfile_path = dump_file_path

    if _outfile_flag in ucsgenutils.AFFIRMATIVE_LIST:
        if _outfile_path:
            print("### Script Output is in file < " + _outfile_path + " >")
            _outfile = open(_outfile_path, 'w')
            _outfile.close()
            # _outfile = open(r"c:\work.txt", 'w+')
        else:
            print("Provide dump_file_path")
            return
    if xml in ucsgenutils.AFFIRMATIVE_LIST:
        if gui_log in ucsgenutils.AFFIRMATIVE_LIST:
            print("parameter <xml> takes precedence over <gui_log>")
        if request:
            _generate_cmdlets(request)
        elif path or literal_path:
            _if_path_or_literal_path(path, literal_path, False)
        else:
            print("Provide request")
            return
    elif gui_log in ucsgenutils.AFFIRMATIVE_LIST:
        if path or literal_path:
            _if_path_or_literal_path(path, literal_path, True)
        else:
            print("Provide path or literal_path")
    else:
        if log_path:
            if not os.path.exists(log_path):
                raise ValueError("%s does not exists." % log_path)
            if not os.path.isdir(log_path):
                raise ValueError("%s is not a directory." % log_path)
            log_file_path = log_path
        else:
            from sys import platform as _platform

            if _platform.lower() == "linux" or _platform.lower() == "linux2":
                # linux
                log_file_path = _get_ucs_default_logpath_linux()
            elif _platform.lower() == "darwin":
                # OS X
                log_file_path = _get_ucs_default_logpath_osx()
            elif _platform.lower() == "win32" or _platform.lower() == "win64":
                # Windows...
                log_file_path = _get_ucs_default_logpath_windows()
            elif "cygwin" in _platform.lower():
                # Cygwin
                log_file_path = _get_ucs_default_logpath_cygwin()
            else:
                print("[Error]: Unsupported OS: %s" % _platform)
                log_file_path = None
                return

        os.chdir(log_file_path)
        files = [file_ for file_ in glob.glob("centrale_*.log") if
                 os.path.isfile(file_)]
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        last_updated_file = files[0]

        print("ucsm logfile: %s\n" % (
            os.path.join(log_file_path, last_updated_file)))

        file_stream = open(last_updated_file, 'r')
        # read the file till the end
        cnt = 0
        for line in file_stream:
            cnt += 1
        # Wait indefinitely until receive new line of set and then again wait
        while True:
            # line = file_stream.readline()
            # if line:
            #     _find_xml_requests_in_file_test(file_stream, True)
            _find_xml_requests_in_file(file_stream, True)
            time.sleep(2)
        file_stream.close()

        # if _outfile_path:
        # _outfile.close()

    print("### End of Convert-To-Python ###")
