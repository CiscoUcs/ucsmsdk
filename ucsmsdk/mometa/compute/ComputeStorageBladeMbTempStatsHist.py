"""This module contains the general information for ComputeStorageBladeMbTempStatsHist ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ComputeStorageBladeMbTempStatsHistConsts():
    FRONT_TEMP_NOT_APPLICABLE = "not-applicable"
    FRONT_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    FRONT_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    FRONT_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    LEFT_REAR_TEMP_NOT_APPLICABLE = "not-applicable"
    LEFT_REAR_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    LEFT_REAR_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    LEFT_REAR_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    RIGHT_REAR_TEMP_NOT_APPLICABLE = "not-applicable"
    RIGHT_REAR_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    RIGHT_REAR_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    RIGHT_REAR_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ComputeStorageBladeMbTempStatsHist(ManagedObject):
    """This is ComputeStorageBladeMbTempStatsHist class."""

    consts = ComputeStorageBladeMbTempStatsHistConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("ComputeStorageBladeMbTempStatsHist", "computeStorageBladeMbTempStatsHist", "[id]", VersionMeta.Version302c, "OutputOnly", 0xfL, [], ["read-only"], [u'computeStorageBladeMbTempStats'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "front_temp": MoPropertyMeta("front_temp", "frontTemp", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "front_temp_avg": MoPropertyMeta("front_temp_avg", "frontTempAvg", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "front_temp_max": MoPropertyMeta("front_temp_max", "frontTempMax", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "front_temp_min": MoPropertyMeta("front_temp_min", "frontTempMin", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version302c, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "left_rear_temp": MoPropertyMeta("left_rear_temp", "leftRearTemp", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_rear_temp_avg": MoPropertyMeta("left_rear_temp_avg", "leftRearTempAvg", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_rear_temp_max": MoPropertyMeta("left_rear_temp_max", "leftRearTempMax", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_rear_temp_min": MoPropertyMeta("left_rear_temp_min", "leftRearTempMin", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "right_rear_temp": MoPropertyMeta("right_rear_temp", "rightRearTemp", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_rear_temp_avg": MoPropertyMeta("right_rear_temp_avg", "rightRearTempAvg", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_rear_temp_max": MoPropertyMeta("right_rear_temp_max", "rightRearTempMax", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_rear_temp_min": MoPropertyMeta("right_rear_temp_min", "rightRearTempMin", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "frontTemp": "front_temp", 
        "frontTempAvg": "front_temp_avg", 
        "frontTempMax": "front_temp_max", 
        "frontTempMin": "front_temp_min", 
        "id": "id", 
        "leftRearTemp": "left_rear_temp", 
        "leftRearTempAvg": "left_rear_temp_avg", 
        "leftRearTempMax": "left_rear_temp_max", 
        "leftRearTempMin": "left_rear_temp_min", 
        "mostRecent": "most_recent", 
        "rightRearTemp": "right_rear_temp", 
        "rightRearTempAvg": "right_rear_temp_avg", 
        "rightRearTempMax": "right_rear_temp_max", 
        "rightRearTempMin": "right_rear_temp_min", 
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
        self.front_temp = None
        self.front_temp_avg = None
        self.front_temp_max = None
        self.front_temp_min = None
        self.left_rear_temp = None
        self.left_rear_temp_avg = None
        self.left_rear_temp_max = None
        self.left_rear_temp_min = None
        self.most_recent = None
        self.right_rear_temp = None
        self.right_rear_temp_avg = None
        self.right_rear_temp_max = None
        self.right_rear_temp_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "ComputeStorageBladeMbTempStatsHist", parent_mo_or_dn, **kwargs)

