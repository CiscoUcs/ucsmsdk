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

"""
This module contains the api used to provide compare and sync functionality
within ucsm or across ucsm.
"""

from __future__ import print_function
from __future__ import absolute_import

import re
import logging

from .. import ucsgenutils
from .. import ucscoreutils
from ..ucscoremeta import MoPropertyMeta, MoMeta
from ..ucsexception import UcsWarning, UcsValidationException
from ..ucsmo import GenericMo

log = logging.getLogger('ucs')

skip_mos = ["LsVersionBeh", "LsmaintAck", "LsIssues", "VnicIpV4PooledAddr",
            "VnicDynamicCon", "LsVConAssign", "ComputePooledSlot",
            "ComputePooledRackUnit", "VnicIPv4PooledIscsiAddr",
            "IppoolPooled", "IqnpoolPooled", "MacpoolPooled",
            "UuidpoolPooled", "VnicConnDef", "VnicFcGroupDef",
            "LsServerExtension"]


class _CompareStatus(object):
    """
    Internal class used as enum.
    """

    TYPES_DIFFERENT = 0
    PROPS_DIFFERENT = 1
    EQUAL = 2


class _PropDiff(object):
    """
    Internal class for property delta
    """
    def __init__(self, prop, old_value, new_value):
        self.prop = prop
        self.old_value = old_value
        self.new_value = new_value


class _MoDiff(object):
    """
    This class represents difference object.
    """

    REMOVE = "<="
    ADD_MODIFY = "=>"
    EQUAL = "=="

    def __init__(self, input_object, side_indicator, diff_property=None,
                 ref_values=None, diff_values=None):
        self.input_object = input_object
        self.dn = input_object.dn
        self.side_indicator = side_indicator
        self.diff_property = diff_property

        if ref_values:
            self.ref_prop_values = ref_values
        else:
            self.ref_prop_values = {}

        if diff_values:
            self.diff_prop_values = diff_values
        else:
            self.diff_prop_values = {}

    def get_prop_diff(self, prop):
        if prop in self.ref_prop_values and prop in self.diff_prop_values:
            prop_name = ""
            for key in self.ref_prop_values:
                if prop.lower() == key.lower():
                    prop_name = key
                    break
            return _PropDiff(prop_name, self.ref_prop_values[prop],
                             self.diff_prop_values[prop])
        return None


def _compare(from_mo, to_mo, diff, include_operational=False):
    """
    Internal method to support compare reference and difference object.
    """

    if from_mo.get_class_id() != to_mo.get_class_id():
        return _CompareStatus.TYPES_DIFFERENT

    # compare for unknown class_id
    if isinstance(from_mo, GenericMo) or isinstance(to_mo, GenericMo):
        for prop in from_mo.properties:
            if prop in to_mo.properties:
                if from_mo.properties[prop] != to_mo.properties[prop]:
                    diff.append(prop)

    # compare for known class_id
    else:
        for prop in sorted(from_mo.prop_meta):
            mo_property_meta = from_mo.prop_meta[prop]
            if mo_property_meta is not None:
                if not include_operational and (
                        mo_property_meta.access == MoPropertyMeta.INTERNAL or
                        mo_property_meta.access == MoPropertyMeta.READ_ONLY):
                    continue
                if prop in to_mo.__dict__ \
                        and getattr(from_mo, prop) != getattr(to_mo, prop):
                    diff.append(prop)

        # comparing xtra property
        from_xtra_props = from_mo._ManagedObject__xtra_props
        to_xtra_props = to_mo._ManagedObject__xtra_props
        if from_xtra_props:
            for prop in from_xtra_props:
                if prop in to_xtra_props and from_xtra_props[prop].value != \
                        to_xtra_props[prop].value:
                    # diff.append(prop)
                    UcsWarning("Ignoring xtra property '%s' of '%s'" % (
                        prop, from_mo.dn))

    if len(diff) > 0:
        return _CompareStatus.PROPS_DIFFERENT

    return _CompareStatus.EQUAL


def _update_mo_dn_along_with_naming_properties(mo, ref_dn):
    """
    Internal method to modify the naming properties of mo using dn.
    """

    # modify diffmo dn with refmo dn
    mo.__dict__['dn'] = ref_dn

    # modify diffmo rn with refmo rn
    ref_rn = re.sub(r'^.*/', '', ref_dn)
    mo.__dict__['rn'] = ref_rn

    # modify diff mo naming properties using ref_rn
    naming_prop_dict = ucscoreutils.get_naming_props(rn_str=ref_rn,
                                                     rn_pattern=mo.mo_meta.rn)
    for prop in naming_prop_dict:
        mo.__dict__[prop] = naming_prop_dict[prop]


