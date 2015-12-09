"""This module contains the general information for ComputeStorageBladeMbTempStats ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ComputeStorageBladeMbTempStatsConsts():
    FRONT_TEMP_NOT_APPLICABLE = "not-applicable"
    FRONT_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    FRONT_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    FRONT_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    LEFT_REAR_TEMP_NOT_APPLICABLE = "not-applicable"
    LEFT_REAR_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    LEFT_REAR_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    LEFT_REAR_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    RIGHT_REAR_TEMP_NOT_APPLICABLE = "not-applicable"
    RIGHT_REAR_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    RIGHT_REAR_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    RIGHT_REAR_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ComputeStorageBladeMbTempStats(ManagedObject):
    """This is ComputeStorageBladeMbTempStats class."""

    consts = ComputeStorageBladeMbTempStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeStorageBladeMbTempStats", "computeStorageBladeMbTempStats", "temp-stats", VersionMeta.Version302c, "OutputOnly", 0xfL, [], ["admin", "operations", "read-only"], [u'computeBoard'], [u'computeStorageBladeMbTempStatsHist'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "front_temp": MoPropertyMeta("front_temp", "frontTemp", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "front_temp_avg": MoPropertyMeta("front_temp_avg", "frontTempAvg", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "front_temp_max": MoPropertyMeta("front_temp_max", "frontTempMax", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "front_temp_min": MoPropertyMeta("front_temp_min", "frontTempMin", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "left_rear_temp": MoPropertyMeta("left_rear_temp", "leftRearTemp", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_rear_temp_avg": MoPropertyMeta("left_rear_temp_avg", "leftRearTempAvg", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_rear_temp_max": MoPropertyMeta("left_rear_temp_max", "leftRearTempMax", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_rear_temp_min": MoPropertyMeta("left_rear_temp_min", "leftRearTempMin", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
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
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "frontTemp": "front_temp", 
        "frontTempAvg": "front_temp_avg", 
        "frontTempMax": "front_temp_max", 
        "frontTempMin": "front_temp_min", 
        "intervals": "intervals", 
        "leftRearTemp": "left_rear_temp", 
        "leftRearTempAvg": "left_rear_temp_avg", 
        "leftRearTempMax": "left_rear_temp_max", 
        "leftRearTempMin": "left_rear_temp_min", 
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
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.front_temp = None
        self.front_temp_avg = None
        self.front_temp_max = None
        self.front_temp_min = None
        self.intervals = None
        self.left_rear_temp = None
        self.left_rear_temp_avg = None
        self.left_rear_temp_max = None
        self.left_rear_temp_min = None
        self.right_rear_temp = None
        self.right_rear_temp_avg = None
        self.right_rear_temp_max = None
        self.right_rear_temp_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "ComputeStorageBladeMbTempStats", parent_mo_or_dn, **kwargs)

