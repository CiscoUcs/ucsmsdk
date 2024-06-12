"""This module contains the general information for AdaptorEthPortErrStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorEthPortErrStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"
    TRAFFIC_DIRECTION_RX = "rx"
    TRAFFIC_DIRECTION_TX = "tx"
    TRAFFIC_DIRECTION_UNKNOWN = "unknown"


class AdaptorEthPortErrStats(ManagedObject):
    """This is AdaptorEthPortErrStats class."""

    consts = AdaptorEthPortErrStatsConsts()
    naming_props = set(['trafficDirection'])

    mo_meta = MoMeta("AdaptorEthPortErrStats", "adaptorEthPortErrStats", "eth-port-err-stats-[traffic_direction]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['adaptorExtEthIf', 'adaptorHostEthIf', 'vmNic'], ['adaptorEthPortErrStatsHist'], ["Get"])

    prop_meta = {
        "bad_crc_packets": MoPropertyMeta("bad_crc_packets", "badCrcPackets", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bad_crc_packets_delta": MoPropertyMeta("bad_crc_packets_delta", "badCrcPacketsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bad_crc_packets_delta_avg": MoPropertyMeta("bad_crc_packets_delta_avg", "badCrcPacketsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bad_crc_packets_delta_max": MoPropertyMeta("bad_crc_packets_delta_max", "badCrcPacketsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bad_crc_packets_delta_min": MoPropertyMeta("bad_crc_packets_delta_min", "badCrcPacketsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bad_length_packets": MoPropertyMeta("bad_length_packets", "badLengthPackets", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bad_length_packets_delta": MoPropertyMeta("bad_length_packets_delta", "badLengthPacketsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bad_length_packets_delta_avg": MoPropertyMeta("bad_length_packets_delta_avg", "badLengthPacketsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bad_length_packets_delta_max": MoPropertyMeta("bad_length_packets_delta_max", "badLengthPacketsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bad_length_packets_delta_min": MoPropertyMeta("bad_length_packets_delta_min", "badLengthPacketsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mac_discarded_packets": MoPropertyMeta("mac_discarded_packets", "macDiscardedPackets", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mac_discarded_packets_delta": MoPropertyMeta("mac_discarded_packets_delta", "macDiscardedPacketsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mac_discarded_packets_delta_avg": MoPropertyMeta("mac_discarded_packets_delta_avg", "macDiscardedPacketsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mac_discarded_packets_delta_max": MoPropertyMeta("mac_discarded_packets_delta_max", "macDiscardedPacketsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mac_discarded_packets_delta_min": MoPropertyMeta("mac_discarded_packets_delta_min", "macDiscardedPacketsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "no_buffer_drop_packets": MoPropertyMeta("no_buffer_drop_packets", "noBufferDropPackets", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "no_buffer_drop_packets_delta": MoPropertyMeta("no_buffer_drop_packets_delta", "noBufferDropPacketsDelta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "no_buffer_drop_packets_delta_avg": MoPropertyMeta("no_buffer_drop_packets_delta_avg", "noBufferDropPacketsDeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "no_buffer_drop_packets_delta_max": MoPropertyMeta("no_buffer_drop_packets_delta_max", "noBufferDropPacketsDeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "no_buffer_drop_packets_delta_min": MoPropertyMeta("no_buffer_drop_packets_delta_min", "noBufferDropPacketsDeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "traffic_direction": MoPropertyMeta("traffic_direction", "trafficDirection", "string", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, ["rx", "tx", "unknown"], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "badCrcPackets": "bad_crc_packets", 
        "badCrcPacketsDelta": "bad_crc_packets_delta", 
        "badCrcPacketsDeltaAvg": "bad_crc_packets_delta_avg", 
        "badCrcPacketsDeltaMax": "bad_crc_packets_delta_max", 
        "badCrcPacketsDeltaMin": "bad_crc_packets_delta_min", 
        "badLengthPackets": "bad_length_packets", 
        "badLengthPacketsDelta": "bad_length_packets_delta", 
        "badLengthPacketsDeltaAvg": "bad_length_packets_delta_avg", 
        "badLengthPacketsDeltaMax": "bad_length_packets_delta_max", 
        "badLengthPacketsDeltaMin": "bad_length_packets_delta_min", 
        "childAction": "child_action", 
        "dn": "dn", 
        "intervals": "intervals", 
        "macDiscardedPackets": "mac_discarded_packets", 
        "macDiscardedPacketsDelta": "mac_discarded_packets_delta", 
        "macDiscardedPacketsDeltaAvg": "mac_discarded_packets_delta_avg", 
        "macDiscardedPacketsDeltaMax": "mac_discarded_packets_delta_max", 
        "macDiscardedPacketsDeltaMin": "mac_discarded_packets_delta_min", 
        "noBufferDropPackets": "no_buffer_drop_packets", 
        "noBufferDropPacketsDelta": "no_buffer_drop_packets_delta", 
        "noBufferDropPacketsDeltaAvg": "no_buffer_drop_packets_delta_avg", 
        "noBufferDropPacketsDeltaMax": "no_buffer_drop_packets_delta_max", 
        "noBufferDropPacketsDeltaMin": "no_buffer_drop_packets_delta_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "trafficDirection": "traffic_direction", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, traffic_direction, **kwargs):
        self._dirty_mask = 0
        self.traffic_direction = traffic_direction
        self.bad_crc_packets = None
        self.bad_crc_packets_delta = None
        self.bad_crc_packets_delta_avg = None
        self.bad_crc_packets_delta_max = None
        self.bad_crc_packets_delta_min = None
        self.bad_length_packets = None
        self.bad_length_packets_delta = None
        self.bad_length_packets_delta_avg = None
        self.bad_length_packets_delta_max = None
        self.bad_length_packets_delta_min = None
        self.child_action = None
        self.intervals = None
        self.mac_discarded_packets = None
        self.mac_discarded_packets_delta = None
        self.mac_discarded_packets_delta_avg = None
        self.mac_discarded_packets_delta_max = None
        self.mac_discarded_packets_delta_min = None
        self.no_buffer_drop_packets = None
        self.no_buffer_drop_packets_delta = None
        self.no_buffer_drop_packets_delta_avg = None
        self.no_buffer_drop_packets_delta_max = None
        self.no_buffer_drop_packets_delta_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "AdaptorEthPortErrStats", parent_mo_or_dn, **kwargs)