def _translate_managed_object(mo, xlate_org, xlate_map):
    """
    Internal method used to translate a managed object which helps in comparing
    two mo with different dn.
    """

    ref_dn = None
    if xlate_org is not None:
        match_obj = re.match(
            r'^(org-[\-\.:_a-zA-Z0-9]{1,16}/)*org-[\-\.:_a-zA-Z0-9]{1,16}',
            mo.dn)
        if match_obj:
            if mo.get_class_id() == "OrgOrg":
                ref_dn = re.sub("%s" % (match_obj.group(0)),
                                "%s" % xlate_org,
                                mo.dn)
            else:
                ref_dn = re.sub("^%s/" % (match_obj.group(0)),
                                "%s/" % xlate_org,
                                mo.dn)
            _update_mo_dn_along_with_naming_properties(mo, ref_dn)

    if xlate_map is not None:
        diff_dn = mo.dn
        if diff_dn in xlate_map:
            ref_dn = xlate_map[diff_dn]
        else:
            diff_dn = re.sub(r'[/]*[^/]+$', '', diff_dn)
            while diff_dn is not None or diff_dn == "":
                if diff_dn not in xlate_map:
                    diff_dn = re.sub(r'[/]*[^/]+$', '', diff_dn)
                    continue

                ref_dn = re.sub("^%s/" % diff_dn,
                                "%s/" % xlate_map[diff_dn],
                                mo.dn)
                break
        _update_mo_dn_along_with_naming_properties(mo, ref_dn)

    return mo


def write_mo_diff(diff_obj):
    """
    Writes the difference managedObject(output of CompareManagedObject)
    on the terminal.
    """

    tab_size = 8
    if isinstance(diff_obj, list) and len(diff_obj) > 0:
        if isinstance(diff_obj[0], _MoDiff):
            print("dn".ljust(tab_size*10), "input_object".ljust(tab_size*4),
                  "side_indicator".ljust(tab_size*3), "diff_property")
            print("--".ljust(tab_size*10), "-----------".ljust(tab_size*4),
                  "-------------".ljust(tab_size*3), "------------")
        for mo in diff_obj:
            if isinstance(mo, _MoDiff):
                print(str(mo.dn).ljust(tab_size*10),
                      str(mo.input_object.get_class_id()).ljust(tab_size*4),
                      str(mo.side_indicator).ljust(tab_size*3),
                      str(mo.diff_property))


