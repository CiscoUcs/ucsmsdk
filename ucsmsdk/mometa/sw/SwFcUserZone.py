"""This module contains the general information for SwFcUserZone ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwFcUserZoneConsts:
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    OPER_STATE_ACTIVE = "active"
    OPER_STATE_APPLIED = "applied"
    OPER_STATE_APPLY_PENDING = "apply-pending"
    OPER_STATE_APPLYING = "applying"
    OPER_STATE_CREATE_FAILED = "create-failed"
    OPER_STATE_CREATED = "created"
    OPER_STATE_DELETED = "deleted"
    OPER_STATE_NOT_ACTIVE = "not-active"
    OPER_STATE_NOT_APPLIED = "not-applied"
    OPER_STATE_ZONE_MERGE_FAILURE = "zone-merge-failure"


class SwFcUserZone(ManagedObject):
    """This is SwFcUserZone class."""

    consts = SwFcUserZoneConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("SwFcUserZone", "swFcUserZone", "zone-[id]", VersionMeta.Version312b, "InputOutput", 0x3f, [], ["read-only"], ['swFcUserZoneGroup'], ['swFcEndpoint'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{1,64}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "applied", "apply-pending", "applying", "create-failed", "created", "deleted", "not-active", "not-applied", "zone-merge-failure"], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "lc": "lc", 
        "name": "name", 
        "operState": "oper_state", 
        "peerDn": "peer_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.lc = None
        self.name = None
        self.oper_state = None
        self.peer_dn = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "SwFcUserZone", parent_mo_or_dn, **kwargs)
