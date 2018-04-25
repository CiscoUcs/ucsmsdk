# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This is an auto-generated module.
It contains supporting classes for Filter and External Method.

"""

from . import ucsgenutils
from . import ucscoreutils as coreutils
from .ucsmethod import ExternalMethod
from .ucscoremeta import WriteXmlOption
from .ucsconstants import YesOrNo


def aaa_change_self_password(cookie, in_confirm_new_password, in_new_password, in_old_password, in_user_name):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaChangeSelfPassword")
    method.cookie = cookie
    method.in_confirm_new_password = in_confirm_new_password
    method.in_new_password = in_new_password
    method.in_old_password = in_old_password
    method.in_user_name = in_user_name

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_check_compute_auth_token(cookie, in_token, in_user):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaCheckComputeAuthToken")
    method.cookie = cookie
    method.in_token = in_token
    method.in_user = in_user

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_check_compute_ext_access(cookie, in_dn, in_user):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaCheckComputeExtAccess")
    method.cookie = cookie
    method.in_dn = in_dn
    method.in_user = in_user

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_get_auth_token_client(in_cookie):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaGetAuthTokenClient")
    method.in_cookie = in_cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_get_auth_token_internal(cookie, in_id, in_ipv4, in_locales, in_parent_sess, in_priv, in_remote, in_role_list, in_user):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaGetAuthTokenInternal")
    method.cookie = cookie
    method.in_id = str(in_id)
    method.in_ipv4 = in_ipv4
    method.in_locales = in_locales
    method.in_parent_sess = in_parent_sess
    method.in_priv = in_priv
    method.in_remote = in_remote
    method.in_role_list = in_role_list
    method.in_user = in_user

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_get_kvm_launch_url(in_cookie, in_ipv4):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaGetKVMLaunchUrl")
    method.in_cookie = in_cookie
    method.in_ipv4 = in_ipv4

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_get_kvm_launch_url_internal(cookie, in_cimc_ipv4, in_ipv4, in_ipv6, in_locales, in_parent_sess, in_priv, in_remote, in_role_list, in_user):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaGetKVMLaunchUrlInternal")
    method.cookie = cookie
    method.in_cimc_ipv4 = in_cimc_ipv4
    method.in_ipv4 = in_ipv4
    method.in_ipv6 = in_ipv6
    method.in_locales = in_locales
    method.in_parent_sess = in_parent_sess
    method.in_priv = in_priv
    method.in_remote = in_remote
    method.in_role_list = in_role_list
    method.in_user = in_user

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_get_n_compute_auth_token_by_dn(cookie, in_cookie, in_dn, in_number_of):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaGetNComputeAuthTokenByDn")
    method.cookie = cookie
    method.in_dn = in_dn
    method.in_number_of = str(in_number_of)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_get_n_compute_auth_token_internal_by_dn(cookie, in_dn, in_id, in_ipv4, in_locales, in_number_of, in_parent_sess, in_priv, in_remote, in_role_list, in_user):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaGetNComputeAuthTokenInternalByDn")
    method.cookie = cookie
    method.in_dn = in_dn
    method.in_id = str(in_id)
    method.in_ipv4 = in_ipv4
    method.in_locales = in_locales
    method.in_number_of = str(in_number_of)
    method.in_parent_sess = in_parent_sess
    method.in_priv = in_priv
    method.in_remote = in_remote
    method.in_role_list = in_role_list
    method.in_user = in_user

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_keep_alive(cookie):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaKeepAlive")
    method.cookie = cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_login(in_name, in_password):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaLogin")
    method.in_name = in_name
    method.in_password = in_password

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_logout(in_cookie, in_delay_secs):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaLogout")
    method.in_cookie = in_cookie
    method.in_delay_secs = str(in_delay_secs)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_refresh(in_cookie, in_name, in_password):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaRefresh")
    method.in_cookie = in_cookie
    method.in_name = in_name
    method.in_password = in_password

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_setup_shell_access_internal(cookie, in_id, in_locales, in_parent_sess, in_priv, in_remote, in_role_list, in_ssh_key, in_user):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaSetupShellAccessInternal")
    method.cookie = cookie
    method.in_id = str(in_id)
    method.in_locales = in_locales
    method.in_parent_sess = in_parent_sess
    method.in_priv = in_priv
    method.in_remote = in_remote
    method.in_role_list = in_role_list
    method.in_ssh_key = in_ssh_key
    method.in_user = in_user

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_token_login(cookie, in_name, in_token):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaTokenLogin")
    method.cookie = cookie
    method.in_name = in_name
    method.in_token = in_token

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_token_refresh(in_cookie, in_name):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("AaaTokenRefresh")
    method.in_cookie = in_cookie
    method.in_name = in_name

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_boot_pnu_os(cookie, in_config):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeBootPnuOs")
    method.cookie = cookie
    method.in_config = in_config

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_configure_cmclif(cookie, in_config):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeConfigureCMCLIF")
    method.cookie = cookie
    method.in_config = in_config

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_create_hv_vnic(cookie, in_blade_slot_id, in_chassis_id, in_config, in_sw_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeCreateHVVnic")
    method.cookie = cookie
    method.in_blade_slot_id = str(in_blade_slot_id)
    method.in_chassis_id = str(in_chassis_id)
    method.in_config = in_config
    method.in_sw_id = in_sw_id

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_create_sfish(cookie, in_blade_slot_id, in_chassis_id, in_config, in_sw_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeCreateSfish")
    method.cookie = cookie
    method.in_blade_slot_id = str(in_blade_slot_id)
    method.in_chassis_id = str(in_chassis_id)
    method.in_config = in_config
    method.in_sw_id = in_sw_id

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_create_vm_vnic(cookie, in_blade_slot_id, in_chassis_id, in_config, in_sw_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeCreateVMVnic")
    method.cookie = cookie
    method.in_blade_slot_id = str(in_blade_slot_id)
    method.in_chassis_id = str(in_chassis_id)
    method.in_config = in_config
    method.in_sw_id = in_sw_id

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_delete_hv_vnic(cookie, in_vnic_dn):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeDeleteHVVnic")
    method.cookie = cookie
    method.in_vnic_dn = in_vnic_dn

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_delete_sfish(cookie, in_vm_switch_dn):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeDeleteSfish")
    method.cookie = cookie
    method.in_vm_switch_dn = in_vm_switch_dn

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_delete_vm_vnic(cookie, in_vnic_dn):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeDeleteVMVnic")
    method.cookie = cookie
    method.in_vnic_dn = in_vnic_dn

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_get_adaptor_connectivity(cookie, in_fru_model, in_fru_serial, in_fru_vendor):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeGetAdaptorConnectivity")
    method.cookie = cookie
    method.in_fru_model = in_fru_model
    method.in_fru_serial = in_fru_serial
    method.in_fru_vendor = in_fru_vendor

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_get_ape_firmware_active_side(cookie, in_field_name, in_ip_addr):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeGetApeFirmwareActiveSide")
    method.cookie = cookie
    method.in_field_name = str(in_field_name)
    method.in_ip_addr = in_ip_addr

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_get_inventory_from_storage_registrar(cookie, in_disk_model, in_disk_serial, in_disk_vendor):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeGetInventoryFromStorageRegistrar")
    method.cookie = cookie
    method.in_disk_model = in_disk_model
    method.in_disk_serial = in_disk_serial
    method.in_disk_vendor = in_disk_vendor

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_get_ip_from_serial(cookie, in_equipment_serial):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeGetIpFromSerial")
    method.cookie = cookie
    method.in_equipment_serial = in_equipment_serial

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_get_mc_stats(cookie, in_equipment_serial):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeGetMcStats")
    method.cookie = cookie
    method.in_equipment_serial = in_equipment_serial

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_get_next_id(cookie, in_chassis_id, in_mo_type, in_server_instance_id, in_slot_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeGetNextId")
    method.cookie = cookie
    method.in_chassis_id = str(in_chassis_id)
    method.in_mo_type = str(in_mo_type)
    method.in_server_instance_id = str(in_server_instance_id)
    method.in_slot_id = str(in_slot_id)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_get_pnu_os_inventory(cookie, in_fru_model, in_fru_serial, in_fru_vendor):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeGetPnuOSInventory")
    method.cookie = cookie
    method.in_fru_model = in_fru_model
    method.in_fru_serial = in_fru_serial
    method.in_fru_vendor = in_fru_vendor

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_get_server_from_ip(cookie, in_ip_addr):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeGetServerFromIp")
    method.cookie = cookie
    method.in_ip_addr = in_ip_addr

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_get_switch_ape_fru(cookie, in_sw_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeGetSwitchApeFru")
    method.cookie = cookie
    method.in_sw_id = in_sw_id

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_inject_stimuli(cookie, in_from_svc, in_stimuli, in_to_svc):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeInjectStimuli")
    method.cookie = cookie
    method.in_from_svc = str(in_from_svc)
    method.in_stimuli = in_stimuli
    method.in_to_svc = str(in_to_svc)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_insert_new_chassis(cookie, in_device_primary_key, in_model, in_peer_type, in_serial, in_vendor):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeInsertNewChassis")
    method.cookie = cookie
    method.in_device_primary_key = in_device_primary_key
    method.in_model = in_model
    method.in_peer_type = in_peer_type
    method.in_serial = in_serial
    method.in_vendor = in_vendor

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_insert_new_fex(cookie, in_device_primary_key, in_model, in_serial, in_vendor):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeInsertNewFex")
    method.cookie = cookie
    method.in_device_primary_key = in_device_primary_key
    method.in_model = in_model
    method.in_serial = in_serial
    method.in_vendor = in_vendor

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_insert_new_rack(cookie, in_config, in_fx_id, in_fx_port_id, in_fx_slot_id, in_is_refresh):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeInsertNewRack")
    method.cookie = cookie
    method.in_config = in_config
    method.in_fx_id = str(in_fx_id)
    method.in_fx_port_id = str(in_fx_port_id)
    method.in_fx_slot_id = str(in_fx_slot_id)
    method.in_is_refresh = str(in_is_refresh)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_issue_adaptor_id(cookie, in_config):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeIssueAdaptorId")
    method.cookie = cookie
    method.in_config = in_config

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_issue_chassis_id(cookie, in_config, in_sw_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeIssueChassisId")
    method.cookie = cookie
    method.in_config = in_config
    method.in_sw_id = in_sw_id

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_issue_fex_id(cookie, in_config):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeIssueFexId")
    method.cookie = cookie
    method.in_config = in_config

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_issue_rack_id(cookie, in_config):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeIssueRackId")
    method.cookie = cookie
    method.in_config = in_config

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_mc_get(cookie, in_mc_address):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeMcGet")
    method.cookie = cookie
    method.in_mc_address = in_mc_address

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_mc_get_attribute(cookie, in_attribute_ids, in_mc_ip):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeMcGetAttribute")
    method.cookie = cookie
    method.in_attribute_ids = in_attribute_ids
    method.in_mc_ip = in_mc_ip

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_mc_get_attribute_data(cookie, in_attribute_id, in_mc_ip):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeMcGetAttributeData")
    method.cookie = cookie
    method.in_attribute_id = str(in_attribute_id)
    method.in_mc_ip = in_mc_ip

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_mc_get_bios_tokens(cookie, in_chassis_id, in_instance_id, in_slot_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeMcGetBiosTokens")
    method.cookie = cookie
    method.in_chassis_id = str(in_chassis_id)
    method.in_instance_id = str(in_instance_id)
    method.in_slot_id = str(in_slot_id)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_mc_get_fru(cookie, in_fru_ids, in_mc_ip):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeMcGetFru")
    method.cookie = cookie
    method.in_fru_ids = in_fru_ids
    method.in_mc_ip = in_mc_ip

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_mc_get_param(cookie, in_mc_ip, in_param_ids):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeMcGetParam")
    method.cookie = cookie
    method.in_mc_ip = in_mc_ip
    method.in_param_ids = in_param_ids

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_mc_get_reading(cookie, in_mc_ip, in_reading_ids):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeMcGetReading")
    method.cookie = cookie
    method.in_mc_ip = in_mc_ip
    method.in_reading_ids = in_reading_ids

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_mc_get_sdr(cookie, in_mc_ip, in_sdr_ids):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeMcGetSdr")
    method.cookie = cookie
    method.in_mc_ip = in_mc_ip
    method.in_sdr_ids = in_sdr_ids

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_mc_get_smbios(cookie, in_ip_addr, in_update_cnt):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeMcGetSmbios")
    method.cookie = cookie
    method.in_ip_addr = in_ip_addr
    method.in_update_cnt = in_update_cnt

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_mc_set(cookie, in_config):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeMcSet")
    method.cookie = cookie
    method.in_config = in_config

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_mc_set_attribute_data(cookie, in_action, in_config, in_mc_ip):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeMcSetAttributeData")
    method.cookie = cookie
    method.in_action = str(in_action)
    method.in_config = in_config
    method.in_mc_ip = in_mc_ip

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_mc_set_param(cookie, in_mc_ip, in_param_ids, in_param_vals):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeMcSetParam")
    method.cookie = cookie
    method.in_mc_ip = in_mc_ip
    method.in_param_ids = in_param_ids
    method.in_param_vals = in_param_vals

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_mux_offline(cookie, in_ch_id, in_mux_slot_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeMuxOffline")
    method.cookie = cookie
    method.in_ch_id = str(in_ch_id)
    method.in_mux_slot_id = str(in_mux_slot_id)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_remove_device(cookie, in_serial):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeRemoveDevice")
    method.cookie = cookie
    method.in_serial = in_serial

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_set_adaptor_firmware_version(cookie, in_adaptor_fw_version, in_adaptor_serial):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeSetAdaptorFirmwareVersion")
    method.cookie = cookie
    method.in_adaptor_fw_version = in_adaptor_fw_version
    method.in_adaptor_serial = in_adaptor_serial

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_set_ape_sensor_reading(cookie, in_chassis_id, in_fault_level, in_instance_id, in_operation, in_sensor_name, in_slot_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeSetApeSensorReading")
    method.cookie = cookie
    method.in_chassis_id = str(in_chassis_id)
    method.in_fault_level = str(in_fault_level)
    method.in_instance_id = str(in_instance_id)
    method.in_operation = str(in_operation)
    method.in_sensor_name = str(in_sensor_name)
    method.in_slot_id = str(in_slot_id)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_set_flex_flash_controller_firmware_version(cookie, in_ip_addr, in_version):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeSetFlexFlashControllerFirmwareVersion")
    method.cookie = cookie
    method.in_ip_addr = str(in_ip_addr)
    method.in_version = in_version

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_set_flex_flash_controller_state(cookie, in_controller_state, in_ip_addr):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeSetFlexFlashControllerState")
    method.cookie = cookie
    method.in_controller_state = str(in_controller_state)
    method.in_ip_addr = str(in_ip_addr)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_set_flex_flash_virtual_raid_information(cookie, in_conrtoller_id, in_ip_addr, in_raid_health, in_raid_state):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeSetFlexFlashVirtualRaidInformation")
    method.cookie = cookie
    method.in_conrtoller_id = str(in_conrtoller_id)
    method.in_ip_addr = str(in_ip_addr)
    method.in_raid_health = str(in_raid_health)
    method.in_raid_state = str(in_raid_state)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_set_mc_stats(cookie, in_equipment_serial, in_mc_stats, in_stat_ids):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeSetMcStats")
    method.cookie = cookie
    method.in_equipment_serial = in_equipment_serial
    method.in_mc_stats = in_mc_stats
    method.in_stat_ids = in_stat_ids

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_set_server_life_cycle(cookie, in_fru_model, in_fru_serial, in_fru_vendor, in_server_lc):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeSetServerLifeCycle")
    method.cookie = cookie
    method.in_fru_model = in_fru_model
    method.in_fru_serial = in_fru_serial
    method.in_fru_vendor = in_fru_vendor
    method.in_server_lc = in_server_lc

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_set_switch_inventory(cookie, in_config, in_sw_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeSetSwitchInventory")
    method.cookie = cookie
    method.in_config = in_config
    method.in_sw_id = in_sw_id

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_set_vmedia_mounts(cookie, in_chassis_id, in_count, in_server_instance_id, in_slot_id, in_v_media_set):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeSetVmediaMounts")
    method.cookie = cookie
    method.in_chassis_id = str(in_chassis_id)
    method.in_count = str(in_count)
    method.in_server_instance_id = str(in_server_instance_id)
    method.in_slot_id = str(in_slot_id)
    method.in_v_media_set = in_v_media_set

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_trigger_sw_inv(cookie, in_model, in_serial, in_sw_id, in_vendor):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeTriggerSwInv")
    method.cookie = cookie
    method.in_model = in_model
    method.in_serial = in_serial
    method.in_sw_id = in_sw_id
    method.in_vendor = in_vendor

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_update_ape_firmware_active_side(cookie, in_field_name, in_ip_addr, in_side):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeUpdateApeFirmwareActiveSide")
    method.cookie = cookie
    method.in_field_name = str(in_field_name)
    method.in_ip_addr = in_ip_addr
    method.in_side = str(in_side)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_update_ape_firmware_param_table(cookie, in_field_name, in_ip_addr, in_version):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeUpdateApeFirmwareParamTable")
    method.cookie = cookie
    method.in_field_name = str(in_field_name)
    method.in_ip_addr = in_ip_addr
    method.in_version = in_version

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_update_bios_firmware_version(cookie, in_config):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeUpdateBIOSFirmwareVersion")
    method.cookie = cookie
    method.in_config = in_config

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_update_server_absence(cookie, in_device_primary_key, in_model, in_serial, in_vendor):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeUpdateServerAbsence")
    method.cookie = cookie
    method.in_device_primary_key = in_device_primary_key
    method.in_model = in_model
    method.in_serial = in_serial
    method.in_vendor = in_vendor

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_update_server_presence(cookie, in_device_primary_key, in_model, in_serial, in_vendor):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeUpdateServerPresence")
    method.cookie = cookie
    method.in_device_primary_key = in_device_primary_key
    method.in_model = in_model
    method.in_serial = in_serial
    method.in_vendor = in_vendor

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ape_update_storage_ctlr_firmware_version(cookie, in_config):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ApeUpdateStorageCtlrFirmwareVersion")
    method.cookie = cookie
    method.in_config = in_config

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def compute_get_inventory(cookie, in_faults_only):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ComputeGetInventory")
    method.cookie = cookie
    method.in_faults_only = in_faults_only

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_check_compatibility(cookie, dn, in_blade_pack_version, in_detail_result, in_infra_pack_version, in_rack_pack_version, in_service_pack_bundle_version):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigCheckCompatibility")
    method.cookie = cookie
    method.dn = dn
    method.in_blade_pack_version = in_blade_pack_version
    method.in_detail_result = in_detail_result
    method.in_infra_pack_version = in_infra_pack_version
    method.in_rack_pack_version = in_rack_pack_version
    method.in_service_pack_bundle_version = in_service_pack_bundle_version

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_check_conformance(cookie, dn):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigCheckConformance")
    method.cookie = cookie
    method.dn = dn

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_check_firmware_updatable(cookie, in_updatable_dns):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigCheckFirmwareUpdatable")
    method.cookie = cookie
    method.in_updatable_dns = in_updatable_dns

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_conf_filtered(cookie, class_id, in_config, in_filter, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigConfFiltered")
    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucsgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_config = in_config
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_conf_mo(cookie, dn, in_config, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigConfMo")
    method.cookie = cookie
    method.dn = dn
    method.in_config = in_config
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_conf_mo_group(cookie, in_config, in_dns, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigConfMoGroup")
    method.cookie = cookie
    method.in_config = in_config
    method.in_dns = in_dns
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_conf_mos(cookie, in_configs, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigConfMos")
    method.cookie = cookie
    method.in_configs = in_configs
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_conf_rename(cookie, dn, in_new_name, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigConfRename")
    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_new_name = in_new_name

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_count_class(cookie, class_id, in_filter, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigCountClass")
    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucsgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_estimate_conf_mos(cookie, in_configs, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigEstimateConfMos")
    method.cookie = cookie
    method.in_configs = in_configs
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_estimate_impact(cookie, in_configs):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigEstimateImpact")
    method.cookie = cookie
    method.in_configs = in_configs

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_find_dependencies(cookie, dn, in_return_configs):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigFindDependencies")
    method.cookie = cookie
    method.dn = dn
    method.in_return_configs = in_return_configs

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_find_dns_by_class_id(cookie, class_id, in_filter):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigFindDnsByClassId")
    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucsgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_filter = in_filter

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_find_host_pack_dependencies(cookie, dn, in_host_pack_dns):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigFindHostPackDependencies")
    method.cookie = cookie
    method.dn = dn
    method.in_host_pack_dns = in_host_pack_dns

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_find_pack_dependencies(cookie, dn, in_chassis_pack_dns, in_host_pack_dns):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigFindPackDependencies")
    method.cookie = cookie
    method.dn = dn
    method.in_chassis_pack_dns = in_chassis_pack_dns
    method.in_host_pack_dns = in_host_pack_dns

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_find_permitted(cookie, dn, in_class_id, in_filter, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigFindPermitted")
    method.cookie = cookie
    method.dn = dn
    method.in_class_id = in_class_id
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_get_estimate_impact(cookie, in_configs, in_deleted_dns, in_impact_analyzer_id, in_is_policy_full_config, in_source_connector_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigGetEstimateImpact")
    method.cookie = cookie
    method.in_configs = in_configs
    method.in_deleted_dns = in_deleted_dns
    method.in_impact_analyzer_id = in_impact_analyzer_id
    method.in_is_policy_full_config = in_is_policy_full_config
    method.in_source_connector_id = str(in_source_connector_id)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_get_remote_policies(cookie, in_context, in_policy_digests, in_stimulus_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigGetRemotePolicies")
    method.cookie = cookie
    method.in_context = in_context
    method.in_policy_digests = in_policy_digests
    method.in_stimulus_id = str(in_stimulus_id)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_get_xml_file(cookie, in_file_path):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigGetXmlFile")
    method.cookie = cookie
    method.in_file_path = in_file_path

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_get_xml_file_str(cookie, in_file_path):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigGetXmlFileStr")
    method.cookie = cookie
    method.in_file_path = in_file_path

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_install_all_impact(cookie, dn, in_blade_pack_version, in_host_pack_dns, in_infra_pack_version, in_rack_pack_version, in_service_pack_bundle_version):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigInstallAllImpact")
    method.cookie = cookie
    method.dn = dn
    method.in_blade_pack_version = in_blade_pack_version
    method.in_host_pack_dns = in_host_pack_dns
    method.in_infra_pack_version = in_infra_pack_version
    method.in_rack_pack_version = in_rack_pack_version
    method.in_service_pack_bundle_version = in_service_pack_bundle_version

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_install_chassis_impact(cookie, dn, in_chassis_pack_dns, in_rack_pack_version, in_service_pack_bundle_version):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigInstallChassisImpact")
    method.cookie = cookie
    method.dn = dn
    method.in_chassis_pack_dns = in_chassis_pack_dns
    method.in_rack_pack_version = in_rack_pack_version
    method.in_service_pack_bundle_version = in_service_pack_bundle_version

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_mo_change_event(cookie, in_config, in_eid):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigMoChangeEvent")
    method.cookie = cookie
    method.in_config = in_config
    method.in_eid = str(in_eid)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_refresh_identity(cookie, dn, in_id_type, in_is_discard_mode, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigRefreshIdentity")
    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_id_type = in_id_type
    method.in_is_discard_mode = in_is_discard_mode

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_release_resolve_context(cookie, in_context):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigReleaseResolveContext")
    method.cookie = cookie
    method.in_context = str(in_context)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_renew_resolve_context(cookie, in_context):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigRenewResolveContext")
    method.cookie = cookie
    method.in_context = str(in_context)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_children(cookie, class_id, in_dn, in_filter, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigResolveChildren")
    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucsgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_dn = in_dn
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_children_sorted(cookie, class_id, in_dn, in_filter, in_size, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigResolveChildrenSorted")
    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucsgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_dn = in_dn
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_size = str(in_size)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_class(cookie, class_id, in_filter, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigResolveClass")
    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucsgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_class_sorted(cookie, class_id, in_filter, in_size, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigResolveClassSorted")
    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucsgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_size = str(in_size)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_classes(cookie, in_ids, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigResolveClasses")
    method.cookie = cookie
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_ids = in_ids

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_classes_sorted(cookie, in_ids, in_size, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigResolveClassesSorted")
    method.cookie = cookie
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_ids = in_ids
    method.in_size = str(in_size)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_context(cookie, in_context, in_size):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigResolveContext")
    method.cookie = cookie
    method.in_context = str(in_context)
    method.in_size = str(in_size)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_dn(cookie, dn, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigResolveDn")
    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_dns(cookie, in_dns, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigResolveDns")
    method.cookie = cookie
    method.in_dns = in_dns
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_parent(cookie, dn, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigResolveParent")
    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_scope(cookie, dn, in_class, in_filter, in_recursive, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigScope")
    method.cookie = cookie
    method.dn = dn
    method.in_class = in_class
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_recursive = in_recursive

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_update_all_impact(cookie, dn, in_blade_pack_version, in_chassis_pack_dns, in_host_pack_dns, in_infra_pack_version, in_rack_pack_version):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("ConfigUpdateAllImpact")
    method.cookie = cookie
    method.dn = dn
    method.in_blade_pack_version = in_blade_pack_version
    method.in_chassis_pack_dns = in_chassis_pack_dns
    method.in_host_pack_dns = in_host_pack_dns
    method.in_infra_pack_version = in_infra_pack_version
    method.in_rack_pack_version = in_rack_pack_version

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def equipment_clone(cookie, dn, in_chassis_profile_name, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("EquipmentClone")
    method.cookie = cookie
    method.dn = dn
    method.in_chassis_profile_name = in_chassis_profile_name
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def equipment_instantiate_n_named_template(cookie, dn, in_error_on_existing, in_name_set, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("EquipmentInstantiateNNamedTemplate")
    method.cookie = cookie
    method.dn = dn
    method.in_error_on_existing = in_error_on_existing
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_name_set = in_name_set
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def equipment_instantiate_n_template(cookie, dn, in_chassis_profile_name_prefix_or_empty, in_number_of, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("EquipmentInstantiateNTemplate")
    method.cookie = cookie
    method.dn = dn
    method.in_chassis_profile_name_prefix_or_empty = in_chassis_profile_name_prefix_or_empty
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_number_of = str(in_number_of)
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def equipment_instantiate_template(cookie, dn, in_chassis_profile_name, in_error_on_existing, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("EquipmentInstantiateTemplate")
    method.cookie = cookie
    method.dn = dn
    method.in_chassis_profile_name = in_chassis_profile_name
    method.in_error_on_existing = in_error_on_existing
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def equipment_resolve_templates(cookie, dn, in_exclude_if_bound, in_filter, in_type, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("EquipmentResolveTemplates")
    method.cookie = cookie
    method.dn = dn
    method.in_exclude_if_bound = in_exclude_if_bound
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_type = in_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def equipment_templatise(cookie, dn, in_target_org, in_template_name, in_template_type, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("EquipmentTemplatise")
    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_target_org = in_target_org
    method.in_template_name = in_template_name
    method.in_template_type = in_template_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def event_register_event_channel(cookie, in_dn):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("EventRegisterEventChannel")
    method.cookie = cookie
    method.in_dn = in_dn

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def event_register_event_channel_resp(cookie, in_ctx, in_dn, in_req_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("EventRegisterEventChannelResp")
    method.cookie = cookie
    method.in_ctx = in_ctx
    method.in_dn = in_dn
    method.in_req_id = str(in_req_id)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def event_send_event(cookie, in_dn, in_event, in_req_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("EventSendEvent")
    method.cookie = cookie
    method.in_dn = in_dn
    method.in_event = in_event
    method.in_req_id = str(in_req_id)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def event_send_heartbeat(cookie):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("EventSendHeartbeat")
    method.cookie = cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def event_subscribe(cookie, in_filter):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("EventSubscribe")
    method.cookie = cookie
    method.in_filter = in_filter

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def event_un_register_event_channel(cookie, in_dn, in_req_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("EventUnRegisterEventChannel")
    method.cookie = cookie
    method.in_dn = in_dn
    method.in_req_id = str(in_req_id)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def event_unsubscribe(cookie):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("EventUnsubscribe")
    method.cookie = cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def fault_ack_fault(cookie, in_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("FaultAckFault")
    method.cookie = cookie
    method.in_id = str(in_id)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def fault_ack_faults(cookie, in_ids):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("FaultAckFaults")
    method.cookie = cookie
    method.in_ids = in_ids

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def fault_resolve_fault(cookie, in_id):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("FaultResolveFault")
    method.cookie = cookie
    method.in_id = str(in_id)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def fsm_debug_action(cookie, dn, in_directive):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("FsmDebugAction")
    method.cookie = cookie
    method.dn = dn
    method.in_directive = in_directive

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def logging_sync_ocns(cookie, in_from_or_zero, in_to_or_zero):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("LoggingSyncOcns")
    method.cookie = cookie
    method.in_from_or_zero = str(in_from_or_zero)
    method.in_to_or_zero = str(in_to_or_zero)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ls_clone(cookie, dn, in_server_name, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("LsClone")
    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_server_name = in_server_name
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ls_instantiate_n_named_template(cookie, dn, in_error_on_existing, in_name_set, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("LsInstantiateNNamedTemplate")
    method.cookie = cookie
    method.dn = dn
    method.in_error_on_existing = in_error_on_existing
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_name_set = in_name_set
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ls_instantiate_n_template(cookie, dn, in_number_of, in_server_name_prefix_or_empty, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("LsInstantiateNTemplate")
    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_number_of = str(in_number_of)
    method.in_server_name_prefix_or_empty = in_server_name_prefix_or_empty
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ls_instantiate_template(cookie, dn, in_error_on_existing, in_server_name, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("LsInstantiateTemplate")
    method.cookie = cookie
    method.dn = dn
    method.in_error_on_existing = in_error_on_existing
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_server_name = in_server_name
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ls_resolve_templates(cookie, dn, in_exclude_if_bound, in_filter, in_type, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("LsResolveTemplates")
    method.cookie = cookie
    method.dn = dn
    method.in_exclude_if_bound = in_exclude_if_bound
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_type = in_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ls_templatise(cookie, dn, in_target_org, in_template_name, in_template_type, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("LsTemplatise")
    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_target_org = in_target_org
    method.in_template_name = in_template_name
    method.in_template_type = in_template_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def lstorage_create_zoning_from_inv(cookie, in_chassis_dn, in_disk_zoning_policy_name, in_target_org):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("LstorageCreateZoningFromInv")
    method.cookie = cookie
    method.in_chassis_dn = in_chassis_dn
    method.in_disk_zoning_policy_name = in_disk_zoning_policy_name
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def method_resolve_vessel(cookie, in_stimuli):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("MethodResolveVessel")
    method.cookie = cookie
    method.in_stimuli = in_stimuli

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def method_vessel(cookie, in_stimuli):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("MethodVessel")
    method.cookie = cookie
    method.in_stimuli = in_stimuli

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def mgmt_resolve_backup_filenames(cookie, in_backup_source, in_type):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("MgmtResolveBackupFilenames")
    method.cookie = cookie
    method.in_backup_source = in_backup_source
    method.in_type = in_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def org_resolve_elements(cookie, dn, in_class, in_filter, in_single_level, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("OrgResolveElements")
    method.cookie = cookie
    method.dn = dn
    method.in_class = in_class
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_single_level = in_single_level

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def org_resolve_logical_parents(cookie, dn, in_single_level, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("OrgResolveLogicalParents")
    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_single_level = in_single_level

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def policy_resolve_names(cookie, in_client_connector_dn, in_context, in_filter, in_policy_type):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("PolicyResolveNames")
    method.cookie = cookie
    method.in_client_connector_dn = in_client_connector_dn
    method.in_context = in_context
    method.in_filter = in_filter
    method.in_policy_type = in_policy_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def policy_set_centrale_storage(cookie, in_data, in_oper, in_side):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("PolicySetCentraleStorage")
    method.cookie = cookie
    method.in_data = in_data
    method.in_oper = str(in_oper)
    method.in_side = in_side

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def pool_resolve_in_scope(cookie, dn, in_class, in_filter, in_single_level, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("PoolResolveInScope")
    method.cookie = cookie
    method.dn = dn
    method.in_class = in_class
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucsgenutils.AFFIRMATIVE_LIST])
    method.in_single_level = in_single_level

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def stats_clear_interval(cookie, in_dns):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("StatsClearInterval")
    method.cookie = cookie
    method.in_dns = in_dns

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def stats_resolve_threshold_policy(cookie, dn):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("StatsResolveThresholdPolicy")
    method.cookie = cookie
    method.dn = dn

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def stats_subscribe(cookie, in_category, in_provider, in_schema_info, in_time_interval):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("StatsSubscribe")
    method.cookie = cookie
    method.in_category = in_category
    method.in_provider = in_provider
    method.in_schema_info = in_schema_info
    method.in_time_interval = in_time_interval

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def swat_example(cookie, in_config):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("SwatExample")
    method.cookie = cookie
    method.in_config = in_config

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def swat_getstats(cookie):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("SwatGetstats")
    method.cookie = cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def swat_inject(cookie, in_config):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("SwatInject")
    method.cookie = cookie
    method.in_config = in_config

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def synthetic_fs_obj_inventory(cookie, dn, in_config):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("SyntheticFSObjInventory")
    method.cookie = cookie
    method.dn = dn
    method.in_config = in_config

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def synthetic_fs_obj_inventory_b(cookie, in_config):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("SyntheticFSObjInventoryB")
    method.cookie = cookie
    method.in_config = in_config

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def synthetic_test_tx(cookie, in_config, in_test, in_what):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("SyntheticTestTx")
    method.cookie = cookie
    method.in_config = in_config
    method.in_test = in_test
    method.in_what = in_what

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def trig_perform_token_action(cookie, in_context, in_ownership, in_sched_name, in_token_action, in_token_id, in_triggerable_dn, in_window_name, in_window_type):
    """ Auto-generated UCS XML API Method. """
    method = ExternalMethod("TrigPerformTokenAction")
    method.cookie = cookie
    method.in_context = in_context
    method.in_ownership = in_ownership
    method.in_sched_name = in_sched_name
    method.in_token_action = in_token_action
    method.in_token_id = str(in_token_id)
    method.in_triggerable_dn = in_triggerable_dn
    method.in_window_name = in_window_name
    method.in_window_type = in_window_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request
