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
from ..deprecated import deprecated
from ..ucsexception import UcsValidationException, UcsWarning
from ..mometa.sysdebug.SysdebugTechSupportCmdOpt import \
    SysdebugTechSupportCmdOptConsts as TechSupOptsConsts

log = logging.getLogger('ucs')


def _create_download_dir(file_dir):
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)


def _validate_download_args(file_dir, file_name):
    if file_dir is None:
        raise UcsValidationException('file_dir is a required parameter')

    if file_name is None:
        raise UcsValidationException('file_name is a required parameter')

    if not file_name.endswith('.tar'):
        raise UcsValidationException('file_name should end with .tar')


def _get_creation_ts():
    dt1 = datetime.datetime(1970, 1, 1, 12, 0, 0, 0)
    dt2 = datetime.datetime.utcnow()
    return int((dt2 - dt1).total_seconds())


def _bootstrap_tech_support_mo(creation_ts):
    from ..mometa.top.TopSystem import TopSystem
    from ..mometa.sysdebug.SysdebugTechSupport import SysdebugTechSupport, \
        SysdebugTechSupportConsts
    from ..mometa.sysdebug.SysdebugTechSupFileRepository import \
        SysdebugTechSupFileRepository

    top_system = TopSystem()
    ts_file_repo = SysdebugTechSupFileRepository(parent_mo_or_dn=top_system)
    ts_mo = SysdebugTechSupport(
        parent_mo_or_dn=ts_file_repo,
        creation_ts=str(creation_ts),
        admin_state=SysdebugTechSupportConsts.ADMIN_STATE_START)
    return ts_mo


def _is_valid_arg(param, kwargs):
    return param in kwargs and kwargs[param] is not None


def _set_ts_options_ucsm(ts_cmd_opt, kwargs):
    ts_cmd_opt.major_opt_type = TechSupOptsConsts.MAJOR_OPT_TYPE_UCSM


def _set_ts_options_ucsm_mgmt(ts_cmd_opt, kwargs):
    ts_cmd_opt.major_opt_type = TechSupOptsConsts.MAJOR_OPT_TYPE_UCSM_MGMT


def _validate_chassis_options(kwargs):
    if not _is_valid_arg("chassis_id", kwargs):
        raise UcsValidationException('chassis_id should be specified')
    if "cimc_id" not in kwargs and "iom_id" not in kwargs and "cartridge_id" not in kwargs:
        raise UcsValidationException('cimc_id/iom_id/cartridge_id should be specified')


def _set_ts_options_chassis(ts_cmd_opt, kwargs):
    _validate_chassis_options(kwargs)
    ts_cmd_opt.chassis_id = str(kwargs["chassis_id"])
    ts_cmd_opt.major_opt_type = TechSupOptsConsts.MAJOR_OPT_TYPE_CHASSIS
    if _is_valid_arg("cimc_id", kwargs):
        ts_cmd_opt.chassis_cimc_id = str(kwargs["cimc_id"])

        if _is_valid_arg("adapter_id", kwargs):
            ts_cmd_opt.cimc_adapter_id = str(kwargs["adapter_id"])
        else:
            ts_cmd_opt.cimc_adapter_id = TechSupOptsConsts.CIMC_ADAPTER_ID_ALL
    elif _is_valid_arg("iom_id", kwargs):
        ts_cmd_opt.chassis_iom_id = str(kwargs["iom_id"])
    elif _is_valid_arg("cartridge_id", kwargs):
        ts_cmd_opt.chassis_cartridge_id = str(kwargs["cartridge_id"])
        if ts_cmd_opt.chassis_cartridge_id != "all":
            if _is_valid_arg("cartridge_cimc_id", kwargs):
                ts_cmd_opt.cartridge_cimc_id = str(kwargs["cartridge_cimc_id"])
            else:
                raise UcsValidationException('cartridge_cimc_id should be specified')


def _validate_rackserver_options(kwargs):
    if not _is_valid_arg("rack_server_id", kwargs):
        raise UcsValidationException('rack_server_id should be specified')


