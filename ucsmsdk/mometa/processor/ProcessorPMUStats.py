"""This module contains the general information for ProcessorPMUStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ProcessorPMUStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ProcessorPMUStats(ManagedObject):
    """This is ProcessorPMUStats class."""

    consts = ProcessorPMUStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcessorPMUStats", "processorPMUStats", "pmu-stats", VersionMeta.Version412a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['processorUnit'], [], [None])

    prop_meta = {
        "system_management_unit_correctable_errors": MoPropertyMeta("system_management_unit_correctable_errors", "SystemManagementUnitCorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_correctable_errors15_min": MoPropertyMeta("system_management_unit_correctable_errors15_min", "SystemManagementUnitCorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_correctable_errors15_min_h": MoPropertyMeta("system_management_unit_correctable_errors15_min_h", "SystemManagementUnitCorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_correctable_errors1_day": MoPropertyMeta("system_management_unit_correctable_errors1_day", "SystemManagementUnitCorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_correctable_errors1_day_h": MoPropertyMeta("system_management_unit_correctable_errors1_day_h", "SystemManagementUnitCorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_correctable_errors1_hour": MoPropertyMeta("system_management_unit_correctable_errors1_hour", "SystemManagementUnitCorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_correctable_errors1_hour_h": MoPropertyMeta("system_management_unit_correctable_errors1_hour_h", "SystemManagementUnitCorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_correctable_errors1_week": MoPropertyMeta("system_management_unit_correctable_errors1_week", "SystemManagementUnitCorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_correctable_errors1_week_h": MoPropertyMeta("system_management_unit_correctable_errors1_week_h", "SystemManagementUnitCorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_correctable_errors2_weeks": MoPropertyMeta("system_management_unit_correctable_errors2_weeks", "SystemManagementUnitCorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_correctable_errors2_weeks_h": MoPropertyMeta("system_management_unit_correctable_errors2_weeks_h", "SystemManagementUnitCorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_uncorrectable_errors": MoPropertyMeta("system_management_unit_uncorrectable_errors", "SystemManagementUnitUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_uncorrectable_errors15_min": MoPropertyMeta("system_management_unit_uncorrectable_errors15_min", "SystemManagementUnitUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_uncorrectable_errors15_min_h": MoPropertyMeta("system_management_unit_uncorrectable_errors15_min_h", "SystemManagementUnitUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_uncorrectable_errors1_day": MoPropertyMeta("system_management_unit_uncorrectable_errors1_day", "SystemManagementUnitUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_uncorrectable_errors1_day_h": MoPropertyMeta("system_management_unit_uncorrectable_errors1_day_h", "SystemManagementUnitUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_uncorrectable_errors1_hour": MoPropertyMeta("system_management_unit_uncorrectable_errors1_hour", "SystemManagementUnitUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_uncorrectable_errors1_hour_h": MoPropertyMeta("system_management_unit_uncorrectable_errors1_hour_h", "SystemManagementUnitUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_uncorrectable_errors1_week": MoPropertyMeta("system_management_unit_uncorrectable_errors1_week", "SystemManagementUnitUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_uncorrectable_errors1_week_h": MoPropertyMeta("system_management_unit_uncorrectable_errors1_week_h", "SystemManagementUnitUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_uncorrectable_errors2_weeks": MoPropertyMeta("system_management_unit_uncorrectable_errors2_weeks", "SystemManagementUnitUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "system_management_unit_uncorrectable_errors2_weeks_h": MoPropertyMeta("system_management_unit_uncorrectable_errors2_weeks_h", "SystemManagementUnitUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
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
        "SystemManagementUnitCorrectableErrors": "system_management_unit_correctable_errors", 
        "SystemManagementUnitCorrectableErrors15Min": "system_management_unit_correctable_errors15_min", 
        "SystemManagementUnitCorrectableErrors15MinH": "system_management_unit_correctable_errors15_min_h", 
        "SystemManagementUnitCorrectableErrors1Day": "system_management_unit_correctable_errors1_day", 
        "SystemManagementUnitCorrectableErrors1DayH": "system_management_unit_correctable_errors1_day_h", 
        "SystemManagementUnitCorrectableErrors1Hour": "system_management_unit_correctable_errors1_hour", 
        "SystemManagementUnitCorrectableErrors1HourH": "system_management_unit_correctable_errors1_hour_h", 
        "SystemManagementUnitCorrectableErrors1Week": "system_management_unit_correctable_errors1_week", 
        "SystemManagementUnitCorrectableErrors1WeekH": "system_management_unit_correctable_errors1_week_h", 
        "SystemManagementUnitCorrectableErrors2Weeks": "system_management_unit_correctable_errors2_weeks", 
        "SystemManagementUnitCorrectableErrors2WeeksH": "system_management_unit_correctable_errors2_weeks_h", 
        "SystemManagementUnitUncorrectableErrors": "system_management_unit_uncorrectable_errors", 
        "SystemManagementUnitUncorrectableErrors15Min": "system_management_unit_uncorrectable_errors15_min", 
        "SystemManagementUnitUncorrectableErrors15MinH": "system_management_unit_uncorrectable_errors15_min_h", 
        "SystemManagementUnitUncorrectableErrors1Day": "system_management_unit_uncorrectable_errors1_day", 
        "SystemManagementUnitUncorrectableErrors1DayH": "system_management_unit_uncorrectable_errors1_day_h", 
        "SystemManagementUnitUncorrectableErrors1Hour": "system_management_unit_uncorrectable_errors1_hour", 
        "SystemManagementUnitUncorrectableErrors1HourH": "system_management_unit_uncorrectable_errors1_hour_h", 
        "SystemManagementUnitUncorrectableErrors1Week": "system_management_unit_uncorrectable_errors1_week", 
        "SystemManagementUnitUncorrectableErrors1WeekH": "system_management_unit_uncorrectable_errors1_week_h", 
        "SystemManagementUnitUncorrectableErrors2Weeks": "system_management_unit_uncorrectable_errors2_weeks", 
        "SystemManagementUnitUncorrectableErrors2WeeksH": "system_management_unit_uncorrectable_errors2_weeks_h", 
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
        self.system_management_unit_correctable_errors = None
        self.system_management_unit_correctable_errors15_min = None
        self.system_management_unit_correctable_errors15_min_h = None
        self.system_management_unit_correctable_errors1_day = None
        self.system_management_unit_correctable_errors1_day_h = None
        self.system_management_unit_correctable_errors1_hour = None
        self.system_management_unit_correctable_errors1_hour_h = None
        self.system_management_unit_correctable_errors1_week = None
        self.system_management_unit_correctable_errors1_week_h = None
        self.system_management_unit_correctable_errors2_weeks = None
        self.system_management_unit_correctable_errors2_weeks_h = None
        self.system_management_unit_uncorrectable_errors = None
        self.system_management_unit_uncorrectable_errors15_min = None
        self.system_management_unit_uncorrectable_errors15_min_h = None
        self.system_management_unit_uncorrectable_errors1_day = None
        self.system_management_unit_uncorrectable_errors1_day_h = None
        self.system_management_unit_uncorrectable_errors1_hour = None
        self.system_management_unit_uncorrectable_errors1_hour_h = None
        self.system_management_unit_uncorrectable_errors1_week = None
        self.system_management_unit_uncorrectable_errors1_week_h = None
        self.system_management_unit_uncorrectable_errors2_weeks = None
        self.system_management_unit_uncorrectable_errors2_weeks_h = None
        self.child_action = None
        self.intervals = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "ProcessorPMUStats", parent_mo_or_dn, **kwargs)
