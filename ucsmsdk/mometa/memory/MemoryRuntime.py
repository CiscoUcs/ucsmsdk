"""This module contains the general information for MemoryRuntime ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MemoryRuntimeConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"
    TYPE_SWAP = "swap"
    TYPE_TOTAL = "total"


class MemoryRuntime(ManagedObject):
    """This is MemoryRuntime class."""

    consts = MemoryRuntimeConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("MemoryRuntime", "memoryRuntime", "[type]-mem-rt", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['computeBlade'], ['memoryRuntimeHist'], ["Get"])

    prop_meta = {
        "available": MoPropertyMeta("available", "available", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "available_avg": MoPropertyMeta("available_avg", "availableAvg", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "available_max": MoPropertyMeta("available_max", "availableMax", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "available_min": MoPropertyMeta("available_min", "availableMin", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "cached": MoPropertyMeta("cached", "cached", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "cached_avg": MoPropertyMeta("cached_avg", "cachedAvg", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "cached_max": MoPropertyMeta("cached_max", "cachedMax", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "cached_min": MoPropertyMeta("cached_min", "cachedMin", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "total": MoPropertyMeta("total", "total", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total_avg": MoPropertyMeta("total_avg", "totalAvg", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total_max": MoPropertyMeta("total_max", "totalMax", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total_min": MoPropertyMeta("total_min", "totalMin", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, ["swap", "total"], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "available": "available", 
        "availableAvg": "available_avg", 
        "availableMax": "available_max", 
        "availableMin": "available_min", 
        "cached": "cached", 
        "cachedAvg": "cached_avg", 
        "cachedMax": "cached_max", 
        "cachedMin": "cached_min", 
        "childAction": "child_action", 
        "dn": "dn", 
        "intervals": "intervals", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "total": "total", 
        "totalAvg": "total_avg", 
        "totalMax": "total_max", 
        "totalMin": "total_min", 
        "type": "type", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.available = None
        self.available_avg = None
        self.available_max = None
        self.available_min = None
        self.cached = None
        self.cached_avg = None
        self.cached_max = None
        self.cached_min = None
        self.child_action = None
        self.intervals = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.total = None
        self.total_avg = None
        self.total_max = None
        self.total_min = None
        self.update = None

        ManagedObject.__init__(self, "MemoryRuntime", parent_mo_or_dn, **kwargs)
