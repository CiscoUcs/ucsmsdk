"""This module contains the general information for EtherMacSecRxStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EtherMacSecRxStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EtherMacSecRxStats(ManagedObject):
    """This is EtherMacSecRxStats class."""

    consts = EtherMacSecRxStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("EtherMacSecRxStats", "etherMacSecRxStats", "macsec-rx-stats", VersionMeta.Version434a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['etherPIo'], ['etherMacSecRxStatsHist'], [None])

    prop_meta = {
        "broadcast_controlled_packets": MoPropertyMeta("broadcast_controlled_packets", "broadcastControlledPackets", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_controlled_packets_delta": MoPropertyMeta("broadcast_controlled_packets_delta", "broadcastControlledPacketsDelta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_controlled_packets_delta_avg": MoPropertyMeta("broadcast_controlled_packets_delta_avg", "broadcastControlledPacketsDeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_controlled_packets_delta_max": MoPropertyMeta("broadcast_controlled_packets_delta_max", "broadcastControlledPacketsDeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_controlled_packets_delta_min": MoPropertyMeta("broadcast_controlled_packets_delta_min", "broadcastControlledPacketsDeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_uncontrolled_packets": MoPropertyMeta("broadcast_uncontrolled_packets", "broadcastUncontrolledPackets", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_uncontrolled_packets_delta": MoPropertyMeta("broadcast_uncontrolled_packets_delta", "broadcastUncontrolledPacketsDelta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_uncontrolled_packets_delta_avg": MoPropertyMeta("broadcast_uncontrolled_packets_delta_avg", "broadcastUncontrolledPacketsDeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_uncontrolled_packets_delta_max": MoPropertyMeta("broadcast_uncontrolled_packets_delta_max", "broadcastUncontrolledPacketsDeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "broadcast_uncontrolled_packets_delta_min": MoPropertyMeta("broadcast_uncontrolled_packets_delta_min", "broadcastUncontrolledPacketsDeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "controlled_packets": MoPropertyMeta("controlled_packets", "controlledPackets", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "controlled_packets_delta": MoPropertyMeta("controlled_packets_delta", "controlledPacketsDelta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "controlled_packets_delta_avg": MoPropertyMeta("controlled_packets_delta_avg", "controlledPacketsDeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "controlled_packets_delta_max": MoPropertyMeta("controlled_packets_delta_max", "controlledPacketsDeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "controlled_packets_delta_min": MoPropertyMeta("controlled_packets_delta_min", "controlledPacketsDeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "controlled_rx_drop_packets": MoPropertyMeta("controlled_rx_drop_packets", "controlledRxDropPackets", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "controlled_rx_drop_packets_delta": MoPropertyMeta("controlled_rx_drop_packets_delta", "controlledRxDropPacketsDelta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "controlled_rx_drop_packets_delta_avg": MoPropertyMeta("controlled_rx_drop_packets_delta_avg", "controlledRxDropPacketsDeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "controlled_rx_drop_packets_delta_max": MoPropertyMeta("controlled_rx_drop_packets_delta_max", "controlledRxDropPacketsDeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "controlled_rx_drop_packets_delta_min": MoPropertyMeta("controlled_rx_drop_packets_delta_min", "controlledRxDropPacketsDeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "controlled_rx_error_packets": MoPropertyMeta("controlled_rx_error_packets", "controlledRxErrorPackets", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "controlled_rx_error_packets_delta": MoPropertyMeta("controlled_rx_error_packets_delta", "controlledRxErrorPacketsDelta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "controlled_rx_error_packets_delta_avg": MoPropertyMeta("controlled_rx_error_packets_delta_avg", "controlledRxErrorPacketsDeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "controlled_rx_error_packets_delta_max": MoPropertyMeta("controlled_rx_error_packets_delta_max", "controlledRxErrorPacketsDeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "controlled_rx_error_packets_delta_min": MoPropertyMeta("controlled_rx_error_packets_delta_min", "controlledRxErrorPacketsDeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multicast_controlled_packets": MoPropertyMeta("multicast_controlled_packets", "multicastControlledPackets", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multicast_controlled_packets_delta": MoPropertyMeta("multicast_controlled_packets_delta", "multicastControlledPacketsDelta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multicast_controlled_packets_delta_avg": MoPropertyMeta("multicast_controlled_packets_delta_avg", "multicastControlledPacketsDeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multicast_controlled_packets_delta_max": MoPropertyMeta("multicast_controlled_packets_delta_max", "multicastControlledPacketsDeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multicast_controlled_packets_delta_min": MoPropertyMeta("multicast_controlled_packets_delta_min", "multicastControlledPacketsDeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multicast_uncontrolled_packets": MoPropertyMeta("multicast_uncontrolled_packets", "multicastUncontrolledPackets", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multicast_uncontrolled_packets_delta": MoPropertyMeta("multicast_uncontrolled_packets_delta", "multicastUncontrolledPacketsDelta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multicast_uncontrolled_packets_delta_avg": MoPropertyMeta("multicast_uncontrolled_packets_delta_avg", "multicastUncontrolledPacketsDeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multicast_uncontrolled_packets_delta_max": MoPropertyMeta("multicast_uncontrolled_packets_delta_max", "multicastUncontrolledPacketsDeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "multicast_uncontrolled_packets_delta_min": MoPropertyMeta("multicast_uncontrolled_packets_delta_min", "multicastUncontrolledPacketsDeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "uncontrolled_rx_drop_packets": MoPropertyMeta("uncontrolled_rx_drop_packets", "uncontrolledRxDropPackets", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncontrolled_rx_drop_packets_delta": MoPropertyMeta("uncontrolled_rx_drop_packets_delta", "uncontrolledRxDropPacketsDelta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncontrolled_rx_drop_packets_delta_avg": MoPropertyMeta("uncontrolled_rx_drop_packets_delta_avg", "uncontrolledRxDropPacketsDeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncontrolled_rx_drop_packets_delta_max": MoPropertyMeta("uncontrolled_rx_drop_packets_delta_max", "uncontrolledRxDropPacketsDeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncontrolled_rx_drop_packets_delta_min": MoPropertyMeta("uncontrolled_rx_drop_packets_delta_min", "uncontrolledRxDropPacketsDeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncontrolled_rx_error_packets": MoPropertyMeta("uncontrolled_rx_error_packets", "uncontrolledRxErrorPackets", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncontrolled_rx_error_packets_delta": MoPropertyMeta("uncontrolled_rx_error_packets_delta", "uncontrolledRxErrorPacketsDelta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncontrolled_rx_error_packets_delta_avg": MoPropertyMeta("uncontrolled_rx_error_packets_delta_avg", "uncontrolledRxErrorPacketsDeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncontrolled_rx_error_packets_delta_max": MoPropertyMeta("uncontrolled_rx_error_packets_delta_max", "uncontrolledRxErrorPacketsDeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncontrolled_rx_error_packets_delta_min": MoPropertyMeta("uncontrolled_rx_error_packets_delta_min", "uncontrolledRxErrorPacketsDeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_controlled_packets": MoPropertyMeta("unicast_controlled_packets", "unicastControlledPackets", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_controlled_packets_delta": MoPropertyMeta("unicast_controlled_packets_delta", "unicastControlledPacketsDelta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_controlled_packets_delta_avg": MoPropertyMeta("unicast_controlled_packets_delta_avg", "unicastControlledPacketsDeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_controlled_packets_delta_max": MoPropertyMeta("unicast_controlled_packets_delta_max", "unicastControlledPacketsDeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_controlled_packets_delta_min": MoPropertyMeta("unicast_controlled_packets_delta_min", "unicastControlledPacketsDeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_uncontrolled_packets": MoPropertyMeta("unicast_uncontrolled_packets", "unicastUncontrolledPackets", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_uncontrolled_packets_delta": MoPropertyMeta("unicast_uncontrolled_packets_delta", "unicastUncontrolledPacketsDelta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_uncontrolled_packets_delta_avg": MoPropertyMeta("unicast_uncontrolled_packets_delta_avg", "unicastUncontrolledPacketsDeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_uncontrolled_packets_delta_max": MoPropertyMeta("unicast_uncontrolled_packets_delta_max", "unicastUncontrolledPacketsDeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "unicast_uncontrolled_packets_delta_min": MoPropertyMeta("unicast_uncontrolled_packets_delta_min", "unicastUncontrolledPacketsDeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "broadcastControlledPackets": "broadcast_controlled_packets", 
        "broadcastControlledPacketsDelta": "broadcast_controlled_packets_delta", 
        "broadcastControlledPacketsDeltaAvg": "broadcast_controlled_packets_delta_avg", 
        "broadcastControlledPacketsDeltaMax": "broadcast_controlled_packets_delta_max", 
        "broadcastControlledPacketsDeltaMin": "broadcast_controlled_packets_delta_min", 
        "broadcastUncontrolledPackets": "broadcast_uncontrolled_packets", 
        "broadcastUncontrolledPacketsDelta": "broadcast_uncontrolled_packets_delta", 
        "broadcastUncontrolledPacketsDeltaAvg": "broadcast_uncontrolled_packets_delta_avg", 
        "broadcastUncontrolledPacketsDeltaMax": "broadcast_uncontrolled_packets_delta_max", 
        "broadcastUncontrolledPacketsDeltaMin": "broadcast_uncontrolled_packets_delta_min", 
        "childAction": "child_action", 
        "controlledPackets": "controlled_packets", 
        "controlledPacketsDelta": "controlled_packets_delta", 
        "controlledPacketsDeltaAvg": "controlled_packets_delta_avg", 
        "controlledPacketsDeltaMax": "controlled_packets_delta_max", 
        "controlledPacketsDeltaMin": "controlled_packets_delta_min", 
        "controlledRxDropPackets": "controlled_rx_drop_packets", 
        "controlledRxDropPacketsDelta": "controlled_rx_drop_packets_delta", 
        "controlledRxDropPacketsDeltaAvg": "controlled_rx_drop_packets_delta_avg", 
        "controlledRxDropPacketsDeltaMax": "controlled_rx_drop_packets_delta_max", 
        "controlledRxDropPacketsDeltaMin": "controlled_rx_drop_packets_delta_min", 
        "controlledRxErrorPackets": "controlled_rx_error_packets", 
        "controlledRxErrorPacketsDelta": "controlled_rx_error_packets_delta", 
        "controlledRxErrorPacketsDeltaAvg": "controlled_rx_error_packets_delta_avg", 
        "controlledRxErrorPacketsDeltaMax": "controlled_rx_error_packets_delta_max", 
        "controlledRxErrorPacketsDeltaMin": "controlled_rx_error_packets_delta_min", 
        "dn": "dn", 
        "intervals": "intervals", 
        "multicastControlledPackets": "multicast_controlled_packets", 
        "multicastControlledPacketsDelta": "multicast_controlled_packets_delta", 
        "multicastControlledPacketsDeltaAvg": "multicast_controlled_packets_delta_avg", 
        "multicastControlledPacketsDeltaMax": "multicast_controlled_packets_delta_max", 
        "multicastControlledPacketsDeltaMin": "multicast_controlled_packets_delta_min", 
        "multicastUncontrolledPackets": "multicast_uncontrolled_packets", 
        "multicastUncontrolledPacketsDelta": "multicast_uncontrolled_packets_delta", 
        "multicastUncontrolledPacketsDeltaAvg": "multicast_uncontrolled_packets_delta_avg", 
        "multicastUncontrolledPacketsDeltaMax": "multicast_uncontrolled_packets_delta_max", 
        "multicastUncontrolledPacketsDeltaMin": "multicast_uncontrolled_packets_delta_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "uncontrolledRxDropPackets": "uncontrolled_rx_drop_packets", 
        "uncontrolledRxDropPacketsDelta": "uncontrolled_rx_drop_packets_delta", 
        "uncontrolledRxDropPacketsDeltaAvg": "uncontrolled_rx_drop_packets_delta_avg", 
        "uncontrolledRxDropPacketsDeltaMax": "uncontrolled_rx_drop_packets_delta_max", 
        "uncontrolledRxDropPacketsDeltaMin": "uncontrolled_rx_drop_packets_delta_min", 
        "uncontrolledRxErrorPackets": "uncontrolled_rx_error_packets", 
        "uncontrolledRxErrorPacketsDelta": "uncontrolled_rx_error_packets_delta", 
        "uncontrolledRxErrorPacketsDeltaAvg": "uncontrolled_rx_error_packets_delta_avg", 
        "uncontrolledRxErrorPacketsDeltaMax": "uncontrolled_rx_error_packets_delta_max", 
        "uncontrolledRxErrorPacketsDeltaMin": "uncontrolled_rx_error_packets_delta_min", 
        "unicastControlledPackets": "unicast_controlled_packets", 
        "unicastControlledPacketsDelta": "unicast_controlled_packets_delta", 
        "unicastControlledPacketsDeltaAvg": "unicast_controlled_packets_delta_avg", 
        "unicastControlledPacketsDeltaMax": "unicast_controlled_packets_delta_max", 
        "unicastControlledPacketsDeltaMin": "unicast_controlled_packets_delta_min", 
        "unicastUncontrolledPackets": "unicast_uncontrolled_packets", 
        "unicastUncontrolledPacketsDelta": "unicast_uncontrolled_packets_delta", 
        "unicastUncontrolledPacketsDeltaAvg": "unicast_uncontrolled_packets_delta_avg", 
        "unicastUncontrolledPacketsDeltaMax": "unicast_uncontrolled_packets_delta_max", 
        "unicastUncontrolledPacketsDeltaMin": "unicast_uncontrolled_packets_delta_min", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.broadcast_controlled_packets = None
        self.broadcast_controlled_packets_delta = None
        self.broadcast_controlled_packets_delta_avg = None
        self.broadcast_controlled_packets_delta_max = None
        self.broadcast_controlled_packets_delta_min = None
        self.broadcast_uncontrolled_packets = None
        self.broadcast_uncontrolled_packets_delta = None
        self.broadcast_uncontrolled_packets_delta_avg = None
        self.broadcast_uncontrolled_packets_delta_max = None
        self.broadcast_uncontrolled_packets_delta_min = None
        self.child_action = None
        self.controlled_packets = None
        self.controlled_packets_delta = None
        self.controlled_packets_delta_avg = None
        self.controlled_packets_delta_max = None
        self.controlled_packets_delta_min = None
        self.controlled_rx_drop_packets = None
        self.controlled_rx_drop_packets_delta = None
        self.controlled_rx_drop_packets_delta_avg = None
        self.controlled_rx_drop_packets_delta_max = None
        self.controlled_rx_drop_packets_delta_min = None
        self.controlled_rx_error_packets = None
        self.controlled_rx_error_packets_delta = None
        self.controlled_rx_error_packets_delta_avg = None
        self.controlled_rx_error_packets_delta_max = None
        self.controlled_rx_error_packets_delta_min = None
        self.intervals = None
        self.multicast_controlled_packets = None
        self.multicast_controlled_packets_delta = None
        self.multicast_controlled_packets_delta_avg = None
        self.multicast_controlled_packets_delta_max = None
        self.multicast_controlled_packets_delta_min = None
        self.multicast_uncontrolled_packets = None
        self.multicast_uncontrolled_packets_delta = None
        self.multicast_uncontrolled_packets_delta_avg = None
        self.multicast_uncontrolled_packets_delta_max = None
        self.multicast_uncontrolled_packets_delta_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.uncontrolled_rx_drop_packets = None
        self.uncontrolled_rx_drop_packets_delta = None
        self.uncontrolled_rx_drop_packets_delta_avg = None
        self.uncontrolled_rx_drop_packets_delta_max = None
        self.uncontrolled_rx_drop_packets_delta_min = None
        self.uncontrolled_rx_error_packets = None
        self.uncontrolled_rx_error_packets_delta = None
        self.uncontrolled_rx_error_packets_delta_avg = None
        self.uncontrolled_rx_error_packets_delta_max = None
        self.uncontrolled_rx_error_packets_delta_min = None
        self.unicast_controlled_packets = None
        self.unicast_controlled_packets_delta = None
        self.unicast_controlled_packets_delta_avg = None
        self.unicast_controlled_packets_delta_max = None
        self.unicast_controlled_packets_delta_min = None
        self.unicast_uncontrolled_packets = None
        self.unicast_uncontrolled_packets_delta = None
        self.unicast_uncontrolled_packets_delta_avg = None
        self.unicast_uncontrolled_packets_delta_max = None
        self.unicast_uncontrolled_packets_delta_min = None
        self.update = None

        ManagedObject.__init__(self, "EtherMacSecRxStats", parent_mo_or_dn, **kwargs)