def _set_ts_options_rackserver(ts_cmd_opt, kwargs):
    _validate_rackserver_options(kwargs)
    ts_cmd_opt.rack_server_id = str(kwargs["rack_server_id"])
    ts_cmd_opt.major_opt_type = TechSupOptsConsts.MAJOR_OPT_TYPE_SERVER

    if _is_valid_arg("rack_adapter_id", kwargs):
        ts_cmd_opt.rack_server_adapter_id = str(kwargs["rack_adapter_id"])
    else:
        ts_cmd_opt.rack_server_adapter_id = TechSupOptsConsts.RACK_SERVER_ADAPTER_ID_ALL


def _validate_fex_options(kwargs):
    if not _is_valid_arg("fex_id", kwargs):
        raise UcsValidationException('fex_id should be specified')


def _set_ts_options_fex(ts_cmd_opt, kwargs):
    _validate_fex_options(kwargs)
    ts_cmd_opt.fab_ext_id = str(kwargs["fex_id"])
    ts_cmd_opt.major_opt_type = TechSupOptsConsts.MAJOR_OPT_TYPE_FEX


def _validate_servermemory_options(kwargs):
    if not _is_valid_arg("server_id_list", kwargs):
        raise UcsValidationException('server_id_list should be specified')


def _set_ts_options_servermemory(ts_cmd_opt, kwargs):
    _validate_servermemory_options(kwargs)
    ts_cmd_opt.server_id_list = str(kwargs["server_id_list"])
    ts_cmd_opt.major_opt_type = TechSupOptsConsts.MAJOR_OPT_TYPE_SERVER_MEMORY


def _set_ts_command_options(ts_cmd_opt, kwargs):
    if _is_valid_arg("command_options", kwargs):
        ts_cmd_opt.command_options = str(kwargs["command_options"])


def _set_ts_options(option, ts_cmd_opt, kwargs):
    if option == "ucsm":
        _set_ts_options_ucsm(ts_cmd_opt, kwargs)
    elif option == "ucsm-mgmt":
        _set_ts_options_ucsm_mgmt(ts_cmd_opt, kwargs)
    elif option == "chassis":
        _set_ts_options_chassis(ts_cmd_opt, kwargs)
    elif option == "fabric-extender":
        _set_ts_options_fex(ts_cmd_opt, kwargs)
    elif option == "rack-server":
        _set_ts_options_rackserver(ts_cmd_opt, kwargs)
    elif option == "server-memory":
        _set_ts_options_servermemory(ts_cmd_opt, kwargs)
    else:
        raise UcsValidationException('Unrecognised option value: ' + option)

    _set_ts_command_options(ts_cmd_opt, kwargs)


def _check_for_failure(err):
    # The following error messages define the criteria for
    # the poll loop to be interrupted by an exception.
    # There are occasinal Request Timeouts, which could be ignored
    # if the subsequent calls are being replied to by the server.
    failure_conditions = ["urlopen error",
                          "TechSupport creation timed out",
                          "TechSupport creation failed"]
    for each in failure_conditions:
        if each in str(err):
            raise Exception(each)


def _fail_and_remove_ts(handle, ts_mo, err):
    if ts_mo:
        handle.remove_mo(ts_mo)
        handle.commit()
    raise UcsValidationException(err)


def poll_wait_for_tech_support(handle, ts_mo, timeout):
    from ..mometa.sysdebug.SysdebugTechSupport import \
        SysdebugTechSupportConsts as TechSupConsts

    poll_interval = 5
    duration = timeout
    while True:
        try:
            ts = handle.query_dn(ts_mo.dn)
            if ts is None:
                _fail_and_remove_ts(handle, ts, 'TechSupport creation failed')
            if ts.oper_state == TechSupConsts.OPER_STATE_AVAILABLE:
                break
            if ts.oper_state == TechSupConsts.OPER_STATE_FAILED or \
                    ts.oper_state == TechSupConsts.OPER_STATE_UNAVAILABLE:
                _fail_and_remove_ts(handle, ts, 'TechSupport creation failed')
            time.sleep(min(duration, poll_interval))
            duration = max(0, (duration - poll_interval))
            if duration == 0:
                _fail_and_remove_ts(
                    handle, ts, 'TechSupport creation timed out')
        except Exception as err:
            _check_for_failure(err)


def download_tech_support(handle, name, file_dir, file_name):
    try:
        handle.file_download(url_suffix="techsupport/" + name,
                             file_dir=str(file_dir),
                             file_name=str(file_name))
    except Exception as err:
        UcsWarning(str(err))


