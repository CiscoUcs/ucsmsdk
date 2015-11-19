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

from nose.tools import with_setup
from ..connection.info import custom_setup, custom_teardown

handle = None


def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)


def create_vlan_global(vlan_id):
    from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

    mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name=vlan_id,
                    id=vlan_id, mcast_policy_name="", policy_owner="local",
                    default_net="no", pub_nw_name="",
                    compression_type="included")
    handle.add_mo(mo)
    handle.commit()


def delete_vlan_global(vlan_id):
    obj = handle.query_dn("fabric/lan/net-" + vlan_id)
    handle.remove_mo(obj)
    handle.commit()


@with_setup(setup, teardown)
def test_001_create_modify_vlan():
    create_vlan_global("100")

    obj = handle.query_dn("fabric/lan/net-100")
    obj.id = "101"
    handle.set_mo(obj)
    handle.commit()

    delete_vlan_global("100")
