"""This module contains the general information for ComputePCIeFatalCompletionStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePCIeFatalCompletionStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ComputePCIeFatalCompletionStats(ManagedObject):
    """This is ComputePCIeFatalCompletionStats class."""

    consts = ComputePCIeFatalCompletionStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputePCIeFatalCompletionStats", "computePCIeFatalCompletionStats", "pciefat-completion-stats", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['computeBoard'], [], ["Get"])

    prop_meta = {
        "abort_errors": MoPropertyMeta("abort_errors", "AbortErrors", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "abort_errors15_min": MoPropertyMeta("abort_errors15_min", "AbortErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "abort_errors15_min_h": MoPropertyMeta("abort_errors15_min_h", "AbortErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "abort_errors1_day": MoPropertyMeta("abort_errors1_day", "AbortErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "abort_errors1_day_h": MoPropertyMeta("abort_errors1_day_h", "AbortErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "abort_errors1_hour": MoPropertyMeta("abort_errors1_hour", "AbortErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "abort_errors1_hour_h": MoPropertyMeta("abort_errors1_hour_h", "AbortErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "abort_errors1_week": MoPropertyMeta("abort_errors1_week", "AbortErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "abort_errors1_week_h": MoPropertyMeta("abort_errors1_week_h", "AbortErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "abort_errors2_weeks": MoPropertyMeta("abort_errors2_weeks", "AbortErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "abort_errors2_weeks_h": MoPropertyMeta("abort_errors2_weeks_h", "AbortErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "timeout_errors": MoPropertyMeta("timeout_errors", "TimeoutErrors", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "timeout_errors15_min": MoPropertyMeta("timeout_errors15_min", "TimeoutErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "timeout_errors15_min_h": MoPropertyMeta("timeout_errors15_min_h", "TimeoutErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "timeout_errors1_day": MoPropertyMeta("timeout_errors1_day", "TimeoutErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "timeout_errors1_day_h": MoPropertyMeta("timeout_errors1_day_h", "TimeoutErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "timeout_errors1_hour": MoPropertyMeta("timeout_errors1_hour", "TimeoutErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "timeout_errors1_hour_h": MoPropertyMeta("timeout_errors1_hour_h", "TimeoutErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "timeout_errors1_week": MoPropertyMeta("timeout_errors1_week", "TimeoutErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "timeout_errors1_week_h": MoPropertyMeta("timeout_errors1_week_h", "TimeoutErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "timeout_errors2_weeks": MoPropertyMeta("timeout_errors2_weeks", "TimeoutErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "timeout_errors2_weeks_h": MoPropertyMeta("timeout_errors2_weeks_h", "TimeoutErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "unexpected_errors": MoPropertyMeta("unexpected_errors", "unexpectedErrors", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unexpected_errors15_min": MoPropertyMeta("unexpected_errors15_min", "unexpectedErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unexpected_errors15_min_h": MoPropertyMeta("unexpected_errors15_min_h", "unexpectedErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unexpected_errors1_day": MoPropertyMeta("unexpected_errors1_day", "unexpectedErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unexpected_errors1_day_h": MoPropertyMeta("unexpected_errors1_day_h", "unexpectedErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unexpected_errors1_hour": MoPropertyMeta("unexpected_errors1_hour", "unexpectedErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unexpected_errors1_hour_h": MoPropertyMeta("unexpected_errors1_hour_h", "unexpectedErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unexpected_errors1_week": MoPropertyMeta("unexpected_errors1_week", "unexpectedErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unexpected_errors1_week_h": MoPropertyMeta("unexpected_errors1_week_h", "unexpectedErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unexpected_errors2_weeks": MoPropertyMeta("unexpected_errors2_weeks", "unexpectedErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unexpected_errors2_weeks_h": MoPropertyMeta("unexpected_errors2_weeks_h", "unexpectedErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "AbortErrors": "abort_errors", 
        "AbortErrors15Min": "abort_errors15_min", 
        "AbortErrors15MinH": "abort_errors15_min_h", 
        "AbortErrors1Day": "abort_errors1_day", 
        "AbortErrors1DayH": "abort_errors1_day_h", 
        "AbortErrors1Hour": "abort_errors1_hour", 
        "AbortErrors1HourH": "abort_errors1_hour_h", 
        "AbortErrors1Week": "abort_errors1_week", 
        "AbortErrors1WeekH": "abort_errors1_week_h", 
        "AbortErrors2Weeks": "abort_errors2_weeks", 
        "AbortErrors2WeeksH": "abort_errors2_weeks_h", 
        "TimeoutErrors": "timeout_errors", 
        "TimeoutErrors15Min": "timeout_errors15_min", 
        "TimeoutErrors15MinH": "timeout_errors15_min_h", 
        "TimeoutErrors1Day": "timeout_errors1_day", 
        "TimeoutErrors1DayH": "timeout_errors1_day_h", 
        "TimeoutErrors1Hour": "timeout_errors1_hour", 
        "TimeoutErrors1HourH": "timeout_errors1_hour_h", 
        "TimeoutErrors1Week": "timeout_errors1_week", 
        "TimeoutErrors1WeekH": "timeout_errors1_week_h", 
        "TimeoutErrors2Weeks": "timeout_errors2_weeks", 
        "TimeoutErrors2WeeksH": "timeout_errors2_weeks_h", 
        "childAction": "child_action", 
        "dn": "dn", 
        "intervals": "intervals", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "unexpectedErrors": "unexpected_errors", 
        "unexpectedErrors15Min": "unexpected_errors15_min", 
        "unexpectedErrors15MinH": "unexpected_errors15_min_h", 
        "unexpectedErrors1Day": "unexpected_errors1_day", 
        "unexpectedErrors1DayH": "unexpected_errors1_day_h", 
        "unexpectedErrors1Hour": "unexpected_errors1_hour", 
        "unexpectedErrors1HourH": "unexpected_errors1_hour_h", 
        "unexpectedErrors1Week": "unexpected_errors1_week", 
        "unexpectedErrors1WeekH": "unexpected_errors1_week_h", 
        "unexpectedErrors2Weeks": "unexpected_errors2_weeks", 
        "unexpectedErrors2WeeksH": "unexpected_errors2_weeks_h", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.abort_errors = None
        self.abort_errors15_min = None
        self.abort_errors15_min_h = None
        self.abort_errors1_day = None
        self.abort_errors1_day_h = None
        self.abort_errors1_hour = None
        self.abort_errors1_hour_h = None
        self.abort_errors1_week = None
        self.abort_errors1_week_h = None
        self.abort_errors2_weeks = None
        self.abort_errors2_weeks_h = None
        self.timeout_errors = None
        self.timeout_errors15_min = None
        self.timeout_errors15_min_h = None
        self.timeout_errors1_day = None
        self.timeout_errors1_day_h = None
        self.timeout_errors1_hour = None
        self.timeout_errors1_hour_h = None
        self.timeout_errors1_week = None
        self.timeout_errors1_week_h = None
        self.timeout_errors2_weeks = None
        self.timeout_errors2_weeks_h = None
        self.child_action = None
        self.intervals = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.unexpected_errors = None
        self.unexpected_errors15_min = None
        self.unexpected_errors15_min_h = None
        self.unexpected_errors1_day = None
        self.unexpected_errors1_day_h = None
        self.unexpected_errors1_hour = None
        self.unexpected_errors1_hour_h = None
        self.unexpected_errors1_week = None
        self.unexpected_errors1_week_h = None
        self.unexpected_errors2_weeks = None
        self.unexpected_errors2_weeks_h = None
        self.update = None

        ManagedObject.__init__(self, "ComputePCIeFatalCompletionStats", parent_mo_or_dn, **kwargs)
