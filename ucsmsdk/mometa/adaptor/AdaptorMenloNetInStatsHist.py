"""This module contains the general information for AdaptorMenloNetInStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorMenloNetInStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorMenloNetInStatsHist(ManagedObject):
    """This is AdaptorMenloNetInStatsHist class."""

    consts = AdaptorMenloNetInStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorMenloNetInStatsHist", "adaptorMenloNetInStatsHist", "[id]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["read-only"], ['adaptorMenloNetInStats'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "drop_fc_lif_invalid": MoPropertyMeta("drop_fc_lif_invalid", "dropFcLifInvalid", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_fc_lif_invalid_delta": MoPropertyMeta("drop_fc_lif_invalid_delta", "dropFcLifInvalidDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_fc_lif_invalid_delta_avg": MoPropertyMeta("drop_fc_lif_invalid_delta_avg", "dropFcLifInvalidDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_fc_lif_invalid_delta_max": MoPropertyMeta("drop_fc_lif_invalid_delta_max", "dropFcLifInvalidDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_fc_lif_invalid_delta_min": MoPropertyMeta("drop_fc_lif_invalid_delta_min", "dropFcLifInvalidDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_fc_multicast": MoPropertyMeta("drop_fc_multicast", "dropFcMulticast", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_fc_multicast_delta": MoPropertyMeta("drop_fc_multicast_delta", "dropFcMulticastDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_fc_multicast_delta_avg": MoPropertyMeta("drop_fc_multicast_delta_avg", "dropFcMulticastDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_fc_multicast_delta_max": MoPropertyMeta("drop_fc_multicast_delta_max", "dropFcMulticastDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_fc_multicast_delta_min": MoPropertyMeta("drop_fc_multicast_delta_min", "dropFcMulticastDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_null_pif": MoPropertyMeta("drop_null_pif", "dropNullPif", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_null_pif_delta": MoPropertyMeta("drop_null_pif_delta", "dropNullPifDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_null_pif_delta_avg": MoPropertyMeta("drop_null_pif_delta_avg", "dropNullPifDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_null_pif_delta_max": MoPropertyMeta("drop_null_pif_delta_max", "dropNullPifDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_null_pif_delta_min": MoPropertyMeta("drop_null_pif_delta_min", "dropNullPifDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fwd_lookup_no_hit": MoPropertyMeta("fwd_lookup_no_hit", "fwdLookupNoHit", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fwd_lookup_no_hit_delta": MoPropertyMeta("fwd_lookup_no_hit_delta", "fwdLookupNoHitDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fwd_lookup_no_hit_delta_avg": MoPropertyMeta("fwd_lookup_no_hit_delta_avg", "fwdLookupNoHitDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fwd_lookup_no_hit_delta_max": MoPropertyMeta("fwd_lookup_no_hit_delta_max", "fwdLookupNoHitDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fwd_lookup_no_hit_delta_min": MoPropertyMeta("fwd_lookup_no_hit_delta_min", "fwdLookupNoHitDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, [], []),
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
        "dropFcLifInvalid": "drop_fc_lif_invalid", 
        "dropFcLifInvalidDelta": "drop_fc_lif_invalid_delta", 
        "dropFcLifInvalidDeltaAvg": "drop_fc_lif_invalid_delta_avg", 
        "dropFcLifInvalidDeltaMax": "drop_fc_lif_invalid_delta_max", 
        "dropFcLifInvalidDeltaMin": "drop_fc_lif_invalid_delta_min", 
        "dropFcMulticast": "drop_fc_multicast", 
        "dropFcMulticastDelta": "drop_fc_multicast_delta", 
        "dropFcMulticastDeltaAvg": "drop_fc_multicast_delta_avg", 
        "dropFcMulticastDeltaMax": "drop_fc_multicast_delta_max", 
        "dropFcMulticastDeltaMin": "drop_fc_multicast_delta_min", 
        "dropNullPif": "drop_null_pif", 
        "dropNullPifDelta": "drop_null_pif_delta", 
        "dropNullPifDeltaAvg": "drop_null_pif_delta_avg", 
        "dropNullPifDeltaMax": "drop_null_pif_delta_max", 
        "dropNullPifDeltaMin": "drop_null_pif_delta_min", 
        "fwdLookupNoHit": "fwd_lookup_no_hit", 
        "fwdLookupNoHitDelta": "fwd_lookup_no_hit_delta", 
        "fwdLookupNoHitDeltaAvg": "fwd_lookup_no_hit_delta_avg", 
        "fwdLookupNoHitDeltaMax": "fwd_lookup_no_hit_delta_max", 
        "fwdLookupNoHitDeltaMin": "fwd_lookup_no_hit_delta_min", 
        "id": "id", 
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
        self.drop_fc_lif_invalid = None
        self.drop_fc_lif_invalid_delta = None
        self.drop_fc_lif_invalid_delta_avg = None
        self.drop_fc_lif_invalid_delta_max = None
        self.drop_fc_lif_invalid_delta_min = None
        self.drop_fc_multicast = None
        self.drop_fc_multicast_delta = None
        self.drop_fc_multicast_delta_avg = None
        self.drop_fc_multicast_delta_max = None
        self.drop_fc_multicast_delta_min = None
        self.drop_null_pif = None
        self.drop_null_pif_delta = None
        self.drop_null_pif_delta_avg = None
        self.drop_null_pif_delta_max = None
        self.drop_null_pif_delta_min = None
        self.fwd_lookup_no_hit = None
        self.fwd_lookup_no_hit_delta = None
        self.fwd_lookup_no_hit_delta_avg = None
        self.fwd_lookup_no_hit_delta_max = None
        self.fwd_lookup_no_hit_delta_min = None
        self.most_recent = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "AdaptorMenloNetInStatsHist", parent_mo_or_dn, **kwargs)
