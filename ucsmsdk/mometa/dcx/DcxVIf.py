"""This module contains the general information for DcxVIf ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class DcxVIfConsts:
    STATIC_MAC_LIMIT_STATUS_AVAILABLE = "available"
    STATIC_MAC_LIMIT_STATUS_REACHED = "reached"
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
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
    INST_TYPE_DEFAULT = "default"
    INST_TYPE_DYNAMIC = "dynamic"
    INST_TYPE_DYNAMIC_VF = "dynamic-vf"
    INST_TYPE_MANUAL = "manual"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    LINK_STATE_ADMIN_DOWN = "admin-down"
    LINK_STATE_DOWN = "down"
    LINK_STATE_ERROR = "error"
    LINK_STATE_OFFLINE = "offline"
    LINK_STATE_UNALLOCATED = "unallocated"
    LINK_STATE_UNAVAILABLE = "unavailable"
    LINK_STATE_UNKNOWN = "unknown"
    LINK_STATE_UP = "up"
    OPER_STATE_ACTIVE = "active"
    OPER_STATE_ADMIN_DOWN = "admin-down"
    OPER_STATE_ERROR = "error"
    OPER_STATE_LINK_DOWN = "link-down"
    OPER_STATE_PASSIVE = "passive"
    OPER_STATE_UNKNOWN = "unknown"
    PROT_ROLE_BACKUP = "backup"
    PROT_ROLE_PRIMARY = "primary"
    PROT_ROLE_UNPROTECTED = "unprotected"
    PROT_STATE_ACTIVE = "active"
    PROT_STATE_NO_PROTECTION = "no-protection"
    PROT_STATE_PASSIVE = "passive"
    QOS_CONTROL_FULL = "full"
    QOS_CONTROL_FULL_WITH_EXCEPTION = "full-with-exception"
    QOS_CONTROL_NONE = "none"
    STATE_CREATE_PEND = "CreatePend"
    STATE_CREATING = "Creating"
    STATE_DESTROY_PEND = "DestroyPend"
    STATE_DESTROYING = "Destroying"
    STATE_MODIFY_PEND = "ModifyPend"
    STATE_MODIFYING = "Modifying"
    STATE_PRESENT = "Present"
    STATE_UNKNOWN = "Unknown"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class DcxVIf(ManagedObject):
    """This is DcxVIf class."""

    consts = DcxVIfConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("DcxVIf", "dcxVIf", "vif-[id]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["read-only"], ['adaptorExtEthIf', 'adaptorExtEthIfPc', 'adaptorFcOEIf', 'adaptorHostEthIf', 'adaptorHostFcIf', 'adaptorHostServiceEthIf'], ['faultInst'], ["Get"])

    prop_meta = {
        "static_mac_limit_status": MoPropertyMeta("static_mac_limit_status", "StaticMacLimitStatus", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["available", "reached"], []),
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cookie": MoPropertyMeta("cookie", "cookie", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
        "inst_type": MoPropertyMeta("inst_type", "instType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["default", "dynamic", "dynamic-vf", "manual"], []),
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []),
        "link_state": MoPropertyMeta("link_state", "linkState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["admin-down", "down", "error", "offline", "unallocated", "unavailable", "unknown", "up"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "admin-down", "error", "link-down", "passive", "unknown"], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "prot_peer_id": MoPropertyMeta("prot_peer_id", "protPeerId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "prot_role": MoPropertyMeta("prot_role", "protRole", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["backup", "primary", "unprotected"], []),
        "prot_state": MoPropertyMeta("prot_state", "protState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "no-protection", "passive"], []),
        "qos_control": MoPropertyMeta("qos_control", "qosControl", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["full", "full-with-exception", "none"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["CreatePend", "Creating", "DestroyPend", "Destroying", "ModifyPend", "Modifying", "Present", "Unknown"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "tag": MoPropertyMeta("tag", "tag", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "StaticMacLimitStatus": "static_mac_limit_status", 
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "cookie": "cookie", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "id": "id", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "instType": "inst_type", 
        "lc": "lc", 
        "linkState": "link_state", 
        "locale": "locale", 
        "name": "name", 
        "operState": "oper_state", 
        "peerDn": "peer_dn", 
        "protPeerId": "prot_peer_id", 
        "protRole": "prot_role", 
        "protState": "prot_state", 
        "qosControl": "qos_control", 
        "rn": "rn", 
        "sacl": "sacl", 
        "state": "state", 
        "status": "status", 
        "switchId": "switch_id", 
        "tag": "tag", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.static_mac_limit_status = None
        self.admin_state = None
        self.child_action = None
        self.cookie = None
        self.ep_dn = None
        self.if_role = None
        self.if_type = None
        self.inst_type = None
        self.lc = None
        self.link_state = None
        self.locale = None
        self.name = None
        self.oper_state = None
        self.peer_dn = None
        self.prot_peer_id = None
        self.prot_role = None
        self.prot_state = None
        self.qos_control = None
        self.sacl = None
        self.state = None
        self.status = None
        self.switch_id = None
        self.tag = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "DcxVIf", parent_mo_or_dn, **kwargs)
