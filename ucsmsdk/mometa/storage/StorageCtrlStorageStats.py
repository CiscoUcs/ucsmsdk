"""This module contains the general information for StorageCtrlStorageStats ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageCtrlStorageStatsConsts():
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class StorageCtrlStorageStats(ManagedObject):
    """This is StorageCtrlStorageStats class."""

    consts = StorageCtrlStorageStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageCtrlStorageStats", "storageCtrlStorageStats", "ctrl-storage-stats", VersionMeta.Version302c, "OutputOnly", 0xfL, [], ["admin", "operations", "read-only"], [], [u'storageCtrlStorageStatsHist'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cpu_load": MoPropertyMeta("cpu_load", "cpuLoad", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "cpu_load_avg": MoPropertyMeta("cpu_load_avg", "cpuLoadAvg", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "cpu_load_max": MoPropertyMeta("cpu_load_max", "cpuLoadMax", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "cpu_load_min": MoPropertyMeta("cpu_load_min", "cpuLoadMin", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "memory_usage": MoPropertyMeta("memory_usage", "memoryUsage", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "memory_usage_avg": MoPropertyMeta("memory_usage_avg", "memoryUsageAvg", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "memory_usage_max": MoPropertyMeta("memory_usage_max", "memoryUsageMax", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "memory_usage_min": MoPropertyMeta("memory_usage_min", "memoryUsageMin", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "cpuLoad": "cpu_load", 
        "cpuLoadAvg": "cpu_load_avg", 
        "cpuLoadMax": "cpu_load_max", 
        "cpuLoadMin": "cpu_load_min", 
        "dn": "dn", 
        "intervals": "intervals", 
        "memoryUsage": "memory_usage", 
        "memoryUsageAvg": "memory_usage_avg", 
        "memoryUsageMax": "memory_usage_max", 
        "memoryUsageMin": "memory_usage_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.cpu_load = None
        self.cpu_load_avg = None
        self.cpu_load_max = None
        self.cpu_load_min = None
        self.intervals = None
        self.memory_usage = None
        self.memory_usage_avg = None
        self.memory_usage_max = None
        self.memory_usage_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "StorageCtrlStorageStats", parent_mo_or_dn, **kwargs)

