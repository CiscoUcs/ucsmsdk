"""This module contains the general information for AdaptorMenloNetEgStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorMenloNetEgStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorMenloNetEgStatsHist(ManagedObject):
    """This is AdaptorMenloNetEgStatsHist class."""

    consts = AdaptorMenloNetEgStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorMenloNetEgStatsHist", "adaptorMenloNetEgStatsHist", "[id]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["read-only"], ['adaptorMenloNetEgStats'], [], ["Get"])

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
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "learn_req_drop": MoPropertyMeta("learn_req_drop", "learnReqDrop", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "learn_req_drop_delta": MoPropertyMeta("learn_req_drop_delta", "learnReqDropDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "learn_req_drop_delta_avg": MoPropertyMeta("learn_req_drop_delta_avg", "learnReqDropDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "learn_req_drop_delta_max": MoPropertyMeta("learn_req_drop_delta_max", "learnReqDropDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "learn_req_drop_delta_min": MoPropertyMeta("learn_req_drop_delta_min", "learnReqDropDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
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
        "id": "id", 
        "learnReqDrop": "learn_req_drop", 
        "learnReqDropDelta": "learn_req_drop_delta", 
        "learnReqDropDeltaAvg": "learn_req_drop_delta_avg", 
        "learnReqDropDeltaMax": "learn_req_drop_delta_max", 
        "learnReqDropDeltaMin": "learn_req_drop_delta_min", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
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
        self.learn_req_drop = None
        self.learn_req_drop_delta = None
        self.learn_req_drop_delta_avg = None
        self.learn_req_drop_delta_max = None
        self.learn_req_drop_delta_min = None
        self.most_recent = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "AdaptorMenloNetEgStatsHist", parent_mo_or_dn, **kwargs)
