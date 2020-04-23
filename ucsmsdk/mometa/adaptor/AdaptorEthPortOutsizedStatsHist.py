"""This module contains the general information for AdaptorEthPortOutsizedStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorEthPortOutsizedStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorEthPortOutsizedStatsHist(ManagedObject):
    """This is AdaptorEthPortOutsizedStatsHist class."""

    consts = AdaptorEthPortOutsizedStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorEthPortOutsizedStatsHist", "adaptorEthPortOutsizedStatsHist", "[id]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["read-only"], ['adaptorEthPortOutsizedStats'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "oversized_bad_crc_packets": MoPropertyMeta("oversized_bad_crc_packets", "oversizedBadCrcPackets", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oversized_bad_crc_packets_delta": MoPropertyMeta("oversized_bad_crc_packets_delta", "oversizedBadCrcPacketsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oversized_bad_crc_packets_delta_avg": MoPropertyMeta("oversized_bad_crc_packets_delta_avg", "oversizedBadCrcPacketsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oversized_bad_crc_packets_delta_max": MoPropertyMeta("oversized_bad_crc_packets_delta_max", "oversizedBadCrcPacketsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oversized_bad_crc_packets_delta_min": MoPropertyMeta("oversized_bad_crc_packets_delta_min", "oversizedBadCrcPacketsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oversized_good_crc_packets": MoPropertyMeta("oversized_good_crc_packets", "oversizedGoodCrcPackets", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oversized_good_crc_packets_delta": MoPropertyMeta("oversized_good_crc_packets_delta", "oversizedGoodCrcPacketsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oversized_good_crc_packets_delta_avg": MoPropertyMeta("oversized_good_crc_packets_delta_avg", "oversizedGoodCrcPacketsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oversized_good_crc_packets_delta_max": MoPropertyMeta("oversized_good_crc_packets_delta_max", "oversizedGoodCrcPacketsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oversized_good_crc_packets_delta_min": MoPropertyMeta("oversized_good_crc_packets_delta_min", "oversizedGoodCrcPacketsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oversized_packets": MoPropertyMeta("oversized_packets", "oversizedPackets", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oversized_packets_delta": MoPropertyMeta("oversized_packets_delta", "oversizedPacketsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oversized_packets_delta_avg": MoPropertyMeta("oversized_packets_delta_avg", "oversizedPacketsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oversized_packets_delta_max": MoPropertyMeta("oversized_packets_delta_max", "oversizedPacketsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oversized_packets_delta_min": MoPropertyMeta("oversized_packets_delta_min", "oversizedPacketsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "undersized_bad_crc_packets": MoPropertyMeta("undersized_bad_crc_packets", "undersizedBadCrcPackets", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "undersized_bad_crc_packets_delta": MoPropertyMeta("undersized_bad_crc_packets_delta", "undersizedBadCrcPacketsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "undersized_bad_crc_packets_delta_avg": MoPropertyMeta("undersized_bad_crc_packets_delta_avg", "undersizedBadCrcPacketsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "undersized_bad_crc_packets_delta_max": MoPropertyMeta("undersized_bad_crc_packets_delta_max", "undersizedBadCrcPacketsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "undersized_bad_crc_packets_delta_min": MoPropertyMeta("undersized_bad_crc_packets_delta_min", "undersizedBadCrcPacketsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "undersized_good_crc_packets": MoPropertyMeta("undersized_good_crc_packets", "undersizedGoodCrcPackets", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "undersized_good_crc_packets_delta": MoPropertyMeta("undersized_good_crc_packets_delta", "undersizedGoodCrcPacketsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "undersized_good_crc_packets_delta_avg": MoPropertyMeta("undersized_good_crc_packets_delta_avg", "undersizedGoodCrcPacketsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "undersized_good_crc_packets_delta_max": MoPropertyMeta("undersized_good_crc_packets_delta_max", "undersizedGoodCrcPacketsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "undersized_good_crc_packets_delta_min": MoPropertyMeta("undersized_good_crc_packets_delta_min", "undersizedGoodCrcPacketsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "mostRecent": "most_recent", 
        "oversizedBadCrcPackets": "oversized_bad_crc_packets", 
        "oversizedBadCrcPacketsDelta": "oversized_bad_crc_packets_delta", 
        "oversizedBadCrcPacketsDeltaAvg": "oversized_bad_crc_packets_delta_avg", 
        "oversizedBadCrcPacketsDeltaMax": "oversized_bad_crc_packets_delta_max", 
        "oversizedBadCrcPacketsDeltaMin": "oversized_bad_crc_packets_delta_min", 
        "oversizedGoodCrcPackets": "oversized_good_crc_packets", 
        "oversizedGoodCrcPacketsDelta": "oversized_good_crc_packets_delta", 
        "oversizedGoodCrcPacketsDeltaAvg": "oversized_good_crc_packets_delta_avg", 
        "oversizedGoodCrcPacketsDeltaMax": "oversized_good_crc_packets_delta_max", 
        "oversizedGoodCrcPacketsDeltaMin": "oversized_good_crc_packets_delta_min", 
        "oversizedPackets": "oversized_packets", 
        "oversizedPacketsDelta": "oversized_packets_delta", 
        "oversizedPacketsDeltaAvg": "oversized_packets_delta_avg", 
        "oversizedPacketsDeltaMax": "oversized_packets_delta_max", 
        "oversizedPacketsDeltaMin": "oversized_packets_delta_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "undersizedBadCrcPackets": "undersized_bad_crc_packets", 
        "undersizedBadCrcPacketsDelta": "undersized_bad_crc_packets_delta", 
        "undersizedBadCrcPacketsDeltaAvg": "undersized_bad_crc_packets_delta_avg", 
        "undersizedBadCrcPacketsDeltaMax": "undersized_bad_crc_packets_delta_max", 
        "undersizedBadCrcPacketsDeltaMin": "undersized_bad_crc_packets_delta_min", 
        "undersizedGoodCrcPackets": "undersized_good_crc_packets", 
        "undersizedGoodCrcPacketsDelta": "undersized_good_crc_packets_delta", 
        "undersizedGoodCrcPacketsDeltaAvg": "undersized_good_crc_packets_delta_avg", 
        "undersizedGoodCrcPacketsDeltaMax": "undersized_good_crc_packets_delta_max", 
        "undersizedGoodCrcPacketsDeltaMin": "undersized_good_crc_packets_delta_min", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.most_recent = None
        self.oversized_bad_crc_packets = None
        self.oversized_bad_crc_packets_delta = None
        self.oversized_bad_crc_packets_delta_avg = None
        self.oversized_bad_crc_packets_delta_max = None
        self.oversized_bad_crc_packets_delta_min = None
        self.oversized_good_crc_packets = None
        self.oversized_good_crc_packets_delta = None
        self.oversized_good_crc_packets_delta_avg = None
        self.oversized_good_crc_packets_delta_max = None
        self.oversized_good_crc_packets_delta_min = None
        self.oversized_packets = None
        self.oversized_packets_delta = None
        self.oversized_packets_delta_avg = None
        self.oversized_packets_delta_max = None
        self.oversized_packets_delta_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.undersized_bad_crc_packets = None
        self.undersized_bad_crc_packets_delta = None
        self.undersized_bad_crc_packets_delta_avg = None
        self.undersized_bad_crc_packets_delta_max = None
        self.undersized_bad_crc_packets_delta_min = None
        self.undersized_good_crc_packets = None
        self.undersized_good_crc_packets_delta = None
        self.undersized_good_crc_packets_delta_avg = None
        self.undersized_good_crc_packets_delta_max = None
        self.undersized_good_crc_packets_delta_min = None

        ManagedObject.__init__(self, "AdaptorEthPortOutsizedStatsHist", parent_mo_or_dn, **kwargs)
