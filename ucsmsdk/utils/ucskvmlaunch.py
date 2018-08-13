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
This module contains the APIs used to launch ucs kvm.
"""
import subprocess
import logging

from .. import ucsgenutils
from ..ucsconstants import NamingId, YesOrNo
from ..ucsexception import UcsWarning, UcsValidationException, UcsException
from ..ucscoremeta import UcsVersion
from six.moves.urllib.parse import urlencode


log = logging.getLogger('ucs')


class _ParamKvm(object):
    # Internal class to act as enum to support ucs_kvm_launch utility.

    CENTRALE_PASSWORD = "centralePassword"
    CENTRALE_USER = "centraleUser"
    DN = "dn"
    FRAME_TITLE = "frame_title"
    KVM_IP_ADDR = "kvmIpAddr"
    KVM_PASSWORD = "kvmPassword"
    KVM_PN_DN = "kvmPnDn"
    KVM_USER = "kvmUser"
    TEMP_UNPW = "tempunpw"
    KVM_DN = "kvmDn"


def ucs_kvm_launch(handle, service_profile=None, blade=None, rack_unit=None,
                   frame_title=None, need_url=False):
    """
    ucs_kvm_launch launches the kvm session for a specified server.

    Args:
        handle (UcsHandle)
        service_profile (LsServer)
        blade (ComputeBlade)
        rack_unit (ComputeRackUnit)
        frame_title (str): title of launched frame
        need_url (bool): True/False,
                         Returns URL to launch kvm, if True

    Example:
        # sp is service profile object \n
        ucs_kvm_launch(handle, service_profile=sp)\n
        ucs_kvm_launch(handle, service_profile=sp, frame_title="using sp")\n
        ucs_kvm_launch(handle, service_profile=sp, need_url=True)\n

        # blade1 is ComputeBlade object\n
        ucs_kvm_launch(handle, blade=blade1)\n

        # rack1 is ComputeRackUnit object\n
        ucs_kvm_launch(handle, rack_unit=rack1)\n
    """

    from ..mometa.mgmt.MgmtIf import MgmtIfConsts
    from ..ucsmethodfactory import config_scope
    from ..ucsmethodfactory import aaa_get_n_compute_auth_token_by_dn

    if (blade is not None and rack_unit is not None) or \
        (service_profile is not None and rack_unit is not None) or \
            (blade is not None and service_profile is not None):
        raise UcsValidationException(
            "Provide only one parameter from blade, "
            "rack_unit and service profile.")
    if service_profile is None and blade is None and rack_unit is None:
        raise UcsValidationException(
            "Provide at least one parameter from blade, rack_unit and "
            "service profile.")

    min_version = UcsVersion('1.4(1a)')
    if handle.version < min_version:
        raise UcsValidationException(
            "start_kvm_session not supported for Ucs version older than %s. "
            "You are connected to Ucs Version %s" % (min_version,
                                                     handle.version))

    # lock = Lock()
    sp_bool = False
    nvc = {}
    dn = None
    pn_dn = None
    ip_address = None

    if blade is not None or rack_unit is not None:
        if blade is not None:
            pn_dn = blade.dn
        else:
            pn_dn = rack_unit.dn

        nvc[_ParamKvm.DN] = pn_dn

        if frame_title is None:
            frame_title = handle.name + ':' + pn_dn + ' KVM Console'
        nvc[_ParamKvm.FRAME_TITLE] = frame_title
        nvc[_ParamKvm.KVM_PN_DN] = pn_dn

        elem = config_scope(cookie=handle.cookie,
                            dn=pn_dn,
                            in_class=NamingId.MGMT_IF,
                            in_filter=None,
                            in_recursive=YesOrNo.FALSE,
                            in_hierarchical=YesOrNo.FALSE)

        response = handle.post_elem(elem)
        if response.error_code == 0:
            for mgmt_if in response.out_configs.child:
                if mgmt_if.subject == MgmtIfConsts.SUBJECT_BLADE and \
                   mgmt_if.admin_state == MgmtIfConsts.ADMIN_STATE_ENABLE:
                    ip_address = mgmt_if.ext_ip
        else:
            raise UcsException(response.error_code, response.error_descr)

        # If the blade does not have an IP,
        # check if a service profile is associated
        if ip_address is None or ip_address == '0.0.0.0':
            mo = handle.query_dn(dn=pn_dn)
            dn = mo.assigned_to_dn
            if dn is not None:
                sp_bool = True

    if sp_bool or service_profile is not None:
        if dn is None:
            dn = service_profile.dn
            if frame_title is None:
                frame_title = handle.name + ':' + dn + ' KVM Console'
            nvc[_ParamKvm.FRAME_TITLE] = frame_title
            sp_mo = service_profile
        else:
            sp_mo = handle.query_dn(dn)

        nvc[_ParamKvm.KVM_DN] = dn

        # sp_mo = service_profile

        if not sp_mo.pn_dn:
            raise UcsValidationException(
                'Service Profile is not associated with blade or rack_unit.')

        pn_dn = sp_mo.pn_dn
        nvc[_ParamKvm.DN] = pn_dn

        mo_list = handle.query_children(in_dn=dn, class_id='vnicIpV4Addr')
        # TODO:replace class_id with proper constantafter generating mos.py
        # or Constant.py

        for mo in mo_list:
            # gmo = _GenericMo(mo=mo, option=WriteXmlOption.ALL)
            # if 'Addr' not in gmo.properties:
            #     continue
            # ip_address = gmo.GetAttribute('Addr')
            # if ip_address is not None:
            #     break
            if hasattr(mo, "addr") or hasattr(mo, "Addr"):
                if hasattr(mo, "addr"):
                    ip_address = getattr(mo, "addr")
                elif hasattr(mo, "Addr"):
                    ip_address = getattr(mo, "Addr")
                if ip_address is not None:
                    break

    if (ip_address is None or ip_address == '0.0.0.0') and \
            service_profile is not None:

        elem = config_scope(cookie=handle.cookie,
                            dn=pn_dn,
                            in_class=NamingId.MGMT_IF,
                            in_filter=None,
                            in_recursive=YesOrNo.FALSE,
                            in_hierarchical=YesOrNo.FALSE)

        response = handle.post_elem(elem)
        if response.error_code == 0:
            for mgmt_if in response.out_configs.child:
                if mgmt_if.subject == MgmtIfConsts.SUBJECT_BLADE and \
                   mgmt_if.admin_state == MgmtIfConsts.ADMIN_STATE_ENABLE:
                    ip_address = mgmt_if.ext_ip

    if ip_address is None or ip_address == '0.0.0.0':
        raise UcsValidationException("No assigned IP address to use.")

    nvc[_ParamKvm.KVM_IP_ADDR] = ip_address
    elem = aaa_get_n_compute_auth_token_by_dn(cookie=handle.cookie,
                                              in_cookie=handle.cookie,
                                              in_dn=pn_dn,
                                              in_number_of=2)
    response = handle.post_elem(elem)
    if response.error_code == 0:
        nvc[_ParamKvm.CENTRALE_PASSWORD] = response.out_tokens.split(',')[0]
        nvc[_ParamKvm.CENTRALE_USER] = response.out_user
        nvc[_ParamKvm.KVM_PASSWORD] = response.out_tokens.split(',')[1]
        nvc[_ParamKvm.KVM_USER] = response.out_user
    else:
        raise UcsException(response.error_code, response.error_descr)

    nvc[_ParamKvm.TEMP_UNPW] = "true"
    uri = handle.uri
    kvm_url = '%s/ucsm/kvm.jnlp?%s' % (uri, urlencode(nvc))

    if need_url:
        return kvm_url
    else:
        install_path = ucsgenutils.get_java_installation_path()
        if install_path is not None:
            subprocess.call([install_path, kvm_url])
        else:
            UcsWarning("Java is not installed on System.")
            subprocess.Popen(kvm_url)
