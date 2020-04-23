"""This module contains the general information for EtherLossStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EtherLossStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EtherLossStats(ManagedObject):
    """This is EtherLossStats class."""

    consts = EtherLossStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("EtherLossStats", "etherLossStats", "loss-stats", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['etherPIo', 'etherServerIntFIo', 'fabricEthEstcPc', 'fabricEthLanPc'], ['etherLossStatsHist'], ["Get"])

    prop_meta = {
        "sqe_test": MoPropertyMeta("sqe_test", "SQETest", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sqe_test_delta": MoPropertyMeta("sqe_test_delta", "SQETestDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sqe_test_delta_avg": MoPropertyMeta("sqe_test_delta_avg", "SQETestDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sqe_test_delta_max": MoPropertyMeta("sqe_test_delta_max", "SQETestDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sqe_test_delta_min": MoPropertyMeta("sqe_test_delta_min", "SQETestDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "carrier_sense": MoPropertyMeta("carrier_sense", "carrierSense", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "carrier_sense_delta": MoPropertyMeta("carrier_sense_delta", "carrierSenseDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "carrier_sense_delta_avg": MoPropertyMeta("carrier_sense_delta_avg", "carrierSenseDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "carrier_sense_delta_max": MoPropertyMeta("carrier_sense_delta_max", "carrierSenseDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "carrier_sense_delta_min": MoPropertyMeta("carrier_sense_delta_min", "carrierSenseDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "excess_collision": MoPropertyMeta("excess_collision", "excessCollision", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "excess_collision_delta": MoPropertyMeta("excess_collision_delta", "excessCollisionDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "excess_collision_delta_avg": MoPropertyMeta("excess_collision_delta_avg", "excessCollisionDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "excess_collision_delta_max": MoPropertyMeta("excess_collision_delta_max", "excessCollisionDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "excess_collision_delta_min": MoPropertyMeta("excess_collision_delta_min", "excessCollisionDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "giants": MoPropertyMeta("giants", "giants", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "giants_delta": MoPropertyMeta("giants_delta", "giantsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "giants_delta_avg": MoPropertyMeta("giants_delta_avg", "giantsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "giants_delta_max": MoPropertyMeta("giants_delta_max", "giantsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "giants_delta_min": MoPropertyMeta("giants_delta_min", "giantsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "late_collision": MoPropertyMeta("late_collision", "lateCollision", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "late_collision_delta": MoPropertyMeta("late_collision_delta", "lateCollisionDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "late_collision_delta_avg": MoPropertyMeta("late_collision_delta_avg", "lateCollisionDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "late_collision_delta_max": MoPropertyMeta("late_collision_delta_max", "lateCollisionDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "late_collision_delta_min": MoPropertyMeta("late_collision_delta_min", "lateCollisionDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multi_collision": MoPropertyMeta("multi_collision", "multiCollision", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multi_collision_delta": MoPropertyMeta("multi_collision_delta", "multiCollisionDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multi_collision_delta_avg": MoPropertyMeta("multi_collision_delta_avg", "multiCollisionDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multi_collision_delta_max": MoPropertyMeta("multi_collision_delta_max", "multiCollisionDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multi_collision_delta_min": MoPropertyMeta("multi_collision_delta_min", "multiCollisionDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "single_collision": MoPropertyMeta("single_collision", "singleCollision", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "single_collision_delta": MoPropertyMeta("single_collision_delta", "singleCollisionDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "single_collision_delta_avg": MoPropertyMeta("single_collision_delta_avg", "singleCollisionDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "single_collision_delta_max": MoPropertyMeta("single_collision_delta_max", "singleCollisionDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "single_collision_delta_min": MoPropertyMeta("single_collision_delta_min", "singleCollisionDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "symbol": MoPropertyMeta("symbol", "symbol", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "symbol_delta": MoPropertyMeta("symbol_delta", "symbolDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "symbol_delta_avg": MoPropertyMeta("symbol_delta_avg", "symbolDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "symbol_delta_max": MoPropertyMeta("symbol_delta_max", "symbolDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "symbol_delta_min": MoPropertyMeta("symbol_delta_min", "symbolDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "SQETest": "sqe_test", 
        "SQETestDelta": "sqe_test_delta", 
        "SQETestDeltaAvg": "sqe_test_delta_avg", 
        "SQETestDeltaMax": "sqe_test_delta_max", 
        "SQETestDeltaMin": "sqe_test_delta_min", 
        "carrierSense": "carrier_sense", 
        "carrierSenseDelta": "carrier_sense_delta", 
        "carrierSenseDeltaAvg": "carrier_sense_delta_avg", 
        "carrierSenseDeltaMax": "carrier_sense_delta_max", 
        "carrierSenseDeltaMin": "carrier_sense_delta_min", 
        "childAction": "child_action", 
        "dn": "dn", 
        "excessCollision": "excess_collision", 
        "excessCollisionDelta": "excess_collision_delta", 
        "excessCollisionDeltaAvg": "excess_collision_delta_avg", 
        "excessCollisionDeltaMax": "excess_collision_delta_max", 
        "excessCollisionDeltaMin": "excess_collision_delta_min", 
        "giants": "giants", 
        "giantsDelta": "giants_delta", 
        "giantsDeltaAvg": "giants_delta_avg", 
        "giantsDeltaMax": "giants_delta_max", 
        "giantsDeltaMin": "giants_delta_min", 
        "intervals": "intervals", 
        "lateCollision": "late_collision", 
        "lateCollisionDelta": "late_collision_delta", 
        "lateCollisionDeltaAvg": "late_collision_delta_avg", 
        "lateCollisionDeltaMax": "late_collision_delta_max", 
        "lateCollisionDeltaMin": "late_collision_delta_min", 
        "multiCollision": "multi_collision", 
        "multiCollisionDelta": "multi_collision_delta", 
        "multiCollisionDeltaAvg": "multi_collision_delta_avg", 
        "multiCollisionDeltaMax": "multi_collision_delta_max", 
        "multiCollisionDeltaMin": "multi_collision_delta_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "singleCollision": "single_collision", 
        "singleCollisionDelta": "single_collision_delta", 
        "singleCollisionDeltaAvg": "single_collision_delta_avg", 
        "singleCollisionDeltaMax": "single_collision_delta_max", 
        "singleCollisionDeltaMin": "single_collision_delta_min", 
        "status": "status", 
        "suspect": "suspect", 
        "symbol": "symbol", 
        "symbolDelta": "symbol_delta", 
        "symbolDeltaAvg": "symbol_delta_avg", 
        "symbolDeltaMax": "symbol_delta_max", 
        "symbolDeltaMin": "symbol_delta_min", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.sqe_test = None
        self.sqe_test_delta = None
        self.sqe_test_delta_avg = None
        self.sqe_test_delta_max = None
        self.sqe_test_delta_min = None
        self.carrier_sense = None
        self.carrier_sense_delta = None
        self.carrier_sense_delta_avg = None
        self.carrier_sense_delta_max = None
        self.carrier_sense_delta_min = None
        self.child_action = None
        self.excess_collision = None
        self.excess_collision_delta = None
        self.excess_collision_delta_avg = None
        self.excess_collision_delta_max = None
        self.excess_collision_delta_min = None
        self.giants = None
        self.giants_delta = None
        self.giants_delta_avg = None
        self.giants_delta_max = None
        self.giants_delta_min = None
        self.intervals = None
        self.late_collision = None
        self.late_collision_delta = None
        self.late_collision_delta_avg = None
        self.late_collision_delta_max = None
        self.late_collision_delta_min = None
        self.multi_collision = None
        self.multi_collision_delta = None
        self.multi_collision_delta_avg = None
        self.multi_collision_delta_max = None
        self.multi_collision_delta_min = None
        self.sacl = None
        self.single_collision = None
        self.single_collision_delta = None
        self.single_collision_delta_avg = None
        self.single_collision_delta_max = None
        self.single_collision_delta_min = None
        self.status = None
        self.suspect = None
        self.symbol = None
        self.symbol_delta = None
        self.symbol_delta_avg = None
        self.symbol_delta_max = None
        self.symbol_delta_min = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "EtherLossStats", parent_mo_or_dn, **kwargs)
