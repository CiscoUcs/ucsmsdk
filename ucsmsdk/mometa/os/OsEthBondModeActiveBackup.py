"""This module contains the general information for OsEthBondModeActiveBackup ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class OsEthBondModeActiveBackupConsts:
    MAC_ADDRESS_POLICY_ACTIVE = "active"
    MAC_ADDRESS_POLICY_FOLLOW = "follow"
    MAC_ADDRESS_POLICY_NONE = "none"
    TYPE_ACTIVE_ACTIVE = "active-active"
    TYPE_ACTIVE_PASSIVE = "active-passive"


class OsEthBondModeActiveBackup(ManagedObject):
    """This is OsEthBondModeActiveBackup class."""

    consts = OsEthBondModeActiveBackupConsts()
    naming_props = set([])

    mo_meta = MoMeta("OsEthBondModeActiveBackup", "osEthBondModeActiveBackup", "eth-bond-mode", VersionMeta.Version302c, "InputOutput", 0x3f, [], ["read-only"], ['osEthBondIntf'], ['osPrimarySlave'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "mac_address_policy": MoPropertyMeta("mac_address_policy", "macAddressPolicy", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "follow", "none"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "num_peer_notifications": MoPropertyMeta("num_peer_notifications", "numPeerNotifications", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-255"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active-active", "active-passive"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "macAddressPolicy": "mac_address_policy", 
        "name": "name", 
        "numPeerNotifications": "num_peer_notifications", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.mac_address_policy = None
        self.name = None
        self.num_peer_notifications = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "OsEthBondModeActiveBackup", parent_mo_or_dn, **kwargs)
