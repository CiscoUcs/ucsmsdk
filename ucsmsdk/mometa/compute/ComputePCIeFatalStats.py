"""This module contains the general information for ComputePCIeFatalStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePCIeFatalStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ComputePCIeFatalStats(ManagedObject):
    """This is ComputePCIeFatalStats class."""

    consts = ComputePCIeFatalStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputePCIeFatalStats", "computePCIeFatalStats", "pciefat-stats", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['computeBoard'], [], ["Get"])

    prop_meta = {
        "acs_violation_errors": MoPropertyMeta("acs_violation_errors", "acsViolationErrors", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "acs_violation_errors15_min": MoPropertyMeta("acs_violation_errors15_min", "acsViolationErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "acs_violation_errors15_min_h": MoPropertyMeta("acs_violation_errors15_min_h", "acsViolationErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "acs_violation_errors1_day": MoPropertyMeta("acs_violation_errors1_day", "acsViolationErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "acs_violation_errors1_day_h": MoPropertyMeta("acs_violation_errors1_day_h", "acsViolationErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "acs_violation_errors1_hour": MoPropertyMeta("acs_violation_errors1_hour", "acsViolationErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "acs_violation_errors1_hour_h": MoPropertyMeta("acs_violation_errors1_hour_h", "acsViolationErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "acs_violation_errors1_week": MoPropertyMeta("acs_violation_errors1_week", "acsViolationErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "acs_violation_errors1_week_h": MoPropertyMeta("acs_violation_errors1_week_h", "acsViolationErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "acs_violation_errors2_weeks": MoPropertyMeta("acs_violation_errors2_weeks", "acsViolationErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "acs_violation_errors2_weeks_h": MoPropertyMeta("acs_violation_errors2_weeks_h", "acsViolationErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "malformed_tlp_errors": MoPropertyMeta("malformed_tlp_errors", "malformedTLPErrors", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "malformed_tlp_errors15_min": MoPropertyMeta("malformed_tlp_errors15_min", "malformedTLPErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "malformed_tlp_errors15_min_h": MoPropertyMeta("malformed_tlp_errors15_min_h", "malformedTLPErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "malformed_tlp_errors1_day": MoPropertyMeta("malformed_tlp_errors1_day", "malformedTLPErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "malformed_tlp_errors1_day_h": MoPropertyMeta("malformed_tlp_errors1_day_h", "malformedTLPErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "malformed_tlp_errors1_hour": MoPropertyMeta("malformed_tlp_errors1_hour", "malformedTLPErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "malformed_tlp_errors1_hour_h": MoPropertyMeta("malformed_tlp_errors1_hour_h", "malformedTLPErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "malformed_tlp_errors1_week": MoPropertyMeta("malformed_tlp_errors1_week", "malformedTLPErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "malformed_tlp_errors1_week_h": MoPropertyMeta("malformed_tlp_errors1_week_h", "malformedTLPErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "malformed_tlp_errors2_weeks": MoPropertyMeta("malformed_tlp_errors2_weeks", "malformedTLPErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "malformed_tlp_errors2_weeks_h": MoPropertyMeta("malformed_tlp_errors2_weeks_h", "malformedTLPErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "poisoned_tlp_errors": MoPropertyMeta("poisoned_tlp_errors", "poisonedTLPErrors", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "poisoned_tlp_errors15_min": MoPropertyMeta("poisoned_tlp_errors15_min", "poisonedTLPErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "poisoned_tlp_errors15_min_h": MoPropertyMeta("poisoned_tlp_errors15_min_h", "poisonedTLPErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "poisoned_tlp_errors1_day": MoPropertyMeta("poisoned_tlp_errors1_day", "poisonedTLPErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "poisoned_tlp_errors1_day_h": MoPropertyMeta("poisoned_tlp_errors1_day_h", "poisonedTLPErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "poisoned_tlp_errors1_hour": MoPropertyMeta("poisoned_tlp_errors1_hour", "poisonedTLPErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "poisoned_tlp_errors1_hour_h": MoPropertyMeta("poisoned_tlp_errors1_hour_h", "poisonedTLPErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "poisoned_tlp_errors1_week": MoPropertyMeta("poisoned_tlp_errors1_week", "poisonedTLPErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "poisoned_tlp_errors1_week_h": MoPropertyMeta("poisoned_tlp_errors1_week_h", "poisonedTLPErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "poisoned_tlp_errors2_weeks": MoPropertyMeta("poisoned_tlp_errors2_weeks", "poisonedTLPErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "poisoned_tlp_errors2_weeks_h": MoPropertyMeta("poisoned_tlp_errors2_weeks_h", "poisonedTLPErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "surprise_link_down_errors": MoPropertyMeta("surprise_link_down_errors", "surpriseLinkDownErrors", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "surprise_link_down_errors15_min": MoPropertyMeta("surprise_link_down_errors15_min", "surpriseLinkDownErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "surprise_link_down_errors15_min_h": MoPropertyMeta("surprise_link_down_errors15_min_h", "surpriseLinkDownErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "surprise_link_down_errors1_day": MoPropertyMeta("surprise_link_down_errors1_day", "surpriseLinkDownErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "surprise_link_down_errors1_day_h": MoPropertyMeta("surprise_link_down_errors1_day_h", "surpriseLinkDownErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "surprise_link_down_errors1_hour": MoPropertyMeta("surprise_link_down_errors1_hour", "surpriseLinkDownErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "surprise_link_down_errors1_hour_h": MoPropertyMeta("surprise_link_down_errors1_hour_h", "surpriseLinkDownErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "surprise_link_down_errors1_week": MoPropertyMeta("surprise_link_down_errors1_week", "surpriseLinkDownErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "surprise_link_down_errors1_week_h": MoPropertyMeta("surprise_link_down_errors1_week_h", "surpriseLinkDownErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "surprise_link_down_errors2_weeks": MoPropertyMeta("surprise_link_down_errors2_weeks", "surpriseLinkDownErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "surprise_link_down_errors2_weeks_h": MoPropertyMeta("surprise_link_down_errors2_weeks_h", "surpriseLinkDownErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "acsViolationErrors": "acs_violation_errors", 
        "acsViolationErrors15Min": "acs_violation_errors15_min", 
        "acsViolationErrors15MinH": "acs_violation_errors15_min_h", 
        "acsViolationErrors1Day": "acs_violation_errors1_day", 
        "acsViolationErrors1DayH": "acs_violation_errors1_day_h", 
        "acsViolationErrors1Hour": "acs_violation_errors1_hour", 
        "acsViolationErrors1HourH": "acs_violation_errors1_hour_h", 
        "acsViolationErrors1Week": "acs_violation_errors1_week", 
        "acsViolationErrors1WeekH": "acs_violation_errors1_week_h", 
        "acsViolationErrors2Weeks": "acs_violation_errors2_weeks", 
        "acsViolationErrors2WeeksH": "acs_violation_errors2_weeks_h", 
        "childAction": "child_action", 
        "dn": "dn", 
        "intervals": "intervals", 
        "malformedTLPErrors": "malformed_tlp_errors", 
        "malformedTLPErrors15Min": "malformed_tlp_errors15_min", 
        "malformedTLPErrors15MinH": "malformed_tlp_errors15_min_h", 
        "malformedTLPErrors1Day": "malformed_tlp_errors1_day", 
        "malformedTLPErrors1DayH": "malformed_tlp_errors1_day_h", 
        "malformedTLPErrors1Hour": "malformed_tlp_errors1_hour", 
        "malformedTLPErrors1HourH": "malformed_tlp_errors1_hour_h", 
        "malformedTLPErrors1Week": "malformed_tlp_errors1_week", 
        "malformedTLPErrors1WeekH": "malformed_tlp_errors1_week_h", 
        "malformedTLPErrors2Weeks": "malformed_tlp_errors2_weeks", 
        "malformedTLPErrors2WeeksH": "malformed_tlp_errors2_weeks_h", 
        "poisonedTLPErrors": "poisoned_tlp_errors", 
        "poisonedTLPErrors15Min": "poisoned_tlp_errors15_min", 
        "poisonedTLPErrors15MinH": "poisoned_tlp_errors15_min_h", 
        "poisonedTLPErrors1Day": "poisoned_tlp_errors1_day", 
        "poisonedTLPErrors1DayH": "poisoned_tlp_errors1_day_h", 
        "poisonedTLPErrors1Hour": "poisoned_tlp_errors1_hour", 
        "poisonedTLPErrors1HourH": "poisoned_tlp_errors1_hour_h", 
        "poisonedTLPErrors1Week": "poisoned_tlp_errors1_week", 
        "poisonedTLPErrors1WeekH": "poisoned_tlp_errors1_week_h", 
        "poisonedTLPErrors2Weeks": "poisoned_tlp_errors2_weeks", 
        "poisonedTLPErrors2WeeksH": "poisoned_tlp_errors2_weeks_h", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "surpriseLinkDownErrors": "surprise_link_down_errors", 
        "surpriseLinkDownErrors15Min": "surprise_link_down_errors15_min", 
        "surpriseLinkDownErrors15MinH": "surprise_link_down_errors15_min_h", 
        "surpriseLinkDownErrors1Day": "surprise_link_down_errors1_day", 
        "surpriseLinkDownErrors1DayH": "surprise_link_down_errors1_day_h", 
        "surpriseLinkDownErrors1Hour": "surprise_link_down_errors1_hour", 
        "surpriseLinkDownErrors1HourH": "surprise_link_down_errors1_hour_h", 
        "surpriseLinkDownErrors1Week": "surprise_link_down_errors1_week", 
        "surpriseLinkDownErrors1WeekH": "surprise_link_down_errors1_week_h", 
        "surpriseLinkDownErrors2Weeks": "surprise_link_down_errors2_weeks", 
        "surpriseLinkDownErrors2WeeksH": "surprise_link_down_errors2_weeks_h", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.acs_violation_errors = None
        self.acs_violation_errors15_min = None
        self.acs_violation_errors15_min_h = None
        self.acs_violation_errors1_day = None
        self.acs_violation_errors1_day_h = None
        self.acs_violation_errors1_hour = None
        self.acs_violation_errors1_hour_h = None
        self.acs_violation_errors1_week = None
        self.acs_violation_errors1_week_h = None
        self.acs_violation_errors2_weeks = None
        self.acs_violation_errors2_weeks_h = None
        self.child_action = None
        self.intervals = None
        self.malformed_tlp_errors = None
        self.malformed_tlp_errors15_min = None
        self.malformed_tlp_errors15_min_h = None
        self.malformed_tlp_errors1_day = None
        self.malformed_tlp_errors1_day_h = None
        self.malformed_tlp_errors1_hour = None
        self.malformed_tlp_errors1_hour_h = None
        self.malformed_tlp_errors1_week = None
        self.malformed_tlp_errors1_week_h = None
        self.malformed_tlp_errors2_weeks = None
        self.malformed_tlp_errors2_weeks_h = None
        self.poisoned_tlp_errors = None
        self.poisoned_tlp_errors15_min = None
        self.poisoned_tlp_errors15_min_h = None
        self.poisoned_tlp_errors1_day = None
        self.poisoned_tlp_errors1_day_h = None
        self.poisoned_tlp_errors1_hour = None
        self.poisoned_tlp_errors1_hour_h = None
        self.poisoned_tlp_errors1_week = None
        self.poisoned_tlp_errors1_week_h = None
        self.poisoned_tlp_errors2_weeks = None
        self.poisoned_tlp_errors2_weeks_h = None
        self.sacl = None
        self.status = None
        self.surprise_link_down_errors = None
        self.surprise_link_down_errors15_min = None
        self.surprise_link_down_errors15_min_h = None
        self.surprise_link_down_errors1_day = None
        self.surprise_link_down_errors1_day_h = None
        self.surprise_link_down_errors1_hour = None
        self.surprise_link_down_errors1_hour_h = None
        self.surprise_link_down_errors1_week = None
        self.surprise_link_down_errors1_week_h = None
        self.surprise_link_down_errors2_weeks = None
        self.surprise_link_down_errors2_weeks_h = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "ComputePCIeFatalStats", parent_mo_or_dn, **kwargs)
