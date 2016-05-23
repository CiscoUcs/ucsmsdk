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
This module contains the APIs used to create and download tech_support file.
"""

import os
import time
import datetime
import logging
from ..ucsexception import UcsValidationException, UcsWarning

log = logging.getLogger('ucs')


def get_ucs_tech_support(handle,
                         ucs_manager=False,
                         ucs_mgmt=False,
                         chassis_id=None, cimc_id=None,
                         adapter_id=None, iom_id=None,
                         fex_id=None,
                         rack_server_id=None, rack_adapter_id=None,
                         remove_from_ucs=False,
                         download_techsupp=True, file_dir=None, file_name=None,
                         timeout_in_sec=600):
    """
    This operation creates and downloads the technical support file for
    the specified Ucs server.

    Args:
        handle (UcsHandle): Ucs connection handle
        ucs_manager (bool): True/False,
                            False - by default
                            Create and download TechSupport for UCSM, if true
        ucs_mgmt (bool): True/False,
                         False - by default
                         Create and download TechSupport for UCSM Management
                         services(excluding Fabric interconnects), if true
        chassis_id (int): chassis id
        cimc_id (int/string): for a specific chassis. Can be 'all'.
        adapter_id (int/string): for a specific chassis. Can be 'all'.
        iom_id (int/string): for a specific chassis. Can be 'all'.
        fex_id (int): id of a fabric extender.
        rack_server_id (int): id of a rack server.
        rack_adapter_id (int/string): adaptor_id for a specific rack server.
                              Can be 'all'.
        remove_from_ucs (bool): True/False,
                                False - by default
                                TechSupport will be removed from server, if True
        download_techsupp (bool): True/False,
                                    True - by default
                                    Download the TechSupport file, if True
        file_dir (str): directory to download tech support file to
        file_name (str): name of the download tech support file
        timeout_in_sec (int): specifies the time in seconds after which
                                the operation times-out.

    Example:
        * M - Manadatory, O - Optional
        * Note:
          Mandatory in ALL param sets: file_dir, file_name
          Optional in ALL param sets: timeout_in_sec, remove_from_ucs,
                                      download_techsupp

        * param set 1:
        * M - ucs_manager
        ---------------------------------------------------------------
        file_dir = "/home/user/techsupp"
        file_name = "techsupp_ucs_manager.tar"
        get_ucs_tech_support(handle,
                            file_dir=file_dir,
                            file_name=file_name,
                            ucs_manager=True)

        get_ucs_tech_support(handle,
                    file_dir=file_dir,
                    file_name=file_name,
                    ucs_manager=True,
                    timeout_in_sec=300,
                    remove_from_ucs=True)

        * param set 2:
        * M - ucs_manager
        ---------------------------------------------------------------
        file_dir = "/home/user/techsupp"
        file_name = "techsupp_ucs_mgmt.tar"
        get_ucs_tech_support(handle,
                            file_dir=file_dir,
                            file_name=file_name,
                            ucs_mgmt=True)

        * param set 3:
        * M - chassis_id, cimc_id
        * O - adapter_id
        ---------------------------------------------------------------
        file_dir = "/home/user/techsupp"
        file_name = "techsupp_ucs_mgmt.tar"
        get_ucs_tech_support(handle,
                            file_dir=file_dir,
                            file_name=file_name,
                            chassis_id=1,
                            cimc_id=1,
                            adapter_id=1)

        * param set 4:
        * M - chassis_id, iom_id
        ---------------------------------------------------------------
        file_dir = "/home/user/techsupp"
        file_name = "techsupp_ucs_mgmt.tar"
        get_ucs_tech_support(handle,
                            file_dir=file_dir,
                            file_name=file_name,
                            chassis_id=1,
                            iom_id=1)

        * param set 5:
        * M - fex_id
        ---------------------------------------------------------------
        file_dir = "/home/user/techsupp"
        file_name = "techsupp_ucs_mgmt.tar"
        get_ucs_tech_support(handle,
                            file_dir=file_dir,
                            file_name=file_name,
                            fex_id=1)

        * param set 6:
        * M - rack_server_id
        * O - rack_adapter_id
        ---------------------------------------------------------------
        file_dir = "/home/user/techsupp"
        file_name = "techsupp_ucs_mgmt.tar"
        get_ucs_tech_support(handle,
                            file_dir=file_dir,
                            file_name=file_name,
                            rack_server_id=1,
                            rack_adapter_id=1)
    """

    from ..mometa.top.TopSystem import TopSystem
    from ..mometa.sysdebug.SysdebugTechSupport import SysdebugTechSupport, \
        SysdebugTechSupportConsts
    from ..mometa.sysdebug.SysdebugTechSupFileRepository import \
        SysdebugTechSupFileRepository
    from ..mometa.sysdebug.SysdebugTechSupportCmdOpt import \
        SysdebugTechSupportCmdOpt, SysdebugTechSupportCmdOptConsts

    if download_techsupp:
        if file_name is None:
            raise UcsValidationException('provide file_name')
        if file_dir is None:
            raise UcsValidationException('provide dir_name')

        if not file_name.endswith('.tar'):
            raise UcsValidationException('file_name should end with .tar')

        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

    # Converting timedelta in to total seconds for Python version compatibility
    dt1 = datetime.datetime(1970, 1, 1, 12, 0, 0, 0)
    dt2 = datetime.datetime.utcnow()
    creation_ts = int((dt2 - dt1).total_seconds())

    # create SysdebugTechSupport
    top_system = TopSystem()
    sysdebug_techsup_file_repo = SysdebugTechSupFileRepository(
        parent_mo_or_dn=top_system)
    sys_debug_tech_support = SysdebugTechSupport(
        parent_mo_or_dn=sysdebug_techsup_file_repo,
        creation_ts=str(creation_ts),
        admin_state=SysdebugTechSupportConsts.ADMIN_STATE_START)

    sys_debug_tech_support_cmd_opt = SysdebugTechSupportCmdOpt(
        parent_mo_or_dn=sys_debug_tech_support)

    # Parameter Set UCSM
    if ucs_manager:
        sys_debug_tech_support_cmd_opt.major_opt_type = \
            SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_UCSM
    elif ucs_mgmt:
        sys_debug_tech_support_cmd_opt.major_opt_type = \
            SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_UCSM_MGMT
    elif chassis_id is not None:
        if cimc_id is not None:
            sys_debug_tech_support_cmd_opt.chassis_cimc_id = str(cimc_id)
            sys_debug_tech_support_cmd_opt.chassis_id = str(chassis_id)
            sys_debug_tech_support_cmd_opt.major_opt_type = \
                SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_CHASSIS

            if adapter_id is None:
                sys_debug_tech_support_cmd_opt.cimc_adapter_id = \
                    SysdebugTechSupportCmdOptConsts.CIMC_ADAPTER_ID_ALL
            else:
                sys_debug_tech_support_cmd_opt.cimc_adapter_id = \
                    str(adapter_id)
        elif iom_id is not None:
            sys_debug_tech_support_cmd_opt.chassis_iom_id = str(iom_id)
            sys_debug_tech_support_cmd_opt.chassis_id = str(chassis_id)
            sys_debug_tech_support_cmd_opt.major_opt_type = \
                SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_CHASSIS
    elif rack_server_id is not None:
        sys_debug_tech_support_cmd_opt.rack_server_id = str(iom_id)

        if rack_adapter_id is None:
            sys_debug_tech_support_cmd_opt.rack_server_adapter_id = \
                SysdebugTechSupportCmdOptConsts.RACK_SERVER_ADAPTER_ID_ALL
        else:
            sys_debug_tech_support_cmd_opt.rack_server_adapter_id = \
                str(rack_adapter_id)
            sys_debug_tech_support_cmd_opt.major_opt_type = \
                SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_SERVER
    elif fex_id is not None:
        sys_debug_tech_support_cmd_opt.fab_ext_id = str(iom_id)
        sys_debug_tech_support_cmd_opt.major_opt_type = \
            SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_FEX

    handle.add_mo(sys_debug_tech_support)
    handle.commit()

    # poll for tech support to complete
    duration = timeout_in_sec
    poll_interval = 2
    status = False

    while True:
        tech_support = handle.query_dn(sys_debug_tech_support.dn)
        if tech_support.oper_state == \
                SysdebugTechSupportConsts.OPER_STATE_AVAILABLE:
            status = True
        if status:
            break
        time.sleep(min(duration, poll_interval))
        duration = max(0, (duration - poll_interval))
        if duration == 0:
            handle.remove_mo(tech_support)
            handle.commit()
            raise UcsValidationException('TechSupport file creation timed out')

    # download tech support file
    if download_techsupp:
        url_suffix = "techsupport/" + tech_support.name
        try:
            handle.file_download(url_suffix=url_suffix,
                                 file_dir=file_dir,
                                 file_name=file_name)
        except Exception as err:
            UcsWarning(str(err))

    # remove tech support file from ucs
    if remove_from_ucs:
        tech_support.admin_state = "delete"
        handle.set_mo(tech_support)
        handle.commit()

    return tech_support
