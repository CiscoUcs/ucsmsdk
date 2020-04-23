"""This module contains the general information for ComputePCIeFatalReceiveStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePCIeFatalReceiveStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ComputePCIeFatalReceiveStats(ManagedObject):
    """This is ComputePCIeFatalReceiveStats class."""

    consts = ComputePCIeFatalReceiveStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputePCIeFatalReceiveStats", "computePCIeFatalReceiveStats", "pciefat-receive-stats", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['computeBoard'], [], ["Get"])

    prop_meta = {
        "buffer_overflow_errors": MoPropertyMeta("buffer_overflow_errors", "bufferOverflowErrors", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "buffer_overflow_errors15_min": MoPropertyMeta("buffer_overflow_errors15_min", "bufferOverflowErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "buffer_overflow_errors15_min_h": MoPropertyMeta("buffer_overflow_errors15_min_h", "bufferOverflowErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "buffer_overflow_errors1_day": MoPropertyMeta("buffer_overflow_errors1_day", "bufferOverflowErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "buffer_overflow_errors1_day_h": MoPropertyMeta("buffer_overflow_errors1_day_h", "bufferOverflowErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "buffer_overflow_errors1_hour": MoPropertyMeta("buffer_overflow_errors1_hour", "bufferOverflowErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "buffer_overflow_errors1_hour_h": MoPropertyMeta("buffer_overflow_errors1_hour_h", "bufferOverflowErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "buffer_overflow_errors1_week": MoPropertyMeta("buffer_overflow_errors1_week", "bufferOverflowErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "buffer_overflow_errors1_week_h": MoPropertyMeta("buffer_overflow_errors1_week_h", "bufferOverflowErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "buffer_overflow_errors2_weeks": MoPropertyMeta("buffer_overflow_errors2_weeks", "bufferOverflowErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "buffer_overflow_errors2_weeks_h": MoPropertyMeta("buffer_overflow_errors2_weeks_h", "bufferOverflowErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "err_fatal_errors": MoPropertyMeta("err_fatal_errors", "errFatalErrors", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_fatal_errors15_min": MoPropertyMeta("err_fatal_errors15_min", "errFatalErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_fatal_errors15_min_h": MoPropertyMeta("err_fatal_errors15_min_h", "errFatalErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_fatal_errors1_day": MoPropertyMeta("err_fatal_errors1_day", "errFatalErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_fatal_errors1_day_h": MoPropertyMeta("err_fatal_errors1_day_h", "errFatalErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_fatal_errors1_hour": MoPropertyMeta("err_fatal_errors1_hour", "errFatalErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_fatal_errors1_hour_h": MoPropertyMeta("err_fatal_errors1_hour_h", "errFatalErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_fatal_errors1_week": MoPropertyMeta("err_fatal_errors1_week", "errFatalErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_fatal_errors1_week_h": MoPropertyMeta("err_fatal_errors1_week_h", "errFatalErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_fatal_errors2_weeks": MoPropertyMeta("err_fatal_errors2_weeks", "errFatalErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_fatal_errors2_weeks_h": MoPropertyMeta("err_fatal_errors2_weeks_h", "errFatalErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_non_fatal_errors": MoPropertyMeta("err_non_fatal_errors", "errNonFatalErrors", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_non_fatal_errors15_min": MoPropertyMeta("err_non_fatal_errors15_min", "errNonFatalErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_non_fatal_errors15_min_h": MoPropertyMeta("err_non_fatal_errors15_min_h", "errNonFatalErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_non_fatal_errors1_day": MoPropertyMeta("err_non_fatal_errors1_day", "errNonFatalErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_non_fatal_errors1_day_h": MoPropertyMeta("err_non_fatal_errors1_day_h", "errNonFatalErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_non_fatal_errors1_hour": MoPropertyMeta("err_non_fatal_errors1_hour", "errNonFatalErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_non_fatal_errors1_hour_h": MoPropertyMeta("err_non_fatal_errors1_hour_h", "errNonFatalErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_non_fatal_errors1_week": MoPropertyMeta("err_non_fatal_errors1_week", "errNonFatalErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_non_fatal_errors1_week_h": MoPropertyMeta("err_non_fatal_errors1_week_h", "errNonFatalErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_non_fatal_errors2_weeks": MoPropertyMeta("err_non_fatal_errors2_weeks", "errNonFatalErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "err_non_fatal_errors2_weeks_h": MoPropertyMeta("err_non_fatal_errors2_weeks_h", "errNonFatalErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "unsupported_request_errors": MoPropertyMeta("unsupported_request_errors", "unsupportedRequestErrors", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unsupported_request_errors15_min": MoPropertyMeta("unsupported_request_errors15_min", "unsupportedRequestErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unsupported_request_errors15_min_h": MoPropertyMeta("unsupported_request_errors15_min_h", "unsupportedRequestErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unsupported_request_errors1_day": MoPropertyMeta("unsupported_request_errors1_day", "unsupportedRequestErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unsupported_request_errors1_day_h": MoPropertyMeta("unsupported_request_errors1_day_h", "unsupportedRequestErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unsupported_request_errors1_hour": MoPropertyMeta("unsupported_request_errors1_hour", "unsupportedRequestErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unsupported_request_errors1_hour_h": MoPropertyMeta("unsupported_request_errors1_hour_h", "unsupportedRequestErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unsupported_request_errors1_week": MoPropertyMeta("unsupported_request_errors1_week", "unsupportedRequestErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unsupported_request_errors1_week_h": MoPropertyMeta("unsupported_request_errors1_week_h", "unsupportedRequestErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unsupported_request_errors2_weeks": MoPropertyMeta("unsupported_request_errors2_weeks", "unsupportedRequestErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unsupported_request_errors2_weeks_h": MoPropertyMeta("unsupported_request_errors2_weeks_h", "unsupportedRequestErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "bufferOverflowErrors": "buffer_overflow_errors", 
        "bufferOverflowErrors15Min": "buffer_overflow_errors15_min", 
        "bufferOverflowErrors15MinH": "buffer_overflow_errors15_min_h", 
        "bufferOverflowErrors1Day": "buffer_overflow_errors1_day", 
        "bufferOverflowErrors1DayH": "buffer_overflow_errors1_day_h", 
        "bufferOverflowErrors1Hour": "buffer_overflow_errors1_hour", 
        "bufferOverflowErrors1HourH": "buffer_overflow_errors1_hour_h", 
        "bufferOverflowErrors1Week": "buffer_overflow_errors1_week", 
        "bufferOverflowErrors1WeekH": "buffer_overflow_errors1_week_h", 
        "bufferOverflowErrors2Weeks": "buffer_overflow_errors2_weeks", 
        "bufferOverflowErrors2WeeksH": "buffer_overflow_errors2_weeks_h", 
        "childAction": "child_action", 
        "dn": "dn", 
        "errFatalErrors": "err_fatal_errors", 
        "errFatalErrors15Min": "err_fatal_errors15_min", 
        "errFatalErrors15MinH": "err_fatal_errors15_min_h", 
        "errFatalErrors1Day": "err_fatal_errors1_day", 
        "errFatalErrors1DayH": "err_fatal_errors1_day_h", 
        "errFatalErrors1Hour": "err_fatal_errors1_hour", 
        "errFatalErrors1HourH": "err_fatal_errors1_hour_h", 
        "errFatalErrors1Week": "err_fatal_errors1_week", 
        "errFatalErrors1WeekH": "err_fatal_errors1_week_h", 
        "errFatalErrors2Weeks": "err_fatal_errors2_weeks", 
        "errFatalErrors2WeeksH": "err_fatal_errors2_weeks_h", 
        "errNonFatalErrors": "err_non_fatal_errors", 
        "errNonFatalErrors15Min": "err_non_fatal_errors15_min", 
        "errNonFatalErrors15MinH": "err_non_fatal_errors15_min_h", 
        "errNonFatalErrors1Day": "err_non_fatal_errors1_day", 
        "errNonFatalErrors1DayH": "err_non_fatal_errors1_day_h", 
        "errNonFatalErrors1Hour": "err_non_fatal_errors1_hour", 
        "errNonFatalErrors1HourH": "err_non_fatal_errors1_hour_h", 
        "errNonFatalErrors1Week": "err_non_fatal_errors1_week", 
        "errNonFatalErrors1WeekH": "err_non_fatal_errors1_week_h", 
        "errNonFatalErrors2Weeks": "err_non_fatal_errors2_weeks", 
        "errNonFatalErrors2WeeksH": "err_non_fatal_errors2_weeks_h", 
        "intervals": "intervals", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "unsupportedRequestErrors": "unsupported_request_errors", 
        "unsupportedRequestErrors15Min": "unsupported_request_errors15_min", 
        "unsupportedRequestErrors15MinH": "unsupported_request_errors15_min_h", 
        "unsupportedRequestErrors1Day": "unsupported_request_errors1_day", 
        "unsupportedRequestErrors1DayH": "unsupported_request_errors1_day_h", 
        "unsupportedRequestErrors1Hour": "unsupported_request_errors1_hour", 
        "unsupportedRequestErrors1HourH": "unsupported_request_errors1_hour_h", 
        "unsupportedRequestErrors1Week": "unsupported_request_errors1_week", 
        "unsupportedRequestErrors1WeekH": "unsupported_request_errors1_week_h", 
        "unsupportedRequestErrors2Weeks": "unsupported_request_errors2_weeks", 
        "unsupportedRequestErrors2WeeksH": "unsupported_request_errors2_weeks_h", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.buffer_overflow_errors = None
        self.buffer_overflow_errors15_min = None
        self.buffer_overflow_errors15_min_h = None
        self.buffer_overflow_errors1_day = None
        self.buffer_overflow_errors1_day_h = None
        self.buffer_overflow_errors1_hour = None
        self.buffer_overflow_errors1_hour_h = None
        self.buffer_overflow_errors1_week = None
        self.buffer_overflow_errors1_week_h = None
        self.buffer_overflow_errors2_weeks = None
        self.buffer_overflow_errors2_weeks_h = None
        self.child_action = None
        self.err_fatal_errors = None
        self.err_fatal_errors15_min = None
        self.err_fatal_errors15_min_h = None
        self.err_fatal_errors1_day = None
        self.err_fatal_errors1_day_h = None
        self.err_fatal_errors1_hour = None
        self.err_fatal_errors1_hour_h = None
        self.err_fatal_errors1_week = None
        self.err_fatal_errors1_week_h = None
        self.err_fatal_errors2_weeks = None
        self.err_fatal_errors2_weeks_h = None
        self.err_non_fatal_errors = None
        self.err_non_fatal_errors15_min = None
        self.err_non_fatal_errors15_min_h = None
        self.err_non_fatal_errors1_day = None
        self.err_non_fatal_errors1_day_h = None
        self.err_non_fatal_errors1_hour = None
        self.err_non_fatal_errors1_hour_h = None
        self.err_non_fatal_errors1_week = None
        self.err_non_fatal_errors1_week_h = None
        self.err_non_fatal_errors2_weeks = None
        self.err_non_fatal_errors2_weeks_h = None
        self.intervals = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.unsupported_request_errors = None
        self.unsupported_request_errors15_min = None
        self.unsupported_request_errors15_min_h = None
        self.unsupported_request_errors1_day = None
        self.unsupported_request_errors1_day_h = None
        self.unsupported_request_errors1_hour = None
        self.unsupported_request_errors1_hour_h = None
        self.unsupported_request_errors1_week = None
        self.unsupported_request_errors1_week_h = None
        self.unsupported_request_errors2_weeks = None
        self.unsupported_request_errors2_weeks_h = None
        self.update = None

        ManagedObject.__init__(self, "ComputePCIeFatalReceiveStats", parent_mo_or_dn, **kwargs)
