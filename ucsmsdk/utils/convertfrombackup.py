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

try:
    import xml.etree.cElementTree as ET
    from xml.etree.cElementTree import Element, SubElement
except ImportError:
    import cElementTree as ET
    from cElementTree import Element, SubElement


import os
import re
from .. import ucsgenutils
from .. import ucscoreutils

import logging

log = logging.getLogger('ucs')

classid_dn_map = {
    "OrgOrg": "org-root",
    "FabricEp": "fabric",
    "FaultHolder": "fault",
    "StatsHolder": "stats",
    "CallHomeEp": "call-home",
    "TopSystem": "sys"
}


def _ignore_elem(elem):
    if elem.tag.startswith('aaa'):
        return True
    if elem.tag in ["biosVfUCSMBootOrderRuleControl",
                    "biosVfOptionROMLoad",
                    "policyControlEp",
                    "storageLocalDiskPartition"]:
        return True
    return False


class Node(object):

    def __init__(self, elem, tag,
                 parent_dn=None, parent_tag=None, parent_verb=None):
        self.elem = elem
        self.tag = tag
        self.parent_dn = parent_dn
        self.parent_tag = parent_tag
        self.parent_verb = parent_verb
        self.class_id = ucsgenutils.word_u(elem.tag)
        self.class_ref = ucscoreutils.load_class(self.class_id)
        self.mo_meta = self.class_ref.mo_meta
        self.prop_meta = self.class_ref.prop_meta
        self.prop_map = self.class_ref.prop_map
        self.dn = self._make_dn()
        self.verb = self._get_verb()
        self.is_used = False
        self.child = []

    def _get_verb(self):
        verbs = self.mo_meta.verbs

        if "Add" in verbs:
            return "Add"
        elif "Set" in verbs:
            return "Set"
        else:
            return "Get"

    def _make_rn(self):
        rn_pattern = self.class_ref.mo_meta.rn
        prop_meta = self.class_ref.prop_meta

        for prop in re.findall(r"""\[([^\]]*)\]""", rn_pattern):
            prop_val = self.elem.attrib[prop_meta[prop].xml_attribute]
            rn_pattern = re.sub(r"""\[%s\]""" % prop, prop_val, rn_pattern)
        return rn_pattern

    def _make_dn(self):
        if self.parent_dn:
            return self.parent_dn + "/" + self._make_rn()
        return self._make_rn()

    def _create_prop_map(self, *args):
        property_map = {}
        for attribute in self.elem.attrib:
            prop_name_py = self.prop_map[attribute]
            prop_access = self.prop_meta[prop_name_py].access
            if prop_access in args:
                continue
            property_map[prop_name_py] = self.elem.attrib[attribute]

        return property_map

    def _create_add_prop_map(self):
        return self._create_prop_map(2, 4)

    def _create_set_prop_map(self):
        return self._create_prop_map(0, 1, 2, 4)

    def _create_add_query(self):
        property_map = self._create_add_prop_map()
        property_map_str = ", ".join(
            [k + "=" + '"' + v + '"'
             for k, v in ucsgenutils.iteritems(property_map)])

        return "%s = %s(parent_mo_or_dn=%s, %s)\n" % (
            self.tag, self.class_id, self.parent_tag, property_map_str)

    def _create_set_query(self):
        if self.parent_verb not in ("Add", "Set"):
            query = '%s = handle.query_dn("%s")\n' % (self.tag, self.dn)
            property_map = self._create_set_prop_map()
            for prop in property_map:
                query += '%s.%s = "%s"\n' % (self.tag, prop,
                                             property_map[prop])
            return query
        else:
            return self._create_add_query()

    def _create_get_query(self):
        return '%s = handle.query_dn("%s")\n' % (self.tag, self.dn)

    def get_query(self):
        query = ""
        if self.verb == "Get" and self.is_used:
            query = self._create_get_query()
        elif self.verb == "Add":
            query = self._create_add_query()

        elif self.verb == "Set":
            query = self._create_set_query()

        return query

    def process_query(self):
        query = ""
        query_ = self.get_query()
        if query_:
            query += query_
        for child in self.child:
            query += child.process_query()

        if self.parent_verb == "Get" and self.verb == "Add":
            query += "handle.add_mo(%s, True)\n" % self.tag
        if self.parent_verb == "Get" and self.verb == "Set":
            query += "handle.set_mo(%s)\n" % self.tag
        return query

    def __str__(self):
        query = self.process_query()
        if query:
            query += "handle.commit()\n"
        return query


def _generate_inner_nodes(elem, tag, parent_dn, parent_tag, parent_verb):

    class_id = ucsgenutils.word_u(elem.tag)
    if not ucscoreutils.is_valid_class_id(class_id):
        return

    node = Node(elem, tag, parent_dn, parent_tag, parent_verb)

    call_count = 1
    for child in elem.getchildren():
        if _ignore_elem(child):
            continue

        child_tag = tag + '_' + str(call_count)
        child_node = Node(elem=child,
                          tag=child_tag,
                          parent_dn=node.dn,
                          parent_tag=node.tag,
                          parent_verb=node.verb)
        if node.verb == "Get" and child_node.verb == "Add":
            node.is_used = True

        node.child.append(child_node)
        if node.verb != "Get" and child_node.verb != "Get":
            call_count += 1

    return node


def _generate_outer_nodes(elem):

    if elem.tag == "topRoot":

        top_nodes = []
        for child in elem.getchildren():
            class_id = ucsgenutils.word_u(child.tag)
            if not ucscoreutils.is_valid_class_id(class_id) \
                    or class_id not in classid_dn_map:
                continue

            parent_nodes = []
            for sub_child in child.getchildren():
                if _ignore_elem(sub_child):
                    continue
                parent_node = Node(elem=child,
                                   tag="obj",
                                   parent_dn=None,
                                   parent_tag=None,
                                   parent_verb=None)
                parent_node.verb = "Get"
                parent_node.dn = classid_dn_map[class_id]

                child_node = _generate_inner_nodes(
                    elem=sub_child,
                    tag="mo",
                    parent_dn=parent_node.dn,
                    parent_tag=parent_node.tag,
                    parent_verb=parent_node.verb)
                if child_node.verb == "Add":
                    parent_node.is_used = True

                parent_node.child.append(child_node)
                parent_nodes.append(parent_node)
            top_nodes.append(parent_nodes)

        return top_nodes


def _generate_query(elem):

    query = ""
    top_nodes = _generate_outer_nodes(elem)
    for parent_nodes in top_nodes:
        query += "\n"
        for parent_node in parent_nodes:
            query += str(parent_node)
            query += "\n"

    return query


def convert_from_backup(file_path, dump_to_file=False, dump_file_path=None):
    if not os.path.exists(file_path):
        raise ValueError("%s does not exists." % file_path)

    tree = ET.parse(file_path)
    root = tree.getroot()

    if dump_to_file in ucsgenutils.AFFIRMATIVE_LIST:
        if dump_file_path:
            script_output = _generate_query(root)
            print("### Script Output is in file < " + dump_file_path + " >")
            _outfile = open(dump_file_path, 'w')
            _outfile.write(script_output)
            _outfile.close()
        else:
            print("Provide dump_file_path")
            return
    else:
        script_output = _generate_query(root)
        print(script_output)
