"""This module contains the general information for SwVsan ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwVsanConsts:
    DEFAULT_ZONING_DISABLED = "disabled"
    DEFAULT_ZONING_ENABLED = "enabled"
    FC_ZONE_SHARING_MODE_CLEAR_UNMANAGED_ZONE_ALL = "clear-unmanaged-zone-all"
    FC_ZONE_SHARING_MODE_COALESCE = "coalesce"
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
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    MON_TRAF_DIR_BOTH = "both"
    MON_TRAF_DIR_RX = "rx"
    MON_TRAF_DIR_TX = "tx"
    OPER_STATE_ERROR_MISCONFIGURED = "error-misconfigured"
    OPER_STATE_ERROR_RESERVED = "error-reserved"
    OPER_STATE_OK = "ok"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    ZONING_STATE_DISABLED = "disabled"
    ZONING_STATE_ENABLED = "enabled"


class SwVsan(ManagedObject):
    """This is SwVsan class."""

    consts = SwVsanConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("SwVsan", "swVsan", "vsan-[id]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["read-only"], ['dcxFcoeVifEp', 'dcxVc', 'dcxVifEp', 'swFcMon', 'swFcSanBorder'], ['swFcZoneSet'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "default_zoning": MoPropertyMeta("default_zoning", "defaultZoning", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["disabled", "enabled"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "fc_zone_sharing_mode": MoPropertyMeta("fc_zone_sharing_mode", "fcZoneSharingMode", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["clear-unmanaged-zone-all", "coalesce"], []),
        "fcoe_vlan": MoPropertyMeta("fcoe_vlan", "fcoeVlan", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4042", "4048-4093"]),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-4093"]),
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "mon_traf_dir": MoPropertyMeta("mon_traf_dir", "monTrafDir", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["both", "rx", "tx"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,32}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["error-misconfigured", "error-reserved", "ok"], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
        "zoning_state": MoPropertyMeta("zoning_state", "zoningState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["disabled", "enabled"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "defaultZoning": "default_zoning", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "fcZoneSharingMode": "fc_zone_sharing_mode", 
        "fcoeVlan": "fcoe_vlan", 
        "fltAggr": "flt_aggr", 
        "id": "id", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "lc": "lc", 
        "locale": "locale", 
        "monTrafDir": "mon_traf_dir", 
        "name": "name", 
        "operState": "oper_state", 
        "peerDn": "peer_dn", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
        "zoningState": "zoning_state", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.default_zoning = None
        self.ep_dn = None
        self.fc_zone_sharing_mode = None
        self.fcoe_vlan = None
        self.flt_aggr = None
        self.if_role = None
        self.if_type = None
        self.lc = None
        self.locale = None
        self.mon_traf_dir = None
        self.name = None
        self.oper_state = None
        self.peer_dn = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None
        self.zoning_state = None

        ManagedObject.__init__(self, "SwVsan", parent_mo_or_dn, **kwargs)
