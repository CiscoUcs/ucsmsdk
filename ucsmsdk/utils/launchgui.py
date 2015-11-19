"""Copyright 2015 Cisco Systems, Inc.

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

"""
This module contains the external api exposed by ucsmsdk package.
"""

import os
import re
import urllib2
import urllib
import subprocess
import logging

from .. import ucsgenutils
from ..ucsconstants import NamingId, YesOrNo
from ..ucsexception import UcsWarning, UcsValidationException, UcsException
from ..ucscoremeta import UcsVersion
from ..import ucsmethodfactory as mf

log = logging.getLogger('ucs')


class _ParamKvm(object):
    """
    Internal class to act as enum to support start_ucs_kvm_session utility.
    """
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


def start_ucs_kvm_session(handle, service_profile=None, blade=None,
                          rack_unit=None, frame_title=None, need_url=False):
    """
    Starts KVM session.

    Launches the KVM session for the specific service profile,
    blade or rack_unit.
    - service_profile specifies an object of type lsServer.
      Launches KVM session with which the service profile is associated.
    - blade specifies an object of type computeBlade.
      Launches KVM session of blade server.
    - rack_unit specifies an object of type computeRackUnit.
      Launches KVM session of rack Unit.
    - frame_title specifies the title of the frame window.
    """
    from ..mometa.mgmt.MgmtIf import MgmtIfConsts

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

        xml_element = mf.config_scope(cookie=handle.cookie,
                                      dn=pn_dn,
                                      in_class=NamingId.MGMT_IF,
                                      in_filter=None,
                                      in_recursive=YesOrNo.FALSE,
                                      in_hierarchical=YesOrNo.FALSE)
        response = handle.post(xml_element)
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

        nvc[_ParamKvm.KVM_DN] = dn

        sp_mo = service_profile

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

        xml_element = mf.config_scope(cookie=handle.cookie,
                                      dn=pn_dn,
                                      in_class=NamingId.MGMT_IF,
                                      in_filter=None,
                                      in_recursive=YesOrNo.FALSE,
                                    in_hierarchical=YesOrNo.FALSE)
        response = handle.post(xml_element)
        if response.error_code == 0:
            for mgmt_if in response.out_configs.child:
                if mgmt_if.subject == MgmtIfConsts.SUBJECT_BLADE and \
                   mgmt_if.admin_state == MgmtIfConsts.ADMIN_STATE_ENABLE:
                    ip_address = mgmt_if.ext_ip

    if ip_address is None or ip_address == '0.0.0.0':
        raise UcsValidationException("No assigned IP address to use.")

    nvc[_ParamKvm.KVM_IP_ADDR] = ip_address
    xml_element = mf.aaa_get_n_compute_auth_token_by_dn(cookie=handle.cookie,
                                                    in_cookie=handle.cookie,
                                                    in_dn=pn_dn,
                                                    in_number_of=2)
    response = handle.post(xml_element)
    if response.error_code == 0:
        nvc[_ParamKvm.CENTRALE_PASSWORD] = response.out_tokens.split(',')[0]
        nvc[_ParamKvm.CENTRALE_USER] = response.out_user
        nvc[_ParamKvm.KVM_PASSWORD] = response.out_tokens.split(',')[1]
        nvc[_ParamKvm.KVM_USER] = response.out_user
    else:
        raise UcsException(response.error_code, response.error_descr)

    nvc[_ParamKvm.TEMP_UNPW] = "true"
    uri = handle.uri
    uri = uri.rstrip("/nuova")
    kvm_url = '%s/ucsm/kvm.jnlp?%s' % (uri, urllib.urlencode(nvc))

    if need_url:
        return kvm_url
    else:
        install_path = ucsgenutils.get_java_installation_path()
        if install_path is not None:
            subprocess.call([install_path, kvm_url])
        else:
            UcsWarning("Java is not installed on System.")
            subprocess.Popen(kvm_url)


def start_ucs_gui_session(handle, need_url=False):
    """Launches the UCSM GUI via specific UCS handle."""
    import tempfile
    import fileinput
    import platform

    os_support = ["Windows", "Linux", "Microsoft", "Darwin"]
    if platform.system() not in os_support:
        raise UcsValidationException(
            "Currently works with Windows OS and Ubuntu")

    jnlp_file = None
    uri = handle.uri
    uri = uri.rstrip('/nuova')
    try:
        ucsm_url = "%s/ucsm/ucsm.jnlp" % uri
        log.debug("UCSM URL: <%s>" % ucsm_url)
        if handle:
            auth_token = handle.get_auth_token()
            log.debug("AuthToken: <%s>" % auth_token)
            if auth_token:
                ucsm_url = "%s?ucsmToken=%s" % (ucsm_url, auth_token)

        log.debug("UCSM URL: <%s>" % ucsm_url)

        if need_url:
            return ucsm_url
        else:
            javaws_path = ucsgenutils.get_java_installation_path()
            log.debug("javaws path: <%s>" % javaws_path)
            if javaws_path is not None:
                source = urllib2.urlopen(ucsm_url).read()
                jnlp_dir = tempfile.gettempdir()
                log.debug("Temp Directory: <%s>" % jnlp_dir)
                jnlp_file = os.path.join(jnlp_dir, "temp.jnlp")
                if os.path.exists(jnlp_file):
                    os.remove(jnlp_file)

                jnlp_fh = open(jnlp_file, "w+")
                jnlp_fh.write(source)
                jnlp_fh.close()

                java_str = ucsgenutils.get_java_version()
                log.debug("Java Version: <%s>" % java_str)
                if re.match(r'1.8', java_str):
                    debug_str = '\t<property ' \
                                    'name="jnlp.ucsm.log.show.encrypted" ' \
                                    'value="true"/>'
                elif re.match(r'1.7', java_str):
                    if int(java_str.rsplit('_')[1]) >= 45:
                        debug_str = '\t<property ' \
                                    'name="jnlp.ucsm.log.show.encrypted" ' \
                                    'value="true"/>'
                    else:
                        debug_str = '\t<property ' \
                                    'name="log.show.encrypted" ' \
                                    'value="true"/>'
                else:
                    debug_str = '\t<property ' \
                                'name="log.show.encrypted" ' \
                                'value="true"/>'

                log.debug("Enable Log String is %s." % debug_str)
                for line in fileinput.input(jnlp_file, inplace=1):
                    if re.search(r'^\s*</resources>\s*$', line):
                        print debug_str
                    print line,
                subprocess.call([javaws_path, jnlp_file])
                if os.path.exists(jnlp_file):
                    os.remove(jnlp_file)
            else:
                return None
    except Exception:
        fileinput.close()
        if os.path.exists(jnlp_file):
            os.remove(jnlp_file)
        raise
