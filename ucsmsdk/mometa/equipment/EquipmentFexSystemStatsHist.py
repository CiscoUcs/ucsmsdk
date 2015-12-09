"""This module contains the general information for EquipmentFexSystemStatsHist ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentFexSystemStatsHistConsts():
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EquipmentFexSystemStatsHist(ManagedObject):
    """This is EquipmentFexSystemStatsHist class."""

    consts = EquipmentFexSystemStatsHistConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("EquipmentFexSystemStatsHist", "equipmentFexSystemStatsHist", "[id]", None, "OutputOnly", 0xfL, [], ["read-only"], [u'equipmentFexSystemStats'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", None, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "kernel_mem_free": MoPropertyMeta("kernel_mem_free", "kernelMemFree", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "kernel_mem_free_avg": MoPropertyMeta("kernel_mem_free_avg", "kernelMemFreeAvg", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "kernel_mem_free_max": MoPropertyMeta("kernel_mem_free_max", "kernelMemFreeMax", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "kernel_mem_free_min": MoPropertyMeta("kernel_mem_free_min", "kernelMemFreeMin", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "kernel_mem_total": MoPropertyMeta("kernel_mem_total", "kernelMemTotal", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "kernel_mem_total_avg": MoPropertyMeta("kernel_mem_total_avg", "kernelMemTotalAvg", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "kernel_mem_total_max": MoPropertyMeta("kernel_mem_total_max", "kernelMemTotalMax", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "kernel_mem_total_min": MoPropertyMeta("kernel_mem_total_min", "kernelMemTotalMin", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "load": MoPropertyMeta("load", "load", "float", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "load_avg": MoPropertyMeta("load_avg", "loadAvg", "float", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "load_max": MoPropertyMeta("load_max", "loadMax", "float", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "load_min": MoPropertyMeta("load_min", "loadMin", "float", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_available": MoPropertyMeta("mem_available", "memAvailable", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_available_avg": MoPropertyMeta("mem_available_avg", "memAvailableAvg", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_available_max": MoPropertyMeta("mem_available_max", "memAvailableMax", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_available_min": MoPropertyMeta("mem_available_min", "memAvailableMin", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_cached": MoPropertyMeta("mem_cached", "memCached", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_cached_avg": MoPropertyMeta("mem_cached_avg", "memCachedAvg", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_cached_max": MoPropertyMeta("mem_cached_max", "memCachedMax", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mem_cached_min": MoPropertyMeta("mem_cached_min", "memCachedMin", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "kernelMemFree": "kernel_mem_free", 
        "kernelMemFreeAvg": "kernel_mem_free_avg", 
        "kernelMemFreeMax": "kernel_mem_free_max", 
        "kernelMemFreeMin": "kernel_mem_free_min", 
        "kernelMemTotal": "kernel_mem_total", 
        "kernelMemTotalAvg": "kernel_mem_total_avg", 
        "kernelMemTotalMax": "kernel_mem_total_max", 
        "kernelMemTotalMin": "kernel_mem_total_min", 
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
        self.kernel_mem_free = None
        self.kernel_mem_free_avg = None
        self.kernel_mem_free_max = None
        self.kernel_mem_free_min = None
        self.kernel_mem_total = None
        self.kernel_mem_total_avg = None
        self.kernel_mem_total_max = None
        self.kernel_mem_total_min = None
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

        ManagedObject.__init__(self, "EquipmentFexSystemStatsHist", parent_mo_or_dn, **kwargs)

