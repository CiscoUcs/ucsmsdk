"""This module contains the general information for OsEthBondModeBroadcast ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class OsEthBondModeBroadcastConsts:
    TYPE_ACTIVE_ACTIVE = "active-active"
    TYPE_ACTIVE_PASSIVE = "active-passive"


class OsEthBondModeBroadcast(ManagedObject):
    """This is OsEthBondModeBroadcast class."""

    consts = OsEthBondModeBroadcastConsts()
    naming_props = set([])

    mo_meta = MoMeta("OsEthBondModeBroadcast", "osEthBondModeBroadcast", "eth-bond-mode", VersionMeta.Version302c, "InputOutput", 0x3f, [], ["read-only"], ['osEthBondIntf'], ['osPrimarySlave'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active-active", "active-passive"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.name = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "OsEthBondModeBroadcast", parent_mo_or_dn, **kwargs)
