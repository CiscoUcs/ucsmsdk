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


def _update_mo_dn_and_naming_props(mo, ref_dn):
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

    if not xlate_org and not xlate_map:
        return mo

    mo = mo.clone()
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
            _update_mo_dn_and_naming_props(mo, ref_dn)

    if xlate_map is not None:
        diff_dn = mo.dn
        if diff_dn in xlate_map:
            ref_dn = xlate_map[diff_dn]
            _update_mo_dn_and_naming_props(mo, ref_dn)
        else:
            diff_dn = re.sub(r'[/]*[^/]+$', '', diff_dn)
            while diff_dn:
                if diff_dn not in xlate_map:
                    diff_dn = re.sub(r'[/]*[^/]+$', '', diff_dn)
                    continue

                ref_dn = re.sub("^%s/" % diff_dn,
                                "%s/" % xlate_map[diff_dn],
                                mo.dn)
                _update_mo_dn_and_naming_props(mo, ref_dn)
                break
    return mo


def _list_has_values(obj):
    """
    Internal function to check if obj is non empty list.
    """

    return isinstance(obj, list) and len(obj) > 0


def _should_skip_mo(mo):
    """
    Internal function to check if mo to be skipped from comparison.
    """

    if mo is None:
        return True
    if isinstance(mo, GenericMo):
        if ucsgenutils.word_u(mo.get_class_id()) in skip_mos:
            return True
    elif mo.get_class_id() in skip_mos or \
            mo.mo_meta.inp_out == MoMeta.ACCESS_TYPE_OUTPUTONLY or \
            (mo.mo_meta.inp_out == MoMeta.ACCESS_TYPE_IO
             and len(mo.mo_meta.access) == 1
             and mo.mo_meta.access[0] == "read-only"):
        return True
    return False


def _get_skip_props(mo, include_operational=False, version_filter=True):
    """
    Internal function to skip mo property if not to be considered for sync.
    """

    skip_props = []
    for prop in mo.prop_meta:
        mo_property_meta = mo.prop_meta[prop]
        if mo_property_meta is None:
            continue

        # not include operational property
        if not include_operational:
            if mo_property_meta.access in (MoPropertyMeta.INTERNAL,
                                           MoPropertyMeta.READ_ONLY):
                skip_props.append(prop)
        # checks if property is part of current or earlier ucsm schema
        if version_filter:
            version = mo.get_handle().version
            if version is None or version < mo_property_meta.version or \
               mo_property_meta.access == MoPropertyMeta.INTERNAL:
                skip_props.append(prop)
    return skip_props


def _compare_known_mo(from_mo, to_mo, diff, include_operational=False,
                      version_filter=True):
    """
    Internal function to compare if both the ref and diff obj is known mo.
    """

    from_mo_skip_props = None
    if not include_operational or version_filter:
        from_mo_skip_props = _get_skip_props(from_mo, include_operational,
                                             version_filter)

    # comparing known properties of ref mo
    for prop in from_mo.prop_meta:
        if from_mo_skip_props and prop in from_mo_skip_props:
            continue
        # if not exist in diff mo
        if not hasattr(to_mo, prop):
            log.debug("Property '%s' of '%s' does not exist in diff obj." % (
                prop, from_mo.dn))
            continue

        if getattr(from_mo, prop) != getattr(to_mo, prop):
            diff.append(prop)

    # comparing unknown properties of ref mo
    from_xtra_props = from_mo._ManagedObject__xtra_props
    to_xtra_props = to_mo._ManagedObject__xtra_props
    if not to_xtra_props:
        return
    for prop in from_xtra_props:
        if prop not in to_xtra_props:
            continue

        if from_xtra_props[prop].value != to_xtra_props[prop].value:
            if version_filter:
                UcsWarning("Ignoring xtra property '%s' of '%s'" % (
                    prop, from_mo.dn))
            else:
                diff.append(prop)


def _compare_unknown_mo(from_mo, to_mo, diff, version_filter=True):
    """
    Internal function to compare if any or both of the  ref and diff obj is
    unknown mo.
    """

    # both unknown mo
    if version_filter:
        return
    for prop in from_mo.properties:
        if prop not in to_mo.properties:
            continue
        if from_mo.properties[prop] != to_mo.properties[prop]:
            diff.append(prop)


def _compare(from_mo, to_mo, diff, include_operational=False,
             version_filter=True):
    """
    Internal method to support compare reference and difference object.
    """

    # compare mo of different types
    if from_mo.get_class_id() != to_mo.get_class_id():
        return _CompareStatus.TYPES_DIFFERENT

    # compare for unknown class_id
    if isinstance(from_mo, GenericMo) or isinstance(to_mo, GenericMo):
        _compare_unknown_mo(from_mo, to_mo, diff, version_filter)

    # compare for known class_id
    else:
        _compare_known_mo(from_mo, to_mo, diff, include_operational,
                          version_filter)

    if len(diff) > 0:
        return _CompareStatus.PROPS_DIFFERENT

    return _CompareStatus.EQUAL


