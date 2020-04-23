"""This module contains the general information for EquipmentNetworkElementFanStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentNetworkElementFanStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EquipmentNetworkElementFanStatsHist(ManagedObject):
    """This is EquipmentNetworkElementFanStatsHist class."""

    consts = EquipmentNetworkElementFanStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EquipmentNetworkElementFanStatsHist", "equipmentNetworkElementFanStatsHist", "[id]", VersionMeta.Version201m, "OutputOnly", 0xf, [], ["read-only"], ['equipmentNetworkElementFanStats'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "drive_percentage": MoPropertyMeta("drive_percentage", "drivePercentage", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "drive_percentage_avg": MoPropertyMeta("drive_percentage_avg", "drivePercentageAvg", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "drive_percentage_max": MoPropertyMeta("drive_percentage_max", "drivePercentageMax", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "drive_percentage_min": MoPropertyMeta("drive_percentage_min", "drivePercentageMin", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version201m, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "speed": MoPropertyMeta("speed", "speed", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "speed_avg": MoPropertyMeta("speed_avg", "speedAvg", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "speed_max": MoPropertyMeta("speed_max", "speedMax", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "speed_min": MoPropertyMeta("speed_min", "speedMin", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "drivePercentage": "drive_percentage", 
        "drivePercentageAvg": "drive_percentage_avg", 
        "drivePercentageMax": "drive_percentage_max", 
        "drivePercentageMin": "drive_percentage_min", 
        "id": "id", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "sacl": "sacl", 
        "speed": "speed", 
        "speedAvg": "speed_avg", 
        "speedMax": "speed_max", 
        "speedMin": "speed_min", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.drive_percentage = None
        self.drive_percentage_avg = None
        self.drive_percentage_max = None
        self.drive_percentage_min = None
        self.most_recent = None
        self.sacl = None
        self.speed = None
        self.speed_avg = None
        self.speed_max = None
        self.speed_min = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "EquipmentNetworkElementFanStatsHist", parent_mo_or_dn, **kwargs)
