"""This module contains the general information for AdaptorEthPortPfcStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorEthPortPfcStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorEthPortPfcStatsHist(ManagedObject):
    """This is AdaptorEthPortPfcStatsHist class."""

    consts = AdaptorEthPortPfcStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorEthPortPfcStatsHist", "adaptorEthPortPfcStatsHist", "[id]", VersionMeta.Version434a, "OutputOnly", 0xf, [], ["read-only"], ['adaptorEthPortPfcStats'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version434a, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "priority0_queue_wait_time": MoPropertyMeta("priority0_queue_wait_time", "priority0QueueWaitTime", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority0_queue_wait_time_avg": MoPropertyMeta("priority0_queue_wait_time_avg", "priority0QueueWaitTimeAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority0_queue_wait_time_max": MoPropertyMeta("priority0_queue_wait_time_max", "priority0QueueWaitTimeMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority0_queue_wait_time_min": MoPropertyMeta("priority0_queue_wait_time_min", "priority0QueueWaitTimeMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority1_queue_wait_time": MoPropertyMeta("priority1_queue_wait_time", "priority1QueueWaitTime", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority1_queue_wait_time_avg": MoPropertyMeta("priority1_queue_wait_time_avg", "priority1QueueWaitTimeAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority1_queue_wait_time_max": MoPropertyMeta("priority1_queue_wait_time_max", "priority1QueueWaitTimeMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority1_queue_wait_time_min": MoPropertyMeta("priority1_queue_wait_time_min", "priority1QueueWaitTimeMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority2_queue_wait_time": MoPropertyMeta("priority2_queue_wait_time", "priority2QueueWaitTime", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority2_queue_wait_time_avg": MoPropertyMeta("priority2_queue_wait_time_avg", "priority2QueueWaitTimeAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority2_queue_wait_time_max": MoPropertyMeta("priority2_queue_wait_time_max", "priority2QueueWaitTimeMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority2_queue_wait_time_min": MoPropertyMeta("priority2_queue_wait_time_min", "priority2QueueWaitTimeMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority3_queue_wait_time": MoPropertyMeta("priority3_queue_wait_time", "priority3QueueWaitTime", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority3_queue_wait_time_avg": MoPropertyMeta("priority3_queue_wait_time_avg", "priority3QueueWaitTimeAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority3_queue_wait_time_max": MoPropertyMeta("priority3_queue_wait_time_max", "priority3QueueWaitTimeMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority3_queue_wait_time_min": MoPropertyMeta("priority3_queue_wait_time_min", "priority3QueueWaitTimeMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority4_queue_wait_time": MoPropertyMeta("priority4_queue_wait_time", "priority4QueueWaitTime", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority4_queue_wait_time_avg": MoPropertyMeta("priority4_queue_wait_time_avg", "priority4QueueWaitTimeAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority4_queue_wait_time_max": MoPropertyMeta("priority4_queue_wait_time_max", "priority4QueueWaitTimeMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority4_queue_wait_time_min": MoPropertyMeta("priority4_queue_wait_time_min", "priority4QueueWaitTimeMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority5_queue_wait_time": MoPropertyMeta("priority5_queue_wait_time", "priority5QueueWaitTime", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority5_queue_wait_time_avg": MoPropertyMeta("priority5_queue_wait_time_avg", "priority5QueueWaitTimeAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority5_queue_wait_time_max": MoPropertyMeta("priority5_queue_wait_time_max", "priority5QueueWaitTimeMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority5_queue_wait_time_min": MoPropertyMeta("priority5_queue_wait_time_min", "priority5QueueWaitTimeMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority6_queue_wait_time": MoPropertyMeta("priority6_queue_wait_time", "priority6QueueWaitTime", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority6_queue_wait_time_avg": MoPropertyMeta("priority6_queue_wait_time_avg", "priority6QueueWaitTimeAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority6_queue_wait_time_max": MoPropertyMeta("priority6_queue_wait_time_max", "priority6QueueWaitTimeMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority6_queue_wait_time_min": MoPropertyMeta("priority6_queue_wait_time_min", "priority6QueueWaitTimeMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority7_queue_wait_time": MoPropertyMeta("priority7_queue_wait_time", "priority7QueueWaitTime", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority7_queue_wait_time_avg": MoPropertyMeta("priority7_queue_wait_time_avg", "priority7QueueWaitTimeAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority7_queue_wait_time_max": MoPropertyMeta("priority7_queue_wait_time_max", "priority7QueueWaitTimeMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority7_queue_wait_time_min": MoPropertyMeta("priority7_queue_wait_time_min", "priority7QueueWaitTimeMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "mostRecent": "most_recent", 
        "priority0QueueWaitTime": "priority0_queue_wait_time", 
        "priority0QueueWaitTimeAvg": "priority0_queue_wait_time_avg", 
        "priority0QueueWaitTimeMax": "priority0_queue_wait_time_max", 
        "priority0QueueWaitTimeMin": "priority0_queue_wait_time_min", 
        "priority1QueueWaitTime": "priority1_queue_wait_time", 
        "priority1QueueWaitTimeAvg": "priority1_queue_wait_time_avg", 
        "priority1QueueWaitTimeMax": "priority1_queue_wait_time_max", 
        "priority1QueueWaitTimeMin": "priority1_queue_wait_time_min", 
        "priority2QueueWaitTime": "priority2_queue_wait_time", 
        "priority2QueueWaitTimeAvg": "priority2_queue_wait_time_avg", 
        "priority2QueueWaitTimeMax": "priority2_queue_wait_time_max", 
        "priority2QueueWaitTimeMin": "priority2_queue_wait_time_min", 
        "priority3QueueWaitTime": "priority3_queue_wait_time", 
        "priority3QueueWaitTimeAvg": "priority3_queue_wait_time_avg", 
        "priority3QueueWaitTimeMax": "priority3_queue_wait_time_max", 
        "priority3QueueWaitTimeMin": "priority3_queue_wait_time_min", 
        "priority4QueueWaitTime": "priority4_queue_wait_time", 
        "priority4QueueWaitTimeAvg": "priority4_queue_wait_time_avg", 
        "priority4QueueWaitTimeMax": "priority4_queue_wait_time_max", 
        "priority4QueueWaitTimeMin": "priority4_queue_wait_time_min", 
        "priority5QueueWaitTime": "priority5_queue_wait_time", 
        "priority5QueueWaitTimeAvg": "priority5_queue_wait_time_avg", 
        "priority5QueueWaitTimeMax": "priority5_queue_wait_time_max", 
        "priority5QueueWaitTimeMin": "priority5_queue_wait_time_min", 
        "priority6QueueWaitTime": "priority6_queue_wait_time", 
        "priority6QueueWaitTimeAvg": "priority6_queue_wait_time_avg", 
        "priority6QueueWaitTimeMax": "priority6_queue_wait_time_max", 
        "priority6QueueWaitTimeMin": "priority6_queue_wait_time_min", 
        "priority7QueueWaitTime": "priority7_queue_wait_time", 
        "priority7QueueWaitTimeAvg": "priority7_queue_wait_time_avg", 
        "priority7QueueWaitTimeMax": "priority7_queue_wait_time_max", 
        "priority7QueueWaitTimeMin": "priority7_queue_wait_time_min", 
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
        self.most_recent = None
        self.priority0_queue_wait_time = None
        self.priority0_queue_wait_time_avg = None
        self.priority0_queue_wait_time_max = None
        self.priority0_queue_wait_time_min = None
        self.priority1_queue_wait_time = None
        self.priority1_queue_wait_time_avg = None
        self.priority1_queue_wait_time_max = None
        self.priority1_queue_wait_time_min = None
        self.priority2_queue_wait_time = None
        self.priority2_queue_wait_time_avg = None
        self.priority2_queue_wait_time_max = None
        self.priority2_queue_wait_time_min = None
        self.priority3_queue_wait_time = None
        self.priority3_queue_wait_time_avg = None
        self.priority3_queue_wait_time_max = None
        self.priority3_queue_wait_time_min = None
        self.priority4_queue_wait_time = None
        self.priority4_queue_wait_time_avg = None
        self.priority4_queue_wait_time_max = None
        self.priority4_queue_wait_time_min = None
        self.priority5_queue_wait_time = None
        self.priority5_queue_wait_time_avg = None
        self.priority5_queue_wait_time_max = None
        self.priority5_queue_wait_time_min = None
        self.priority6_queue_wait_time = None
        self.priority6_queue_wait_time_avg = None
        self.priority6_queue_wait_time_max = None
        self.priority6_queue_wait_time_min = None
        self.priority7_queue_wait_time = None
        self.priority7_queue_wait_time_avg = None
        self.priority7_queue_wait_time_max = None
        self.priority7_queue_wait_time_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "AdaptorEthPortPfcStatsHist", parent_mo_or_dn, **kwargs)
