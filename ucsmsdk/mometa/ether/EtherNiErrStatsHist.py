"""This module contains the general information for EtherNiErrStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EtherNiErrStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EtherNiErrStatsHist(ManagedObject):
    """This is EtherNiErrStatsHist class."""

    consts = EtherNiErrStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EtherNiErrStatsHist", "etherNiErrStatsHist", "[id]", VersionMeta.Version223a, "OutputOnly", 0xf, [], ["read-only"], ['etherNiErrStats'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "crc": MoPropertyMeta("crc", "crc", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "crc_delta": MoPropertyMeta("crc_delta", "crcDelta", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "crc_delta_avg": MoPropertyMeta("crc_delta_avg", "crcDeltaAvg", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "crc_delta_max": MoPropertyMeta("crc_delta_max", "crcDeltaMax", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "crc_delta_min": MoPropertyMeta("crc_delta_min", "crcDeltaMin", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "frame_tx": MoPropertyMeta("frame_tx", "frameTx", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "frame_tx_delta": MoPropertyMeta("frame_tx_delta", "frameTxDelta", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "frame_tx_delta_avg": MoPropertyMeta("frame_tx_delta_avg", "frameTxDeltaAvg", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "frame_tx_delta_max": MoPropertyMeta("frame_tx_delta_max", "frameTxDeltaMax", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "frame_tx_delta_min": MoPropertyMeta("frame_tx_delta_min", "frameTxDeltaMin", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version223a, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "in_range": MoPropertyMeta("in_range", "inRange", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "in_range_delta": MoPropertyMeta("in_range_delta", "inRangeDelta", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "in_range_delta_avg": MoPropertyMeta("in_range_delta_avg", "inRangeDeltaAvg", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "in_range_delta_max": MoPropertyMeta("in_range_delta_max", "inRangeDeltaMax", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "in_range_delta_min": MoPropertyMeta("in_range_delta_min", "inRangeDeltaMin", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "too_long": MoPropertyMeta("too_long", "tooLong", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_long_delta": MoPropertyMeta("too_long_delta", "tooLongDelta", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_long_delta_avg": MoPropertyMeta("too_long_delta_avg", "tooLongDeltaAvg", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_long_delta_max": MoPropertyMeta("too_long_delta_max", "tooLongDeltaMax", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_long_delta_min": MoPropertyMeta("too_long_delta_min", "tooLongDeltaMin", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_short": MoPropertyMeta("too_short", "tooShort", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_short_delta": MoPropertyMeta("too_short_delta", "tooShortDelta", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_short_delta_avg": MoPropertyMeta("too_short_delta_avg", "tooShortDeltaAvg", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_short_delta_max": MoPropertyMeta("too_short_delta_max", "tooShortDeltaMax", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_short_delta_min": MoPropertyMeta("too_short_delta_min", "tooShortDeltaMin", "ulong", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "crc": "crc", 
        "crcDelta": "crc_delta", 
        "crcDeltaAvg": "crc_delta_avg", 
        "crcDeltaMax": "crc_delta_max", 
        "crcDeltaMin": "crc_delta_min", 
        "dn": "dn", 
        "frameTx": "frame_tx", 
        "frameTxDelta": "frame_tx_delta", 
        "frameTxDeltaAvg": "frame_tx_delta_avg", 
        "frameTxDeltaMax": "frame_tx_delta_max", 
        "frameTxDeltaMin": "frame_tx_delta_min", 
        "id": "id", 
        "inRange": "in_range", 
        "inRangeDelta": "in_range_delta", 
        "inRangeDeltaAvg": "in_range_delta_avg", 
        "inRangeDeltaMax": "in_range_delta_max", 
        "inRangeDeltaMin": "in_range_delta_min", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "tooLong": "too_long", 
        "tooLongDelta": "too_long_delta", 
        "tooLongDeltaAvg": "too_long_delta_avg", 
        "tooLongDeltaMax": "too_long_delta_max", 
        "tooLongDeltaMin": "too_long_delta_min", 
        "tooShort": "too_short", 
        "tooShortDelta": "too_short_delta", 
        "tooShortDeltaAvg": "too_short_delta_avg", 
        "tooShortDeltaMax": "too_short_delta_max", 
        "tooShortDeltaMin": "too_short_delta_min", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.crc = None
        self.crc_delta = None
        self.crc_delta_avg = None
        self.crc_delta_max = None
        self.crc_delta_min = None
        self.frame_tx = None
        self.frame_tx_delta = None
        self.frame_tx_delta_avg = None
        self.frame_tx_delta_max = None
        self.frame_tx_delta_min = None
        self.in_range = None
        self.in_range_delta = None
        self.in_range_delta_avg = None
        self.in_range_delta_max = None
        self.in_range_delta_min = None
        self.most_recent = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.too_long = None
        self.too_long_delta = None
        self.too_long_delta_avg = None
        self.too_long_delta_max = None
        self.too_long_delta_min = None
        self.too_short = None
        self.too_short_delta = None
        self.too_short_delta_avg = None
        self.too_short_delta_max = None
        self.too_short_delta_min = None

        ManagedObject.__init__(self, "EtherNiErrStatsHist", parent_mo_or_dn, **kwargs)
