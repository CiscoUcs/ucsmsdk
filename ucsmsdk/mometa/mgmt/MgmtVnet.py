"""This module contains the general information for MgmtVnet ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtVnetConsts:
    CONFIG_STATE_INCOMPLETE = "incomplete"
    CONFIG_STATE_INVALID_PINNING = "invalidPinning"
    CONFIG_STATE_UNRESOLVED_VLAN = "unresolvedVlan"
    CONFIG_STATE_UNSUPPORTED_FIRMWARE = "unsupportedFirmware"
    CONFIG_STATE_UNSUPPORTED_SERVER = "unsupportedServer"
    CONFIG_STATE_UNSUPPORTED_VLAN = "unsupportedVlan"
    CONFIG_STATE_VALID = "valid"


class MgmtVnet(ManagedObject):
    """This is MgmtVnet class."""

    consts = MgmtVnetConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtVnet", "mgmtVnet", "network", VersionMeta.Version221b, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server"], ['mgmtInterface', 'mgmtProfDerivedInterface'], ['vnicIpV4MgmtPooledAddr', 'vnicIpV4PooledAddr', 'vnicIpV4StaticAddr', 'vnicIpV6MgmtPooledAddr', 'vnicIpV6StaticAddr'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["incomplete", "invalidPinning", "unresolvedVlan", "unsupportedFirmware", "unsupportedServer", "unsupportedVlan", "valid"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-4093"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configState": "config_state", 
        "dn": "dn", 
        "id": "id", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.config_state = None
        self.id = None
        self.name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtVnet", parent_mo_or_dn, **kwargs)
