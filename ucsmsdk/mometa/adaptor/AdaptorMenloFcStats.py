"""This module contains the general information for AdaptorMenloFcStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorMenloFcStatsConsts:
    MENLO_FC_INDEX_0 = "0"
    MENLO_FC_INDEX_0_A = "0_A"
    MENLO_FC_INDEX_0_B = "0_B"
    MENLO_FC_INDEX_1 = "1"
    MENLO_FC_INDEX_1_A = "1_A"
    MENLO_FC_INDEX_1_B = "1_B"
    MENLO_FC_INDEX_UNKNOWN = "unknown"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorMenloFcStats(ManagedObject):
    """This is AdaptorMenloFcStats class."""

    consts = AdaptorMenloFcStatsConsts()
    naming_props = set(['menloFcIndex'])

    mo_meta = MoMeta("AdaptorMenloFcStats", "adaptorMenloFcStats", "menlo-fc-stats-[menlo_fc_index]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['adaptorUnit'], ['adaptorMenloFcStatsHist'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "drop_acl": MoPropertyMeta("drop_acl", "dropAcl", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_acl_delta": MoPropertyMeta("drop_acl_delta", "dropAclDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_acl_delta_avg": MoPropertyMeta("drop_acl_delta_avg", "dropAclDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_acl_delta_max": MoPropertyMeta("drop_acl_delta_max", "dropAclDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_acl_delta_min": MoPropertyMeta("drop_acl_delta_min", "dropAclDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_overrun": MoPropertyMeta("drop_overrun", "dropOverrun", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_overrun_delta": MoPropertyMeta("drop_overrun_delta", "dropOverrunDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_overrun_delta_avg": MoPropertyMeta("drop_overrun_delta_avg", "dropOverrunDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_overrun_delta_max": MoPropertyMeta("drop_overrun_delta_max", "dropOverrunDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_overrun_delta_min": MoPropertyMeta("drop_overrun_delta_min", "dropOverrunDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_runt": MoPropertyMeta("drop_runt", "dropRunt", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_runt_delta": MoPropertyMeta("drop_runt_delta", "dropRuntDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_runt_delta_avg": MoPropertyMeta("drop_runt_delta_avg", "dropRuntDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_runt_delta_max": MoPropertyMeta("drop_runt_delta_max", "dropRuntDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_runt_delta_min": MoPropertyMeta("drop_runt_delta_min", "dropRuntDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "menlo_fc_index": MoPropertyMeta("menlo_fc_index", "menloFcIndex", "string", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, ["0", "0_A", "0_B", "1", "1_A", "1_B", "unknown"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "truncate_overrun": MoPropertyMeta("truncate_overrun", "truncateOverrun", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "truncate_overrun_delta": MoPropertyMeta("truncate_overrun_delta", "truncateOverrunDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "truncate_overrun_delta_avg": MoPropertyMeta("truncate_overrun_delta_avg", "truncateOverrunDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "truncate_overrun_delta_max": MoPropertyMeta("truncate_overrun_delta_max", "truncateOverrunDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "truncate_overrun_delta_min": MoPropertyMeta("truncate_overrun_delta_min", "truncateOverrunDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "dropAcl": "drop_acl", 
        "dropAclDelta": "drop_acl_delta", 
        "dropAclDeltaAvg": "drop_acl_delta_avg", 
        "dropAclDeltaMax": "drop_acl_delta_max", 
        "dropAclDeltaMin": "drop_acl_delta_min", 
        "dropOverrun": "drop_overrun", 
        "dropOverrunDelta": "drop_overrun_delta", 
        "dropOverrunDeltaAvg": "drop_overrun_delta_avg", 
        "dropOverrunDeltaMax": "drop_overrun_delta_max", 
        "dropOverrunDeltaMin": "drop_overrun_delta_min", 
        "dropRunt": "drop_runt", 
        "dropRuntDelta": "drop_runt_delta", 
        "dropRuntDeltaAvg": "drop_runt_delta_avg", 
        "dropRuntDeltaMax": "drop_runt_delta_max", 
        "dropRuntDeltaMin": "drop_runt_delta_min", 
        "intervals": "intervals", 
        "menloFcIndex": "menlo_fc_index", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "truncateOverrun": "truncate_overrun", 
        "truncateOverrunDelta": "truncate_overrun_delta", 
        "truncateOverrunDeltaAvg": "truncate_overrun_delta_avg", 
        "truncateOverrunDeltaMax": "truncate_overrun_delta_max", 
        "truncateOverrunDeltaMin": "truncate_overrun_delta_min", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, menlo_fc_index, **kwargs):
        self._dirty_mask = 0
        self.menlo_fc_index = menlo_fc_index
        self.child_action = None
        self.drop_acl = None
        self.drop_acl_delta = None
        self.drop_acl_delta_avg = None
        self.drop_acl_delta_max = None
        self.drop_acl_delta_min = None
        self.drop_overrun = None
        self.drop_overrun_delta = None
        self.drop_overrun_delta_avg = None
        self.drop_overrun_delta_max = None
        self.drop_overrun_delta_min = None
        self.drop_runt = None
        self.drop_runt_delta = None
        self.drop_runt_delta_avg = None
        self.drop_runt_delta_max = None
        self.drop_runt_delta_min = None
        self.intervals = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.truncate_overrun = None
        self.truncate_overrun_delta = None
        self.truncate_overrun_delta_avg = None
        self.truncate_overrun_delta_max = None
        self.truncate_overrun_delta_min = None
        self.update = None

        ManagedObject.__init__(self, "AdaptorMenloFcStats", parent_mo_or_dn, **kwargs)
