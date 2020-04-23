"""This module contains the general information for OsEthBondModeBalancedRR ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class OsEthBondModeBalancedRRConsts:
    TYPE_ACTIVE_ACTIVE = "active-active"
    TYPE_ACTIVE_PASSIVE = "active-passive"


class OsEthBondModeBalancedRR(ManagedObject):
    """This is OsEthBondModeBalancedRR class."""

    consts = OsEthBondModeBalancedRRConsts()
    naming_props = set([])

    mo_meta = MoMeta("OsEthBondModeBalancedRR", "osEthBondModeBalancedRR", "eth-bond-mode", VersionMeta.Version302c, "InputOutput", 0x3f, [], ["read-only"], ['osEthBondIntf'], ['osPrimarySlave'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "igmp_resend_count": MoPropertyMeta("igmp_resend_count", "igmpResendCount", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-255"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "pkts_per_slave": MoPropertyMeta("pkts_per_slave", "pktsPerSlave", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active-active", "active-passive"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "igmpResendCount": "igmp_resend_count", 
        "name": "name", 
        "pktsPerSlave": "pkts_per_slave", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.igmp_resend_count = None
        self.name = None
        self.pkts_per_slave = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "OsEthBondModeBalancedRR", parent_mo_or_dn, **kwargs)
