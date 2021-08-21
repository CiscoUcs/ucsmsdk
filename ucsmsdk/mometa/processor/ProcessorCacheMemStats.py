"""This module contains the general information for ProcessorCacheMemStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ProcessorCacheMemStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ProcessorCacheMemStats(ManagedObject):
    """This is ProcessorCacheMemStats class."""

    consts = ProcessorCacheMemStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcessorCacheMemStats", "processorCacheMemStats", "cache-mem-stats", VersionMeta.Version412a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['processorUnit'], [], [None])

    prop_meta = {
        "l2_cache_unit_correctable_errors": MoPropertyMeta("l2_cache_unit_correctable_errors", "L2CacheUnitCorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_correctable_errors15_min": MoPropertyMeta("l2_cache_unit_correctable_errors15_min", "L2CacheUnitCorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_correctable_errors15_min_h": MoPropertyMeta("l2_cache_unit_correctable_errors15_min_h", "L2CacheUnitCorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_correctable_errors1_day": MoPropertyMeta("l2_cache_unit_correctable_errors1_day", "L2CacheUnitCorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_correctable_errors1_day_h": MoPropertyMeta("l2_cache_unit_correctable_errors1_day_h", "L2CacheUnitCorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_correctable_errors1_hour": MoPropertyMeta("l2_cache_unit_correctable_errors1_hour", "L2CacheUnitCorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_correctable_errors1_hour_h": MoPropertyMeta("l2_cache_unit_correctable_errors1_hour_h", "L2CacheUnitCorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_correctable_errors1_week": MoPropertyMeta("l2_cache_unit_correctable_errors1_week", "L2CacheUnitCorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_correctable_errors1_week_h": MoPropertyMeta("l2_cache_unit_correctable_errors1_week_h", "L2CacheUnitCorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_correctable_errors2_weeks": MoPropertyMeta("l2_cache_unit_correctable_errors2_weeks", "L2CacheUnitCorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_correctable_errors2_weeks_h": MoPropertyMeta("l2_cache_unit_correctable_errors2_weeks_h", "L2CacheUnitCorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_uncorrectable_errors": MoPropertyMeta("l2_cache_unit_uncorrectable_errors", "L2CacheUnitUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_uncorrectable_errors15_min": MoPropertyMeta("l2_cache_unit_uncorrectable_errors15_min", "L2CacheUnitUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_uncorrectable_errors15_min_h": MoPropertyMeta("l2_cache_unit_uncorrectable_errors15_min_h", "L2CacheUnitUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_uncorrectable_errors1_day": MoPropertyMeta("l2_cache_unit_uncorrectable_errors1_day", "L2CacheUnitUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_uncorrectable_errors1_day_h": MoPropertyMeta("l2_cache_unit_uncorrectable_errors1_day_h", "L2CacheUnitUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_uncorrectable_errors1_hour": MoPropertyMeta("l2_cache_unit_uncorrectable_errors1_hour", "L2CacheUnitUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_uncorrectable_errors1_hour_h": MoPropertyMeta("l2_cache_unit_uncorrectable_errors1_hour_h", "L2CacheUnitUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_uncorrectable_errors1_week": MoPropertyMeta("l2_cache_unit_uncorrectable_errors1_week", "L2CacheUnitUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_uncorrectable_errors1_week_h": MoPropertyMeta("l2_cache_unit_uncorrectable_errors1_week_h", "L2CacheUnitUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_uncorrectable_errors2_weeks": MoPropertyMeta("l2_cache_unit_uncorrectable_errors2_weeks", "L2CacheUnitUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l2_cache_unit_uncorrectable_errors2_weeks_h": MoPropertyMeta("l2_cache_unit_uncorrectable_errors2_weeks_h", "L2CacheUnitUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_correctable_errors": MoPropertyMeta("l3_cache_unit_correctable_errors", "L3CacheUnitCorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_correctable_errors15_min": MoPropertyMeta("l3_cache_unit_correctable_errors15_min", "L3CacheUnitCorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_correctable_errors15_min_h": MoPropertyMeta("l3_cache_unit_correctable_errors15_min_h", "L3CacheUnitCorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_correctable_errors1_day": MoPropertyMeta("l3_cache_unit_correctable_errors1_day", "L3CacheUnitCorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_correctable_errors1_day_h": MoPropertyMeta("l3_cache_unit_correctable_errors1_day_h", "L3CacheUnitCorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_correctable_errors1_hour": MoPropertyMeta("l3_cache_unit_correctable_errors1_hour", "L3CacheUnitCorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_correctable_errors1_hour_h": MoPropertyMeta("l3_cache_unit_correctable_errors1_hour_h", "L3CacheUnitCorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_correctable_errors1_week": MoPropertyMeta("l3_cache_unit_correctable_errors1_week", "L3CacheUnitCorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_correctable_errors1_week_h": MoPropertyMeta("l3_cache_unit_correctable_errors1_week_h", "L3CacheUnitCorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_correctable_errors2_weeks": MoPropertyMeta("l3_cache_unit_correctable_errors2_weeks", "L3CacheUnitCorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_correctable_errors2_weeks_h": MoPropertyMeta("l3_cache_unit_correctable_errors2_weeks_h", "L3CacheUnitCorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_uncorrectable_errors": MoPropertyMeta("l3_cache_unit_uncorrectable_errors", "L3CacheUnitUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_uncorrectable_errors15_min": MoPropertyMeta("l3_cache_unit_uncorrectable_errors15_min", "L3CacheUnitUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_uncorrectable_errors15_min_h": MoPropertyMeta("l3_cache_unit_uncorrectable_errors15_min_h", "L3CacheUnitUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_uncorrectable_errors1_day": MoPropertyMeta("l3_cache_unit_uncorrectable_errors1_day", "L3CacheUnitUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_uncorrectable_errors1_day_h": MoPropertyMeta("l3_cache_unit_uncorrectable_errors1_day_h", "L3CacheUnitUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_uncorrectable_errors1_hour": MoPropertyMeta("l3_cache_unit_uncorrectable_errors1_hour", "L3CacheUnitUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_uncorrectable_errors1_hour_h": MoPropertyMeta("l3_cache_unit_uncorrectable_errors1_hour_h", "L3CacheUnitUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_uncorrectable_errors1_week": MoPropertyMeta("l3_cache_unit_uncorrectable_errors1_week", "L3CacheUnitUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_uncorrectable_errors1_week_h": MoPropertyMeta("l3_cache_unit_uncorrectable_errors1_week_h", "L3CacheUnitUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_uncorrectable_errors2_weeks": MoPropertyMeta("l3_cache_unit_uncorrectable_errors2_weeks", "L3CacheUnitUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "l3_cache_unit_uncorrectable_errors2_weeks_h": MoPropertyMeta("l3_cache_unit_uncorrectable_errors2_weeks_h", "L3CacheUnitUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mem_testcorrectable_errors": MoPropertyMeta("mem_testcorrectable_errors", "MemTestcorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mem_testcorrectable_errors15_min": MoPropertyMeta("mem_testcorrectable_errors15_min", "MemTestcorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mem_testcorrectable_errors15_min_h": MoPropertyMeta("mem_testcorrectable_errors15_min_h", "MemTestcorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mem_testcorrectable_errors1_day": MoPropertyMeta("mem_testcorrectable_errors1_day", "MemTestcorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mem_testcorrectable_errors1_day_h": MoPropertyMeta("mem_testcorrectable_errors1_day_h", "MemTestcorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mem_testcorrectable_errors1_hour": MoPropertyMeta("mem_testcorrectable_errors1_hour", "MemTestcorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mem_testcorrectable_errors1_hour_h": MoPropertyMeta("mem_testcorrectable_errors1_hour_h", "MemTestcorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mem_testcorrectable_errors1_week": MoPropertyMeta("mem_testcorrectable_errors1_week", "MemTestcorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mem_testcorrectable_errors1_week_h": MoPropertyMeta("mem_testcorrectable_errors1_week_h", "MemTestcorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mem_testcorrectable_errors2_weeks": MoPropertyMeta("mem_testcorrectable_errors2_weeks", "MemTestcorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mem_testcorrectable_errors2_weeks_h": MoPropertyMeta("mem_testcorrectable_errors2_weeks_h", "MemTestcorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "L2CacheUnitCorrectableErrors": "l2_cache_unit_correctable_errors", 
        "L2CacheUnitCorrectableErrors15Min": "l2_cache_unit_correctable_errors15_min", 
        "L2CacheUnitCorrectableErrors15MinH": "l2_cache_unit_correctable_errors15_min_h", 
        "L2CacheUnitCorrectableErrors1Day": "l2_cache_unit_correctable_errors1_day", 
        "L2CacheUnitCorrectableErrors1DayH": "l2_cache_unit_correctable_errors1_day_h", 
        "L2CacheUnitCorrectableErrors1Hour": "l2_cache_unit_correctable_errors1_hour", 
        "L2CacheUnitCorrectableErrors1HourH": "l2_cache_unit_correctable_errors1_hour_h", 
        "L2CacheUnitCorrectableErrors1Week": "l2_cache_unit_correctable_errors1_week", 
        "L2CacheUnitCorrectableErrors1WeekH": "l2_cache_unit_correctable_errors1_week_h", 
        "L2CacheUnitCorrectableErrors2Weeks": "l2_cache_unit_correctable_errors2_weeks", 
        "L2CacheUnitCorrectableErrors2WeeksH": "l2_cache_unit_correctable_errors2_weeks_h", 
        "L2CacheUnitUncorrectableErrors": "l2_cache_unit_uncorrectable_errors", 
        "L2CacheUnitUncorrectableErrors15Min": "l2_cache_unit_uncorrectable_errors15_min", 
        "L2CacheUnitUncorrectableErrors15MinH": "l2_cache_unit_uncorrectable_errors15_min_h", 
        "L2CacheUnitUncorrectableErrors1Day": "l2_cache_unit_uncorrectable_errors1_day", 
        "L2CacheUnitUncorrectableErrors1DayH": "l2_cache_unit_uncorrectable_errors1_day_h", 
        "L2CacheUnitUncorrectableErrors1Hour": "l2_cache_unit_uncorrectable_errors1_hour", 
        "L2CacheUnitUncorrectableErrors1HourH": "l2_cache_unit_uncorrectable_errors1_hour_h", 
        "L2CacheUnitUncorrectableErrors1Week": "l2_cache_unit_uncorrectable_errors1_week", 
        "L2CacheUnitUncorrectableErrors1WeekH": "l2_cache_unit_uncorrectable_errors1_week_h", 
        "L2CacheUnitUncorrectableErrors2Weeks": "l2_cache_unit_uncorrectable_errors2_weeks", 
        "L2CacheUnitUncorrectableErrors2WeeksH": "l2_cache_unit_uncorrectable_errors2_weeks_h", 
        "L3CacheUnitCorrectableErrors": "l3_cache_unit_correctable_errors", 
        "L3CacheUnitCorrectableErrors15Min": "l3_cache_unit_correctable_errors15_min", 
        "L3CacheUnitCorrectableErrors15MinH": "l3_cache_unit_correctable_errors15_min_h", 
        "L3CacheUnitCorrectableErrors1Day": "l3_cache_unit_correctable_errors1_day", 
        "L3CacheUnitCorrectableErrors1DayH": "l3_cache_unit_correctable_errors1_day_h", 
        "L3CacheUnitCorrectableErrors1Hour": "l3_cache_unit_correctable_errors1_hour", 
        "L3CacheUnitCorrectableErrors1HourH": "l3_cache_unit_correctable_errors1_hour_h", 
        "L3CacheUnitCorrectableErrors1Week": "l3_cache_unit_correctable_errors1_week", 
        "L3CacheUnitCorrectableErrors1WeekH": "l3_cache_unit_correctable_errors1_week_h", 
        "L3CacheUnitCorrectableErrors2Weeks": "l3_cache_unit_correctable_errors2_weeks", 
        "L3CacheUnitCorrectableErrors2WeeksH": "l3_cache_unit_correctable_errors2_weeks_h", 
        "L3CacheUnitUncorrectableErrors": "l3_cache_unit_uncorrectable_errors", 
        "L3CacheUnitUncorrectableErrors15Min": "l3_cache_unit_uncorrectable_errors15_min", 
        "L3CacheUnitUncorrectableErrors15MinH": "l3_cache_unit_uncorrectable_errors15_min_h", 
        "L3CacheUnitUncorrectableErrors1Day": "l3_cache_unit_uncorrectable_errors1_day", 
        "L3CacheUnitUncorrectableErrors1DayH": "l3_cache_unit_uncorrectable_errors1_day_h", 
        "L3CacheUnitUncorrectableErrors1Hour": "l3_cache_unit_uncorrectable_errors1_hour", 
        "L3CacheUnitUncorrectableErrors1HourH": "l3_cache_unit_uncorrectable_errors1_hour_h", 
        "L3CacheUnitUncorrectableErrors1Week": "l3_cache_unit_uncorrectable_errors1_week", 
        "L3CacheUnitUncorrectableErrors1WeekH": "l3_cache_unit_uncorrectable_errors1_week_h", 
        "L3CacheUnitUncorrectableErrors2Weeks": "l3_cache_unit_uncorrectable_errors2_weeks", 
        "L3CacheUnitUncorrectableErrors2WeeksH": "l3_cache_unit_uncorrectable_errors2_weeks_h", 
        "MemTestcorrectableErrors": "mem_testcorrectable_errors", 
        "MemTestcorrectableErrors15Min": "mem_testcorrectable_errors15_min", 
        "MemTestcorrectableErrors15MinH": "mem_testcorrectable_errors15_min_h", 
        "MemTestcorrectableErrors1Day": "mem_testcorrectable_errors1_day", 
        "MemTestcorrectableErrors1DayH": "mem_testcorrectable_errors1_day_h", 
        "MemTestcorrectableErrors1Hour": "mem_testcorrectable_errors1_hour", 
        "MemTestcorrectableErrors1HourH": "mem_testcorrectable_errors1_hour_h", 
        "MemTestcorrectableErrors1Week": "mem_testcorrectable_errors1_week", 
        "MemTestcorrectableErrors1WeekH": "mem_testcorrectable_errors1_week_h", 
        "MemTestcorrectableErrors2Weeks": "mem_testcorrectable_errors2_weeks", 
        "MemTestcorrectableErrors2WeeksH": "mem_testcorrectable_errors2_weeks_h", 
        "childAction": "child_action", 
        "dn": "dn", 
        "intervals": "intervals", 
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
        self.l2_cache_unit_correctable_errors = None
        self.l2_cache_unit_correctable_errors15_min = None
        self.l2_cache_unit_correctable_errors15_min_h = None
        self.l2_cache_unit_correctable_errors1_day = None
        self.l2_cache_unit_correctable_errors1_day_h = None
        self.l2_cache_unit_correctable_errors1_hour = None
        self.l2_cache_unit_correctable_errors1_hour_h = None
        self.l2_cache_unit_correctable_errors1_week = None
        self.l2_cache_unit_correctable_errors1_week_h = None
        self.l2_cache_unit_correctable_errors2_weeks = None
        self.l2_cache_unit_correctable_errors2_weeks_h = None
        self.l2_cache_unit_uncorrectable_errors = None
        self.l2_cache_unit_uncorrectable_errors15_min = None
        self.l2_cache_unit_uncorrectable_errors15_min_h = None
        self.l2_cache_unit_uncorrectable_errors1_day = None
        self.l2_cache_unit_uncorrectable_errors1_day_h = None
        self.l2_cache_unit_uncorrectable_errors1_hour = None
        self.l2_cache_unit_uncorrectable_errors1_hour_h = None
        self.l2_cache_unit_uncorrectable_errors1_week = None
        self.l2_cache_unit_uncorrectable_errors1_week_h = None
        self.l2_cache_unit_uncorrectable_errors2_weeks = None
        self.l2_cache_unit_uncorrectable_errors2_weeks_h = None
        self.l3_cache_unit_correctable_errors = None
        self.l3_cache_unit_correctable_errors15_min = None
        self.l3_cache_unit_correctable_errors15_min_h = None
        self.l3_cache_unit_correctable_errors1_day = None
        self.l3_cache_unit_correctable_errors1_day_h = None
        self.l3_cache_unit_correctable_errors1_hour = None
        self.l3_cache_unit_correctable_errors1_hour_h = None
        self.l3_cache_unit_correctable_errors1_week = None
        self.l3_cache_unit_correctable_errors1_week_h = None
        self.l3_cache_unit_correctable_errors2_weeks = None
        self.l3_cache_unit_correctable_errors2_weeks_h = None
        self.l3_cache_unit_uncorrectable_errors = None
        self.l3_cache_unit_uncorrectable_errors15_min = None
        self.l3_cache_unit_uncorrectable_errors15_min_h = None
        self.l3_cache_unit_uncorrectable_errors1_day = None
        self.l3_cache_unit_uncorrectable_errors1_day_h = None
        self.l3_cache_unit_uncorrectable_errors1_hour = None
        self.l3_cache_unit_uncorrectable_errors1_hour_h = None
        self.l3_cache_unit_uncorrectable_errors1_week = None
        self.l3_cache_unit_uncorrectable_errors1_week_h = None
        self.l3_cache_unit_uncorrectable_errors2_weeks = None
        self.l3_cache_unit_uncorrectable_errors2_weeks_h = None
        self.mem_testcorrectable_errors = None
        self.mem_testcorrectable_errors15_min = None
        self.mem_testcorrectable_errors15_min_h = None
        self.mem_testcorrectable_errors1_day = None
        self.mem_testcorrectable_errors1_day_h = None
        self.mem_testcorrectable_errors1_hour = None
        self.mem_testcorrectable_errors1_hour_h = None
        self.mem_testcorrectable_errors1_week = None
        self.mem_testcorrectable_errors1_week_h = None
        self.mem_testcorrectable_errors2_weeks = None
        self.mem_testcorrectable_errors2_weeks_h = None
        self.child_action = None
        self.intervals = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "ProcessorCacheMemStats", parent_mo_or_dn, **kwargs)
