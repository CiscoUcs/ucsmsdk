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


class TestUCSProposal(BaseTest):
    def setUp(self):
        super().setUp()
        from ucsmsdk.mometa.ls.LsServer import LsServer
        self.obj = LsServer("org-root", "test", usr_lbl="sample")

        self.handle.add_mo(obj, True)
        self.handle.commit()

    def tearDown(self):
        if self.handle:
            self.handle.remove_mo(self.obj)
            self.handle.commit()
        super().tearDown()

    def test_001_set_ro_property(self):
        # This is a read only property
        # Should fail with an exception
        with self.assertRaises(Exception):
            self.obj.oper_state = "up"

    def test_002_set_rw_property(self):
        # This is a read write property.
        # Should happen without any issues
        self.obj.descr = "test_description"

    def test_003_set_naming_property(self):
        # This is a naming property. so, it is create only
        # Should fail with an exception
        with self.assertRaises(Exception):
            self.obj.name = "test1"

    def test_004_check_existing_prop_match(self):
        # Checking property aginst existing property
        self.assertTrue(self.obj.check_prop_match(usr_lbl="sample"))

    def test_005_check_nonexisting_prop_match(self):
        # Checking property aginst non-existing property
        with self.assertRaises(Exception):
            self.assertTrue(self.obj.check_prop_match(usr_lbl="new_label"))

    def test_006_set_prop_multiple(self):
        # Setting multiple property of object
        self.obj.set_prop_multiple(usr_lbl="new_label",
                              vmedia_policy_name="test_vmedia_pol")
        self.handle.set_mo(obj)
        self.handle.commit()

        new_obj = self.handle.query_dn(obj.dn)
        self.assertEqual(new_obj.usr_lbl, "new_label")
        self.assertEqual(new_obj.vmedia_policy_name, "test_vmedia_pol")
