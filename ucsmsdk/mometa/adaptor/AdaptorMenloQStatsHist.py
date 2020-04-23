"""This module contains the general information for AdaptorMenloQStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorMenloQStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorMenloQStatsHist(ManagedObject):
    """This is AdaptorMenloQStatsHist class."""

    consts = AdaptorMenloQStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorMenloQStatsHist", "adaptorMenloQStatsHist", "[id]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["read-only"], ['adaptorMenloQStats'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "drop_overrun_n0": MoPropertyMeta("drop_overrun_n0", "dropOverrunN0", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_overrun_n0_delta": MoPropertyMeta("drop_overrun_n0_delta", "dropOverrunN0Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_overrun_n0_delta_avg": MoPropertyMeta("drop_overrun_n0_delta_avg", "dropOverrunN0DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_overrun_n0_delta_max": MoPropertyMeta("drop_overrun_n0_delta_max", "dropOverrunN0DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_overrun_n0_delta_min": MoPropertyMeta("drop_overrun_n0_delta_min", "dropOverrunN0DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_overrun_n1": MoPropertyMeta("drop_overrun_n1", "dropOverrunN1", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_overrun_n1_delta": MoPropertyMeta("drop_overrun_n1_delta", "dropOverrunN1Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_overrun_n1_delta_avg": MoPropertyMeta("drop_overrun_n1_delta_avg", "dropOverrunN1DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_overrun_n1_delta_max": MoPropertyMeta("drop_overrun_n1_delta_max", "dropOverrunN1DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "drop_overrun_n1_delta_min": MoPropertyMeta("drop_overrun_n1_delta_min", "dropOverrunN1DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "truncate_overrun_n0": MoPropertyMeta("truncate_overrun_n0", "truncateOverrunN0", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "truncate_overrun_n0_delta": MoPropertyMeta("truncate_overrun_n0_delta", "truncateOverrunN0Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "truncate_overrun_n0_delta_avg": MoPropertyMeta("truncate_overrun_n0_delta_avg", "truncateOverrunN0DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "truncate_overrun_n0_delta_max": MoPropertyMeta("truncate_overrun_n0_delta_max", "truncateOverrunN0DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "truncate_overrun_n0_delta_min": MoPropertyMeta("truncate_overrun_n0_delta_min", "truncateOverrunN0DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "truncate_overrun_n1": MoPropertyMeta("truncate_overrun_n1", "truncateOverrunN1", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "truncate_overrun_n1_delta": MoPropertyMeta("truncate_overrun_n1_delta", "truncateOverrunN1Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "truncate_overrun_n1_delta_avg": MoPropertyMeta("truncate_overrun_n1_delta_avg", "truncateOverrunN1DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "truncate_overrun_n1_delta_max": MoPropertyMeta("truncate_overrun_n1_delta_max", "truncateOverrunN1DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "truncate_overrun_n1_delta_min": MoPropertyMeta("truncate_overrun_n1_delta_min", "truncateOverrunN1DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "dropOverrunN0": "drop_overrun_n0", 
        "dropOverrunN0Delta": "drop_overrun_n0_delta", 
        "dropOverrunN0DeltaAvg": "drop_overrun_n0_delta_avg", 
        "dropOverrunN0DeltaMax": "drop_overrun_n0_delta_max", 
        "dropOverrunN0DeltaMin": "drop_overrun_n0_delta_min", 
        "dropOverrunN1": "drop_overrun_n1", 
        "dropOverrunN1Delta": "drop_overrun_n1_delta", 
        "dropOverrunN1DeltaAvg": "drop_overrun_n1_delta_avg", 
        "dropOverrunN1DeltaMax": "drop_overrun_n1_delta_max", 
        "dropOverrunN1DeltaMin": "drop_overrun_n1_delta_min", 
        "id": "id", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "truncateOverrunN0": "truncate_overrun_n0", 
        "truncateOverrunN0Delta": "truncate_overrun_n0_delta", 
        "truncateOverrunN0DeltaAvg": "truncate_overrun_n0_delta_avg", 
        "truncateOverrunN0DeltaMax": "truncate_overrun_n0_delta_max", 
        "truncateOverrunN0DeltaMin": "truncate_overrun_n0_delta_min", 
        "truncateOverrunN1": "truncate_overrun_n1", 
        "truncateOverrunN1Delta": "truncate_overrun_n1_delta", 
        "truncateOverrunN1DeltaAvg": "truncate_overrun_n1_delta_avg", 
        "truncateOverrunN1DeltaMax": "truncate_overrun_n1_delta_max", 
        "truncateOverrunN1DeltaMin": "truncate_overrun_n1_delta_min", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.drop_overrun_n0 = None
        self.drop_overrun_n0_delta = None
        self.drop_overrun_n0_delta_avg = None
        self.drop_overrun_n0_delta_max = None
        self.drop_overrun_n0_delta_min = None
        self.drop_overrun_n1 = None
        self.drop_overrun_n1_delta = None
        self.drop_overrun_n1_delta_avg = None
        self.drop_overrun_n1_delta_max = None
        self.drop_overrun_n1_delta_min = None
        self.most_recent = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.truncate_overrun_n0 = None
        self.truncate_overrun_n0_delta = None
        self.truncate_overrun_n0_delta_avg = None
        self.truncate_overrun_n0_delta_max = None
        self.truncate_overrun_n0_delta_min = None
        self.truncate_overrun_n1 = None
        self.truncate_overrun_n1_delta = None
        self.truncate_overrun_n1_delta_avg = None
        self.truncate_overrun_n1_delta_max = None
        self.truncate_overrun_n1_delta_min = None

        ManagedObject.__init__(self, "AdaptorMenloQStatsHist", parent_mo_or_dn, **kwargs)
