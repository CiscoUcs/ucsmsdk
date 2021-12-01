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


class TestQueryChildren(BaseTest):
    def setUp(self):
        super().setUp()
        self.sp_list = []
        from ucsmsdk.mometa.ls.LsServer import LsServer
        org = handle.query_dn("org-root")

        sp_TEST = LsServer(org, name="TEST", usr_lbl="TEST")
        self.handle.add_mo(sp_TEST, True)
        self.sp_list.append(sp_TEST)

        sp_test = LsServer(org, name="test", usr_lbl="test", descr="test")
        self.handle.add_mo(sp_test, True)
        self.sp_list.append(sp_test)

        sp_test11 = LsServer(org, name="test11", usr_lbl="test11")
        self.handle.add_mo(sp_test11, True)
        self.sp_list.append(sp_test11)

        sp_test12 = LsServer(org, name="test12", usr_lbl="test12")
        self.handle.add_mo(sp_test12, True)
        self.sp_list.append(sp_test12)

        self.handle.commit()

    def tearDown(self):
        for sp in self.sp_list:
            self.handle.remove_mo(sp)
        self.handle.commit()
        super().tearDown()

    def test_default_filter(self):
        mos = handle.query_children(in_dn="org-root", class_id="LsServer",
                                    filter_str="(usr_lbl, 'test')")
        self.assertEqual(len(mos), 3)

    def test_default_case_insensitive(self):
        mos = handle.query_children(in_dn="org-root", class_id="LsServer",
                                    filter_str="(usr_lbl, 'test', flag='I')")
        self.assertEqual(len(mos), 4)

    def test_type_eq(self):
        mos = handle.query_children(in_dn="org-root", class_id="LsServer",
                                    filter_str="(usr_lbl, 'test', type='eq')")
        self.assertEqual(len(mos), 1)

    def test_type_eq_prop_without_underscore(self):
        mos = handle.query_children(in_dn="org-root", class_id="LsServer",
                                    filter_str="(descr, 'test', type='eq')")
        self.assertEqual(len(mos), 1)

    def test_type_re(self):
        filter_ = "(usr_lbl, 'test.*1.*', type='re')"
        mos = handle.query_children(in_dn="org-root", class_id="LsServer",
                                    filter_str=filter_)
        self.assertEqual(len(mos), 2)
