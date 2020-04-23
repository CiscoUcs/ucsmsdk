"""This module contains the general information for NetworkLanNeighborEntry ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class NetworkLanNeighborEntryConsts:
    pass


class NetworkLanNeighborEntry(ManagedObject):
    """This is NetworkLanNeighborEntry class."""

    consts = NetworkLanNeighborEntryConsts()
    naming_props = set(['localInterface'])

    mo_meta = MoMeta("NetworkLanNeighborEntry", "networkLanNeighborEntry", "if-[local_interface]", VersionMeta.Version223a, "InputOutput", 0x3f, [], ["read-only"], ['networkLanNeighbors'], [], ["Get"])

    prop_meta = {
        "capabilities": MoPropertyMeta("capabilities", "capabilities", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "device_id": MoPropertyMeta("device_id", "deviceId", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "fi_port_dn": MoPropertyMeta("fi_port_dn", "fiPortDn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "ip_v4_address": MoPropertyMeta("ip_v4_address", "ipV4Address", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "ip_v4_mgmt_address": MoPropertyMeta("ip_v4_mgmt_address", "ipV4MgmtAddress", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "local_interface": MoPropertyMeta("local_interface", "localInterface", "string", VersionMeta.Version223a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "native_vlan": MoPropertyMeta("native_vlan", "nativeVlan", "ushort", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "platform": MoPropertyMeta("platform", "platform", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "remote_interface": MoPropertyMeta("remote_interface", "remoteInterface", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial_number": MoPropertyMeta("serial_number", "serialNumber", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "system_name": MoPropertyMeta("system_name", "systemName", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "capabilities": "capabilities", 
        "childAction": "child_action", 
        "deviceId": "device_id", 
        "dn": "dn", 
        "fiPortDn": "fi_port_dn", 
        "ipV4Address": "ip_v4_address", 
        "ipV4MgmtAddress": "ip_v4_mgmt_address", 
        "localInterface": "local_interface", 
        "nativeVlan": "native_vlan", 
        "platform": "platform", 
        "remoteInterface": "remote_interface", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serialNumber": "serial_number", 
        "status": "status", 
        "systemName": "system_name", 
    }

    def __init__(self, parent_mo_or_dn, local_interface, **kwargs):
        self._dirty_mask = 0
        self.local_interface = local_interface
        self.capabilities = None
        self.child_action = None
        self.device_id = None
        self.fi_port_dn = None
        self.ip_v4_address = None
        self.ip_v4_mgmt_address = None
        self.native_vlan = None
        self.platform = None
        self.remote_interface = None
        self.sacl = None
        self.serial_number = None
        self.status = None
        self.system_name = None

        ManagedObject.__init__(self, "NetworkLanNeighborEntry", parent_mo_or_dn, **kwargs)
