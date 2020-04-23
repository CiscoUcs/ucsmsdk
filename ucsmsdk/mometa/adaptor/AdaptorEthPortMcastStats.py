"""This module contains the general information for AdaptorEthPortMcastStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorEthPortMcastStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"
    TRAFFIC_DIRECTION_RX = "rx"
    TRAFFIC_DIRECTION_TX = "tx"
    TRAFFIC_DIRECTION_UNKNOWN = "unknown"


class AdaptorEthPortMcastStats(ManagedObject):
    """This is AdaptorEthPortMcastStats class."""

    consts = AdaptorEthPortMcastStatsConsts()
    naming_props = set(['trafficDirection'])

    mo_meta = MoMeta("AdaptorEthPortMcastStats", "adaptorEthPortMcastStats", "eth-port-mcast-stats-[traffic_direction]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['adaptorExtEthIf', 'adaptorHostEthIf', 'vmNic'], ['adaptorEthPortMcastStatsHist'], ["Get"])

    prop_meta = {
        "broadcast_packets": MoPropertyMeta("broadcast_packets", "broadcastPackets", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_packets_delta": MoPropertyMeta("broadcast_packets_delta", "broadcastPacketsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_packets_delta_avg": MoPropertyMeta("broadcast_packets_delta_avg", "broadcastPacketsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_packets_delta_max": MoPropertyMeta("broadcast_packets_delta_max", "broadcastPacketsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_packets_delta_min": MoPropertyMeta("broadcast_packets_delta_min", "broadcastPacketsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multicast_packets": MoPropertyMeta("multicast_packets", "multicastPackets", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multicast_packets_delta": MoPropertyMeta("multicast_packets_delta", "multicastPacketsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multicast_packets_delta_avg": MoPropertyMeta("multicast_packets_delta_avg", "multicastPacketsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multicast_packets_delta_max": MoPropertyMeta("multicast_packets_delta_max", "multicastPacketsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multicast_packets_delta_min": MoPropertyMeta("multicast_packets_delta_min", "multicastPacketsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "traffic_direction": MoPropertyMeta("traffic_direction", "trafficDirection", "string", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, ["rx", "tx", "unknown"], []),
        "unicast_packets": MoPropertyMeta("unicast_packets", "unicastPackets", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_packets_delta": MoPropertyMeta("unicast_packets_delta", "unicastPacketsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_packets_delta_avg": MoPropertyMeta("unicast_packets_delta_avg", "unicastPacketsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_packets_delta_max": MoPropertyMeta("unicast_packets_delta_max", "unicastPacketsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_packets_delta_min": MoPropertyMeta("unicast_packets_delta_min", "unicastPacketsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "broadcastPackets": "broadcast_packets", 
        "broadcastPacketsDelta": "broadcast_packets_delta", 
        "broadcastPacketsDeltaAvg": "broadcast_packets_delta_avg", 
        "broadcastPacketsDeltaMax": "broadcast_packets_delta_max", 
        "broadcastPacketsDeltaMin": "broadcast_packets_delta_min", 
        "childAction": "child_action", 
        "dn": "dn", 
        "intervals": "intervals", 
        "multicastPackets": "multicast_packets", 
        "multicastPacketsDelta": "multicast_packets_delta", 
        "multicastPacketsDeltaAvg": "multicast_packets_delta_avg", 
        "multicastPacketsDeltaMax": "multicast_packets_delta_max", 
        "multicastPacketsDeltaMin": "multicast_packets_delta_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "trafficDirection": "traffic_direction", 
        "unicastPackets": "unicast_packets", 
        "unicastPacketsDelta": "unicast_packets_delta", 
        "unicastPacketsDeltaAvg": "unicast_packets_delta_avg", 
        "unicastPacketsDeltaMax": "unicast_packets_delta_max", 
        "unicastPacketsDeltaMin": "unicast_packets_delta_min", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, traffic_direction, **kwargs):
        self._dirty_mask = 0
        self.traffic_direction = traffic_direction
        self.broadcast_packets = None
        self.broadcast_packets_delta = None
        self.broadcast_packets_delta_avg = None
        self.broadcast_packets_delta_max = None
        self.broadcast_packets_delta_min = None
        self.child_action = None
        self.intervals = None
        self.multicast_packets = None
        self.multicast_packets_delta = None
        self.multicast_packets_delta_avg = None
        self.multicast_packets_delta_max = None
        self.multicast_packets_delta_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.unicast_packets = None
        self.unicast_packets_delta = None
        self.unicast_packets_delta_avg = None
        self.unicast_packets_delta_max = None
        self.unicast_packets_delta_min = None
        self.update = None

        ManagedObject.__init__(self, "AdaptorEthPortMcastStats", parent_mo_or_dn, **kwargs)
