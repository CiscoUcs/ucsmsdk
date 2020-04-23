"""This module contains the general information for EtherTxStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EtherTxStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EtherTxStatsHist(ManagedObject):
    """This is EtherTxStatsHist class."""

    consts = EtherTxStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EtherTxStatsHist", "etherTxStatsHist", "[id]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["read-only"], ['etherTxStats'], [], ["Get"])

    prop_meta = {
        "broadcast_packets": MoPropertyMeta("broadcast_packets", "broadcastPackets", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_packets_delta": MoPropertyMeta("broadcast_packets_delta", "broadcastPacketsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_packets_delta_avg": MoPropertyMeta("broadcast_packets_delta_avg", "broadcastPacketsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_packets_delta_max": MoPropertyMeta("broadcast_packets_delta_max", "broadcastPacketsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_packets_delta_min": MoPropertyMeta("broadcast_packets_delta_min", "broadcastPacketsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "jumbo_packets": MoPropertyMeta("jumbo_packets", "jumboPackets", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "jumbo_packets_delta": MoPropertyMeta("jumbo_packets_delta", "jumboPacketsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "jumbo_packets_delta_avg": MoPropertyMeta("jumbo_packets_delta_avg", "jumboPacketsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "jumbo_packets_delta_max": MoPropertyMeta("jumbo_packets_delta_max", "jumboPacketsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "jumbo_packets_delta_min": MoPropertyMeta("jumbo_packets_delta_min", "jumboPacketsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
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
        "total_bytes": MoPropertyMeta("total_bytes", "totalBytes", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total_bytes_delta": MoPropertyMeta("total_bytes_delta", "totalBytesDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total_bytes_delta_avg": MoPropertyMeta("total_bytes_delta_avg", "totalBytesDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total_bytes_delta_max": MoPropertyMeta("total_bytes_delta_max", "totalBytesDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total_bytes_delta_min": MoPropertyMeta("total_bytes_delta_min", "totalBytesDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total_packets": MoPropertyMeta("total_packets", "totalPackets", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total_packets_delta": MoPropertyMeta("total_packets_delta", "totalPacketsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total_packets_delta_avg": MoPropertyMeta("total_packets_delta_avg", "totalPacketsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total_packets_delta_max": MoPropertyMeta("total_packets_delta_max", "totalPacketsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total_packets_delta_min": MoPropertyMeta("total_packets_delta_min", "totalPacketsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_packets": MoPropertyMeta("unicast_packets", "unicastPackets", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_packets_delta": MoPropertyMeta("unicast_packets_delta", "unicastPacketsDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_packets_delta_avg": MoPropertyMeta("unicast_packets_delta_avg", "unicastPacketsDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_packets_delta_max": MoPropertyMeta("unicast_packets_delta_max", "unicastPacketsDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_packets_delta_min": MoPropertyMeta("unicast_packets_delta_min", "unicastPacketsDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "broadcastPackets": "broadcast_packets", 
        "broadcastPacketsDelta": "broadcast_packets_delta", 
        "broadcastPacketsDeltaAvg": "broadcast_packets_delta_avg", 
        "broadcastPacketsDeltaMax": "broadcast_packets_delta_max", 
        "broadcastPacketsDeltaMin": "broadcast_packets_delta_min", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "jumboPackets": "jumbo_packets", 
        "jumboPacketsDelta": "jumbo_packets_delta", 
        "jumboPacketsDeltaAvg": "jumbo_packets_delta_avg", 
        "jumboPacketsDeltaMax": "jumbo_packets_delta_max", 
        "jumboPacketsDeltaMin": "jumbo_packets_delta_min", 
        "mostRecent": "most_recent", 
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
        "totalBytes": "total_bytes", 
        "totalBytesDelta": "total_bytes_delta", 
        "totalBytesDeltaAvg": "total_bytes_delta_avg", 
        "totalBytesDeltaMax": "total_bytes_delta_max", 
        "totalBytesDeltaMin": "total_bytes_delta_min", 
        "totalPackets": "total_packets", 
        "totalPacketsDelta": "total_packets_delta", 
        "totalPacketsDeltaAvg": "total_packets_delta_avg", 
        "totalPacketsDeltaMax": "total_packets_delta_max", 
        "totalPacketsDeltaMin": "total_packets_delta_min", 
        "unicastPackets": "unicast_packets", 
        "unicastPacketsDelta": "unicast_packets_delta", 
        "unicastPacketsDeltaAvg": "unicast_packets_delta_avg", 
        "unicastPacketsDeltaMax": "unicast_packets_delta_max", 
        "unicastPacketsDeltaMin": "unicast_packets_delta_min", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.broadcast_packets = None
        self.broadcast_packets_delta = None
        self.broadcast_packets_delta_avg = None
        self.broadcast_packets_delta_max = None
        self.broadcast_packets_delta_min = None
        self.child_action = None
        self.jumbo_packets = None
        self.jumbo_packets_delta = None
        self.jumbo_packets_delta_avg = None
        self.jumbo_packets_delta_max = None
        self.jumbo_packets_delta_min = None
        self.most_recent = None
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
        self.total_bytes = None
        self.total_bytes_delta = None
        self.total_bytes_delta_avg = None
        self.total_bytes_delta_max = None
        self.total_bytes_delta_min = None
        self.total_packets = None
        self.total_packets_delta = None
        self.total_packets_delta_avg = None
        self.total_packets_delta_max = None
        self.total_packets_delta_min = None
        self.unicast_packets = None
        self.unicast_packets_delta = None
        self.unicast_packets_delta_avg = None
        self.unicast_packets_delta_max = None
        self.unicast_packets_delta_min = None

        ManagedObject.__init__(self, "EtherTxStatsHist", parent_mo_or_dn, **kwargs)
