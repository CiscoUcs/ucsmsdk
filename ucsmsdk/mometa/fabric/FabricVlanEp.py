"""This module contains the general information for FabricVlanEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricVlanEpConsts:
    ASSOC_PRIMARY_VLAN_STATE_DOES_NOT_EXISTS = "does-not-exists"
    ASSOC_PRIMARY_VLAN_STATE_IS_EMPTY = "is-empty"
    ASSOC_PRIMARY_VLAN_STATE_IS_IN_ERROR_STATE = "is-in-error-state"
    ASSOC_PRIMARY_VLAN_STATE_IS_NOT_PRIMARY_TYPE = "is-not-primary-type"
    ASSOC_PRIMARY_VLAN_STATE_OK = "ok"
    ASSOC_PRIMARY_VLAN_SWITCH_ID_A = "A"
    ASSOC_PRIMARY_VLAN_SWITCH_ID_B = "B"
    ASSOC_PRIMARY_VLAN_SWITCH_ID_NONE = "NONE"
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
    IS_NATIVE_FALSE = "false"
    IS_NATIVE_NO = "no"
    IS_NATIVE_TRUE = "true"
    IS_NATIVE_YES = "yes"
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


class FabricVlanEp(ManagedObject):
    """This is FabricVlanEp class."""

    consts = FabricVlanEpConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("FabricVlanEp", "fabricVlanEp", "vlan-[id]", VersionMeta.Version141i, "InputOutput", 0x3ff, [], ["read-only"], ['fabricEthEstcEp', 'fabricEthEstcPc', 'fabricEthLanEp'], [], ["Get"])

    prop_meta = {
        "assoc_primary_vlan_state": MoPropertyMeta("assoc_primary_vlan_state", "assocPrimaryVlanState", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["does-not-exists", "is-empty", "is-in-error-state", "is-not-primary-type", "ok"], []),
        "assoc_primary_vlan_switch_id": MoPropertyMeta("assoc_primary_vlan_switch_id", "assocPrimaryVlanSwitchId", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-4093"]),
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
        "is_native": MoPropertyMeta("is_native", "isNative", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.CREATE_ONLY, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,32}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["error-misconfigured", "ok"], []),
        "overlap_state_for_a": MoPropertyMeta("overlap_state_for_a", "overlapStateForA", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "not-active", "ok", "primary-id-mismatch", "sharing-type-mismatch"], []),
        "overlap_state_for_b": MoPropertyMeta("overlap_state_for_b", "overlapStateForB", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "not-active", "ok", "primary-id-mismatch", "sharing-type-mismatch"], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "pub_nw_dn": MoPropertyMeta("pub_nw_dn", "pubNwDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "pub_nw_id": MoPropertyMeta("pub_nw_id", "pubNwId", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pub_nw_name": MoPropertyMeta("pub_nw_name", "pubNwName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sharing": MoPropertyMeta("sharing", "sharing", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["community", "isolated", "none", "primary"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "assocPrimaryVlanState": "assoc_primary_vlan_state", 
        "assocPrimaryVlanSwitchId": "assoc_primary_vlan_switch_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "id": "id", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "isNative": "is_native", 
        "locale": "locale", 
        "name": "name", 
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

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.assoc_primary_vlan_state = None
        self.assoc_primary_vlan_switch_id = None
        self.child_action = None
        self.ep_dn = None
        self.if_role = None
        self.if_type = None
        self.is_native = None
        self.locale = None
        self.name = None
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

        ManagedObject.__init__(self, "FabricVlanEp", parent_mo_or_dn, **kwargs)
