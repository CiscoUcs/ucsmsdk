"""This module contains the general information for LldpAcquired ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LldpAcquiredConsts:
    pass


class LldpAcquired(ManagedObject):
    """This is LldpAcquired class."""

    consts = LldpAcquiredConsts()
    naming_props = set([])

    mo_meta = MoMeta("LldpAcquired", "lldpAcquired", "lldp", VersionMeta.Version141i, "InputOutput", 0x1f, [], ["read-only"], ['etherPIo', 'etherServerIntFIo', 'fcPIo'], [], ["Get"])

    prop_meta = {
        "acqts": MoPropertyMeta("acqts", "acqts", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "chassis_mac": MoPropertyMeta("chassis_mac", "chassisMac", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "port_mac": MoPropertyMeta("port_mac", "portMac", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "acqts": "acqts", 
        "chassisMac": "chassis_mac", 
        "childAction": "child_action", 
        "dn": "dn", 
        "peerDn": "peer_dn", 
        "portMac": "port_mac", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.acqts = None
        self.chassis_mac = None
        self.child_action = None
        self.peer_dn = None
        self.port_mac = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LldpAcquired", parent_mo_or_dn, **kwargs)
