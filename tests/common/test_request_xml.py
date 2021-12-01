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


class TestRequestXML(BaseTest):
    def setUp(self):
        super().setUp()
        self.to_commit = {}

    def commit(self):
        from ucsmsdk.ucsbasetype import ConfigMap, Dn, DnSet, Pair
        import ucsmsdk.ucsmethodfactory as mf
        import ucsmsdk.ucsxmlcodec as xc

        refresh_dict = {}
        mo_dict = self.to_commit
        if not mo_dict:
            print("No Mo to be Committed")
            return None

        config_map = ConfigMap()
        for mo_dn in mo_dict:
            mo = mo_dict[mo_dn]
            child_list = mo.child
            while len(child_list) > 0:
                current_child_list = child_list
                child_list = []
                for child_mo in current_child_list:
                    if child_mo.is_dirty():
                        refresh_dict[child_mo.dn] = child_mo
                    child_list.extend(child_mo.child)

            pair = Pair()
            pair.key = mo_dn
            pair.child_add(mo_dict[mo_dn])
            config_map.child_add(pair)

        xml_element = mf.config_conf_mos("cookie", config_map, False)
        xml_str = xc.to_xml_str(xml_element)
        self.to_commit = {}
        return xml_str

    def add_mo(self, mo, modify_present=False):
        import ucsmsdk.ucsgenutils as ucsgenutils

        if modify_present in ucsgenutils.AFFIRMATIVE_LIST:
            mo.status = "created,modified"
        else:
            mo.status = "created"

        self.to_commit[mo.dn] = mo

    def set_mo(self, mo):
        if mo.is_dirty():
            mo.status = "modified"
            self.to_commit[mo.dn] = mo
        else:
            print("Nothing Modified")

    def test_001_add_sp(self):
        from ucsmsdk.mometa.ls.LsServer import LsServer
        sp = LsServer(parent_mo_or_dn="org-root", name="test_sp")
        self.add_mo(mo=sp)
        xml_str = self.commit()
        print(xml_str)

        expected = b'''<configConfMos cookie="cookie" inHierarchical="false"><inConfigs><pair key="org-root/ls-test_sp"><lsServer dn="org-root/ls-test_sp" name="test_sp" status="created" /></pair></inConfigs></configConfMos>'''
        self.assertEqual(xml_str, expected)

    def test_002_add_hierarchy(self):
        from ucsmsdk.mometa.org.OrgOrg import OrgOrg
        from ucsmsdk.mometa.ls.LsServer import LsServer

        org = OrgOrg(parent_mo_or_dn="org-root", name="test_org")
        sp = LsServer(parent_mo_or_dn=org, name="test_sp")
        self.add_mo(mo=org)
        xml_str = self.commit()
        print(xml_str)

        expected = b'''<configConfMos cookie="cookie" inHierarchical="false"><inConfigs><pair key="org-root/org-test_org"><orgOrg dn="org-root/org-test_org" name="test_org" status="created"><lsServer dn="org-root/org-test_org/ls-test_sp" name="test_sp" /></orgOrg></pair></inConfigs></configConfMos>'''
        self.assertEqual(xml_str, expected)

    def test_003_get_then_set_sp(self):
        from ucsmsdk.mometa.ls.LsServer import LsServer

        sp = LsServer(parent_mo_or_dn="org-root", name="test_sp")
        self.handle.add_mo(sp)
        self.handle.commit()

        test_sp = self.handle.query_dn("org-root/ls-test_sp")
        test_sp.descr = "change"
        self.set_mo(test_sp)
        xml_str = self.commit()
        print(xml_str)

        self.handle.remove_mo(sp)
        self.handle.commit()

        expected = b'''<configConfMos cookie="cookie" inHierarchical="false"><inConfigs><pair key="org-root/ls-test_sp"><lsServer descr="change" dn="org-root/ls-test_sp" status="modified" /></pair></inConfigs></configConfMos>'''
        self.assertEqual(xml_str, expected)

    def test_004_get_org_and_add_sp_add_mo_sp(self):
        from ucsmsdk.mometa.ls.LsServer import LsServer

        org = self.handle.query_dn("org-root")
        sp = LsServer(parent_mo_or_dn=org, name="test_sp")

        self.add_mo(sp)
        xml_str = self.commit()
        print(xml_str)

        expected = b'''<configConfMos cookie="cookie" inHierarchical="false"><inConfigs><pair key="org-root/ls-test_sp"><lsServer dn="org-root/ls-test_sp" name="test_sp" status="created" /></pair></inConfigs></configConfMos>'''
        self.assertEqual(xml_str, expected)

    def test_005_get_org_and_add_sp_set_mo_org(self):
        from ucsmsdk.mometa.ls.LsServer import LsServer

        org = self.handle.query_dn("org-root")
        sp = LsServer(parent_mo_or_dn=org, name="test_sp")

        self.set_mo(org)
        xml_str = self.commit()
        print(xml_str)

        expected = b'''<configConfMos cookie="cookie" inHierarchical="false"><inConfigs><pair key="org-root"><orgOrg dn="org-root" status="modified"><lsServer dn="org-root/ls-test_sp" name="test_sp" /></orgOrg></pair></inConfigs></configConfMos>'''
        self.assertEqual(xml_str, expected)
