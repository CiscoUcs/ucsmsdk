"""This module contains the general information for FabricMulticastPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricMulticastPolicyConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    QUERIER_STATE_DISABLED = "disabled"
    QUERIER_STATE_ENABLED = "enabled"
    SNOOPING_STATE_DISABLED = "disabled"
    SNOOPING_STATE_ENABLED = "enabled"
    SOURCE_IP_PROXY_STATE_DISABLED = "disabled"
    SOURCE_IP_PROXY_STATE_ENABLED = "enabled"


class FabricMulticastPolicy(ManagedObject):
    """This is FabricMulticastPolicy class."""

    consts = FabricMulticastPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricMulticastPolicy", "fabricMulticastPolicy", "mc-policy-[name]", VersionMeta.Version211a, "InputOutput", 0x1fff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['orgOrg'], ['faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|conflicting-or-empty-querier-ip),){0,2}(defaultValue|not-applicable|conflicting-or-empty-querier-ip){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "querier_ip_addr": MoPropertyMeta("querier_ip_addr", "querierIpAddr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "querier_ip_addr_peer": MoPropertyMeta("querier_ip_addr_peer", "querierIpAddrPeer", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x80, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "querier_state": MoPropertyMeta("querier_state", "querierState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["disabled", "enabled"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "snooping_state": MoPropertyMeta("snooping_state", "snoopingState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["disabled", "enabled"], []),
        "source_ip_proxy_state": MoPropertyMeta("source_ip_proxy_state", "sourceIpProxyState", "string", VersionMeta.Version422d, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["disabled", "enabled"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "querierIpAddr": "querier_ip_addr", 
        "querierIpAddrPeer": "querier_ip_addr_peer", 
        "querierState": "querier_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "snoopingState": "snooping_state", 
        "sourceIpProxyState": "source_ip_proxy_state", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.config_qualifier = None
        self.descr = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.querier_ip_addr = None
        self.querier_ip_addr_peer = None
        self.querier_state = None
        self.sacl = None
        self.snooping_state = None
        self.source_ip_proxy_state = None
        self.status = None

        ManagedObject.__init__(self, "FabricMulticastPolicy", parent_mo_or_dn, **kwargs)
