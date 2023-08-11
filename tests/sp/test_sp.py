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

from tests.base import BaseTest


class TestSp(BaseTest):
    def test_001_sp_minimal(self):
        from ucsmsdk.mometa.ls.LsServer import LsServer
        mo = LsServer(parent_mo_or_dn="org-root", vmedia_policy_name="",
                      ext_ip_state="none", bios_profile_name="",
                      mgmt_fw_policy_name="", agent_policy_name="",
                      mgmt_access_policy_name="", dynamic_con_policy_name="",
                      kvm_mgmt_policy_name="", sol_policy_name="", uuid="0",
                      descr="", stats_policy_name="default",
                      policy_owner="local", ext_ip_pool_name="ext-mgmt",
                      boot_policy_name="", usr_lbl="", host_fw_policy_name="",
                      vcon_profile_name="", ident_pool_name="default",
                      src_templ_name="", local_disk_policy_name="",
                      scrub_policy_name="", power_policy_name="default",
                      maint_policy_name="", name="test_sp",
                      resolve_remote="yes")

        self.handle.add_mo(mo)
        self.handle.commit()

        ##########################################################
        # Modify a single property in the Sp created above
        # and genertate XML with DIRTY option set
        ##########################################################
        import ucsmsdk.ucsxmlcodec as xc
        from ucsmsdk.ucscoremeta import WriteXmlOption
        obj = handle.query_dn("org-root/ls-test_sp")
        obj.usr_lbl = "new_label"
        print(xc.to_xml_str(obj.to_xml(option=WriteXmlOption.DIRTY)))
        print(xc.to_xml_str(obj.to_xml(option=WriteXmlOption.ALL_CONFIG)))
        print(xc.to_xml_str(obj.to_xml()))

        ##########################################################
        # Delete the SP
        ##########################################################
        obj = self.handle.query_dn("org-root/ls-test_sp")
        self.handle.remove_mo(obj)
        self.handle.commit()

    def test_002_sp_expert(self):
        '''
            This case is generated based on SP expert mode creation wizard.
        '''
        from ucsmsdk.mometa.ls.LsServer import LsServer
        from ucsmsdk.mometa.ls.LsVConAssign import LsVConAssign
        from ucsmsdk.mometa.vnic.VnicEther import VnicEther
        from ucsmsdk.mometa.vnic.VnicEtherIf import VnicEtherIf
        from ucsmsdk.mometa.vnic.VnicFc import VnicFc
        from ucsmsdk.mometa.vnic.VnicFcIf import VnicFcIf
        from ucsmsdk.mometa.vnic.VnicFcNode import VnicFcNode
        from ucsmsdk.mometa.storage.StorageIniGroup import StorageIniGroup
        from ucsmsdk.mometa.vnic.VnicFcGroupDef import VnicFcGroupDef
        from ucsmsdk.mometa.storage.StorageInitiator import StorageInitiator
        from ucsmsdk.mometa.ls.LsPower import LsPower
        from ucsmsdk.mometa.fabric.FabricVCon import FabricVCon

        mo = LsServer(parent_mo_or_dn="org-root", vmedia_policy_name="",
                      ext_ip_state="none", bios_profile_name="SRIOV",
                      mgmt_fw_policy_name="", agent_policy_name="",
                      mgmt_access_policy_name="", dynamic_con_policy_name="",
                      kvm_mgmt_policy_name="", sol_policy_name="",
                      uuid="00000000-0000-0000-0000-0000000000bb", descr="",
                      stats_policy_name="default", policy_owner="local",
                      ext_ip_pool_name="ext-mgmt", boot_policy_name="default",
                      usr_lbl="", host_fw_policy_name="", vcon_profile_name="",
                      ident_pool_name="", src_templ_name="",
                      local_disk_policy_name="default", scrub_policy_name="",
                      power_policy_name="default", maint_policy_name="",
                      name="test_sp", resolve_remote="yes")
        mo_1 = LsVConAssign(parent_mo_or_dn=mo, admin_vcon="any", order="1",
                            transport="ethernet", vnic_name="eth0")
        mo_2 = LsVConAssign(parent_mo_or_dn=mo, admin_vcon="any", order="2",
                            transport="fc", vnic_name="fc0")
        mo_3 = VnicEther(parent_mo_or_dn=mo, nw_ctrl_policy_name="",
                         name="eth0", admin_host_port="ANY", admin_vcon="any",
                         stats_policy_name="default", admin_cdn_name="",
                         switch_id="A", pin_to_group_name="", mtu="1500",
                         qos_policy_name="", adaptor_profile_name="",
                         ident_pool_name="default", order="1",
                         nw_templ_name="", addr="derived")
        mo_3_1 = VnicEtherIf(parent_mo_or_dn=mo_3, default_net="yes",
                             name="default")
        mo_4 = VnicFc(parent_mo_or_dn=mo, addr="derived", name="fc0",
                      admin_host_port="ANY", admin_vcon="any",
                      stats_policy_name="default", admin_cdn_name="",
                      switch_id="A", pin_to_group_name="", pers_bind="disabled",
                      pers_bind_clear="no", qos_policy_name="",
                      adaptor_profile_name="", ident_pool_name="", order="2",
                      nw_templ_name="", max_data_field_size="2048")
        mo_4_1 = VnicFcIf(parent_mo_or_dn=mo_4, name="default")
        mo_5 = VnicFcNode(parent_mo_or_dn=mo, ident_pool_name="",
                          addr="20:00:00:25:B5:00:00:00")
        mo_6 = StorageIniGroup(parent_mo_or_dn=mo, name="test", descr="",
                               group_policy_name="", policy_name="",
                               policy_owner="local", rmt_disk_cfg_name="")
        mo_6_1 = VnicFcGroupDef(parent_mo_or_dn=mo_6,
                                storage_conn_policy_name="",
                                policy_owner="local", name="", descr="",
                                stats_policy_name="default")
        mo_6_2 = StorageInitiator(parent_mo_or_dn=mo_6, policy_owner="local",
                                  name="fc0", descr="")
        mo_7 = LsPower(parent_mo_or_dn=mo, state="admin-up")
        mo_8 = FabricVCon(parent_mo_or_dn=mo, placement="physical",
                          fabric="NONE", share="shared", select="all",
                          transport="ethernet,fc", id="1", inst_type="auto")
        mo_9 = FabricVCon(parent_mo_or_dn=mo, placement="physical",
                          fabric="NONE", share="shared", select="all",
                          transport="ethernet,fc", id="2", inst_type="auto")
        mo_10 = FabricVCon(parent_mo_or_dn=mo, placement="physical",
                           fabric="NONE", share="shared", select="all",
                           transport="ethernet,fc", id="3", inst_type="auto")
        mo_11 = FabricVCon(parent_mo_or_dn=mo, placement="physical",
                           fabric="NONE", share="shared", select="all",
                           transport="ethernet,fc", id="4", inst_type="auto")
        self.handle.add_mo(mo)
        self.handle.commit()

        obj = self.handle.query_dn("org-root/ls-test_sp")
        self.handle.remove_mo(obj)
        self.handle.commit()
