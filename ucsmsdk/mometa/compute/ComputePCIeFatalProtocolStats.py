"""This module contains the general information for ComputePCIeFatalProtocolStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePCIeFatalProtocolStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ComputePCIeFatalProtocolStats(ManagedObject):
    """This is ComputePCIeFatalProtocolStats class."""

    consts = ComputePCIeFatalProtocolStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputePCIeFatalProtocolStats", "computePCIeFatalProtocolStats", "pciefat-protocol-stats", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['computeBoard'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dllp_errors": MoPropertyMeta("dllp_errors", "dllpErrors", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dllp_errors15_min": MoPropertyMeta("dllp_errors15_min", "dllpErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dllp_errors15_min_h": MoPropertyMeta("dllp_errors15_min_h", "dllpErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dllp_errors1_day": MoPropertyMeta("dllp_errors1_day", "dllpErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dllp_errors1_day_h": MoPropertyMeta("dllp_errors1_day_h", "dllpErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dllp_errors1_hour": MoPropertyMeta("dllp_errors1_hour", "dllpErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dllp_errors1_hour_h": MoPropertyMeta("dllp_errors1_hour_h", "dllpErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dllp_errors1_week": MoPropertyMeta("dllp_errors1_week", "dllpErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dllp_errors1_week_h": MoPropertyMeta("dllp_errors1_week_h", "dllpErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dllp_errors2_weeks": MoPropertyMeta("dllp_errors2_weeks", "dllpErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dllp_errors2_weeks_h": MoPropertyMeta("dllp_errors2_weeks_h", "dllpErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "flow_control_errors": MoPropertyMeta("flow_control_errors", "flowControlErrors", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "flow_control_errors15_min": MoPropertyMeta("flow_control_errors15_min", "flowControlErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "flow_control_errors15_min_h": MoPropertyMeta("flow_control_errors15_min_h", "flowControlErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "flow_control_errors1_day": MoPropertyMeta("flow_control_errors1_day", "flowControlErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "flow_control_errors1_day_h": MoPropertyMeta("flow_control_errors1_day_h", "flowControlErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "flow_control_errors1_hour": MoPropertyMeta("flow_control_errors1_hour", "flowControlErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "flow_control_errors1_hour_h": MoPropertyMeta("flow_control_errors1_hour_h", "flowControlErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "flow_control_errors1_week": MoPropertyMeta("flow_control_errors1_week", "flowControlErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "flow_control_errors1_week_h": MoPropertyMeta("flow_control_errors1_week_h", "flowControlErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "flow_control_errors2_weeks": MoPropertyMeta("flow_control_errors2_weeks", "flowControlErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "flow_control_errors2_weeks_h": MoPropertyMeta("flow_control_errors2_weeks_h", "flowControlErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dllpErrors": "dllp_errors", 
        "dllpErrors15Min": "dllp_errors15_min", 
        "dllpErrors15MinH": "dllp_errors15_min_h", 
        "dllpErrors1Day": "dllp_errors1_day", 
        "dllpErrors1DayH": "dllp_errors1_day_h", 
        "dllpErrors1Hour": "dllp_errors1_hour", 
        "dllpErrors1HourH": "dllp_errors1_hour_h", 
        "dllpErrors1Week": "dllp_errors1_week", 
        "dllpErrors1WeekH": "dllp_errors1_week_h", 
        "dllpErrors2Weeks": "dllp_errors2_weeks", 
        "dllpErrors2WeeksH": "dllp_errors2_weeks_h", 
        "dn": "dn", 
        "flowControlErrors": "flow_control_errors", 
        "flowControlErrors15Min": "flow_control_errors15_min", 
        "flowControlErrors15MinH": "flow_control_errors15_min_h", 
        "flowControlErrors1Day": "flow_control_errors1_day", 
        "flowControlErrors1DayH": "flow_control_errors1_day_h", 
        "flowControlErrors1Hour": "flow_control_errors1_hour", 
        "flowControlErrors1HourH": "flow_control_errors1_hour_h", 
        "flowControlErrors1Week": "flow_control_errors1_week", 
        "flowControlErrors1WeekH": "flow_control_errors1_week_h", 
        "flowControlErrors2Weeks": "flow_control_errors2_weeks", 
        "flowControlErrors2WeeksH": "flow_control_errors2_weeks_h", 
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
        self.child_action = None
        self.dllp_errors = None
        self.dllp_errors15_min = None
        self.dllp_errors15_min_h = None
        self.dllp_errors1_day = None
        self.dllp_errors1_day_h = None
        self.dllp_errors1_hour = None
        self.dllp_errors1_hour_h = None
        self.dllp_errors1_week = None
        self.dllp_errors1_week_h = None
        self.dllp_errors2_weeks = None
        self.dllp_errors2_weeks_h = None
        self.flow_control_errors = None
        self.flow_control_errors15_min = None
        self.flow_control_errors15_min_h = None
        self.flow_control_errors1_day = None
        self.flow_control_errors1_day_h = None
        self.flow_control_errors1_hour = None
        self.flow_control_errors1_hour_h = None
        self.flow_control_errors1_week = None
        self.flow_control_errors1_week_h = None
        self.flow_control_errors2_weeks = None
        self.flow_control_errors2_weeks_h = None
        self.intervals = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "ComputePCIeFatalProtocolStats", parent_mo_or_dn, **kwargs)
