"""This module contains the general information for AdaptorEthPortBySizeLargeStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorEthPortBySizeLargeStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"
    TRAFFIC_DIRECTION_RX = "rx"
    TRAFFIC_DIRECTION_TX = "tx"
    TRAFFIC_DIRECTION_UNKNOWN = "unknown"


class AdaptorEthPortBySizeLargeStats(ManagedObject):
    """This is AdaptorEthPortBySizeLargeStats class."""

    consts = AdaptorEthPortBySizeLargeStatsConsts()
    naming_props = set(['trafficDirection'])

    mo_meta = MoMeta("AdaptorEthPortBySizeLargeStats", "adaptorEthPortBySizeLargeStats", "eth-port-by-size-large-stats-[traffic_direction]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['adaptorExtEthIf', 'adaptorHostEthIf', 'vmNic'], ['adaptorEthPortBySizeLargeStatsHist'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "greater_than_or_equal_to9216": MoPropertyMeta("greater_than_or_equal_to9216", "greaterThanOrEqualTo9216", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "greater_than_or_equal_to9216_delta": MoPropertyMeta("greater_than_or_equal_to9216_delta", "greaterThanOrEqualTo9216Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "greater_than_or_equal_to9216_delta_avg": MoPropertyMeta("greater_than_or_equal_to9216_delta_avg", "greaterThanOrEqualTo9216DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "greater_than_or_equal_to9216_delta_max": MoPropertyMeta("greater_than_or_equal_to9216_delta_max", "greaterThanOrEqualTo9216DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "greater_than_or_equal_to9216_delta_min": MoPropertyMeta("greater_than_or_equal_to9216_delta_min", "greaterThanOrEqualTo9216DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than2048": MoPropertyMeta("less_than2048", "lessThan2048", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than2048_delta": MoPropertyMeta("less_than2048_delta", "lessThan2048Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than2048_delta_avg": MoPropertyMeta("less_than2048_delta_avg", "lessThan2048DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than2048_delta_max": MoPropertyMeta("less_than2048_delta_max", "lessThan2048DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than2048_delta_min": MoPropertyMeta("less_than2048_delta_min", "lessThan2048DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than4096": MoPropertyMeta("less_than4096", "lessThan4096", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than4096_delta": MoPropertyMeta("less_than4096_delta", "lessThan4096Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than4096_delta_avg": MoPropertyMeta("less_than4096_delta_avg", "lessThan4096DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than4096_delta_max": MoPropertyMeta("less_than4096_delta_max", "lessThan4096DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than4096_delta_min": MoPropertyMeta("less_than4096_delta_min", "lessThan4096DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than8192": MoPropertyMeta("less_than8192", "lessThan8192", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than8192_delta": MoPropertyMeta("less_than8192_delta", "lessThan8192Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than8192_delta_avg": MoPropertyMeta("less_than8192_delta_avg", "lessThan8192DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than8192_delta_max": MoPropertyMeta("less_than8192_delta_max", "lessThan8192DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than8192_delta_min": MoPropertyMeta("less_than8192_delta_min", "lessThan8192DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than9216": MoPropertyMeta("less_than9216", "lessThan9216", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than9216_delta": MoPropertyMeta("less_than9216_delta", "lessThan9216Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than9216_delta_avg": MoPropertyMeta("less_than9216_delta_avg", "lessThan9216DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than9216_delta_max": MoPropertyMeta("less_than9216_delta_max", "lessThan9216DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than9216_delta_min": MoPropertyMeta("less_than9216_delta_min", "lessThan9216DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than_or_equal_to1518": MoPropertyMeta("less_than_or_equal_to1518", "lessThanOrEqualTo1518", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than_or_equal_to1518_delta": MoPropertyMeta("less_than_or_equal_to1518_delta", "lessThanOrEqualTo1518Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than_or_equal_to1518_delta_avg": MoPropertyMeta("less_than_or_equal_to1518_delta_avg", "lessThanOrEqualTo1518DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than_or_equal_to1518_delta_max": MoPropertyMeta("less_than_or_equal_to1518_delta_max", "lessThanOrEqualTo1518DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than_or_equal_to1518_delta_min": MoPropertyMeta("less_than_or_equal_to1518_delta_min", "lessThanOrEqualTo1518DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "no_breakdown_greater_than1518": MoPropertyMeta("no_breakdown_greater_than1518", "noBreakdownGreaterThan1518", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "no_breakdown_greater_than1518_delta": MoPropertyMeta("no_breakdown_greater_than1518_delta", "noBreakdownGreaterThan1518Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "no_breakdown_greater_than1518_delta_avg": MoPropertyMeta("no_breakdown_greater_than1518_delta_avg", "noBreakdownGreaterThan1518DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "no_breakdown_greater_than1518_delta_max": MoPropertyMeta("no_breakdown_greater_than1518_delta_max", "noBreakdownGreaterThan1518DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "no_breakdown_greater_than1518_delta_min": MoPropertyMeta("no_breakdown_greater_than1518_delta_min", "noBreakdownGreaterThan1518DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "traffic_direction": MoPropertyMeta("traffic_direction", "trafficDirection", "string", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, ["rx", "tx", "unknown"], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "greaterThanOrEqualTo9216": "greater_than_or_equal_to9216", 
        "greaterThanOrEqualTo9216Delta": "greater_than_or_equal_to9216_delta", 
        "greaterThanOrEqualTo9216DeltaAvg": "greater_than_or_equal_to9216_delta_avg", 
        "greaterThanOrEqualTo9216DeltaMax": "greater_than_or_equal_to9216_delta_max", 
        "greaterThanOrEqualTo9216DeltaMin": "greater_than_or_equal_to9216_delta_min", 
        "intervals": "intervals", 
        "lessThan2048": "less_than2048", 
        "lessThan2048Delta": "less_than2048_delta", 
        "lessThan2048DeltaAvg": "less_than2048_delta_avg", 
        "lessThan2048DeltaMax": "less_than2048_delta_max", 
        "lessThan2048DeltaMin": "less_than2048_delta_min", 
        "lessThan4096": "less_than4096", 
        "lessThan4096Delta": "less_than4096_delta", 
        "lessThan4096DeltaAvg": "less_than4096_delta_avg", 
        "lessThan4096DeltaMax": "less_than4096_delta_max", 
        "lessThan4096DeltaMin": "less_than4096_delta_min", 
        "lessThan8192": "less_than8192", 
        "lessThan8192Delta": "less_than8192_delta", 
        "lessThan8192DeltaAvg": "less_than8192_delta_avg", 
        "lessThan8192DeltaMax": "less_than8192_delta_max", 
        "lessThan8192DeltaMin": "less_than8192_delta_min", 
        "lessThan9216": "less_than9216", 
        "lessThan9216Delta": "less_than9216_delta", 
        "lessThan9216DeltaAvg": "less_than9216_delta_avg", 
        "lessThan9216DeltaMax": "less_than9216_delta_max", 
        "lessThan9216DeltaMin": "less_than9216_delta_min", 
        "lessThanOrEqualTo1518": "less_than_or_equal_to1518", 
        "lessThanOrEqualTo1518Delta": "less_than_or_equal_to1518_delta", 
        "lessThanOrEqualTo1518DeltaAvg": "less_than_or_equal_to1518_delta_avg", 
        "lessThanOrEqualTo1518DeltaMax": "less_than_or_equal_to1518_delta_max", 
        "lessThanOrEqualTo1518DeltaMin": "less_than_or_equal_to1518_delta_min", 
        "noBreakdownGreaterThan1518": "no_breakdown_greater_than1518", 
        "noBreakdownGreaterThan1518Delta": "no_breakdown_greater_than1518_delta", 
        "noBreakdownGreaterThan1518DeltaAvg": "no_breakdown_greater_than1518_delta_avg", 
        "noBreakdownGreaterThan1518DeltaMax": "no_breakdown_greater_than1518_delta_max", 
        "noBreakdownGreaterThan1518DeltaMin": "no_breakdown_greater_than1518_delta_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "trafficDirection": "traffic_direction", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, traffic_direction, **kwargs):
        self._dirty_mask = 0
        self.traffic_direction = traffic_direction
        self.child_action = None
        self.greater_than_or_equal_to9216 = None
        self.greater_than_or_equal_to9216_delta = None
        self.greater_than_or_equal_to9216_delta_avg = None
        self.greater_than_or_equal_to9216_delta_max = None
        self.greater_than_or_equal_to9216_delta_min = None
        self.intervals = None
        self.less_than2048 = None
        self.less_than2048_delta = None
        self.less_than2048_delta_avg = None
        self.less_than2048_delta_max = None
        self.less_than2048_delta_min = None
        self.less_than4096 = None
        self.less_than4096_delta = None
        self.less_than4096_delta_avg = None
        self.less_than4096_delta_max = None
        self.less_than4096_delta_min = None
        self.less_than8192 = None
        self.less_than8192_delta = None
        self.less_than8192_delta_avg = None
        self.less_than8192_delta_max = None
        self.less_than8192_delta_min = None
        self.less_than9216 = None
        self.less_than9216_delta = None
        self.less_than9216_delta_avg = None
        self.less_than9216_delta_max = None
        self.less_than9216_delta_min = None
        self.less_than_or_equal_to1518 = None
        self.less_than_or_equal_to1518_delta = None
        self.less_than_or_equal_to1518_delta_avg = None
        self.less_than_or_equal_to1518_delta_max = None
        self.less_than_or_equal_to1518_delta_min = None
        self.no_breakdown_greater_than1518 = None
        self.no_breakdown_greater_than1518_delta = None
        self.no_breakdown_greater_than1518_delta_avg = None
        self.no_breakdown_greater_than1518_delta_max = None
        self.no_breakdown_greater_than1518_delta_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "AdaptorEthPortBySizeLargeStats", parent_mo_or_dn, **kwargs)
