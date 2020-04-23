"""This module contains the general information for FabricVlan ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricVlanConsts:
    ASSOC_PRIMARY_VLAN_STATE_DOES_NOT_EXISTS = "does-not-exists"
    ASSOC_PRIMARY_VLAN_STATE_IS_EMPTY = "is-empty"
    ASSOC_PRIMARY_VLAN_STATE_IS_IN_ERROR_STATE = "is-in-error-state"
    ASSOC_PRIMARY_VLAN_STATE_IS_NOT_PRIMARY_TYPE = "is-not-primary-type"
    ASSOC_PRIMARY_VLAN_STATE_OK = "ok"
    ASSOC_PRIMARY_VLAN_SWITCH_ID_A = "A"
    ASSOC_PRIMARY_VLAN_SWITCH_ID_B = "B"
    ASSOC_PRIMARY_VLAN_SWITCH_ID_NONE = "NONE"
    COMPRESSION_TYPE_EXCLUDED = "excluded"
    COMPRESSION_TYPE_INCLUDED = "included"
    CONFIG_OVERLAP_ERROR_RESERVED_CONFLICT = "error-reserved-conflict"
    CONFIG_OVERLAP_OK = "ok"
    DEFAULT_NET_FALSE = "false"
    DEFAULT_NET_NO = "no"
    DEFAULT_NET_TRUE = "true"
    DEFAULT_NET_YES = "yes"
    IF_ROLE_DIAG = "diag"
    IF_ROLE_FCOE_NAS_STORAGE = "fcoe-nas-storage"
    IF_ROLE_FCOE_STORAGE = "fcoe-storage"
    IF_ROLE_FCOE_UPLINK = "fcoe-uplink"
    IF_ROLE_MGMT = "mgmt"
    IF_ROLE_MONITOR = "monitor"
    IF_ROLE_NAS_STORAGE = "nas-storage"
    IF_ROLE_NETWORK = "network"
    IF_ROLE_NETWORK_FCOE_UPLINK = "network-fcoe-uplink"
    IF_ROLE_SERVER = "server"
    IF_ROLE_SERVICE = "service"
    IF_ROLE_STORAGE = "storage"
    IF_ROLE_UNKNOWN = "unknown"
    IF_TYPE_AGGREGATION = "aggregation"
    IF_TYPE_PHYSICAL = "physical"
    IF_TYPE_UNKNOWN = "unknown"
    IF_TYPE_VIRTUAL = "virtual"
    OPER_STATE_ERROR_MISCONFIGURED = "error-misconfigured"
    OPER_STATE_OK = "ok"
    OVERLAP_STATE_FOR_A_ACTIVE = "active"
    OVERLAP_STATE_FOR_A_NOT_ACTIVE = "not-active"
    OVERLAP_STATE_FOR_A_OK = "ok"
    OVERLAP_STATE_FOR_A_PRIMARY_ID_MISMATCH = "primary-id-mismatch"
    OVERLAP_STATE_FOR_A_SHARING_TYPE_MISMATCH = "sharing-type-mismatch"
    OVERLAP_STATE_FOR_B_ACTIVE = "active"
    OVERLAP_STATE_FOR_B_NOT_ACTIVE = "not-active"
    OVERLAP_STATE_FOR_B_OK = "ok"
    OVERLAP_STATE_FOR_B_PRIMARY_ID_MISMATCH = "primary-id-mismatch"
    OVERLAP_STATE_FOR_B_SHARING_TYPE_MISMATCH = "sharing-type-mismatch"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SHARING_COMMUNITY = "community"
    SHARING_ISOLATED = "isolated"
    SHARING_NONE = "none"
    SHARING_PRIMARY = "primary"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_DUAL = "dual"


class FabricVlan(ManagedObject):
    """This is FabricVlan class."""

    consts = FabricVlanConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricVlan", "fabricVlan", "net-[name]", VersionMeta.Version101e, "InputOutput", 0x1fff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricEthEstc', 'fabricEthEstcCloud', 'fabricEthLan', 'fabricLanCloud'], ['fabricEthMonFiltEp', 'fabricEthMonSrcEp', 'fabricEthVlanPc', 'fabricEthVlanPortEp', 'fabricPoolableVlan', 'fabricSwSubGroup', 'faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "assoc_primary_vlan_state": MoPropertyMeta("assoc_primary_vlan_state", "assocPrimaryVlanState", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["does-not-exists", "is-empty", "is-in-error-state", "is-not-primary-type", "ok"], []),
        "assoc_primary_vlan_switch_id": MoPropertyMeta("assoc_primary_vlan_switch_id", "assocPrimaryVlanSwitchId", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cloud": MoPropertyMeta("cloud", "cloud", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|fcsanmon|ethlan|ethestclan|fcestc|ethlanmon|fcsan),){0,7}(defaultValue|unknown|fcsanmon|ethlan|ethestclan|fcestc|ethlanmon|fcsan){0,1}""", [], []),
        "compression_type": MoPropertyMeta("compression_type", "compressionType", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["excluded", "included"], []),
        "config_issues": MoPropertyMeta("config_issues", "configIssues", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|conflicting-vlan-access|unsupported-multicast-policy),){0,3}(defaultValue|not-applicable|conflicting-vlan-access|unsupported-multicast-policy){0,1}""", [], []),
        "config_overlap": MoPropertyMeta("config_overlap", "configOverlap", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["error-reserved-conflict", "ok"], []),
        "default_net": MoPropertyMeta("default_net", "defaultNet", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["false", "no", "true", "yes"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "r_global": MoPropertyMeta("r_global", "global", "ulong", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-4042", "4048-4093"]),
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
        "local": MoPropertyMeta("local", "local", "ulong", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "mcast_policy_name": MoPropertyMeta("mcast_policy_name", "mcastPolicyName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []),
        "oper_mcast_policy_name": MoPropertyMeta("oper_mcast_policy_name", "operMcastPolicyName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["error-misconfigured", "ok"], []),
        "overlap_state_for_a": MoPropertyMeta("overlap_state_for_a", "overlapStateForA", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "not-active", "ok", "primary-id-mismatch", "sharing-type-mismatch"], []),
        "overlap_state_for_b": MoPropertyMeta("overlap_state_for_b", "overlapStateForB", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "not-active", "ok", "primary-id-mismatch", "sharing-type-mismatch"], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["local", "pending-policy", "policy"], []),
        "pub_nw_dn": MoPropertyMeta("pub_nw_dn", "pubNwDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "pub_nw_id": MoPropertyMeta("pub_nw_id", "pubNwId", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pub_nw_name": MoPropertyMeta("pub_nw_name", "pubNwName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x200, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sharing": MoPropertyMeta("sharing", "sharing", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["community", "isolated", "none", "primary"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "dual"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "assocPrimaryVlanState": "assoc_primary_vlan_state", 
        "assocPrimaryVlanSwitchId": "assoc_primary_vlan_switch_id", 
        "childAction": "child_action", 
        "cloud": "cloud", 
        "compressionType": "compression_type", 
        "configIssues": "config_issues", 
        "configOverlap": "config_overlap", 
        "defaultNet": "default_net", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "fltAggr": "flt_aggr", 
        "global": "r_global", 
        "id": "id", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "local": "local", 
        "locale": "locale", 
        "mcastPolicyName": "mcast_policy_name", 
        "name": "name", 
        "operMcastPolicyName": "oper_mcast_policy_name", 
        "operState": "oper_state", 
        "overlapStateForA": "overlap_state_for_a", 
        "overlapStateForB": "overlap_state_for_b", 
        "peerDn": "peer_dn", 
        "policyOwner": "policy_owner", 
        "pubNwDn": "pub_nw_dn", 
        "pubNwId": "pub_nw_id", 
        "pubNwName": "pub_nw_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sharing": "sharing", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.assoc_primary_vlan_state = None
        self.assoc_primary_vlan_switch_id = None
        self.child_action = None
        self.cloud = None
        self.compression_type = None
        self.config_issues = None
        self.config_overlap = None
        self.default_net = None
        self.ep_dn = None
        self.flt_aggr = None
        self.r_global = None
        self.id = None
        self.if_role = None
        self.if_type = None
        self.local = None
        self.locale = None
        self.mcast_policy_name = None
        self.oper_mcast_policy_name = None
        self.oper_state = None
        self.overlap_state_for_a = None
        self.overlap_state_for_b = None
        self.peer_dn = None
        self.policy_owner = None
        self.pub_nw_dn = None
        self.pub_nw_id = None
        self.pub_nw_name = None
        self.sacl = None
        self.sharing = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "FabricVlan", parent_mo_or_dn, **kwargs)
