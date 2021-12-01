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


class TestVLan(BaseTest):
    def create_vlan_global(self, vlan_id):
        from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

        mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none",
                        name=vlan_id, id=vlan_id, mcast_policy_name="",
                        policy_owner="local", default_net="no",
                        pub_nw_name="", compression_type="included")
        self.handle.add_mo(mo)
        self.handle.commit()

    def delete_vlan_global(self, vlan_id):
        obj = self.handle.query_dn("fabric/lan/net-" + vlan_id)
        self.handle.remove_mo(obj)
        self.handle.commit()

    def test_001_create_modify_vlan(self):
        self.create_vlan_global("100")

        obj = self.handle.query_dn("fabric/lan/net-100")
        obj.id = "101"
        self.handle.set_mo(obj)
        self.handle.commit()

        self.delete_vlan_global("100")
