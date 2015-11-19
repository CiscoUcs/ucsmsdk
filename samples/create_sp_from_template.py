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

from connection.info import ucs_login, ucs_logout

handle = None


def create_sp_from_template():
    import ucsmsdk.ucsmethodfactory as mf
    from ucsmsdk.ucsbasetype import DnSet, Dn

    dn_set = DnSet()
    dn_set.child_add(Dn(value="sp_from_template1"))
    dn_set.child_add(Dn(value="sp_from_template2"))
    xml_element = mf.ls_instantiate_n_named_template(
        cookie=handle.cookie,
        dn="org-root/ls-test_sp_template",
        in_error_on_existing="true",
        in_name_set=dn_set,
        in_target_org="org-root",
        in_hierarchical="YesOrNo.FALSE")
    mo_list = handle.process_xml_element(xml_element)

    return mo_list


def delete_sp_created_from_template():
    obj = handle.query_dn("org-root/ls-sp_from_template2")
    handle.remove_mo(obj)

    obj = handle.query_dn("org-root/ls-sp_from_template1")
    handle.remove_mo(obj)

    handle.commit()


def main():
    try:
        global handle
        handle = ucs_login()
        # ###########################################
        # Create the SP from template
        # ###########################################
        mo_list = create_sp_from_template()
        if mo_list:
            for mo in mo_list:
                print mo.dn

        # ###########################################
        # Delete_sp_created_from_template
        # ###########################################
        delete_sp_created_from_template()

        ucs_logout(handle)

    except:
        ucs_logout(handle)
        raise

main()
