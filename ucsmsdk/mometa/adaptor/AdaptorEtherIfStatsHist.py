"""This module contains the general information for AdaptorEtherIfStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorEtherIfStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorEtherIfStatsHist(ManagedObject):
    """This is AdaptorEtherIfStatsHist class."""

    consts = AdaptorEtherIfStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorEtherIfStatsHist", "adaptorEtherIfStatsHist", "[id]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["read-only"], ['adaptorEtherIfStats'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rx_bytes": MoPropertyMeta("rx_bytes", "rxBytes", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_bytes_delta": MoPropertyMeta("rx_bytes_delta", "rxBytesDelta", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_bytes_delta_avg": MoPropertyMeta("rx_bytes_delta_avg", "rxBytesDeltaAvg", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_bytes_delta_max": MoPropertyMeta("rx_bytes_delta_max", "rxBytesDeltaMax", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_bytes_delta_min": MoPropertyMeta("rx_bytes_delta_min", "rxBytesDeltaMin", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_dropped": MoPropertyMeta("rx_dropped", "rxDropped", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_dropped_delta": MoPropertyMeta("rx_dropped_delta", "rxDroppedDelta", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_dropped_delta_avg": MoPropertyMeta("rx_dropped_delta_avg", "rxDroppedDeltaAvg", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_dropped_delta_max": MoPropertyMeta("rx_dropped_delta_max", "rxDroppedDeltaMax", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_dropped_delta_min": MoPropertyMeta("rx_dropped_delta_min", "rxDroppedDeltaMin", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_errors": MoPropertyMeta("rx_errors", "rxErrors", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_errors_delta": MoPropertyMeta("rx_errors_delta", "rxErrorsDelta", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_errors_delta_avg": MoPropertyMeta("rx_errors_delta_avg", "rxErrorsDeltaAvg", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_errors_delta_max": MoPropertyMeta("rx_errors_delta_max", "rxErrorsDeltaMax", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_errors_delta_min": MoPropertyMeta("rx_errors_delta_min", "rxErrorsDeltaMin", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_packets": MoPropertyMeta("rx_packets", "rxPackets", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_packets_delta": MoPropertyMeta("rx_packets_delta", "rxPacketsDelta", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_packets_delta_avg": MoPropertyMeta("rx_packets_delta_avg", "rxPacketsDeltaAvg", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_packets_delta_max": MoPropertyMeta("rx_packets_delta_max", "rxPacketsDeltaMax", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_packets_delta_min": MoPropertyMeta("rx_packets_delta_min", "rxPacketsDeltaMin", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "tx_bytes": MoPropertyMeta("tx_bytes", "txBytes", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_bytes_delta": MoPropertyMeta("tx_bytes_delta", "txBytesDelta", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_bytes_delta_avg": MoPropertyMeta("tx_bytes_delta_avg", "txBytesDeltaAvg", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_bytes_delta_max": MoPropertyMeta("tx_bytes_delta_max", "txBytesDeltaMax", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_bytes_delta_min": MoPropertyMeta("tx_bytes_delta_min", "txBytesDeltaMin", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_dropped": MoPropertyMeta("tx_dropped", "txDropped", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_dropped_delta": MoPropertyMeta("tx_dropped_delta", "txDroppedDelta", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_dropped_delta_avg": MoPropertyMeta("tx_dropped_delta_avg", "txDroppedDeltaAvg", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_dropped_delta_max": MoPropertyMeta("tx_dropped_delta_max", "txDroppedDeltaMax", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_dropped_delta_min": MoPropertyMeta("tx_dropped_delta_min", "txDroppedDeltaMin", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_errors": MoPropertyMeta("tx_errors", "txErrors", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_errors_delta": MoPropertyMeta("tx_errors_delta", "txErrorsDelta", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_errors_delta_avg": MoPropertyMeta("tx_errors_delta_avg", "txErrorsDeltaAvg", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_errors_delta_max": MoPropertyMeta("tx_errors_delta_max", "txErrorsDeltaMax", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_errors_delta_min": MoPropertyMeta("tx_errors_delta_min", "txErrorsDeltaMin", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_packets": MoPropertyMeta("tx_packets", "txPackets", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_packets_delta": MoPropertyMeta("tx_packets_delta", "txPacketsDelta", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_packets_delta_avg": MoPropertyMeta("tx_packets_delta_avg", "txPacketsDeltaAvg", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_packets_delta_max": MoPropertyMeta("tx_packets_delta_max", "txPacketsDeltaMax", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_packets_delta_min": MoPropertyMeta("tx_packets_delta_min", "txPacketsDeltaMin", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "rxBytes": "rx_bytes", 
        "rxBytesDelta": "rx_bytes_delta", 
        "rxBytesDeltaAvg": "rx_bytes_delta_avg", 
        "rxBytesDeltaMax": "rx_bytes_delta_max", 
        "rxBytesDeltaMin": "rx_bytes_delta_min", 
        "rxDropped": "rx_dropped", 
        "rxDroppedDelta": "rx_dropped_delta", 
        "rxDroppedDeltaAvg": "rx_dropped_delta_avg", 
        "rxDroppedDeltaMax": "rx_dropped_delta_max", 
        "rxDroppedDeltaMin": "rx_dropped_delta_min", 
        "rxErrors": "rx_errors", 
        "rxErrorsDelta": "rx_errors_delta", 
        "rxErrorsDeltaAvg": "rx_errors_delta_avg", 
        "rxErrorsDeltaMax": "rx_errors_delta_max", 
        "rxErrorsDeltaMin": "rx_errors_delta_min", 
        "rxPackets": "rx_packets", 
        "rxPacketsDelta": "rx_packets_delta", 
        "rxPacketsDeltaAvg": "rx_packets_delta_avg", 
        "rxPacketsDeltaMax": "rx_packets_delta_max", 
        "rxPacketsDeltaMin": "rx_packets_delta_min", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "txBytes": "tx_bytes", 
        "txBytesDelta": "tx_bytes_delta", 
        "txBytesDeltaAvg": "tx_bytes_delta_avg", 
        "txBytesDeltaMax": "tx_bytes_delta_max", 
        "txBytesDeltaMin": "tx_bytes_delta_min", 
        "txDropped": "tx_dropped", 
        "txDroppedDelta": "tx_dropped_delta", 
        "txDroppedDeltaAvg": "tx_dropped_delta_avg", 
        "txDroppedDeltaMax": "tx_dropped_delta_max", 
        "txDroppedDeltaMin": "tx_dropped_delta_min", 
        "txErrors": "tx_errors", 
        "txErrorsDelta": "tx_errors_delta", 
        "txErrorsDeltaAvg": "tx_errors_delta_avg", 
        "txErrorsDeltaMax": "tx_errors_delta_max", 
        "txErrorsDeltaMin": "tx_errors_delta_min", 
        "txPackets": "tx_packets", 
        "txPacketsDelta": "tx_packets_delta", 
        "txPacketsDeltaAvg": "tx_packets_delta_avg", 
        "txPacketsDeltaMax": "tx_packets_delta_max", 
        "txPacketsDeltaMin": "tx_packets_delta_min", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.most_recent = None
        self.rx_bytes = None
        self.rx_bytes_delta = None
        self.rx_bytes_delta_avg = None
        self.rx_bytes_delta_max = None
        self.rx_bytes_delta_min = None
        self.rx_dropped = None
        self.rx_dropped_delta = None
        self.rx_dropped_delta_avg = None
        self.rx_dropped_delta_max = None
        self.rx_dropped_delta_min = None
        self.rx_errors = None
        self.rx_errors_delta = None
        self.rx_errors_delta_avg = None
        self.rx_errors_delta_max = None
        self.rx_errors_delta_min = None
        self.rx_packets = None
        self.rx_packets_delta = None
        self.rx_packets_delta_avg = None
        self.rx_packets_delta_max = None
        self.rx_packets_delta_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.tx_bytes = None
        self.tx_bytes_delta = None
        self.tx_bytes_delta_avg = None
        self.tx_bytes_delta_max = None
        self.tx_bytes_delta_min = None
        self.tx_dropped = None
        self.tx_dropped_delta = None
        self.tx_dropped_delta_avg = None
        self.tx_dropped_delta_max = None
        self.tx_dropped_delta_min = None
        self.tx_errors = None
        self.tx_errors_delta = None
        self.tx_errors_delta_avg = None
        self.tx_errors_delta_max = None
        self.tx_errors_delta_min = None
        self.tx_packets = None
        self.tx_packets_delta = None
        self.tx_packets_delta_avg = None
        self.tx_packets_delta_max = None
        self.tx_packets_delta_min = None

        ManagedObject.__init__(self, "AdaptorEtherIfStatsHist", parent_mo_or_dn, **kwargs)