def compare_ucs_mo(ref_handle, ref_obj,
                   diff_handle, diff_obj,
                   exclude_different=False,
                   include_equal=False,
                   no_version_filter=False,
                   include_operational=False,
                   xlate_org=None, xlate_map=None):
    """
    Compares the state of two managed objects with same dn.

    Args:
        ref_handle (UcsHandle): connect handle of reference ucsm
        ref_obj (list): list of Managed Objects of reference ucsm
        diff_handle (UcsHandle): connect handle of difference ucsm
        diff_obj (list): list of Managed Objects of difference ucsm
        exclude_different (bool): by default False. If set to True, will
                                  compare mos only which exist on both
                                  reference and difference ucsm respectively
        include_equal (bool): by default False. If set to True, will also
                              display properties which are equal
        no_version_filter (bool): by default False: If set to True, ignore
                                  properties which is introduced in later ucsm
                                  version than reference ucsm
        include_operational (bool): by default False: If set to True, compares
                                    all the properties of mo.
        xlate_org (str): org-dn, should be used compare objects of same type
                         under different org. org-dn of reference mo.
        xlate_map (dict) : {"difference_dn": "reference_dn"}
                           Should be used to compare objects of same type with
                           different dn.
    Returns:
        List of MoDiff objects:
        MoDiff Object : dn - dn of Managed Object
                        input_object - Managed Object
                        side_indicator -
                            "=>" Add the diff obj to ref ucsm
                              or
                              Modify the ref object by diff object on ref ucsm

                            "<=" Removes the ref obj from ref ucsm

                            "==" object is equal on both ref and diff ucsm
                        diff_property  - property list with different value

    Example:
        #1
        ref_mos = [ref_handle.query_dn(dn="org-root/ls-sp")]
        diff_mos = [diff_handle.query_dn(dn="org-root/ls-sp")]
        compare_ucs_mo(ref_handle, ref_mos,
                                   diff_handle, diff_mos)

        #2
        ref_mos = [ref_handle.query_dn(dn="org-root/org-ref/ls-sp")]
        diff_mos = [diff_handle.query_dn(dn="org-root/org-diff/ls-sp")]
        compare_ucs_mo(ref_handle, ref_mos,
                                   diff_handle, diff_mos,
                                   xlate_org = "org-root/org-ref")

        #3
        ref_mos = [ref_handle.query_dn(dn="org-root/ls-ref")]
        diff_mos = [diff_handle.query_dn(dn="org-root/ls-diff")]
        compare_ucs_mo(ref_handle, ref_mos, diff_handle, diff_mos,
                        xlate_map = {"org-root/ls-diff": "org-root/ls-ref"})
    """

    reference_dict = {}
    difference_dict = {}

    if ref_obj is not None and \
            isinstance(ref_obj, list) and len(ref_obj) > 0:
        for mo in ref_obj:
            if mo is None:
                continue
            if isinstance(mo, GenericMo):
                if ucsgenutils.word_u(mo.get_class_id()) in skip_mos:
                    continue
            elif mo.get_class_id() in skip_mos or \
                    mo.mo_meta.inp_out == MoMeta.ACCESS_TYPE_OUTPUTONLY or \
                    (mo.mo_meta.inp_out == MoMeta.ACCESS_TYPE_IO
                     and len(mo.mo_meta.access) == 1
                     and mo.mo_meta.access[0] == "read-only"):
                continue
            reference_dict[mo.dn] = mo
    # log.debug("reference_dict: %s" % reference_dict)

    if diff_obj is not None and \
            isinstance(diff_obj, list) and len(diff_obj) > 0:
        for mo in diff_obj:
            if mo is None:
                continue
            if isinstance(mo, GenericMo):
                if ucsgenutils.word_u(mo.get_class_id()) in skip_mos:
                    continue
            elif mo.get_class_id() in skip_mos or \
                    mo.mo_meta.inp_out == MoMeta.ACCESS_TYPE_OUTPUTONLY or \
                    (mo.mo_meta.inp_out == MoMeta.ACCESS_TYPE_IO
                     and len(mo.mo_meta.access) == 1
                     and mo.mo_meta.access[0] == "read-only"):
                continue
            translated_mo = _translate_managed_object(mo, xlate_org, xlate_map)
            difference_dict[translated_mo.dn] = translated_mo
    # log.debug("difference_dict: %s" % difference_dict)

    # union of reference and difference
    dn_list = list(set.union(set(reference_dict), set(difference_dict)))
    dn_list = sorted(dn_list)
    diff_output = []

    for dn in dn_list:
        if dn not in difference_dict:
            ref_mo = reference_dict[dn].clone()
            if not exclude_different:
                mo_diff = _MoDiff(ref_mo, _MoDiff.REMOVE)
                diff_output.append(mo_diff)
        elif dn not in reference_dict:
            diff_mo = difference_dict[dn].clone()
            if not exclude_different:
                mo_diff = _MoDiff(diff_mo, _MoDiff.ADD_MODIFY)
                diff_output.append(mo_diff)
        else:
            ref_mo = reference_dict[dn].clone()
            diff_mo = difference_dict[dn].clone()
            diff_props = []

            if not no_version_filter:
                if not isinstance(ref_mo, GenericMo) and \
                        ref_handle.version is not None:
                    for prop in ref_mo.prop_meta:
                        prop_meta = ref_mo.prop_meta[prop]
                        if ref_handle.version < prop_meta.version or \
                                prop_meta.access == MoPropertyMeta.INTERNAL:
                            del ref_mo.__dict__[prop]  # check this

                if not isinstance(diff_mo, GenericMo) and \
                        diff_handle.version is not None:
                    for prop in diff_mo.prop_meta:
                        prop_meta = diff_mo.prop_meta[prop]
                        if diff_handle.version < prop_meta.version or \
                                prop_meta.access == MoPropertyMeta.INTERNAL:
                            del diff_mo.__dict__[prop]  # check this

            # compare both mo for property and type
            diff_status = _compare(ref_mo, diff_mo, diff_props,
                                   include_operational)

            if diff_status == _CompareStatus.EQUAL and include_equal:
                mo_diff = _MoDiff(ref_mo, _MoDiff.EQUAL)
                diff_output.append(mo_diff)
            elif diff_status == _CompareStatus.TYPES_DIFFERENT and \
                    not exclude_different:
                mo_diff = _MoDiff(ref_mo, _MoDiff.REMOVE)
                diff_output.append(mo_diff)
                mo_diff = _MoDiff(diff_mo, _MoDiff.ADD_MODIFY)
                diff_output.append(mo_diff)
            elif diff_status == _CompareStatus.PROPS_DIFFERENT and \
                    not exclude_different:
                ref_values = {}
                diff_values = {}
                for prop in diff_props:
                    ref_values[prop] = getattr(ref_mo, prop)
                    diff_values[prop] = getattr(diff_mo, prop)
                mo_diff = _MoDiff(diff_mo, _MoDiff.ADD_MODIFY,
                                  diff_props, ref_values, diff_values)
                diff_output.append(mo_diff)

    return diff_output


