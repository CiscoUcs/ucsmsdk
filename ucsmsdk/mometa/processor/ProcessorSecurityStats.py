"""This module contains the general information for ProcessorSecurityStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ProcessorSecurityStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ProcessorSecurityStats(ManagedObject):
    """This is ProcessorSecurityStats class."""

    consts = ProcessorSecurityStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcessorSecurityStats", "processorSecurityStats", "security-stats", VersionMeta.Version412a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['processorUnit'], [], [None])

    prop_meta = {
        "psp_correctable_errors": MoPropertyMeta("psp_correctable_errors", "PSPCorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_correctable_errors15_min": MoPropertyMeta("psp_correctable_errors15_min", "PSPCorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_correctable_errors15_min_h": MoPropertyMeta("psp_correctable_errors15_min_h", "PSPCorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_correctable_errors1_day": MoPropertyMeta("psp_correctable_errors1_day", "PSPCorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_correctable_errors1_day_h": MoPropertyMeta("psp_correctable_errors1_day_h", "PSPCorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_correctable_errors1_hour": MoPropertyMeta("psp_correctable_errors1_hour", "PSPCorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_correctable_errors1_hour_h": MoPropertyMeta("psp_correctable_errors1_hour_h", "PSPCorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_correctable_errors1_week": MoPropertyMeta("psp_correctable_errors1_week", "PSPCorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_correctable_errors1_week_h": MoPropertyMeta("psp_correctable_errors1_week_h", "PSPCorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_correctable_errors2_weeks": MoPropertyMeta("psp_correctable_errors2_weeks", "PSPCorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_correctable_errors2_weeks_h": MoPropertyMeta("psp_correctable_errors2_weeks_h", "PSPCorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_uncorrectable_errors": MoPropertyMeta("psp_uncorrectable_errors", "PSPUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_uncorrectable_errors15_min": MoPropertyMeta("psp_uncorrectable_errors15_min", "PSPUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_uncorrectable_errors15_min_h": MoPropertyMeta("psp_uncorrectable_errors15_min_h", "PSPUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_uncorrectable_errors1_day": MoPropertyMeta("psp_uncorrectable_errors1_day", "PSPUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_uncorrectable_errors1_day_h": MoPropertyMeta("psp_uncorrectable_errors1_day_h", "PSPUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_uncorrectable_errors1_hour": MoPropertyMeta("psp_uncorrectable_errors1_hour", "PSPUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_uncorrectable_errors1_hour_h": MoPropertyMeta("psp_uncorrectable_errors1_hour_h", "PSPUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_uncorrectable_errors1_week": MoPropertyMeta("psp_uncorrectable_errors1_week", "PSPUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_uncorrectable_errors1_week_h": MoPropertyMeta("psp_uncorrectable_errors1_week_h", "PSPUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_uncorrectable_errors2_weeks": MoPropertyMeta("psp_uncorrectable_errors2_weeks", "PSPUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "psp_uncorrectable_errors2_weeks_h": MoPropertyMeta("psp_uncorrectable_errors2_weeks_h", "PSPUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
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
        "PSPCorrectableErrors": "psp_correctable_errors", 
        "PSPCorrectableErrors15Min": "psp_correctable_errors15_min", 
        "PSPCorrectableErrors15MinH": "psp_correctable_errors15_min_h", 
        "PSPCorrectableErrors1Day": "psp_correctable_errors1_day", 
        "PSPCorrectableErrors1DayH": "psp_correctable_errors1_day_h", 
        "PSPCorrectableErrors1Hour": "psp_correctable_errors1_hour", 
        "PSPCorrectableErrors1HourH": "psp_correctable_errors1_hour_h", 
        "PSPCorrectableErrors1Week": "psp_correctable_errors1_week", 
        "PSPCorrectableErrors1WeekH": "psp_correctable_errors1_week_h", 
        "PSPCorrectableErrors2Weeks": "psp_correctable_errors2_weeks", 
        "PSPCorrectableErrors2WeeksH": "psp_correctable_errors2_weeks_h", 
        "PSPUncorrectableErrors": "psp_uncorrectable_errors", 
        "PSPUncorrectableErrors15Min": "psp_uncorrectable_errors15_min", 
        "PSPUncorrectableErrors15MinH": "psp_uncorrectable_errors15_min_h", 
        "PSPUncorrectableErrors1Day": "psp_uncorrectable_errors1_day", 
        "PSPUncorrectableErrors1DayH": "psp_uncorrectable_errors1_day_h", 
        "PSPUncorrectableErrors1Hour": "psp_uncorrectable_errors1_hour", 
        "PSPUncorrectableErrors1HourH": "psp_uncorrectable_errors1_hour_h", 
        "PSPUncorrectableErrors1Week": "psp_uncorrectable_errors1_week", 
        "PSPUncorrectableErrors1WeekH": "psp_uncorrectable_errors1_week_h", 
        "PSPUncorrectableErrors2Weeks": "psp_uncorrectable_errors2_weeks", 
        "PSPUncorrectableErrors2WeeksH": "psp_uncorrectable_errors2_weeks_h", 
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
        self.psp_correctable_errors = None
        self.psp_correctable_errors15_min = None
        self.psp_correctable_errors15_min_h = None
        self.psp_correctable_errors1_day = None
        self.psp_correctable_errors1_day_h = None
        self.psp_correctable_errors1_hour = None
        self.psp_correctable_errors1_hour_h = None
        self.psp_correctable_errors1_week = None
        self.psp_correctable_errors1_week_h = None
        self.psp_correctable_errors2_weeks = None
        self.psp_correctable_errors2_weeks_h = None
        self.psp_uncorrectable_errors = None
        self.psp_uncorrectable_errors15_min = None
        self.psp_uncorrectable_errors15_min_h = None
        self.psp_uncorrectable_errors1_day = None
        self.psp_uncorrectable_errors1_day_h = None
        self.psp_uncorrectable_errors1_hour = None
        self.psp_uncorrectable_errors1_hour_h = None
        self.psp_uncorrectable_errors1_week = None
        self.psp_uncorrectable_errors1_week_h = None
        self.psp_uncorrectable_errors2_weeks = None
        self.psp_uncorrectable_errors2_weeks_h = None
        self.child_action = None
        self.intervals = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "ProcessorSecurityStats", parent_mo_or_dn, **kwargs)
