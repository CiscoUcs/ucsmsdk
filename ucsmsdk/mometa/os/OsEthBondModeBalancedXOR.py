"""This module contains the general information for OsEthBondModeBalancedXOR ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class OsEthBondModeBalancedXORConsts:
    LB_TYPE_RECEIVE_XMIT = "receive-xmit"
    LB_TYPE_XMIT_ONLY = "xmit-only"
    TYPE_ACTIVE_ACTIVE = "active-active"
    TYPE_ACTIVE_PASSIVE = "active-passive"
    XMIT_HASH_TYPE_ENCAP2_3 = "encap2+3"
    XMIT_HASH_TYPE_ENCAP3_4 = "encap3+4"
    XMIT_HASH_TYPE_LAYER2 = "layer2"
    XMIT_HASH_TYPE_LAYER2_3 = "layer2+3"
    XMIT_HASH_TYPE_LAYER3_4 = "layer3+4"


class OsEthBondModeBalancedXOR(ManagedObject):
    """This is OsEthBondModeBalancedXOR class."""

    consts = OsEthBondModeBalancedXORConsts()
    naming_props = set([])

    mo_meta = MoMeta("OsEthBondModeBalancedXOR", "osEthBondModeBalancedXOR", "eth-bond-mode", VersionMeta.Version302c, "InputOutput", 0x3f, [], ["read-only"], ['osEthBondIntf'], ['osPrimarySlave'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "lb_type": MoPropertyMeta("lb_type", "lbType", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["receive-xmit", "xmit-only"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active-active", "active-passive"], []),
        "xmit_hash_type": MoPropertyMeta("xmit_hash_type", "xmitHashType", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["encap2+3", "encap3+4", "layer2", "layer2+3", "layer3+4"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "lbType": "lb_type", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
        "xmitHashType": "xmit_hash_type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.lb_type = None
        self.name = None
        self.sacl = None
        self.status = None
        self.type = None
        self.xmit_hash_type = None

        ManagedObject.__init__(self, "OsEthBondModeBalancedXOR", parent_mo_or_dn, **kwargs)
