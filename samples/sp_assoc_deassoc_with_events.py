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

import logging
import time
from ucsmsdk.ucseventhandler import UcsEventHandle
from ucsmsdk.mometa.ls.LsServer import LsServerConsts
from connection.info import ucs_login, ucs_logout

handle = None
end_script = False
assoc_done = False
ucs_event_handler = None

log = logging.getLogger('ucs')
log.setLevel(logging.DEBUG)

blade_dn = "sys/chassis-1/blade-2"


def sp_create():
    # ###########################################
    # Create the SP that will be associated later
    # ###########################################
    log.debug("sp_create")
    from ucsmsdk.mometa.ls.LsServer import LsServer
    from ucsmsdk.mometa.lsboot.LsbootDef import LsbootDef
    from ucsmsdk.mometa.lsboot.LsbootStorage import LsbootStorage
    from ucsmsdk.mometa.lsboot.LsbootLocalStorage import LsbootLocalStorage
    from ucsmsdk.mometa.lsboot.LsbootDefaultLocalImage import\
        LsbootDefaultLocalImage
    from ucsmsdk.mometa.vnic.VnicEther import VnicEther
    from ucsmsdk.mometa.vnic.VnicEtherIf import VnicEtherIf
    from ucsmsdk.mometa.vnic.VnicFcNode import VnicFcNode

    mo = LsServer(parent_mo_or_dn="org-root", vmedia_policy_name="",
                  ext_ip_state="none", bios_profile_name="",
                  mgmt_fw_policy_name="", agent_policy_name="",
                  mgmt_access_policy_name="", dynamic_con_policy_name="",
                  kvm_mgmt_policy_name="", sol_policy_name="", uuid="0",
                  descr="", stats_policy_name="default", policy_owner="local",
                  ext_ip_pool_name="ext-mgmt", boot_policy_name="", usr_lbl="",
                  host_fw_policy_name="", vcon_profile_name="",
                  ident_pool_name="", src_templ_name="",
                  local_disk_policy_name="", scrub_policy_name="",
                  power_policy_name="default", maint_policy_name="",
                  name="test_sp", resolve_remote="yes")
    mo_1 = LsbootDef(parent_mo_or_dn=mo, descr="", reboot_on_update="no",
                     adv_boot_order_applicable="no", policy_owner="local",
                     enforce_vnic_name="yes", boot_mode="legacy")
    mo_1_1 = LsbootStorage(parent_mo_or_dn=mo_1, order="1")
    mo_1_1_1 = LsbootLocalStorage(parent_mo_or_dn=mo_1_1, )
    mo_1_1_1_1 = LsbootDefaultLocalImage(parent_mo_or_dn=mo_1_1_1, order="1")
    mo_2 = VnicEther(parent_mo_or_dn=mo, nw_ctrl_policy_name="", name="eth0",
                     admin_host_port="ANY", admin_vcon="any",
                     stats_policy_name="default", admin_cdn_name="",
                     switch_id="A", pin_to_group_name="", mtu="1500",
                     qos_policy_name="", adaptor_profile_name="",
                     ident_pool_name="", order="unspecified", nw_templ_name="",
                     addr="derived")
    mo_2_1 = VnicEtherIf(parent_mo_or_dn=mo_2, default_net="yes",
                         name="default")
    mo_3 = VnicFcNode(parent_mo_or_dn=mo, ident_pool_name="",
                      addr="pool-derived")
    handle.add_mo(mo)
    handle.commit()


def sp_assoc_wait(mo):
    # ###########################################
    # Create a Event handler to monitor sp assoc
    # ###########################################
    log.debug("sp_assoc_wait")
    ucs_event_handler.add(
                managed_object=mo,
                prop="assoc_state",
                success_value=[LsServerConsts.ASSOC_STATE_ASSOCIATED],
                failure_value=[LsServerConsts.ASSOC_STATE_FAILED],
                timeout_sec=600,
                call_back=sp_assoc_wait_done_cb)


def sp_assoc_wait_done_cb(mce):
    log.debug("sp_assoc_wait_done_cb")
    log.debug("SP:" + mce.mo.dn + " Assoc Done Callback. assoc_state: " +
              mce.mo.assoc_state)
    if mce.mo.assoc_state == LsServerConsts.ASSOC_STATE_ASSOCIATED:
        sp_deassoc()


def sp_deassoc_wait(mo):
    # ###########################################
    # Create a Event handler to monitor sp assoc
    # ###########################################
    log.debug("sp_deassoc_wait")
    ucs_event_handler.add(
                managed_object=mo,
                prop="assoc_state",
                success_value=[LsServerConsts.ASSOC_STATE_UNASSOCIATED],
                failure_value=[LsServerConsts.ASSOC_STATE_FAILED],
                timeout_sec=600,
                call_back=sp_deassoc_wait_done_cb)


def sp_deassoc_wait_done_cb(mce):
    log.debug("sp_deassoc_wait_done_cb")
    log.debug("SP:" + mce.mo.dn + " Deassoc Done Callback. assoc_state: " +
              mce.mo.assoc_state)
    if mce.mo.assoc_state == LsServerConsts.ASSOC_STATE_UNASSOCIATED:
        blade_wait_for_availability()


def blade_wait_for_availability_done_cb(mce):
    log.debug("blade_wait_for_availability_done_cb")
    if mce.mo.availability == 'available':
        sp_delete()
    ucs_logout(handle)
    global end_script
    end_script = True


def blade_wait_for_availability():
    log.debug("blade_wait_for_availability")
    mo = handle.query_dn(blade_dn)
    ucs_event_handler.add(
                managed_object=mo,
                prop="availability",
                success_value=['available'],
                timeout_sec=600,
                poll_sec=10,
                call_back=blade_wait_for_availability_done_cb)


def sp_assoc():
    # ###########################################
    # associate the SP to a blade
    # ###########################################
    log.debug("sp_assoc")
    from ucsmsdk.mometa.ls.LsBinding import LsBinding
    mo = LsBinding(parent_mo_or_dn="org-root/ls-test_sp",
                   pn_dn=blade_dn, restrict_migration="no")
    handle.add_mo(mo)
    handle.commit()

    # ###########################################
    # add a handler to watch for sp assoc
    # ###########################################
    mo = handle.query_dn("org-root/ls-test_sp")
    sp_assoc_wait(mo)


def sp_deassoc():
    # ###########################################
    # add a handler to watch for sp assoc
    # ###########################################
    mo = handle.query_dn("org-root/ls-test_sp")
    sp_deassoc_wait(mo)

    # ###########################################
    # deassociate the SP
    # ###########################################
    log.debug("sp_deassoc")
    obj = handle.query_dn("org-root/ls-test_sp/pn")
    handle.remove_mo(obj)
    handle.commit()


def sp_delete():
    # ###########################################
    # delete the SP
    # ###########################################
    log.debug("sp_delete")
    obj = handle.query_dn("org-root/ls-test_sp")
    handle.remove_mo(obj)
    handle.commit()


def main():
    global handle
    global ucs_event_handler
    global assoc_done

    handle = ucs_login()
    ucs_event_handler = UcsEventHandle(handle)

    sp_create()
    sp_assoc()

    # Wait for the background processing to complete.
    # quit when end_script flag is set to True
    while not end_script:
        time.sleep(1)

main()
