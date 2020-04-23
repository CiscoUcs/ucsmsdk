"""This module contains the general information for MgmtInbandProfile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtInbandProfileConsts:
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class MgmtInbandProfile(ManagedObject):
    """This is MgmtInbandProfile class."""

    consts = MgmtInbandProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtInbandProfile", "mgmtInbandProfile", "ib-profile", VersionMeta.Version221b, "InputOutput", 0x3ff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricLanCloud'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "default_vlan_name": MoPropertyMeta("default_vlan_name", "defaultVlanName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,32}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "monitor_interval": MoPropertyMeta("monitor_interval", "monitorInterval", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-5"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,32}""", [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "pool_name": MoPropertyMeta("pool_name", "poolName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "defaultVlanName": "default_vlan_name", 
        "dn": "dn", 
        "monitorInterval": "monitor_interval", 
        "name": "name", 
        "policyOwner": "policy_owner", 
        "poolName": "pool_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.default_vlan_name = None
        self.monitor_interval = None
        self.name = None
        self.policy_owner = None
        self.pool_name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtInbandProfile", parent_mo_or_dn, **kwargs)
