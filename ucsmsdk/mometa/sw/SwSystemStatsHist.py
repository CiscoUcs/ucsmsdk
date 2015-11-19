"""This module contains the general information for SwSystemStatsHist ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class SwSystemStatsHistConsts():
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class SwSystemStatsHist(ManagedObject):
    """This is SwSystemStatsHist class."""

    consts = SwSystemStatsHistConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("SwSystemStatsHist", "swSystemStatsHist", "[id]", VersionMeta.Version111j, "OutputOnly", 0x7L, [], ["read-only"], [u'swSystemStats'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x1L, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "load": MoPropertyMeta("load", "load", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "load_avg": MoPropertyMeta("load_avg", "loadAvg", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "load_max": MoPropertyMeta("load_max", "loadMax", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "load_min": MoPropertyMeta("load_min", "loadMin", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_available": MoPropertyMeta("mem_available", "memAvailable", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_available_avg": MoPropertyMeta("mem_available_avg", "memAvailableAvg", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_available_max": MoPropertyMeta("mem_available_max", "memAvailableMax", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_available_min": MoPropertyMeta("mem_available_min", "memAvailableMin", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_cached": MoPropertyMeta("mem_cached", "memCached", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_cached_avg": MoPropertyMeta("mem_cached_avg", "memCachedAvg", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_cached_max": MoPropertyMeta("mem_cached_max", "memCachedMax", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_cached_min": MoPropertyMeta("mem_cached_min", "memCachedMin", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "load": "load", 
        "loadAvg": "load_avg", 
        "loadMax": "load_max", 
        "loadMin": "load_min", 
        "memAvailable": "mem_available", 
        "memAvailableAvg": "mem_available_avg", 
        "memAvailableMax": "mem_available_max", 
        "memAvailableMin": "mem_available_min", 
        "memCached": "mem_cached", 
        "memCachedAvg": "mem_cached_avg", 
        "memCachedMax": "mem_cached_max", 
        "memCachedMin": "mem_cached_min", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.load = None
        self.load_avg = None
        self.load_max = None
        self.load_min = None
        self.mem_available = None
        self.mem_available_avg = None
        self.mem_available_max = None
        self.mem_available_min = None
        self.mem_cached = None
        self.mem_cached_avg = None
        self.mem_cached_max = None
        self.mem_cached_min = None
        self.most_recent = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "SwSystemStatsHist", parent_mo_or_dn, **kwargs)

