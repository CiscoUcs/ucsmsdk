"""This module contains the general information for AdaptorMenloNetEgStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorMenloNetEgStatsConsts:
    MENLO_NET_INDEX_0 = "0"
    MENLO_NET_INDEX_0_A = "0_A"
    MENLO_NET_INDEX_0_B = "0_B"
    MENLO_NET_INDEX_1 = "1"
    MENLO_NET_INDEX_1_A = "1_A"
    MENLO_NET_INDEX_1_B = "1_B"
    MENLO_NET_INDEX_UNKNOWN = "unknown"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorMenloNetEgStats(ManagedObject):
    """This is AdaptorMenloNetEgStats class."""

    consts = AdaptorMenloNetEgStatsConsts()
    naming_props = set(['menloNetIndex'])

    mo_meta = MoMeta("AdaptorMenloNetEgStats", "adaptorMenloNetEgStats", "menlo-net-eg-stats-[menlo_net_index]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['adaptorUnit'], ['adaptorMenloNetEgStatsHist'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "drop_cmd": MoPropertyMeta("drop_cmd", "dropCmd", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_cmd_delta": MoPropertyMeta("drop_cmd_delta", "dropCmdDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_cmd_delta_avg": MoPropertyMeta("drop_cmd_delta_avg", "dropCmdDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_cmd_delta_max": MoPropertyMeta("drop_cmd_delta_max", "dropCmdDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_cmd_delta_min": MoPropertyMeta("drop_cmd_delta_min", "dropCmdDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_lif_cfg_invalid": MoPropertyMeta("drop_lif_cfg_invalid", "dropLifCfgInvalid", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_lif_cfg_invalid_delta": MoPropertyMeta("drop_lif_cfg_invalid_delta", "dropLifCfgInvalidDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_lif_cfg_invalid_delta_avg": MoPropertyMeta("drop_lif_cfg_invalid_delta_avg", "dropLifCfgInvalidDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_lif_cfg_invalid_delta_max": MoPropertyMeta("drop_lif_cfg_invalid_delta_max", "dropLifCfgInvalidDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_lif_cfg_invalid_delta_min": MoPropertyMeta("drop_lif_cfg_invalid_delta_min", "dropLifCfgInvalidDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_lif_map_no_hit": MoPropertyMeta("drop_lif_map_no_hit", "dropLifMapNoHit", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_lif_map_no_hit_delta": MoPropertyMeta("drop_lif_map_no_hit_delta", "dropLifMapNoHitDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_lif_map_no_hit_delta_avg": MoPropertyMeta("drop_lif_map_no_hit_delta_avg", "dropLifMapNoHitDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_lif_map_no_hit_delta_max": MoPropertyMeta("drop_lif_map_no_hit_delta_max", "dropLifMapNoHitDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_lif_map_no_hit_delta_min": MoPropertyMeta("drop_lif_map_no_hit_delta_min", "dropLifMapNoHitDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_src_bind": MoPropertyMeta("drop_src_bind", "dropSrcBind", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_src_bind_delta": MoPropertyMeta("drop_src_bind_delta", "dropSrcBindDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_src_bind_delta_avg": MoPropertyMeta("drop_src_bind_delta_avg", "dropSrcBindDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_src_bind_delta_max": MoPropertyMeta("drop_src_bind_delta_max", "dropSrcBindDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_src_bind_delta_min": MoPropertyMeta("drop_src_bind_delta_min", "dropSrcBindDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "learn_req_drop": MoPropertyMeta("learn_req_drop", "learnReqDrop", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "learn_req_drop_delta": MoPropertyMeta("learn_req_drop_delta", "learnReqDropDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "learn_req_drop_delta_avg": MoPropertyMeta("learn_req_drop_delta_avg", "learnReqDropDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "learn_req_drop_delta_max": MoPropertyMeta("learn_req_drop_delta_max", "learnReqDropDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "learn_req_drop_delta_min": MoPropertyMeta("learn_req_drop_delta_min", "learnReqDropDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "menlo_net_index": MoPropertyMeta("menlo_net_index", "menloNetIndex", "string", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, ["0", "0_A", "0_B", "1", "1_A", "1_B", "unknown"], []),
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
        "dn": "dn", 
        "dropCmd": "drop_cmd", 
        "dropCmdDelta": "drop_cmd_delta", 
        "dropCmdDeltaAvg": "drop_cmd_delta_avg", 
        "dropCmdDeltaMax": "drop_cmd_delta_max", 
        "dropCmdDeltaMin": "drop_cmd_delta_min", 
        "dropLifCfgInvalid": "drop_lif_cfg_invalid", 
        "dropLifCfgInvalidDelta": "drop_lif_cfg_invalid_delta", 
        "dropLifCfgInvalidDeltaAvg": "drop_lif_cfg_invalid_delta_avg", 
        "dropLifCfgInvalidDeltaMax": "drop_lif_cfg_invalid_delta_max", 
        "dropLifCfgInvalidDeltaMin": "drop_lif_cfg_invalid_delta_min", 
        "dropLifMapNoHit": "drop_lif_map_no_hit", 
        "dropLifMapNoHitDelta": "drop_lif_map_no_hit_delta", 
        "dropLifMapNoHitDeltaAvg": "drop_lif_map_no_hit_delta_avg", 
        "dropLifMapNoHitDeltaMax": "drop_lif_map_no_hit_delta_max", 
        "dropLifMapNoHitDeltaMin": "drop_lif_map_no_hit_delta_min", 
        "dropSrcBind": "drop_src_bind", 
        "dropSrcBindDelta": "drop_src_bind_delta", 
        "dropSrcBindDeltaAvg": "drop_src_bind_delta_avg", 
        "dropSrcBindDeltaMax": "drop_src_bind_delta_max", 
        "dropSrcBindDeltaMin": "drop_src_bind_delta_min", 
        "intervals": "intervals", 
        "learnReqDrop": "learn_req_drop", 
        "learnReqDropDelta": "learn_req_drop_delta", 
        "learnReqDropDeltaAvg": "learn_req_drop_delta_avg", 
        "learnReqDropDeltaMax": "learn_req_drop_delta_max", 
        "learnReqDropDeltaMin": "learn_req_drop_delta_min", 
        "menloNetIndex": "menlo_net_index", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, menlo_net_index, **kwargs):
        self._dirty_mask = 0
        self.menlo_net_index = menlo_net_index
        self.child_action = None
        self.drop_cmd = None
        self.drop_cmd_delta = None
        self.drop_cmd_delta_avg = None
        self.drop_cmd_delta_max = None
        self.drop_cmd_delta_min = None
        self.drop_lif_cfg_invalid = None
        self.drop_lif_cfg_invalid_delta = None
        self.drop_lif_cfg_invalid_delta_avg = None
        self.drop_lif_cfg_invalid_delta_max = None
        self.drop_lif_cfg_invalid_delta_min = None
        self.drop_lif_map_no_hit = None
        self.drop_lif_map_no_hit_delta = None
        self.drop_lif_map_no_hit_delta_avg = None
        self.drop_lif_map_no_hit_delta_max = None
        self.drop_lif_map_no_hit_delta_min = None
        self.drop_src_bind = None
        self.drop_src_bind_delta = None
        self.drop_src_bind_delta_avg = None
        self.drop_src_bind_delta_max = None
        self.drop_src_bind_delta_min = None
        self.intervals = None
        self.learn_req_drop = None
        self.learn_req_drop_delta = None
        self.learn_req_drop_delta_avg = None
        self.learn_req_drop_delta_max = None
        self.learn_req_drop_delta_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "AdaptorMenloNetEgStats", parent_mo_or_dn, **kwargs)
