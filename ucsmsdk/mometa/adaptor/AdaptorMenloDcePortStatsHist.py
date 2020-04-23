"""This module contains the general information for AdaptorMenloDcePortStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorMenloDcePortStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorMenloDcePortStatsHist(ManagedObject):
    """This is AdaptorMenloDcePortStatsHist class."""

    consts = AdaptorMenloDcePortStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorMenloDcePortStatsHist", "adaptorMenloDcePortStatsHist", "[id]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["read-only"], ['adaptorMenloDcePortStats'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rx_pause_cfc": MoPropertyMeta("rx_pause_cfc", "rxPauseCFC", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_pause_cfc_delta": MoPropertyMeta("rx_pause_cfc_delta", "rxPauseCFCDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_pause_cfc_delta_avg": MoPropertyMeta("rx_pause_cfc_delta_avg", "rxPauseCFCDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_pause_cfc_delta_max": MoPropertyMeta("rx_pause_cfc_delta_max", "rxPauseCFCDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_pause_cfc_delta_min": MoPropertyMeta("rx_pause_cfc_delta_min", "rxPauseCFCDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_pause_pfc": MoPropertyMeta("rx_pause_pfc", "rxPausePFC", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_pause_pfc_delta": MoPropertyMeta("rx_pause_pfc_delta", "rxPausePFCDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_pause_pfc_delta_avg": MoPropertyMeta("rx_pause_pfc_delta_avg", "rxPausePFCDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_pause_pfc_delta_max": MoPropertyMeta("rx_pause_pfc_delta_max", "rxPausePFCDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_pause_pfc_delta_min": MoPropertyMeta("rx_pause_pfc_delta_min", "rxPausePFCDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "tx_pause_cfc": MoPropertyMeta("tx_pause_cfc", "txPauseCFC", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_pause_cfc_delta": MoPropertyMeta("tx_pause_cfc_delta", "txPauseCFCDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_pause_cfc_delta_avg": MoPropertyMeta("tx_pause_cfc_delta_avg", "txPauseCFCDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_pause_cfc_delta_max": MoPropertyMeta("tx_pause_cfc_delta_max", "txPauseCFCDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_pause_cfc_delta_min": MoPropertyMeta("tx_pause_cfc_delta_min", "txPauseCFCDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_pause_pfc": MoPropertyMeta("tx_pause_pfc", "txPausePFC", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_pause_pfc_delta": MoPropertyMeta("tx_pause_pfc_delta", "txPausePFCDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_pause_pfc_delta_avg": MoPropertyMeta("tx_pause_pfc_delta_avg", "txPausePFCDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_pause_pfc_delta_max": MoPropertyMeta("tx_pause_pfc_delta_max", "txPausePFCDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_pause_pfc_delta_min": MoPropertyMeta("tx_pause_pfc_delta_min", "txPausePFCDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "rxPauseCFC": "rx_pause_cfc", 
        "rxPauseCFCDelta": "rx_pause_cfc_delta", 
        "rxPauseCFCDeltaAvg": "rx_pause_cfc_delta_avg", 
        "rxPauseCFCDeltaMax": "rx_pause_cfc_delta_max", 
        "rxPauseCFCDeltaMin": "rx_pause_cfc_delta_min", 
        "rxPausePFC": "rx_pause_pfc", 
        "rxPausePFCDelta": "rx_pause_pfc_delta", 
        "rxPausePFCDeltaAvg": "rx_pause_pfc_delta_avg", 
        "rxPausePFCDeltaMax": "rx_pause_pfc_delta_max", 
        "rxPausePFCDeltaMin": "rx_pause_pfc_delta_min", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "txPauseCFC": "tx_pause_cfc", 
        "txPauseCFCDelta": "tx_pause_cfc_delta", 
        "txPauseCFCDeltaAvg": "tx_pause_cfc_delta_avg", 
        "txPauseCFCDeltaMax": "tx_pause_cfc_delta_max", 
        "txPauseCFCDeltaMin": "tx_pause_cfc_delta_min", 
        "txPausePFC": "tx_pause_pfc", 
        "txPausePFCDelta": "tx_pause_pfc_delta", 
        "txPausePFCDeltaAvg": "tx_pause_pfc_delta_avg", 
        "txPausePFCDeltaMax": "tx_pause_pfc_delta_max", 
        "txPausePFCDeltaMin": "tx_pause_pfc_delta_min", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.most_recent = None
        self.rx_pause_cfc = None
        self.rx_pause_cfc_delta = None
        self.rx_pause_cfc_delta_avg = None
        self.rx_pause_cfc_delta_max = None
        self.rx_pause_cfc_delta_min = None
        self.rx_pause_pfc = None
        self.rx_pause_pfc_delta = None
        self.rx_pause_pfc_delta_avg = None
        self.rx_pause_pfc_delta_max = None
        self.rx_pause_pfc_delta_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.tx_pause_cfc = None
        self.tx_pause_cfc_delta = None
        self.tx_pause_cfc_delta_avg = None
        self.tx_pause_cfc_delta_max = None
        self.tx_pause_cfc_delta_min = None
        self.tx_pause_pfc = None
        self.tx_pause_pfc_delta = None
        self.tx_pause_pfc_delta_avg = None
        self.tx_pause_pfc_delta_max = None
        self.tx_pause_pfc_delta_min = None

        ManagedObject.__init__(self, "AdaptorMenloDcePortStatsHist", parent_mo_or_dn, **kwargs)