def sync_ucs_mo(ref_handle, difference,
                delete_not_present=False,
                no_version_filter=False):
    """
    syncs the difference object on reference ucsm.
    In other words, make the state of reference ucsm for the respective
    ref object same as difference object on reference ucsm.

    Args:
        ref_handle (UcsHandle): connect handle of reference ucsm
        difference (list of MoDiff objects): output of compare-ucs-mo api
        delete_not_present (bool): by dafault False. If set to true, will
                                   delete ref mo which does not exist on
                                   difference ucsm
        no_version_filter (bool): by default False: If set to True, ignore
                                  properties which is introduced in later ucsm
                                  version than reference ucsm

    Returns:
        None

    Example:
        #1
        ref_mos = [ref_handle.query_dn(dn="org-root/ls-sp")]
        diff_mos = [diff_handle.query_dn(dn="org-root/ls-sp")]
        difference = compare_ucs_mo(ref_handle, ref_mos,diff_handle, diff_mos)
        sync_ucs_mo(ref_handle, difference=difference, delete_not_present=True)
    """

    if difference is None or \
            (isinstance(difference, list) and len(difference) == 0):
        raise UcsValidationException(
            "difference object parameter is not provided.")

    to_commit = False

    for mo_diff in difference:
        mo = mo_diff.input_object
        class_id = mo.get_class_id()

        if isinstance(mo, GenericMo):
            UcsWarning("Ignoring '%s'.Unknown ClasId '%s'" % (mo.dn, class_id))
            continue

        # Remove
        if mo_diff.side_indicator == _MoDiff.REMOVE and delete_not_present:
            log.debug("removing mo '%s'." % mo.dn)
            ref_handle.remove_mo(mo)
            to_commit = True

        if not no_version_filter:
            mo_meta = mo.mo_meta
            if ref_handle.version < mo_meta.version:
                UcsWarning("Ignoring unsupported class_id '%s' for dn '%s'" %
                           (class_id, mo.dn))
                continue

        # Add or Modify
        if mo_diff.side_indicator == _MoDiff.ADD_MODIFY:
            add_exists = False
            if isinstance(mo, GenericMo):
                mo_meta = None
            else:
                mo_meta = mo.mo_meta

            if mo_meta is not None and 'Add' in mo_meta.verbs:
                add_exists = True

            # Add
            if add_exists and (mo_diff.diff_property is None
                               or len(mo_diff.diff_property) == 0):
                log.debug("adding mo '%s'" % mo.dn)
                mo.mark_dirty()
                ref_handle.add_mo(mo)
                to_commit = True

            # Modify the Managed Object
            else:
                if mo_diff.diff_property is None \
                        or len(mo_diff.diff_property) == 0:
                    continue
                set_flag = False
                for prop in mo_diff.diff_property:
                    if mo.prop_meta[prop].access == MoPropertyMeta.READ_WRITE:
                        setattr(mo, prop, getattr(mo, prop))
                        set_flag = True
                if not set_flag:
                    log.debug("No Configurable Properties Changed for mo '%s'"
                              % mo.dn)
                else:
                    log.debug("set mo '%s'" % mo.dn)
                    ref_handle.set_mo(mo)
                    to_commit = True

    if to_commit:
        ref_handle.commit()
