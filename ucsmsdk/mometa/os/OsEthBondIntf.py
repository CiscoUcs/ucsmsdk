"""This module contains the general information for OsEthBondIntf ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class OsEthBondIntfConsts:
    OPER_STATE_DOWN = "down"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_INDETERMINATE = "indeterminate"
    OPER_STATE_UP = "up"


class OsEthBondIntf(ManagedObject):
    """This is OsEthBondIntf class."""

    consts = OsEthBondIntfConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("OsEthBondIntf", "osEthBondIntf", "bond-intf-[name]", VersionMeta.Version302c, "InputOutput", 0x3f, [], ["read-only"], ['osInstance'], ['osARPLinkMonitoringPolicy', 'osEthBondModeActiveBackup', 'osEthBondModeBalancedALB', 'osEthBondModeBalancedRR', 'osEthBondModeBalancedTLB', 'osEthBondModeBalancedXOR', 'osEthBondModeBroadcast', 'osEthIntf', 'osMiiLinkMonitoringPolicy'], [None])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "max_bonds": MoPropertyMeta("max_bonds", "maxBonds", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "mtu": MoPropertyMeta("mtu", "mtu", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1500-9000"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["down", "failed", "indeterminate", "up"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "dn": "dn", 
        "maxBonds": "max_bonds", 
        "mtu": "mtu", 
        "name": "name", 
        "operState": "oper_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.addr = None
        self.child_action = None
        self.max_bonds = None
        self.mtu = None
        self.oper_state = None
        self.sacl = None
        self.status = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "OsEthBondIntf", parent_mo_or_dn, **kwargs)
