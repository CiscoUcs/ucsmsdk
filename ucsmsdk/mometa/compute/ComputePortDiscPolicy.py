"""This module contains the general information for ComputePortDiscPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePortDiscPolicyConsts:
    ETH_BREAKOUT_AUTO_DISCOVERY_DISABLED = "disabled"
    ETH_BREAKOUT_AUTO_DISCOVERY_ENABLED = "enabled"
    ETH_SVR_AUTO_DISCOVERY_DISABLED = "disabled"
    ETH_SVR_AUTO_DISCOVERY_ENABLED = "enabled"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class ComputePortDiscPolicy(ManagedObject):
    """This is ComputePortDiscPolicy class."""

    consts = ComputePortDiscPolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputePortDiscPolicy", "computePortDiscPolicy", "port-discovery", VersionMeta.Version321d, "InputOutput", 0x7ff, [], ["admin", "pn-policy"], ['orgOrg'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "eth_breakout_auto_discovery": MoPropertyMeta("eth_breakout_auto_discovery", "ethBreakoutAutoDiscovery", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled"], []),
        "eth_svr_auto_discovery": MoPropertyMeta("eth_svr_auto_discovery", "ethSvrAutoDiscovery", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["disabled", "enabled"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "qualifier": MoPropertyMeta("qualifier", "qualifier", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "ethBreakoutAutoDiscovery": "eth_breakout_auto_discovery", 
        "ethSvrAutoDiscovery": "eth_svr_auto_discovery", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "qualifier": "qualifier", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.eth_breakout_auto_discovery = None
        self.eth_svr_auto_discovery = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.qualifier = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputePortDiscPolicy", parent_mo_or_dn, **kwargs)
