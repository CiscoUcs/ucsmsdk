"""This module contains the general information for StorageDiskEnvStats ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageDiskEnvStatsConsts():
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"
    TEMPERATURE_NOT_APPLICABLE = "not-applicable"
    TEMPERATURE_AVG_NOT_APPLICABLE = "not-applicable"
    TEMPERATURE_MAX_NOT_APPLICABLE = "not-applicable"
    TEMPERATURE_MIN_NOT_APPLICABLE = "not-applicable"
    WEAR_PERCENTAGE_UNKNOWN = "unknown"
    WEAR_PERCENTAGE_AVG_UNKNOWN = "unknown"
    WEAR_PERCENTAGE_MAX_UNKNOWN = "unknown"
    WEAR_PERCENTAGE_MIN_UNKNOWN = "unknown"


class StorageDiskEnvStats(ManagedObject):
    """This is StorageDiskEnvStats class."""

    consts = StorageDiskEnvStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageDiskEnvStats", "storageDiskEnvStats", "disk-env-stats", VersionMeta.Version302c, "OutputOnly", 0xfL, [], ["admin", "operations", "read-only"], [u'storageLocalDisk'], [u'faultInst', u'storageDiskEnvStatsHist'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "temperature": MoPropertyMeta("temperature", "temperature", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "temperature_avg": MoPropertyMeta("temperature_avg", "temperatureAvg", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "temperature_max": MoPropertyMeta("temperature_max", "temperatureMax", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "temperature_min": MoPropertyMeta("temperature_min", "temperatureMin", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "wear_percentage": MoPropertyMeta("wear_percentage", "wearPercentage", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-100"]), 
        "wear_percentage_avg": MoPropertyMeta("wear_percentage_avg", "wearPercentageAvg", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-100"]), 
        "wear_percentage_max": MoPropertyMeta("wear_percentage_max", "wearPercentageMax", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-100"]), 
        "wear_percentage_min": MoPropertyMeta("wear_percentage_min", "wearPercentageMin", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-100"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "intervals": "intervals", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "temperature": "temperature", 
        "temperatureAvg": "temperature_avg", 
        "temperatureMax": "temperature_max", 
        "temperatureMin": "temperature_min", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
        "wearPercentage": "wear_percentage", 
        "wearPercentageAvg": "wear_percentage_avg", 
        "wearPercentageMax": "wear_percentage_max", 
        "wearPercentageMin": "wear_percentage_min", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.intervals = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.temperature = None
        self.temperature_avg = None
        self.temperature_max = None
        self.temperature_min = None
        self.thresholded = None
        self.time_collected = None
        self.update = None
        self.wear_percentage = None
        self.wear_percentage_avg = None
        self.wear_percentage_max = None
        self.wear_percentage_min = None

        ManagedObject.__init__(self, "StorageDiskEnvStats", parent_mo_or_dn, **kwargs)
