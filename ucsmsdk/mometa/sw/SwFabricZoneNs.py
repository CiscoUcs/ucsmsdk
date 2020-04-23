"""This module contains the general information for SwFabricZoneNs ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwFabricZoneNsConsts:
    ALLOC_STATUS_AVAILABLE = "available"
    ALLOC_STATUS_FULL = "full"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    USER_ZONE_ALLOC_STATUS_AVAILABLE = "available"
    USER_ZONE_ALLOC_STATUS_FULL = "full"


class SwFabricZoneNs(ManagedObject):
    """This is SwFabricZoneNs class."""

    consts = SwFabricZoneNsConsts()
    naming_props = set([])

    mo_meta = MoMeta("SwFabricZoneNs", "swFabricZoneNs", "fabric-zone-ns", VersionMeta.Version211a, "InputOutput", 0x1f, [], ["read-only"], ['networkElement'], [], [None])

    prop_meta = {
        "alloc_status": MoPropertyMeta("alloc_status", "allocStatus", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["available", "full"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "limit": MoPropertyMeta("limit", "limit", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "user_zone_alloc_status": MoPropertyMeta("user_zone_alloc_status", "userZoneAllocStatus", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["available", "full"], []),
        "user_zone_count": MoPropertyMeta("user_zone_count", "userZoneCount", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "user_zone_limit": MoPropertyMeta("user_zone_limit", "userZoneLimit", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "zone_count": MoPropertyMeta("zone_count", "zoneCount", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
    }

    prop_map = {
        "allocStatus": "alloc_status", 
        "childAction": "child_action", 
        "dn": "dn", 
        "limit": "limit", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
        "userZoneAllocStatus": "user_zone_alloc_status", 
        "userZoneCount": "user_zone_count", 
        "userZoneLimit": "user_zone_limit", 
        "zoneCount": "zone_count", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.alloc_status = None
        self.child_action = None
        self.limit = None
        self.sacl = None
        self.status = None
        self.switch_id = None
        self.user_zone_alloc_status = None
        self.user_zone_count = None
        self.user_zone_limit = None
        self.zone_count = None

        ManagedObject.__init__(self, "SwFabricZoneNs", parent_mo_or_dn, **kwargs)
