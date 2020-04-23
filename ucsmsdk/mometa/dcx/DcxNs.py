"""This module contains the general information for DcxNs ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class DcxNsConsts:
    ALLOC_STATUS_AVAILABLE = "available"
    ALLOC_STATUS_EXCEEDED = "exceeded"
    ALLOC_STATUS_FULL = "full"
    SIDE_LEFT = "left"
    SIDE_RIGHT = "right"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class DcxNs(ManagedObject):
    """This is DcxNs class."""

    consts = DcxNsConsts()
    naming_props = set(['switchId'])

    mo_meta = MoMeta("DcxNs", "dcxNs", "dcxns-[switch_id]", VersionMeta.Version101e, "InputOutput", 0x3f, [], ["read-only"], ['adaptorUnit'], ['faultInst'], ["Get"])

    prop_meta = {
        "alloc_status": MoPropertyMeta("alloc_status", "allocStatus", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["available", "exceeded", "full"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "side": MoPropertyMeta("side", "side", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["left", "right"], []),
        "size": MoPropertyMeta("size", "size", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, None, None, None, ["A", "B", "NONE"], []),
        "used": MoPropertyMeta("used", "used", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "allocStatus": "alloc_status", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "side": "side", 
        "size": "size", 
        "status": "status", 
        "switchId": "switch_id", 
        "used": "used", 
    }

    def __init__(self, parent_mo_or_dn, switch_id, **kwargs):
        self._dirty_mask = 0
        self.switch_id = switch_id
        self.alloc_status = None
        self.child_action = None
        self.sacl = None
        self.side = None
        self.size = None
        self.status = None
        self.used = None

        ManagedObject.__init__(self, "DcxNs", parent_mo_or_dn, **kwargs)
