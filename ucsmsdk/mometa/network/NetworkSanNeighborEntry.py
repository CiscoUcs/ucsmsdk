"""This module contains the general information for NetworkSanNeighborEntry ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class NetworkSanNeighborEntryConsts:
    pass


class NetworkSanNeighborEntry(ManagedObject):
    """This is NetworkSanNeighborEntry class."""

    consts = NetworkSanNeighborEntryConsts()
    naming_props = set(['localInterface'])

    mo_meta = MoMeta("NetworkSanNeighborEntry", "networkSanNeighborEntry", "if-[local_interface]", VersionMeta.Version223a, "InputOutput", 0x3f, [], ["read-only"], ['networkSanNeighbors'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "fabric_mgmt_addr": MoPropertyMeta("fabric_mgmt_addr", "fabricMgmtAddr", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "fabric_nwwn": MoPropertyMeta("fabric_nwwn", "fabricNwwn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "fabric_pwwn": MoPropertyMeta("fabric_pwwn", "fabricPwwn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "fi_port_dn": MoPropertyMeta("fi_port_dn", "fiPortDn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "local_interface": MoPropertyMeta("local_interface", "localInterface", "string", VersionMeta.Version223a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "my_nwwn": MoPropertyMeta("my_nwwn", "myNwwn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "my_pwwn": MoPropertyMeta("my_pwwn", "myPwwn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "port_vsan": MoPropertyMeta("port_vsan", "portVsan", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fabricMgmtAddr": "fabric_mgmt_addr", 
        "fabricNwwn": "fabric_nwwn", 
        "fabricPwwn": "fabric_pwwn", 
        "fiPortDn": "fi_port_dn", 
        "localInterface": "local_interface", 
        "myNwwn": "my_nwwn", 
        "myPwwn": "my_pwwn", 
        "portVsan": "port_vsan", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, local_interface, **kwargs):
        self._dirty_mask = 0
        self.local_interface = local_interface
        self.child_action = None
        self.fabric_mgmt_addr = None
        self.fabric_nwwn = None
        self.fabric_pwwn = None
        self.fi_port_dn = None
        self.my_nwwn = None
        self.my_pwwn = None
        self.port_vsan = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "NetworkSanNeighborEntry", parent_mo_or_dn, **kwargs)
