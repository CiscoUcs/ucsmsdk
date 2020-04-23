"""This module contains the general information for StorageSsdHealthStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageSsdHealthStatsConsts:
    PERCENTAGE_LIFE_LEFT_N_A = "N/A"
    PERCENTAGE_LIFE_LEFT_AVG_N_A = "N/A"
    PERCENTAGE_LIFE_LEFT_MAX_N_A = "N/A"
    PERCENTAGE_LIFE_LEFT_MIN_N_A = "N/A"
    POWER_CYCLE_COUNT_N_A = "N/A"
    POWER_CYCLE_COUNT_AVG_N_A = "N/A"
    POWER_CYCLE_COUNT_MAX_N_A = "N/A"
    POWER_CYCLE_COUNT_MIN_N_A = "N/A"
    POWER_ON_HOURS_N_A = "N/A"
    POWER_ON_HOURS_AVG_N_A = "N/A"
    POWER_ON_HOURS_MAX_N_A = "N/A"
    POWER_ON_HOURS_MIN_N_A = "N/A"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"
    WEAR_STATUS_IN_DAYS_N_A = "N/A"
    WEAR_STATUS_IN_DAYS_AVG_N_A = "N/A"
    WEAR_STATUS_IN_DAYS_MAX_N_A = "N/A"
    WEAR_STATUS_IN_DAYS_MIN_N_A = "N/A"


class StorageSsdHealthStats(ManagedObject):
    """This is StorageSsdHealthStats class."""

    consts = StorageSsdHealthStatsConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("StorageSsdHealthStats", "storageSsdHealthStats", "ssd-health-stats-[id]", VersionMeta.Version321d, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['storageLocalDisk'], ['storageSsdHealthStatsHist'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version321d, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "percentage_life_left": MoPropertyMeta("percentage_life_left", "percentageLifeLeft", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]),
        "percentage_life_left_avg": MoPropertyMeta("percentage_life_left_avg", "percentageLifeLeftAvg", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]),
        "percentage_life_left_max": MoPropertyMeta("percentage_life_left_max", "percentageLifeLeftMax", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]),
        "percentage_life_left_min": MoPropertyMeta("percentage_life_left_min", "percentageLifeLeftMin", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-4294967295"]),
        "power_cycle_count": MoPropertyMeta("power_cycle_count", "powerCycleCount", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-18446744073709551615"]),
        "power_cycle_count_avg": MoPropertyMeta("power_cycle_count_avg", "powerCycleCountAvg", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-18446744073709551615"]),
        "power_cycle_count_max": MoPropertyMeta("power_cycle_count_max", "powerCycleCountMax", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-18446744073709551615"]),
        "power_cycle_count_min": MoPropertyMeta("power_cycle_count_min", "powerCycleCountMin", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-18446744073709551615"]),
        "power_on_hours": MoPropertyMeta("power_on_hours", "powerOnHours", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-18446744073709551615"]),
        "power_on_hours_avg": MoPropertyMeta("power_on_hours_avg", "powerOnHoursAvg", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-18446744073709551615"]),
        "power_on_hours_max": MoPropertyMeta("power_on_hours_max", "powerOnHoursMax", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-18446744073709551615"]),
        "power_on_hours_min": MoPropertyMeta("power_on_hours_min", "powerOnHoursMin", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-18446744073709551615"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "wear_status_in_days": MoPropertyMeta("wear_status_in_days", "wearStatusInDays", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-18446744073709551615"]),
        "wear_status_in_days_avg": MoPropertyMeta("wear_status_in_days_avg", "wearStatusInDaysAvg", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-18446744073709551615"]),
        "wear_status_in_days_max": MoPropertyMeta("wear_status_in_days_max", "wearStatusInDaysMax", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-18446744073709551615"]),
        "wear_status_in_days_min": MoPropertyMeta("wear_status_in_days_min", "wearStatusInDaysMin", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-18446744073709551615"]),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "intervals": "intervals", 
        "percentageLifeLeft": "percentage_life_left", 
        "percentageLifeLeftAvg": "percentage_life_left_avg", 
        "percentageLifeLeftMax": "percentage_life_left_max", 
        "percentageLifeLeftMin": "percentage_life_left_min", 
        "powerCycleCount": "power_cycle_count", 
        "powerCycleCountAvg": "power_cycle_count_avg", 
        "powerCycleCountMax": "power_cycle_count_max", 
        "powerCycleCountMin": "power_cycle_count_min", 
        "powerOnHours": "power_on_hours", 
        "powerOnHoursAvg": "power_on_hours_avg", 
        "powerOnHoursMax": "power_on_hours_max", 
        "powerOnHoursMin": "power_on_hours_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
        "wearStatusInDays": "wear_status_in_days", 
        "wearStatusInDaysAvg": "wear_status_in_days_avg", 
        "wearStatusInDaysMax": "wear_status_in_days_max", 
        "wearStatusInDaysMin": "wear_status_in_days_min", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.intervals = None
        self.percentage_life_left = None
        self.percentage_life_left_avg = None
        self.percentage_life_left_max = None
        self.percentage_life_left_min = None
        self.power_cycle_count = None
        self.power_cycle_count_avg = None
        self.power_cycle_count_max = None
        self.power_cycle_count_min = None
        self.power_on_hours = None
        self.power_on_hours_avg = None
        self.power_on_hours_max = None
        self.power_on_hours_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None
        self.wear_status_in_days = None
        self.wear_status_in_days_avg = None
        self.wear_status_in_days_max = None
        self.wear_status_in_days_min = None

        ManagedObject.__init__(self, "StorageSsdHealthStats", parent_mo_or_dn, **kwargs)