def remove_tech_support(handle, ts_mo):
    ts_mo.admin_state = "delete"
    handle.set_mo(ts_mo)
    handle.commit()


def get_tech_support(handle,
                     option="ucsm",
                     remove_from_ucs=False,
                     download=True, file_dir=".", file_name="techsupport.tar",
                     timeout=1200,
                     **kwargs):
    """
    Create and optionally download technical support for Ucs or individual
        components.

    Args:
        handle (UcsHandle): Ucs connection handle
        option (str): categorty of technical support to be created.
                      possible values:
                        - ucsm
                        - ucsm-mgmt
                        - chassis:
                            Mandates that user specifies "chassis_id"
                            Either "cimc_id" or "iom_id" or "cartridge_id"
                            When specific "cartridge_id" is given, instead of "all",
                            mandatory "cartridge_cimc_id" must also be given
                        - fabric-extender
                            Mandates that user specifies "fex_id"
                        - rack-server
                            Mandates that user specifies "rack_server_id"
                        - server-memory
                            Mandates that user specifies "server_id_list"
        remove_from_ucs (bool): Remove the created technical support, if True
        download (bool): download the technical support if True
        kwargs: key=value pairs relevant to the seleced option

    Examples:
        get_tech_support(handle,
                         option="ucsm",
                         file_dir=".",
                         file_name="techsupport.tar")

        get_tech_support(handle,
                         option="ucsm-mgmt",
                         file_dir=".",
                         file_name="techsupport.tar")

        get_tech_support(handle,
                         option="chassis",
                         file_dir=".",
                         file_name="techsupport.tar",
                         chassis_id=1,
                         cimc_id=1,
                         adapter_id=1)

        get_tech_support(handle,
                         option="chassis",
                         file_dir=".",
                         file_name="techsupport.tar",
                         chassis_id=1,
                         iom_id=1)

        get_tech_support(handle,
                         option="chassis",
                         file_dir=".",
                         file_name="techsupport.tar",
                         chassis_id=1,
                         cartridge_id=1,
                         cartridge_cimc_id=1)

        get_tech_support(handle,
                         option="rack-server",
                         file_dir=".",
                         file_name="techsupport.tar",
                         rack_server_id=1,
                         rack_adapter_id="all")

        get_tech_support(handle,
                         option="fabric-extender",
                         file_dir=".",
                         file_name="techsupport.tar",
                         fex_id=1)

        get_tech_support(handle,
                         option="server-memory",
                         file_dir=".",
                         file_name="techsupport.tar",
                         server_id_list="1,2")

    """
    from ..mometa.sysdebug.SysdebugTechSupportCmdOpt import \
        SysdebugTechSupportCmdOpt

    if download:
        _validate_download_args(file_dir, file_name)
        _create_download_dir(file_dir)

    ts_mo = _bootstrap_tech_support_mo(_get_creation_ts())
    ts_cmd_opt = SysdebugTechSupportCmdOpt(parent_mo_or_dn=ts_mo)
    _set_ts_options(option, ts_cmd_opt, kwargs)

    handle.add_mo(ts_mo)
    handle.commit()

    poll_wait_for_tech_support(handle, ts_mo, timeout)

    # The backend changes the name of the MO in some scenarios.
    # Query it again to have the updated MO name
    ts_mo = handle.query_dn(ts_mo.dn)

    if download:
        download_tech_support(handle, ts_mo.name, file_dir, file_name)

    if remove_from_ucs:
        remove_tech_support(handle, ts_mo)


@deprecated(get_tech_support)
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
        sys_debug_tech_support_cmd_opt.rack_server_id = str(rack_server_id)
        sys_debug_tech_support_cmd_opt.major_opt_type = \
            SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_SERVER

        if rack_adapter_id is None:
            sys_debug_tech_support_cmd_opt.rack_server_adapter_id = \
                SysdebugTechSupportCmdOptConsts.RACK_SERVER_ADAPTER_ID_ALL
        else:
            sys_debug_tech_support_cmd_opt.rack_server_adapter_id = \
                str(rack_adapter_id)
    elif fex_id is not None:
        sys_debug_tech_support_cmd_opt.fab_ext_id = str(fex_id)
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
