"""Copyright 2013 Cisco Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
"""This module generated the python script using UCS GUI, GUI logs."""
import os
import sys
import time
import glob
import re
import xml.dom
import xml.dom.minidom
from os.path import dirname
import logging

log = logging.getLogger('ucs')

from .. import ucsgenutils
from .. import ucscoreutils
from ..ucsconstants import Status, NamingPropertyId
from ..ucsexception import UcsValidationException

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
                      "<lsInstantiateTemplate", "<lsInstantiateNTemplate"]
_single_line_method = ["</configConfMo", "</lsInstantiateNNamedTemplate",
                       "</statsClearInterval", "</lsClone", "</lsTemplatise",
                       "</lsInstantiateTemplate", "</lsInstantiateNTemplate",
                       "/>"]


# class declaration
class _ClassStatus:
    """Constant class for _ClassStatus."""
    NONE_ = 0
    CREATED = 1
    MODIFIED = 2
    REMOVED = 4
    DELETED = 8


# Function Definition
# ---- START - OF - GENERIC - FUCNTION ----
def _get_class_id_for_dn(dn):
    """Get the ClassID for a given DN."""
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
    """Get the ClassID for a given RN."""
    if not prev_class_id:
        prev_class_id = "TopRoot"

    meta_class_id = ucscoreutils.find_class_id_in_mo_meta_ignore_case(
        prev_class_id)
    if meta_class_id is None:
        raise UcsValidationException(
            '[Error]: GetManagedObject: class_id [%s] is not valid' % (
                prev_class_id))

    mo_meta = ucscoreutils.get_mo_property_meta(meta_class_id, "mo_meta")
    if mo_meta is None:
        raise UcsValidationException(
            '[Error]: GetManagedObject: mo_meta for class_id [%s] is not valid'
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
    """Modify the Property Name."""
    new_prop = re.sub('_+', '_',
                      re.sub('^_', '',
                             re.sub(r'[/\-: +]', '_',
                                    re.sub(r'([a-z0-9])([A-Z])',
                                           r'\g<1>_\g<2>', prop)))).upper()
    return new_prop


def _first_capital(string):
    """Makes first letter of string capital."""
    string = string[:1].upper() + string[1:]
    return string


def _is_root_node(dom, tag_name):
    """check if node is root node."""
    root_node_tag_name = dom.documentElement.tag_name
    if root_node_tag_name == tag_name:
        return True
    else:
        return False


def _get_pair_nodes(root_node):
    """get pairnodes in a list."""
    method_elem = root_node
    in_configs_elem_list = method_elem.getElementsByTagName("inConfigs")
    in_configs_elem = in_configs_elem_list[0]
    pair_elems_list = in_configs_elem.getElementsByTagName("pair")
    return pair_elems_list


def _get_only_elem_child_node(node):
    """use if parent only has single childnode."""
    child_list = [child_node for child_node in node.childNodes
                  if child_node.nodeType == child_node.ELEMENT_NODE]
    return child_list[0]


def _get_elem_child_nodes(node):
    """use if parent has more than one child."""
    child_list = [child_node for child_node in node.childNodes if
                  child_node.nodeType == child_node.ELEMENT_NODE]
    return child_list


def _dump_xml_on_screen(doc):
    """used to dump xml on screen."""
    global _outfile_path, _outfile_flag
    xml_new = doc.toprettyxml(indent=" ")
    xml_new = re.sub(r"^.*?xml version.*\n", "", xml_new)
    xml_new = re.sub(r"\n[\s]*\n", "\n", xml_new)
    multiline_pattern = re.compile(r"^(.*)", flags=re.MULTILINE)
    xml_new = re.sub(multiline_pattern, r"#\1", xml_new)
    if _outfile_flag:
        _outfile = open(_outfile_path, 'a')
        print >> _outfile, "\n##### Start-Of-XML #####\n"
        print >> _outfile, "%s" % xml_new
        print >> _outfile, "\n##### End-Of-XML #####"
        _outfile.close()
    else:
        print "\n##### Start-Of-XML #####\n"
        print xml_new
        print "\n##### End-Of-XML #####\n"


def _create_python_property_map(property_map):
    """create a string of dictionary property_map."""
    prop_map_str = "{"
    for key, value in property_map.iteritems():
        prop_map_str = prop_map_str + key + ":" + value + ", "

    if prop_map_str != "{":
        prop_map_str = prop_map_str[:-2]  # removes last 2 char
    return prop_map_str + "}"


def _check_if_any_list_value_in_string(listx, line):
    """Returns True if any of the list value present in line."""
    flag = False
    for value in listx:
        if value in line:
            flag = True
            break
    return flag


# ---- END - OF - GENERIC - FUCNTION ----

# ---- START - OF - METHOD SPECIFIC - FUNCTION ----
def _get_config_conf_cmdlet(node, is_pair_node):
    """Used in function _generate_config_conf_cmdlets."""
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
    if class_node.hasAttribute(NamingPropertyId.DN):
        dn = class_node.getAttribute(NamingPropertyId.DN)

    mo_tag = ""
    if class_node.hasChildNodes() and len(
            _get_elem_child_nodes(class_node)) > 0:
        mo_tag = "mo"

    import_list = []
    cmdlet, op_flag, import_list = _form_python_cmdlet(class_node,
                                                       key,
                                                       mo_tag,
                                                       import_list)

    if class_node.hasChildNodes() and \
                    len(_get_elem_child_nodes(class_node)) > 0:
        call_count = 1
        # cmdlet = "handle.start_ucs_transaction()" + "\n" + cmdlet

        for child_node in _get_elem_child_nodes(class_node):
            sub_cmdlet, import_list = _get_config_conf_sub_cmdlet(child_node,
                                                                  dn, mo_tag,
                                                                  call_count,
                                                                  import_list)
            call_count += 1
            if sub_cmdlet is not None:
                cmdlet += "\n" + sub_cmdlet
            else:
                call_count -= 1

                # cmdlet += "\n" + "handle.complete_ucs_transaction()"
    if op_flag:
        if op_flag == "add":
            cmdlet += "\n" + "handle.add_mo(mo)"

        import_cmdlet = ""
        for mo in import_list:
            mo_folder = re.match("([a-z])+", ucsgenutils.word_l(mo)).group()
            import_cmdlet += "from ucsmsdk.mometa.%s.%s import %s\n" % (
                mo_folder, mo, mo)
        import_cmdlet += "\n" + cmdlet
        cmdlet = import_cmdlet

    return cmdlet


def _get_config_conf_sub_cmdlet(class_node, parent_dn, parent_mo_tag,
                                parent_call_count, import_list):
    """Used in function _generate_config_conf_cmdlets."""
    cmdlet = ""
    dn = ""
    # use_parent_mo = False ##if the parent mo should be used at this level

    if class_node.hasAttribute(NamingPropertyId.DN):
        dn = class_node.getAttribute(NamingPropertyId.DN)
    elif class_node.hasAttribute(NamingPropertyId.RN):
        dn = parent_dn + "/" + class_node.getAttribute(NamingPropertyId.RN)

    count = 1
    tag = parent_mo_tag + "_" + str(parent_call_count)
    cmdlet, op_flag, import_list = _form_python_sub_cmdlet(class_node,
                                                           dn,
                                                           tag,
                                                           parent_mo_tag,
                                                           import_list)

    # Recursively cater to subnodes
    for child_node in _get_elem_child_nodes(class_node):
        sub_cmdlet, import_list = _get_config_conf_sub_cmdlet(child_node,
                                                              dn,
                                                              tag,
                                                              count,
                                                              import_list)
        count += 1
        if sub_cmdlet is not None:
            cmdlet += "\n" + sub_cmdlet
        else:
            count -= 1

    return cmdlet, import_list


def _form_python_cmdlet(class_node, key, tag, import_list):
    """Used in function _generate_config_conf_cmdlets."""
    cmdlet = ""
    class_status = _ClassStatus.NONE_
    property_map = {}
    op_flag = None

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
        class_status = _ClassStatus.CREATED | _ClassStatus.MODIFIED

    # support to handle unknown MOs
    if ucscoreutils.find_class_id_in_mo_meta_ignore_case(
            class_node.localName) is None:
        gmo_flag = True
    else:
        gmo_flag = False

    parent_dn = dirname(key)

    if not gmo_flag:
        peer_class_id = _first_capital(class_node.localName)
        # peer_class_id_str = peer_class_id + ".class_id()"
        # dn_str = '.DN'

        peer_class_ref = ucscoreutils.load_class(peer_class_id)
        peer_class_naming_props = peer_class_ref.naming_props
        peer_class_prop_map = peer_class_ref.prop_map
        peer_class_prop_meta = peer_class_ref.prop_meta

    else:
        # peer_class_id = ""
        # peer_class_id_str = '"'+(class_node.localName)+'"'
        # dn_str = '"dn"'
        pass
    # ToDo Add Generic Mo functionality

    if _get_class_id_for_dn(parent_dn) is None:
        parent_class_id = ""
        parent_class_id_str = "None"
        parent_dn_str = '"dn"'
    else:
        parent_class_id = _get_class_id_for_dn(parent_dn)
        parent_class_id_str = parent_class_id + ".class_id()"
        parent_dn_str = '.DN'

    # create property map for attributes

    for attr, val in class_node.attributes.items():
        name = attr
        value = '"' + val + '"'
        if name != NamingPropertyId.DN and \
                        name != NamingPropertyId.RN and \
                        name != NamingPropertyId.STATUS:
            if name.lower() == "Filter".lower():
                prop_ucs = "FilterValue"
            else:
                prop_ucs = name

            if prop_ucs is None:
                continue

            if not gmo_flag and prop_ucs in peer_class_prop_map:
                prop_py = peer_class_prop_map[prop_ucs]
                if peer_class_prop_meta[prop_py].access != 3:
                    if class_status & _ClassStatus.CREATED == \
                            _ClassStatus.CREATED:
                        if prop_ucs not in peer_class_naming_props:
                            continue
                    else:
                        continue
            else:
                prop_py = prop_ucs

            property_map[prop_py] = value

    tag_elem = ""
    if tag:
        tag_elem = tag + " = "

    # make cmdlet
    if class_status & _ClassStatus.DELETED == _ClassStatus.DELETED or \
                            class_status & \
                            _ClassStatus.REMOVED == _ClassStatus.REMOVED:
        op_flag = "remove"
        cmdlet = "obj = handle.query_dn(\"%s\")\n%shandle.remove_mo(obj)" % (
            key, tag_elem)
    elif class_status & _ClassStatus.CREATED == _ClassStatus.CREATED:
        op_flag = "add"
        if peer_class_id not in import_list:
            import_list.append(peer_class_id)
        if class_status & _ClassStatus.MODIFIED == _ClassStatus.MODIFIED:
            add_prop_map = ",".join(
                [k + "=" + v for k, v in property_map.iteritems()])
            cmdlet = 'mo = %s(parent_mo_or_dn="%s", %s)' % (
                peer_class_id, parent_dn, add_prop_map)
        else:
            add_prop_map = ", ".join(
                [k + "=" + v for k, v in property_map.iteritems()])
            cmdlet = 'mo = %s(parent_mo_or_dn="%s", %s)' % (
                peer_class_id, parent_dn, add_prop_map)
    elif class_status & _ClassStatus.MODIFIED == _ClassStatus.MODIFIED:
        op_flag = "set"
        set_prop_map = "\n".join(
            ["obj." + k + " = " + v for k, v in property_map.iteritems()])
        cmdlet = "obj = handle.query_dn(\"%s\")\n%s\nhandle.set_mo(obj) " % (
            key, set_prop_map)
    else:
        print "Throw Exception XML request status (%s) is invalid." % (
            class_node.getAttribute(NamingPropertyId.STATUS))

    return cmdlet, op_flag, import_list


def _form_python_sub_cmdlet(class_node, key, mo_tag, parent_mo_tag,
                            import_list):
    """Used in function _generate_config_conf_cmdlets."""
    cmdlet = ""
    class_status = _ClassStatus.NONE_
    property_map = {}
    op_flag = None

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
        class_status = _ClassStatus.CREATED | _ClassStatus.MODIFIED

    # support to handle unknown MOs
    if ucscoreutils.find_class_id_in_mo_meta_ignore_case(
            class_node.localName) is None:
        gmo_flag = True
    else:
        gmo_flag = False

    if not gmo_flag:
        peer_class_id = _first_capital(class_node.localName)
        peer_class_ref = ucscoreutils.load_class(peer_class_id)
        peer_class_naming_props = peer_class_ref.naming_props
        peer_class_prop_map = peer_class_ref.prop_map
        peer_class_prop_meta = peer_class_ref.prop_meta
    else:
        pass
    # ToDo Add Generic Mo functionality

    # create property map for attributes
    for attr, val in class_node.attributes.items():
        name = attr
        value = '"' + val + '"'
        if name != NamingPropertyId.DN and \
                        name != NamingPropertyId.RN and \
                        name != NamingPropertyId.STATUS:
            if name.lower() == "Filter".lower():
                prop_ucs = "FilterValue"
            else:
                prop_ucs = name

            if prop_ucs is None:
                continue

            if not gmo_flag and prop_ucs in peer_class_prop_map:
                prop_py = peer_class_prop_map[prop_ucs]
                if peer_class_prop_meta[prop_py].access != 3:
                    if class_status & _ClassStatus.CREATED == \
                            _ClassStatus.CREATED:
                        if prop_ucs not in peer_class_naming_props:
                            continue
                    else:
                        continue
            else:
                prop_py = prop_ucs

            property_map[prop_py] = value

    # make cmdlet
    if class_status & _ClassStatus.DELETED == _ClassStatus.DELETED or \
                            class_status \
                            & _ClassStatus.REMOVED == _ClassStatus.REMOVED:
        cmdlet = "obj = handle.query_dn(\"%s\")\n%shandle.remove_mo(obj)" % (
            key, mo_tag)
    elif class_status & _ClassStatus.CREATED == _ClassStatus.CREATED:
        op_flag = "add"
        if peer_class_id not in import_list:
            import_list.append(peer_class_id)
        add_prop_map = ", ".join(
            [k + "=" + v for k, v in property_map.iteritems()])
        cmdlet = "%s = %s(parent_mo_or_dn=%s, %s)" % (
            mo_tag, peer_class_id, parent_mo_tag, add_prop_map)
    elif class_status & _ClassStatus.MODIFIED == _ClassStatus.MODIFIED:
        set_prop_map = "\n".join(
            ["obj." + k + " = " + v for k, v in property_map.iteritems()])
        cmdlet = "obj = handle.query_dn(\"%s\")\n%s\nhandle.set_mo(obj)" % (
            key, set_prop_map)
    else:
        print "Throw Exception XML request status (%s) is invalid." % (
            class_node.getAttribute(NamingPropertyId.STATUS))

    return cmdlet, op_flag, import_list


def _generate_config_conf_cmdlets(xml_string):
    """
    Takes xmlstring, and generate script for configConfMos
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
    Takes xmlstring, and generate script for configResolveDn,
    configResolveDns, configResolveClass and configResolveClasses methods.
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
            in_hierarchical_value = "YesOrNo.TRUE"
        else:
            in_hierarchical_value = "YesOrNo.FALSE"

        cmdlet = "handle.config_resolve_dn(\"%s\", %s)" % (
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
            in_hierarchical_value = "YesOrNo.TRUE"
        else:
            in_hierarchical_value = "YesOrNo.FALSE"

        cmdlet += "handle.config_resolve_dns(dn_set, %s)" % \
                  in_hierarchical_value
    # <configResolveClass>
    elif method == "configResolveClass":
        _and_count = 0
        _or_count = 0
        _not_count = 0
        top_node = doc.documentElement
        filter_node = _get_only_elem_child_node(top_node)
        print filter_node
        if top_node is None or filter_node is None:
            return

        in_hierarchical = ""
        if top_node.hasAttribute("in_hierarchical") is not None:
            in_hierarchical = top_node.getAttribute("in_hierarchical")

        class_id = ""
        if top_node.hasAttribute("class_id") is not None:
            class_id = top_node.getAttribute("class_id")

        if in_hierarchical.lower() == "true":
            in_hierarchical_value = "YesOrNo.TRUE"
        else:
            in_hierarchical_value = "YesOrNo.FALSE"

        cmdlet = "in_filter = FilterFilter()\n" + _create_python_filter_code(
            filter_node,
            "inFilter") + "handle.config_resolve_class(\"%s\", in_filter, " \
                          "%s)" % (class_id, in_hierarchical_value)
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
            in_hierarchical_value = "YesOrNo.TRUE"
        else:
            in_hierarchical_value = "YesOrNo.FALSE"

        cmdlet += "handle.config_resolve_classes(id_set, %s)" % \
                  in_hierarchical_value

    return cmdlet


def _create_python_filter_code(parent_node, parent_filter_name):
    """provide filter support."""
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
    """Method to handle method <lsClone> and <lsInstantiateTemplate>."""
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
        print "Attribute 'Dn' not available"  # writewarning in dotnet
        return

    sp_new_name = ""
    if node.hasAttribute("inServerName"):
        sp_new_name = node.getAttribute("inServerName")
    else:
        print "Attribute 'inServerName' not available"
        return

    dest_org = ""
    if node.hasAttribute("inTargetOrg"):
        dest_org = node.getAttribute("inTargetOrg")

    # sp_name = re.sub(
    # r"^(org-[\-\.:_a-zA-Z0-9]{1,16}/)*org-[\-\.:_a-zA-Z0-9]{1,16}/ls-",
    #  "",
    #  dn)
    # source_org = ""
    match_object = re.match(
        r"^(org-[\-\.:_a-zA-Z0-9]{1,16}/)*org-[\-\.:_a-zA-Z0-9]{1,16}", dn)
    if match_object is not None:
        # source_org = match_object.group(0)
        pass
    else:
        print "Attribute 'Dn' is corrupt"
        return

    cmdlet = ""
    in_hierarchical = ""
    if node.hasAttribute("in_hierarchical") is not None:
        in_hierarchical = node.getAttribute("in_hierarchical")

    if in_hierarchical.lower() == "true":
        in_hierarchical_value = "YesOrNo.TRUE"
    else:
        in_hierarchical_value = "YesOrNo.FALSE"

    in_error_on_existing = ""
    if node.hasAttribute("inErrorOnExisting") is not None:
        in_error_on_existing = node.getAttribute("inErrorOnExisting")

    if is_template:
        # cmdlet = "handle.ls_instantiate_template(dn=\"%s\",
        # in_error_on_existing=\"%s\", in_server_name=\"%s\",
        # in_target_org=\"%s\", in_hierarchical=%s)"
        # %(dn, in_error_on_existing, sp_new_name, dest_org,
        # in_hierarchical_value)

        cmdlet = '\nfrom ucsmsdk.ucsmethodfactory ' \
                 'import ls_instantiate_template\n'
        cmdlet += 'elem = ls_instantiate_template(cookie=' \
                  'handle.cookie, dn="%s", in_error_on_existing=' \
                  '"%s", in_server_name="%s", in_target_org=' \
                  '"%s", in_hierarchical=%s)' % (dn,
                                                 in_error_on_existing,
                                                 sp_new_name,
                                                 dest_org,
                                                 in_hierarchical_value)
        cmdlet += '\nmo_list = handle.process_xml_elem(elem)\n'
    else:
        # cmdlet = "handle.ls_clone(dn=\"%s\", in_server_name=\"%s\",
        # in_target_org=\"%s\", in_hierarchical=%s)" %(dn, sp_new_name,
        # dest_org, in_hierarchical_value)

        cmdlet = '\nfrom ucsmsdk.ucsmethodfactory import ls_clone\n'
        cmdlet += 'elem = ls_clone(cookie=handle.cookie, dn=' \
                  '"%s", in_server_name="%s", in_target_org=' \
                  '"%s", in_hierarchical=%s)' % (dn,
                                                 sp_new_name,
                                                 dest_org,
                                                 in_hierarchical_value)
        cmdlet += '\nmo_list = handle.process_xml_elem(elem)\n'

    return cmdlet


def _generate_ls_templatise_cmdlets(xml_string):
    """Function to handle method <lsTemplatise>."""
    doc = xml.dom.minidom.parseString(xml_string)
    node = None
    top_node = doc.documentElement
    if top_node is None:
        return

    if top_node.localName == "lsTemplatise":
        node = top_node
    else:
        print "Check if Method is <lsTemplatise>"
        return

    dn = ""
    if node.hasAttribute(NamingPropertyId.DN):
        dn = node.getAttribute(NamingPropertyId.DN)
    else:
        print "Attribute 'Dn' not available"  # writewarning in dotnet
        return

    sp_new_name = ""
    if node.hasAttribute("inTemplateName"):
        sp_new_name = node.getAttribute("inTemplateName")
    else:
        print "Attribute 'inTemplateName' not available"
        return

    template_type = ""
    if node.hasAttribute("inTemplateType"):
        template_type = node.getAttribute("inTemplateType")
    else:
        print "Attribute 'inTemplateType' not available"
        return

    dest_org = ""
    if node.hasAttribute("inTargetOrg"):
        dest_org = node.getAttribute("inTargetOrg")

    # sp_name = re.sub(
    # r"^(org-[\-\.:_a-zA-Z0-9]{1,16}/)*org-[\-\.:_a-zA-Z0-9]{1,16}/ls-",
    #  "", dn)
    # source_org = ""

    match_object = re.match(
        r"^(org-[\-\.:_a-zA-Z0-9]{1,16}/)*org-[\-\.:_a-zA-Z0-9]{1,16}", dn)
    if match_object is not None:
        # source_org = match_object.group(0)
        pass
    else:
        print "Attribute 'Dn' is corrupt"
        return

    cmdlet = ""
    in_hierarchical = ""
    if node.hasAttribute("in_hierarchical") is not None:
        in_hierarchical = node.getAttribute("in_hierarchical")
    if in_hierarchical.lower() == "true":
        in_hierarchical_value = "YesOrNo.TRUE"
    else:
        in_hierarchical_value = "YesOrNo.FALSE"

    if dest_org is not None:
        # cmdlet = "handle.ls_templatise(dn=\"%s\", in_target_org=\"%s\",
        # in_template_name=\"%s\", in_template_type=\"%s\",
        # in_hierarchical=%s)" % (dn, dest_org, sp_new_name,
        # template_type, in_hierarchical_value)

        cmdlet = '\nfrom ucsmsdk.ucsmethodfactory import ls_templatise\n'
        cmdlet += 'elem = ls_templatise(cookie=handle.cookie,' \
                  'dn="%s", in_target_org="%s", in_template_name="%s", ' \
                  'in_template_type="%s", in_hierarchical=%s)' % (dn,
                                                        dest_org,
                                                        sp_new_name,
                                                        template_type,
                                                        in_hierarchical_value)
        cmdlet += '\nmo_list = handle.process_xml_elem(elem)\n'
    else:
        # cmdlet = "handle.ls_templatise(dn=\"%s\", in_target_org=\"org-root\",
        #  in_template_name=\"%s\", in_template_type=\"%s\",
        # in_hierarchical=%s)" % (dn, sp_new_name, template_type,
        # in_hierarchical_value)

        cmdlet = '\nfrom ucsmsdk.ucsmethodfactory import ls_templatise\n'
        cmdlet += 'elem = ls_templatise(cookie=handle.cookie,' \
                  'dn="%s", in_target_org="org-root", in_template_name="%s", '\
                  'in_template_type="%s", in_hierarchical=%s)' % (dn,
                                                        sp_new_name,
                                                        template_type,
                                                        in_hierarchical_value)
        cmdlet += '\nmo_list = handle.process_xml_elem(elem)\n'

    return cmdlet


def _generate_multiple_clone_cmdlets(xml_string, is_prefix_based):
    """
    Function to handle method <lsInstantiateNTemplate> and
    <lsInstantiateNNamedTemplate>.
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
        print "Attribute 'Dn' not available"  # writewarning in dotnet
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
        print "Attribute 'Dn' is corrupt"
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
            print "Attribute 'inServerNamePrefixOrEmpty' not available"
            return

        count = 0
        if node.hasAttribute("inNumberOf") is not None:
            count = node.getAttribute("inNumberOf")
        else:
            print "Attribute 'inNumberOf' not available"
            return

        if in_hierarchical.lower() == "true":
            in_hierarchical_value = "YesOrNo.TRUE"
        else:
            in_hierarchical_value = "YesOrNo.FALSE"

        # cmdlet = "handle.ls_instantiate_n_template(dn=\"%s\",
        # in_number_of=%s, in_server_name_prefix_or_empty=\"%s\",
        # in_target_org=\"%s\", in_hierarchical=%s)" % (dn, count, sp_name,
        # dest_org, in_hierarchical_value)

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
            print "Xml is corrupt. New names not available"
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
                print "Xml is corrupt. New names not available"
                return

        if not new_name_exists:
            print "Xml is corrupt. New names not available"
            return

        new_names = new_names.rstrip(',')
        new_names += ")"

        if in_hierarchical.lower() == "true":
            in_hierarchical_value = "YesOrNo.TRUE"
        else:
            in_hierarchical_value = "YesOrNo.FALSE"

        # cmdlet += "handle.ls_instantiate_n_named_template(dn=\"%s\",
        # in_error_on_existing=\"%s\", in_name_set=dn_set,
        # in_target_org=\"%s\", in_hierarchical=\"%s\")" %(dn,
        # in_error_on_existing, dest_org, in_hierarchical_value)

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
    """Function to handle method <statsClearInterval>."""
    doc = xml.dom.minidom.parseString(xml_string)
    node = None
    top_node = doc.documentElement
    if top_node is None:
        return

    if top_node.localName == "statsClearInterval":
        node = top_node
    else:
        print "Check if Method is <statsClearInterval>"
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
    doc = xml.dom.minidom.parseString(xml_string)
    node = None
    top_node = doc.documentElement
    if top_node is None:
        return

    if top_node.localName == "configConfRename":
        node = top_node
    else:
        print "Check if Method is <configConfRename>"
        return

    if node.hasAttribute('dn'):
        dn = node.getAttribute('dn')
    if node.hasAttribute('inNewName'):
        in_new_name = node.getAttribute('inNewName')
    if node.hasAttribute('inHierarchical'):
        in_hierarchical = node.getAttribute('inHierarchical')
    cmdlet = "\nfrom ucsmsdk.ucsmethodfactory import config_conf_rename\n"
    cmdlet += 'elem = config_conf_rename(' \
              'cookie=handle.cookie, dn="%s", ' \
              'in_new_name="%s", '\
              'in_hierarchical="%s")' % (dn, in_new_name, in_hierarchical)
    cmdlet += '\nhandle.process_xml_elem(elem)\n'
    return cmdlet


# ---- END - OF - METHOD SPECIFIC - FUNCTION ----

def _generate_cmdlets(xml_string):
    """checks which function to call for a specific method."""
    cmdlet = ""
    global _display_xml, _outfile_path
    if _display_xml:
        doc = xml.dom.minidom.parseString(xml_string)
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
        print >> _outfile, '##### Start-Of-PythonScript #####'
        print >> _outfile, cmdlet
        print >> _outfile, '##### End-Of-PythonScript #####'
        _outfile.close()
    else:
        print "##### Start-Of-PythonScript #####"
        print cmdlet
        print "##### End-Of-PythonScript #####"
    return


def _extract_xml(file_stream, line):
    """
    This Extracts xmlstring from the file and calls the _generate_cmdlets()
    on this xmlstring.
    """
    read_flag = False
    request_string = ""
    line_count = 0
    while line != "":
        # print request_string
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


def _find_xml_requests_in_file_test(file_stream, gui_log):
    """Depending on gui_log flag, calls the _extract_xml() internally."""
    # print "Inside _find_xml_requests_in_file_test"
    line = file_stream.readline()
    while line is not None:
        if not gui_log:
            _extract_xml(file_stream, line)
        elif "[------------- Sending Request to Server ------------" in line:
            line = file_stream.readline()
            if line is not None:
                # print "[%s]" %(line)
                _extract_xml(file_stream, line)
        line = file_stream.readline()


def _if_path_or_literal_path(path, literal_path, gui_log):
    """
    checks if path or literal_path present for the respective parameter set
    and if exists then call _find_xml_requests_in_file_test().
    """
    if path:
        if literal_path:
            print "Parameter <path> takes precedence over <literal_path>"
        file_path = path
    elif literal_path:
        file_path = literal_path
    else:
        print "Please provide path or literal_path"
        return

    file_stream = open(file_path, 'r')
    _find_xml_requests_in_file_test(file_stream, gui_log)
    file_stream.close()


def _get_ucs_default_logpath_windows():
    """_get_ucs_default_logpath_windows."""
    if 'APPDATA' in os.environ.keys():
        log_file_path = os.getenv('APPDATA')
    else:
        print os.name
        raise Exception('Not windows OS')

    if sys.getwindowsversion()[0] == 6:  # in case OS is Win 2008 or above
        log_file_path = os.path.join(dirname(log_file_path), "LocalLow")
    log_file_path += r"\Sun\Java\Deployment\log\.ucsm" + "\\"
    return log_file_path


def _get_ucs_default_logpath_linux():
    """_get_ucs_default_logpath_linux."""
    log_file_path = os.getenv('HOME')
    log_file_path += r"/.java/deployment/log/.ucsm/"
    return log_file_path


def _get_ucs_default_logpath_osx():
    """_get_ucs_default_logpath_osx."""
    log_file_path = os.getenv('HOME')
    # log_file_path += r"/Library/Caches/Java/log/.ucsm"
    path = r"/Library/Application Support/Oracle/Java/Deployment/log/.ucsm"
    log_file_path += path
    return log_file_path


def _get_ucs_default_logpath_cygwin():
    """_get_ucs_default_logpath_cygwin."""
    log_file_path = os.getenv('APPDATA')
    log_file_path = log_file_path.replace("\\", "/")
    # TODO:
    # if OSMajorVersion == 6:
    log_file_path = dirname(log_file_path) + "/LocalLow"
    log_file_path += r"/Sun/Java/Deployment/log/.ucsm/"
    return log_file_path


def convert_to_ucs_python(log_path=None, xml=False, request=None, gui_log=False, path=None,
                          literal_path=None, dump_to_file=False,
                          dump_file_path=None, dump_xml=False):
    """
    By default this will generate python script for the action in UCSM GUI.
    log_path : If by default code unable to identify the location of ucsm logs,
    then use this parameter to specify the directory of ucsm logs.
    xml=True & request="xmlstring": Generate Python Script for XML Request.
    xml=True & path/LiteralPath: Generate Python script from the file
    containing XML Request.
    gui_log=True & path/LiteralPath: Generate Python script from the
    UCSM GUI logfile.
    displayXML=True will also dispaly corresponding XML Request.
    """
    print "### Please review the generated cmdlets before deployment.\n"
    global _display_xml, _outfile_flag, _outfile_path, _outfile
    _display_xml = dump_xml
    _outfile_flag = dump_to_file
    _outfile_path = dump_file_path

    if _outfile_flag in ucsgenutils.AFFIRMATIVE_LIST:
        if _outfile_path:
            print "### Script Output is in file < " + _outfile_path + " >"
            _outfile = open(_outfile_path, 'w')
            _outfile.close()
            # _outfile = open(r"c:\work.txt", 'w+')
        else:
            print "Provide dump_file_path"
            return
    if xml in ucsgenutils.AFFIRMATIVE_LIST:
        if gui_log in ucsgenutils.AFFIRMATIVE_LIST:
            print "parameter <xml> takes precedence over <gui_log>"
        if request:
            _generate_cmdlets(request)
        elif path or literal_path:
            _if_path_or_literal_path(path, literal_path, False)
        else:
            print "Provide request"
            return
    elif gui_log in ucsgenutils.AFFIRMATIVE_LIST:
        if path or literal_path:
            _if_path_or_literal_path(path, literal_path, True)
        else:
            print "Provide path or literal_path"
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
                print "[Error]: Unsupported OS:", _platform
                log_file_path = None
                return

        # Get the latest logfile
        # log_file_path =
        # r"C:\Users\username\AppData\LocalLow\Sun\Java\Deployment\log\.ucsm"
        # files = [ file
        # for file in glob.glob(log_file_path + "\\" + "*")
        # if os.path.isfile(file)]

        os.chdir(log_file_path)
        files = [file_ for file_ in glob.glob("centrale_*.log") if
                 os.path.isfile(file_)]
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        last_updated_file = files[0]

        print "ucsm logfile: %s\n" % (
            os.path.join(log_file_path, last_updated_file))

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
            _find_xml_requests_in_file_test(file_stream, True)
            time.sleep(2)
        file_stream.close()

        # if _outfile_path:
        # _outfile.close()

    print "### End of Convert-To-Python ###"
