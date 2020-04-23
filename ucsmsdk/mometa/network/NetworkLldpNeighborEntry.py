"""This module contains the general information for NetworkLldpNeighborEntry ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class NetworkLldpNeighborEntryConsts:
    pass


class NetworkLldpNeighborEntry(ManagedObject):
    """This is NetworkLldpNeighborEntry class."""

    consts = NetworkLldpNeighborEntryConsts()
    naming_props = set(['localInterface'])

    mo_meta = MoMeta("NetworkLldpNeighborEntry", "networkLldpNeighborEntry", "if-[local_interface]", VersionMeta.Version224b, "InputOutput", 0x3f, [], ["read-only"], ['networkLldpNeighbors'], [], ["Get"])

    prop_meta = {
        "capabilities": MoPropertyMeta("capabilities", "capabilities", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "enabled_capabilities": MoPropertyMeta("enabled_capabilities", "enabledCapabilities", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "fi_port_dn": MoPropertyMeta("fi_port_dn", "fiPortDn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "ip_v4_mgmt_address": MoPropertyMeta("ip_v4_mgmt_address", "ipV4MgmtAddress", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "local_interface": MoPropertyMeta("local_interface", "localInterface", "string", VersionMeta.Version224b, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "native_vlan": MoPropertyMeta("native_vlan", "nativeVlan", "ushort", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "remote_if_desc": MoPropertyMeta("remote_if_desc", "remoteIfDesc", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "remote_interface": MoPropertyMeta("remote_interface", "remoteInterface", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "system_desc": MoPropertyMeta("system_desc", "systemDesc", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "system_name": MoPropertyMeta("system_name", "systemName", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "capabilities": "capabilities", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "enabledCapabilities": "enabled_capabilities", 
        "fiPortDn": "fi_port_dn", 
        "ipV4MgmtAddress": "ip_v4_mgmt_address", 
        "localInterface": "local_interface", 
        "nativeVlan": "native_vlan", 
        "remoteIfDesc": "remote_if_desc", 
        "remoteInterface": "remote_interface", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "systemDesc": "system_desc", 
        "systemName": "system_name", 
    }

    def __init__(self, parent_mo_or_dn, local_interface, **kwargs):
        self._dirty_mask = 0
        self.local_interface = local_interface
        self.capabilities = None
        self.chassis_id = None
        self.child_action = None
        self.enabled_capabilities = None
        self.fi_port_dn = None
        self.ip_v4_mgmt_address = None
        self.native_vlan = None
        self.remote_if_desc = None
        self.remote_interface = None
        self.sacl = None
        self.status = None
        self.system_desc = None
        self.system_name = None

        ManagedObject.__init__(self, "NetworkLldpNeighborEntry", parent_mo_or_dn, **kwargs)
