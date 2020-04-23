"""This module contains the general information for AdaptorFcPortStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorFcPortStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorFcPortStatsHist(ManagedObject):
    """This is AdaptorFcPortStatsHist class."""

    consts = AdaptorFcPortStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorFcPortStatsHist", "adaptorFcPortStatsHist", "[id]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["read-only"], ['adaptorFcPortStats'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rx_bad_frames": MoPropertyMeta("rx_bad_frames", "rxBadFrames", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_bad_frames_delta": MoPropertyMeta("rx_bad_frames_delta", "rxBadFramesDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_bad_frames_delta_avg": MoPropertyMeta("rx_bad_frames_delta_avg", "rxBadFramesDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_bad_frames_delta_max": MoPropertyMeta("rx_bad_frames_delta_max", "rxBadFramesDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_bad_frames_delta_min": MoPropertyMeta("rx_bad_frames_delta_min", "rxBadFramesDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_frames": MoPropertyMeta("rx_frames", "rxFrames", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_frames_delta": MoPropertyMeta("rx_frames_delta", "rxFramesDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_frames_delta_avg": MoPropertyMeta("rx_frames_delta_avg", "rxFramesDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_frames_delta_max": MoPropertyMeta("rx_frames_delta_max", "rxFramesDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_frames_delta_min": MoPropertyMeta("rx_frames_delta_min", "rxFramesDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "tx_bad_frames": MoPropertyMeta("tx_bad_frames", "txBadFrames", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_bad_frames_delta": MoPropertyMeta("tx_bad_frames_delta", "txBadFramesDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_bad_frames_delta_avg": MoPropertyMeta("tx_bad_frames_delta_avg", "txBadFramesDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_bad_frames_delta_max": MoPropertyMeta("tx_bad_frames_delta_max", "txBadFramesDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_bad_frames_delta_min": MoPropertyMeta("tx_bad_frames_delta_min", "txBadFramesDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_frames": MoPropertyMeta("tx_frames", "txFrames", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_frames_delta": MoPropertyMeta("tx_frames_delta", "txFramesDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_frames_delta_avg": MoPropertyMeta("tx_frames_delta_avg", "txFramesDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_frames_delta_max": MoPropertyMeta("tx_frames_delta_max", "txFramesDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_frames_delta_min": MoPropertyMeta("tx_frames_delta_min", "txFramesDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "rxBadFrames": "rx_bad_frames", 
        "rxBadFramesDelta": "rx_bad_frames_delta", 
        "rxBadFramesDeltaAvg": "rx_bad_frames_delta_avg", 
        "rxBadFramesDeltaMax": "rx_bad_frames_delta_max", 
        "rxBadFramesDeltaMin": "rx_bad_frames_delta_min", 
        "rxFrames": "rx_frames", 
        "rxFramesDelta": "rx_frames_delta", 
        "rxFramesDeltaAvg": "rx_frames_delta_avg", 
        "rxFramesDeltaMax": "rx_frames_delta_max", 
        "rxFramesDeltaMin": "rx_frames_delta_min", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "txBadFrames": "tx_bad_frames", 
        "txBadFramesDelta": "tx_bad_frames_delta", 
        "txBadFramesDeltaAvg": "tx_bad_frames_delta_avg", 
        "txBadFramesDeltaMax": "tx_bad_frames_delta_max", 
        "txBadFramesDeltaMin": "tx_bad_frames_delta_min", 
        "txFrames": "tx_frames", 
        "txFramesDelta": "tx_frames_delta", 
        "txFramesDeltaAvg": "tx_frames_delta_avg", 
        "txFramesDeltaMax": "tx_frames_delta_max", 
        "txFramesDeltaMin": "tx_frames_delta_min", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.most_recent = None
        self.rx_bad_frames = None
        self.rx_bad_frames_delta = None
        self.rx_bad_frames_delta_avg = None
        self.rx_bad_frames_delta_max = None
        self.rx_bad_frames_delta_min = None
        self.rx_frames = None
        self.rx_frames_delta = None
        self.rx_frames_delta_avg = None
        self.rx_frames_delta_max = None
        self.rx_frames_delta_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.tx_bad_frames = None
        self.tx_bad_frames_delta = None
        self.tx_bad_frames_delta_avg = None
        self.tx_bad_frames_delta_max = None
        self.tx_bad_frames_delta_min = None
        self.tx_frames = None
        self.tx_frames_delta = None
        self.tx_frames_delta_avg = None
        self.tx_frames_delta_max = None
        self.tx_frames_delta_min = None

        ManagedObject.__init__(self, "AdaptorFcPortStatsHist", parent_mo_or_dn, **kwargs)
