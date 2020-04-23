"""This module contains the general information for AdaptorEthPortBySizeSmallStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorEthPortBySizeSmallStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorEthPortBySizeSmallStatsHist(ManagedObject):
    """This is AdaptorEthPortBySizeSmallStatsHist class."""

    consts = AdaptorEthPortBySizeSmallStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorEthPortBySizeSmallStatsHist", "adaptorEthPortBySizeSmallStatsHist", "[id]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["read-only"], ['adaptorEthPortBySizeSmallStats'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "equals64": MoPropertyMeta("equals64", "equals64", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "equals64_delta": MoPropertyMeta("equals64_delta", "equals64Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "equals64_delta_avg": MoPropertyMeta("equals64_delta_avg", "equals64DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "equals64_delta_max": MoPropertyMeta("equals64_delta_max", "equals64DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "equals64_delta_min": MoPropertyMeta("equals64_delta_min", "equals64DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "less_than1024": MoPropertyMeta("less_than1024", "lessThan1024", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than1024_delta": MoPropertyMeta("less_than1024_delta", "lessThan1024Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than1024_delta_avg": MoPropertyMeta("less_than1024_delta_avg", "lessThan1024DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than1024_delta_max": MoPropertyMeta("less_than1024_delta_max", "lessThan1024DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than1024_delta_min": MoPropertyMeta("less_than1024_delta_min", "lessThan1024DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than128": MoPropertyMeta("less_than128", "lessThan128", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than128_delta": MoPropertyMeta("less_than128_delta", "lessThan128Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than128_delta_avg": MoPropertyMeta("less_than128_delta_avg", "lessThan128DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than128_delta_max": MoPropertyMeta("less_than128_delta_max", "lessThan128DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than128_delta_min": MoPropertyMeta("less_than128_delta_min", "lessThan128DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than256": MoPropertyMeta("less_than256", "lessThan256", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than256_delta": MoPropertyMeta("less_than256_delta", "lessThan256Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than256_delta_avg": MoPropertyMeta("less_than256_delta_avg", "lessThan256DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than256_delta_max": MoPropertyMeta("less_than256_delta_max", "lessThan256DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than256_delta_min": MoPropertyMeta("less_than256_delta_min", "lessThan256DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than512": MoPropertyMeta("less_than512", "lessThan512", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than512_delta": MoPropertyMeta("less_than512_delta", "lessThan512Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than512_delta_avg": MoPropertyMeta("less_than512_delta_avg", "lessThan512DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than512_delta_max": MoPropertyMeta("less_than512_delta_max", "lessThan512DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than512_delta_min": MoPropertyMeta("less_than512_delta_min", "lessThan512DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than64": MoPropertyMeta("less_than64", "lessThan64", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than64_delta": MoPropertyMeta("less_than64_delta", "lessThan64Delta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than64_delta_avg": MoPropertyMeta("less_than64_delta_avg", "lessThan64DeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than64_delta_max": MoPropertyMeta("less_than64_delta_max", "lessThan64DeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "less_than64_delta_min": MoPropertyMeta("less_than64_delta_min", "lessThan64DeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
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
        "equals64": "equals64", 
        "equals64Delta": "equals64_delta", 
        "equals64DeltaAvg": "equals64_delta_avg", 
        "equals64DeltaMax": "equals64_delta_max", 
        "equals64DeltaMin": "equals64_delta_min", 
        "id": "id", 
        "lessThan1024": "less_than1024", 
        "lessThan1024Delta": "less_than1024_delta", 
        "lessThan1024DeltaAvg": "less_than1024_delta_avg", 
        "lessThan1024DeltaMax": "less_than1024_delta_max", 
        "lessThan1024DeltaMin": "less_than1024_delta_min", 
        "lessThan128": "less_than128", 
        "lessThan128Delta": "less_than128_delta", 
        "lessThan128DeltaAvg": "less_than128_delta_avg", 
        "lessThan128DeltaMax": "less_than128_delta_max", 
        "lessThan128DeltaMin": "less_than128_delta_min", 
        "lessThan256": "less_than256", 
        "lessThan256Delta": "less_than256_delta", 
        "lessThan256DeltaAvg": "less_than256_delta_avg", 
        "lessThan256DeltaMax": "less_than256_delta_max", 
        "lessThan256DeltaMin": "less_than256_delta_min", 
        "lessThan512": "less_than512", 
        "lessThan512Delta": "less_than512_delta", 
        "lessThan512DeltaAvg": "less_than512_delta_avg", 
        "lessThan512DeltaMax": "less_than512_delta_max", 
        "lessThan512DeltaMin": "less_than512_delta_min", 
        "lessThan64": "less_than64", 
        "lessThan64Delta": "less_than64_delta", 
        "lessThan64DeltaAvg": "less_than64_delta_avg", 
        "lessThan64DeltaMax": "less_than64_delta_max", 
        "lessThan64DeltaMin": "less_than64_delta_min", 
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
        self.equals64 = None
        self.equals64_delta = None
        self.equals64_delta_avg = None
        self.equals64_delta_max = None
        self.equals64_delta_min = None
        self.less_than1024 = None
        self.less_than1024_delta = None
        self.less_than1024_delta_avg = None
        self.less_than1024_delta_max = None
        self.less_than1024_delta_min = None
        self.less_than128 = None
        self.less_than128_delta = None
        self.less_than128_delta_avg = None
        self.less_than128_delta_max = None
        self.less_than128_delta_min = None
        self.less_than256 = None
        self.less_than256_delta = None
        self.less_than256_delta_avg = None
        self.less_than256_delta_max = None
        self.less_than256_delta_min = None
        self.less_than512 = None
        self.less_than512_delta = None
        self.less_than512_delta_avg = None
        self.less_than512_delta_max = None
        self.less_than512_delta_min = None
        self.less_than64 = None
        self.less_than64_delta = None
        self.less_than64_delta_avg = None
        self.less_than64_delta_max = None
        self.less_than64_delta_min = None
        self.most_recent = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "AdaptorEthPortBySizeSmallStatsHist", parent_mo_or_dn, **kwargs)
