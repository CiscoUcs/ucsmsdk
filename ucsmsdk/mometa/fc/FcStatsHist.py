"""This module contains the general information for FcStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FcStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class FcStatsHist(ManagedObject):
    """This is FcStatsHist class."""

    consts = FcStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("FcStatsHist", "fcStatsHist", "[id]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["read-only"], ['fcStats'], [], ["Get"])

    prop_meta = {
        "bytes_rx": MoPropertyMeta("bytes_rx", "bytesRx", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bytes_rx_delta": MoPropertyMeta("bytes_rx_delta", "bytesRxDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bytes_rx_delta_avg": MoPropertyMeta("bytes_rx_delta_avg", "bytesRxDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bytes_rx_delta_max": MoPropertyMeta("bytes_rx_delta_max", "bytesRxDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bytes_rx_delta_min": MoPropertyMeta("bytes_rx_delta_min", "bytesRxDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bytes_tx": MoPropertyMeta("bytes_tx", "bytesTx", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bytes_tx_delta": MoPropertyMeta("bytes_tx_delta", "bytesTxDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bytes_tx_delta_avg": MoPropertyMeta("bytes_tx_delta_avg", "bytesTxDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bytes_tx_delta_max": MoPropertyMeta("bytes_tx_delta_max", "bytesTxDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bytes_tx_delta_min": MoPropertyMeta("bytes_tx_delta_min", "bytesTxDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "packets_rx": MoPropertyMeta("packets_rx", "packetsRx", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "packets_rx_delta": MoPropertyMeta("packets_rx_delta", "packetsRxDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "packets_rx_delta_avg": MoPropertyMeta("packets_rx_delta_avg", "packetsRxDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "packets_rx_delta_max": MoPropertyMeta("packets_rx_delta_max", "packetsRxDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "packets_rx_delta_min": MoPropertyMeta("packets_rx_delta_min", "packetsRxDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "packets_tx": MoPropertyMeta("packets_tx", "packetsTx", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "packets_tx_delta": MoPropertyMeta("packets_tx_delta", "packetsTxDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "packets_tx_delta_avg": MoPropertyMeta("packets_tx_delta_avg", "packetsTxDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "packets_tx_delta_max": MoPropertyMeta("packets_tx_delta_max", "packetsTxDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "packets_tx_delta_min": MoPropertyMeta("packets_tx_delta_min", "packetsTxDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
    }

    prop_map = {
        "bytesRx": "bytes_rx", 
        "bytesRxDelta": "bytes_rx_delta", 
        "bytesRxDeltaAvg": "bytes_rx_delta_avg", 
        "bytesRxDeltaMax": "bytes_rx_delta_max", 
        "bytesRxDeltaMin": "bytes_rx_delta_min", 
        "bytesTx": "bytes_tx", 
        "bytesTxDelta": "bytes_tx_delta", 
        "bytesTxDeltaAvg": "bytes_tx_delta_avg", 
        "bytesTxDeltaMax": "bytes_tx_delta_max", 
        "bytesTxDeltaMin": "bytes_tx_delta_min", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "mostRecent": "most_recent", 
        "packetsRx": "packets_rx", 
        "packetsRxDelta": "packets_rx_delta", 
        "packetsRxDeltaAvg": "packets_rx_delta_avg", 
        "packetsRxDeltaMax": "packets_rx_delta_max", 
        "packetsRxDeltaMin": "packets_rx_delta_min", 
        "packetsTx": "packets_tx", 
        "packetsTxDelta": "packets_tx_delta", 
        "packetsTxDeltaAvg": "packets_tx_delta_avg", 
        "packetsTxDeltaMax": "packets_tx_delta_max", 
        "packetsTxDeltaMin": "packets_tx_delta_min", 
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
        self.bytes_rx = None
        self.bytes_rx_delta = None
        self.bytes_rx_delta_avg = None
        self.bytes_rx_delta_max = None
        self.bytes_rx_delta_min = None
        self.bytes_tx = None
        self.bytes_tx_delta = None
        self.bytes_tx_delta_avg = None
        self.bytes_tx_delta_max = None
        self.bytes_tx_delta_min = None
        self.child_action = None
        self.most_recent = None
        self.packets_rx = None
        self.packets_rx_delta = None
        self.packets_rx_delta_avg = None
        self.packets_rx_delta_max = None
        self.packets_rx_delta_min = None
        self.packets_tx = None
        self.packets_tx_delta = None
        self.packets_tx_delta_avg = None
        self.packets_tx_delta_max = None
        self.packets_tx_delta_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "FcStatsHist", parent_mo_or_dn, **kwargs)
