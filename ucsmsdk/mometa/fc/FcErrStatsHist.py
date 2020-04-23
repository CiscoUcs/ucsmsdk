"""This module contains the general information for FcErrStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FcErrStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class FcErrStatsHist(ManagedObject):
    """This is FcErrStatsHist class."""

    consts = FcErrStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("FcErrStatsHist", "fcErrStatsHist", "[id]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["read-only"], ['fcErrStats'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "crc_rx": MoPropertyMeta("crc_rx", "crcRx", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "crc_rx_delta": MoPropertyMeta("crc_rx_delta", "crcRxDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "crc_rx_delta_avg": MoPropertyMeta("crc_rx_delta_avg", "crcRxDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "crc_rx_delta_max": MoPropertyMeta("crc_rx_delta_max", "crcRxDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "crc_rx_delta_min": MoPropertyMeta("crc_rx_delta_min", "crcRxDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "discard_rx": MoPropertyMeta("discard_rx", "discardRx", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "discard_rx_delta": MoPropertyMeta("discard_rx_delta", "discardRxDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "discard_rx_delta_avg": MoPropertyMeta("discard_rx_delta_avg", "discardRxDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "discard_rx_delta_max": MoPropertyMeta("discard_rx_delta_max", "discardRxDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "discard_rx_delta_min": MoPropertyMeta("discard_rx_delta_min", "discardRxDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "discard_tx": MoPropertyMeta("discard_tx", "discardTx", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "discard_tx_delta": MoPropertyMeta("discard_tx_delta", "discardTxDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "discard_tx_delta_avg": MoPropertyMeta("discard_tx_delta_avg", "discardTxDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "discard_tx_delta_max": MoPropertyMeta("discard_tx_delta_max", "discardTxDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "discard_tx_delta_min": MoPropertyMeta("discard_tx_delta_min", "discardTxDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "link_failures": MoPropertyMeta("link_failures", "linkFailures", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "link_failures_delta": MoPropertyMeta("link_failures_delta", "linkFailuresDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "link_failures_delta_avg": MoPropertyMeta("link_failures_delta_avg", "linkFailuresDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "link_failures_delta_max": MoPropertyMeta("link_failures_delta_max", "linkFailuresDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "link_failures_delta_min": MoPropertyMeta("link_failures_delta_min", "linkFailuresDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rx": MoPropertyMeta("rx", "rx", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_delta": MoPropertyMeta("rx_delta", "rxDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_delta_avg": MoPropertyMeta("rx_delta_avg", "rxDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_delta_max": MoPropertyMeta("rx_delta_max", "rxDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rx_delta_min": MoPropertyMeta("rx_delta_min", "rxDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "signal_losses": MoPropertyMeta("signal_losses", "signalLosses", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "signal_losses_delta": MoPropertyMeta("signal_losses_delta", "signalLossesDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "signal_losses_delta_avg": MoPropertyMeta("signal_losses_delta_avg", "signalLossesDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "signal_losses_delta_max": MoPropertyMeta("signal_losses_delta_max", "signalLossesDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "signal_losses_delta_min": MoPropertyMeta("signal_losses_delta_min", "signalLossesDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "sync_losses": MoPropertyMeta("sync_losses", "syncLosses", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sync_losses_delta": MoPropertyMeta("sync_losses_delta", "syncLossesDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sync_losses_delta_avg": MoPropertyMeta("sync_losses_delta_avg", "syncLossesDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sync_losses_delta_max": MoPropertyMeta("sync_losses_delta_max", "syncLossesDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sync_losses_delta_min": MoPropertyMeta("sync_losses_delta_min", "syncLossesDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "too_long_rx": MoPropertyMeta("too_long_rx", "tooLongRx", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_long_rx_delta": MoPropertyMeta("too_long_rx_delta", "tooLongRxDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_long_rx_delta_avg": MoPropertyMeta("too_long_rx_delta_avg", "tooLongRxDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_long_rx_delta_max": MoPropertyMeta("too_long_rx_delta_max", "tooLongRxDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_long_rx_delta_min": MoPropertyMeta("too_long_rx_delta_min", "tooLongRxDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_short_rx": MoPropertyMeta("too_short_rx", "tooShortRx", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_short_rx_delta": MoPropertyMeta("too_short_rx_delta", "tooShortRxDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_short_rx_delta_avg": MoPropertyMeta("too_short_rx_delta_avg", "tooShortRxDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_short_rx_delta_max": MoPropertyMeta("too_short_rx_delta_max", "tooShortRxDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_short_rx_delta_min": MoPropertyMeta("too_short_rx_delta_min", "tooShortRxDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx": MoPropertyMeta("tx", "tx", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_delta": MoPropertyMeta("tx_delta", "txDelta", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_delta_avg": MoPropertyMeta("tx_delta_avg", "txDeltaAvg", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_delta_max": MoPropertyMeta("tx_delta_max", "txDeltaMax", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "tx_delta_min": MoPropertyMeta("tx_delta_min", "txDeltaMin", "ulong", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "crcRx": "crc_rx", 
        "crcRxDelta": "crc_rx_delta", 
        "crcRxDeltaAvg": "crc_rx_delta_avg", 
        "crcRxDeltaMax": "crc_rx_delta_max", 
        "crcRxDeltaMin": "crc_rx_delta_min", 
        "discardRx": "discard_rx", 
        "discardRxDelta": "discard_rx_delta", 
        "discardRxDeltaAvg": "discard_rx_delta_avg", 
        "discardRxDeltaMax": "discard_rx_delta_max", 
        "discardRxDeltaMin": "discard_rx_delta_min", 
        "discardTx": "discard_tx", 
        "discardTxDelta": "discard_tx_delta", 
        "discardTxDeltaAvg": "discard_tx_delta_avg", 
        "discardTxDeltaMax": "discard_tx_delta_max", 
        "discardTxDeltaMin": "discard_tx_delta_min", 
        "dn": "dn", 
        "id": "id", 
        "linkFailures": "link_failures", 
        "linkFailuresDelta": "link_failures_delta", 
        "linkFailuresDeltaAvg": "link_failures_delta_avg", 
        "linkFailuresDeltaMax": "link_failures_delta_max", 
        "linkFailuresDeltaMin": "link_failures_delta_min", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "rx": "rx", 
        "rxDelta": "rx_delta", 
        "rxDeltaAvg": "rx_delta_avg", 
        "rxDeltaMax": "rx_delta_max", 
        "rxDeltaMin": "rx_delta_min", 
        "sacl": "sacl", 
        "signalLosses": "signal_losses", 
        "signalLossesDelta": "signal_losses_delta", 
        "signalLossesDeltaAvg": "signal_losses_delta_avg", 
        "signalLossesDeltaMax": "signal_losses_delta_max", 
        "signalLossesDeltaMin": "signal_losses_delta_min", 
        "status": "status", 
        "suspect": "suspect", 
        "syncLosses": "sync_losses", 
        "syncLossesDelta": "sync_losses_delta", 
        "syncLossesDeltaAvg": "sync_losses_delta_avg", 
        "syncLossesDeltaMax": "sync_losses_delta_max", 
        "syncLossesDeltaMin": "sync_losses_delta_min", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "tooLongRx": "too_long_rx", 
        "tooLongRxDelta": "too_long_rx_delta", 
        "tooLongRxDeltaAvg": "too_long_rx_delta_avg", 
        "tooLongRxDeltaMax": "too_long_rx_delta_max", 
        "tooLongRxDeltaMin": "too_long_rx_delta_min", 
        "tooShortRx": "too_short_rx", 
        "tooShortRxDelta": "too_short_rx_delta", 
        "tooShortRxDeltaAvg": "too_short_rx_delta_avg", 
        "tooShortRxDeltaMax": "too_short_rx_delta_max", 
        "tooShortRxDeltaMin": "too_short_rx_delta_min", 
        "tx": "tx", 
        "txDelta": "tx_delta", 
        "txDeltaAvg": "tx_delta_avg", 
        "txDeltaMax": "tx_delta_max", 
        "txDeltaMin": "tx_delta_min", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.crc_rx = None
        self.crc_rx_delta = None
        self.crc_rx_delta_avg = None
        self.crc_rx_delta_max = None
        self.crc_rx_delta_min = None
        self.discard_rx = None
        self.discard_rx_delta = None
        self.discard_rx_delta_avg = None
        self.discard_rx_delta_max = None
        self.discard_rx_delta_min = None
        self.discard_tx = None
        self.discard_tx_delta = None
        self.discard_tx_delta_avg = None
        self.discard_tx_delta_max = None
        self.discard_tx_delta_min = None
        self.link_failures = None
        self.link_failures_delta = None
        self.link_failures_delta_avg = None
        self.link_failures_delta_max = None
        self.link_failures_delta_min = None
        self.most_recent = None
        self.rx = None
        self.rx_delta = None
        self.rx_delta_avg = None
        self.rx_delta_max = None
        self.rx_delta_min = None
        self.sacl = None
        self.signal_losses = None
        self.signal_losses_delta = None
        self.signal_losses_delta_avg = None
        self.signal_losses_delta_max = None
        self.signal_losses_delta_min = None
        self.status = None
        self.suspect = None
        self.sync_losses = None
        self.sync_losses_delta = None
        self.sync_losses_delta_avg = None
        self.sync_losses_delta_max = None
        self.sync_losses_delta_min = None
        self.thresholded = None
        self.time_collected = None
        self.too_long_rx = None
        self.too_long_rx_delta = None
        self.too_long_rx_delta_avg = None
        self.too_long_rx_delta_max = None
        self.too_long_rx_delta_min = None
        self.too_short_rx = None
        self.too_short_rx_delta = None
        self.too_short_rx_delta_avg = None
        self.too_short_rx_delta_max = None
        self.too_short_rx_delta_min = None
        self.tx = None
        self.tx_delta = None
        self.tx_delta_avg = None
        self.tx_delta_max = None
        self.tx_delta_min = None

        ManagedObject.__init__(self, "FcErrStatsHist", parent_mo_or_dn, **kwargs)
