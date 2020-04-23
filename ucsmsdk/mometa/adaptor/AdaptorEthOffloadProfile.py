"""This module contains the general information for AdaptorEthOffloadProfile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorEthOffloadProfileConsts:
    LARGE_RECEIVE_DISABLED = "disabled"
    LARGE_RECEIVE_ENABLED = "enabled"
    TCP_RX_CHECKSUM_DISABLED = "disabled"
    TCP_RX_CHECKSUM_ENABLED = "enabled"
    TCP_SEGMENT_DISABLED = "disabled"
    TCP_SEGMENT_ENABLED = "enabled"
    TCP_TX_CHECKSUM_DISABLED = "disabled"
    TCP_TX_CHECKSUM_ENABLED = "enabled"


class AdaptorEthOffloadProfile(ManagedObject):
    """This is AdaptorEthOffloadProfile class."""

    consts = AdaptorEthOffloadProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorEthOffloadProfile", "adaptorEthOffloadProfile", "eth-offload", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"], ['adaptorHostEthIf', 'adaptorHostEthIfProfile', 'adaptorUsnicConnDef'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "large_receive": MoPropertyMeta("large_receive", "largeReceive", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["disabled", "enabled"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "tcp_rx_checksum": MoPropertyMeta("tcp_rx_checksum", "tcpRxChecksum", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["disabled", "enabled"], []),
        "tcp_segment": MoPropertyMeta("tcp_segment", "tcpSegment", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["disabled", "enabled"], []),
        "tcp_tx_checksum": MoPropertyMeta("tcp_tx_checksum", "tcpTxChecksum", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["disabled", "enabled"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "largeReceive": "large_receive", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "tcpRxChecksum": "tcp_rx_checksum", 
        "tcpSegment": "tcp_segment", 
        "tcpTxChecksum": "tcp_tx_checksum", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.large_receive = None
        self.sacl = None
        self.status = None
        self.tcp_rx_checksum = None
        self.tcp_segment = None
        self.tcp_tx_checksum = None

        ManagedObject.__init__(self, "AdaptorEthOffloadProfile", parent_mo_or_dn, **kwargs)
