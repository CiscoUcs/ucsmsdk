"""This module contains the general information for InitiatorRequestorGrpEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class InitiatorRequestorGrpEpConsts:
    ALLOC_STATE_ALLOCATED = "allocated"
    ALLOC_STATE_ALLOCATING = "allocating"
    ALLOC_STATE_FAILED = "failed"
    ALLOC_STATE_NONE = "none"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    TYPE_DEDICATED = "dedicated"
    TYPE_POLICY = "policy"
    TYPE_SHARED = "shared"


class InitiatorRequestorGrpEp(ManagedObject):
    """This is InitiatorRequestorGrpEp class."""

    consts = InitiatorRequestorGrpEpConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("InitiatorRequestorGrpEp", "initiatorRequestorGrpEp", "req-grp-[id]", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["read-only"], ['topSystem'], ['initiatorMemberEp', 'initiatorUnitEp'], [None])

    prop_meta = {
        "alloc_state": MoPropertyMeta("alloc_state", "allocState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "allocating", "failed", "none"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []),
        "pol_dn": MoPropertyMeta("pol_dn", "polDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["dedicated", "policy", "shared"], []),
    }

    prop_map = {
        "allocState": "alloc_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "id": "id", 
        "lc": "lc", 
        "polDn": "pol_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.alloc_state = None
        self.child_action = None
        self.ep_dn = None
        self.lc = None
        self.pol_dn = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "InitiatorRequestorGrpEp", parent_mo_or_dn, **kwargs)
