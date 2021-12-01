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

import unittest


class TestUCSValidateMethod(unittest.TestCase):
    def test_001_fabricvlan_id_100(self):
        # type: uint
        # range: ["1-3967", "1-4029", "4048-4091", "4048-4093"]
        from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

        vlan = FabricVlan(parent_mo_or_dn="parent_dn", name="my_vlan")
        vlan.id = 100

    def test_002_fabricvlan_id_4000(self):
        # type: uint
        # range: ["1-3967", "1-4029", "4048-4091", "4048-4093"]
        from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

        vlan = FabricVlan(parent_mo_or_dn="parent_dn", name="my_vlan")
        vlan.id = 4000

    def test_003_fabricvlan_id_5000(self):
        # type: uint
        # range: ["1-3967", "1-4029", "4048-4091", "4048-4093"]
        from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

        with self.assertRaises(Exception):
            vlan = FabricVlan(parent_mo_or_dn="parent_dn", name="my_vlan")
            vlan.id = 5000

    def test_004_equipmentPOST_globalid(self):
        import ucsmsdk.ucsxmlcodec as xc

        xml_str = '''
        <equipmentPOST childAction="deleteNonPresent" code="POST-2298"

        created="2015-10-27T08:13:03.068" descr="No Errors" globalId="2298"
        localId="No Errors" method="POST" name="" recoverable="recoverable"
        recoveryAction="none" rn="code-2298" severity="info"
        type="adaptor: Cisco Systems Inc N20-AC0002" value="0"/>
        '''

        xc.from_xml_str(xml_str)
