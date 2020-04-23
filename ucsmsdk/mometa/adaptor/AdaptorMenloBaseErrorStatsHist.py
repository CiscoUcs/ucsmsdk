"""This module contains the general information for AdaptorMenloBaseErrorStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorMenloBaseErrorStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorMenloBaseErrorStatsHist(ManagedObject):
    """This is AdaptorMenloBaseErrorStatsHist class."""

    consts = AdaptorMenloBaseErrorStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorMenloBaseErrorStatsHist", "adaptorMenloBaseErrorStatsHist", "[id]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["read-only"], ['adaptorMenloBaseErrorStats'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "correctable_errors": MoPropertyMeta("correctable_errors", "correctableErrors", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "correctable_errors_delta": MoPropertyMeta("correctable_errors_delta", "correctableErrorsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "correctable_errors_delta_avg": MoPropertyMeta("correctable_errors_delta_avg", "correctableErrorsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "correctable_errors_delta_max": MoPropertyMeta("correctable_errors_delta_max", "correctableErrorsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "correctable_errors_delta_min": MoPropertyMeta("correctable_errors_delta_min", "correctableErrorsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "uncorrectable_errors": MoPropertyMeta("uncorrectable_errors", "uncorrectableErrors", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncorrectable_errors_delta": MoPropertyMeta("uncorrectable_errors_delta", "uncorrectableErrorsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncorrectable_errors_delta_avg": MoPropertyMeta("uncorrectable_errors_delta_avg", "uncorrectableErrorsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncorrectable_errors_delta_max": MoPropertyMeta("uncorrectable_errors_delta_max", "uncorrectableErrorsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncorrectable_errors_delta_min": MoPropertyMeta("uncorrectable_errors_delta_min", "uncorrectableErrorsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "correctableErrors": "correctable_errors", 
        "correctableErrorsDelta": "correctable_errors_delta", 
        "correctableErrorsDeltaAvg": "correctable_errors_delta_avg", 
        "correctableErrorsDeltaMax": "correctable_errors_delta_max", 
        "correctableErrorsDeltaMin": "correctable_errors_delta_min", 
        "dn": "dn", 
        "id": "id", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "uncorrectableErrors": "uncorrectable_errors", 
        "uncorrectableErrorsDelta": "uncorrectable_errors_delta", 
        "uncorrectableErrorsDeltaAvg": "uncorrectable_errors_delta_avg", 
        "uncorrectableErrorsDeltaMax": "uncorrectable_errors_delta_max", 
        "uncorrectableErrorsDeltaMin": "uncorrectable_errors_delta_min", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.correctable_errors = None
        self.correctable_errors_delta = None
        self.correctable_errors_delta_avg = None
        self.correctable_errors_delta_max = None
        self.correctable_errors_delta_min = None
        self.most_recent = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.uncorrectable_errors = None
        self.uncorrectable_errors_delta = None
        self.uncorrectable_errors_delta_avg = None
        self.uncorrectable_errors_delta_max = None
        self.uncorrectable_errors_delta_min = None

        ManagedObject.__init__(self, "AdaptorMenloBaseErrorStatsHist", parent_mo_or_dn, **kwargs)