def _compare_common_mo(ref_dict, diff_dict, include_operational=False,
                       version_filter=True, include_equal=False,
                       exclude_different=False):

    diff_output = []
    common_dns = set(ref_dict) & set(diff_dict)
    for dn in common_dns:
        ref_mo = ref_dict[dn]
        diff_mo = diff_dict[dn]
        diff_props = []

        # compare both mo for property and type
        diff_status = _compare(ref_mo, diff_mo, diff_props,
                               include_operational, version_filter)

        if diff_status == _CompareStatus.EQUAL and include_equal:
            mo_diff = _MoDiff(ref_mo, _MoDiff.EQUAL)
            diff_output.append(mo_diff)
            continue

        if exclude_different:
            continue

        if diff_status == _CompareStatus.TYPES_DIFFERENT:
            mo_diff = _MoDiff(ref_mo, _MoDiff.REMOVE)
            diff_output.append(mo_diff)
            mo_diff = _MoDiff(diff_mo, _MoDiff.ADD_MODIFY)
            diff_output.append(mo_diff)
        elif diff_status == _CompareStatus.PROPS_DIFFERENT:
            ref_values = {}
            diff_values = {}
            for prop in diff_props:
                ref_values[prop] = getattr(ref_mo, prop)
                diff_values[prop] = getattr(diff_mo, prop)
            mo_diff = _MoDiff(diff_mo, _MoDiff.ADD_MODIFY,
                              diff_props, ref_values, diff_values)
            diff_output.append(mo_diff)

    return diff_output


def compare_ucs_mo(ref_obj, diff_obj,
                   exclude_different=False,
                   include_equal=False,
                   version_filter=True,
                   include_operational=False,
                   xlate_org=None, xlate_map=None):
    """
    Compares the state of two managed objects with same dn.

    Args:
        ref_obj (list): list of Managed Objects of reference UCSM
        diff_obj (list): list of Managed Objects of difference UCSM
        exclude_different (bool): default:False. When True, compares MOs that
                                  exist on both reference and difference UCSM
        include_equal (bool): default:False. When True, also displays MOs which
                              are equal.
        version_filter (bool): default:True. When False, ignores properties
                               which is introduced in later UCSM version than
                               reference UCSM version.
        include_operational (bool): default:False. When True, compares all the
                                    properties of mo.
        xlate_org (str): org-dn of reference mo, compares objects of same type
                         and same rn under different org.
        xlate_map (dict) : {"difference_dn": "reference_dn"}, compares objects
                            of same type with different dn.
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
        compare_ucs_mo(ref_mos, diff_mos)

        #2
        ref_mos = [ref_handle.query_dn(dn="org-root/org-ref/ls-sp")]
        diff_mos = [diff_handle.query_dn(dn="org-root/org-diff/ls-sp")]
        compare_ucs_mo(ref_mos, diff_mos, xlate_org = "org-root/org-ref")

        #3
        ref_mos = [ref_handle.query_dn(dn="org-root/ls-ref")]
        diff_mos = [diff_handle.query_dn(dn="org-root/ls-diff")]
        compare_ucs_mo(ref_mos, diff_mos,
                       xlate_map = {"org-root/ls-diff": "org-root/ls-ref"})
    """

    reference_dict = {}
    difference_dict = {}
    diff_output = []

    if ref_obj is not None and _list_has_values(ref_obj):
        for mo in ref_obj:
            if _should_skip_mo(mo):
                continue
            reference_dict[mo.dn] = mo

    if diff_obj is not None and _list_has_values(diff_obj):
        for mo in diff_obj:
            if _should_skip_mo(mo):
                continue
            translated_mo = _translate_managed_object(mo, xlate_org, xlate_map)
            difference_dict[translated_mo.dn] = translated_mo

    if not exclude_different:
        only_ref_dns = set(reference_dict) - set(difference_dict)
        only_diff_dns = set(difference_dict) - set(reference_dict)

        for dn in only_ref_dns:
            diff_output.append(_MoDiff(reference_dict[dn],
                                       _MoDiff.REMOVE))

        for dn in only_diff_dns:
            diff_output.append(_MoDiff(difference_dict[dn],
                                       _MoDiff.ADD_MODIFY))

    diff_with_props = _compare_common_mo(reference_dict, difference_dict,
                                         include_operational,
                                         version_filter, include_equal,
                                         exclude_different)

    if diff_with_props:
        diff_output.extend(diff_with_props)

    return diff_output


def sync_ucs_mo(ref_handle, difference,
                delete_not_present=False,
                version_filter=True):
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
        version_filter (bool): by default True: If set to False, ignore
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

    if difference is None or not _list_has_values(difference):
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

        if version_filter:
            mo_meta = mo.mo_meta
            if ref_handle.version < mo_meta.version:
                UcsWarning("Ignoring unsupported class_id '%s' for dn '%s'" %
                           (class_id, mo.dn))
                continue

        # Add or Modify
        if mo_diff.side_indicator == _MoDiff.ADD_MODIFY:
            add_exists = False
            if not isinstance(mo, GenericMo) and 'Add' in mo.mo_meta.verbs:
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


def write_mo_diff(diff_obj):
    """
    Writes the difference managedObject(output of CompareManagedObject)
    on the terminal.
    """

    tab_size = 8
    if not _list_has_values(diff_obj):
        return

    if isinstance(diff_obj[0], _MoDiff):
        print("dn".ljust(tab_size * 10), "input_object".ljust(tab_size * 4),
              "side_indicator".ljust(tab_size * 3), "diff_property")
        print("--".ljust(tab_size * 10), "-----------".ljust(tab_size * 4),
              "-------------".ljust(tab_size * 3), "------------")
    diff_obj_mod = []
    for mo_diff in diff_obj:
        if not isinstance(mo_diff, _MoDiff):
            continue
        diff_obj_mod.append(mo_diff)

    for mo_diff in sorted(diff_obj_mod, key=lambda mo: mo.dn):
        print(str(mo_diff.dn).ljust(tab_size * 10),
              str(mo_diff.input_object.get_class_id()).ljust(tab_size * 4),
              str(mo_diff.side_indicator).ljust(tab_size * 3),
              str(sorted(mo_diff.diff_property))
              if mo_diff.diff_property else str(mo_diff.diff_property))
