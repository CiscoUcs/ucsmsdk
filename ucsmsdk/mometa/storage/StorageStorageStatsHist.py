"""This module contains the general information for StorageStorageStatsHist ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageStorageStatsHistConsts():
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class StorageStorageStatsHist(ManagedObject):
    """This is StorageStorageStatsHist class."""

    consts = StorageStorageStatsHistConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("StorageStorageStatsHist", "storageStorageStatsHist", "[id]", VersionMeta.Version302c, "OutputOnly", 0xfL, [], ["read-only"], [u'storageStorageStats'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version302c, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "iops": MoPropertyMeta("iops", "iops", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "iops_avg": MoPropertyMeta("iops_avg", "iopsAvg", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "iops_max": MoPropertyMeta("iops_max", "iopsMax", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "iops_min": MoPropertyMeta("iops_min", "iopsMin", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "latency": MoPropertyMeta("latency", "latency", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "latency_avg": MoPropertyMeta("latency_avg", "latencyAvg", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "latency_max": MoPropertyMeta("latency_max", "latencyMax", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "latency_min": MoPropertyMeta("latency_min", "latencyMin", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mbps": MoPropertyMeta("mbps", "mbps", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mbps_avg": MoPropertyMeta("mbps_avg", "mbpsAvg", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mbps_max": MoPropertyMeta("mbps_max", "mbpsMax", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mbps_min": MoPropertyMeta("mbps_min", "mbpsMin", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "read_iops": MoPropertyMeta("read_iops", "readIops", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "read_iops_avg": MoPropertyMeta("read_iops_avg", "readIopsAvg", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "read_iops_max": MoPropertyMeta("read_iops_max", "readIopsMax", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "read_iops_min": MoPropertyMeta("read_iops_min", "readIopsMin", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "read_mbps": MoPropertyMeta("read_mbps", "readMbps", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "read_mbps_avg": MoPropertyMeta("read_mbps_avg", "readMbpsAvg", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "read_mbps_max": MoPropertyMeta("read_mbps_max", "readMbpsMax", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "read_mbps_min": MoPropertyMeta("read_mbps_min", "readMbpsMin", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "write_iops": MoPropertyMeta("write_iops", "writeIops", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "write_iops_avg": MoPropertyMeta("write_iops_avg", "writeIopsAvg", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "write_iops_max": MoPropertyMeta("write_iops_max", "writeIopsMax", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "write_iops_min": MoPropertyMeta("write_iops_min", "writeIopsMin", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "write_mbps": MoPropertyMeta("write_mbps", "writeMbps", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "write_mbps_avg": MoPropertyMeta("write_mbps_avg", "writeMbpsAvg", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "write_mbps_max": MoPropertyMeta("write_mbps_max", "writeMbpsMax", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "write_mbps_min": MoPropertyMeta("write_mbps_min", "writeMbpsMin", "float", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "iops": "iops", 
        "iopsAvg": "iops_avg", 
        "iopsMax": "iops_max", 
        "iopsMin": "iops_min", 
        "latency": "latency", 
        "latencyAvg": "latency_avg", 
        "latencyMax": "latency_max", 
        "latencyMin": "latency_min", 
        "mbps": "mbps", 
        "mbpsAvg": "mbps_avg", 
        "mbpsMax": "mbps_max", 
        "mbpsMin": "mbps_min", 
        "mostRecent": "most_recent", 
        "readIops": "read_iops", 
        "readIopsAvg": "read_iops_avg", 
        "readIopsMax": "read_iops_max", 
        "readIopsMin": "read_iops_min", 
        "readMbps": "read_mbps", 
        "readMbpsAvg": "read_mbps_avg", 
        "readMbpsMax": "read_mbps_max", 
        "readMbpsMin": "read_mbps_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "writeIops": "write_iops", 
        "writeIopsAvg": "write_iops_avg", 
        "writeIopsMax": "write_iops_max", 
        "writeIopsMin": "write_iops_min", 
        "writeMbps": "write_mbps", 
        "writeMbpsAvg": "write_mbps_avg", 
        "writeMbpsMax": "write_mbps_max", 
        "writeMbpsMin": "write_mbps_min", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.iops = None
        self.iops_avg = None
        self.iops_max = None
        self.iops_min = None
        self.latency = None
        self.latency_avg = None
        self.latency_max = None
        self.latency_min = None
        self.mbps = None
        self.mbps_avg = None
        self.mbps_max = None
        self.mbps_min = None
        self.most_recent = None
        self.read_iops = None
        self.read_iops_avg = None
        self.read_iops_max = None
        self.read_iops_min = None
        self.read_mbps = None
        self.read_mbps_avg = None
        self.read_mbps_max = None
        self.read_mbps_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.write_iops = None
        self.write_iops_avg = None
        self.write_iops_max = None
        self.write_iops_min = None
        self.write_mbps = None
        self.write_mbps_avg = None
        self.write_mbps_max = None
        self.write_mbps_min = None

        ManagedObject.__init__(self, "StorageStorageStatsHist", parent_mo_or_dn, **kwargs)

