"""This module contains the general information for DcxVc ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class DcxVcConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    CDP_DISABLED = "disabled"
    CDP_ENABLED = "enabled"
    COS_ANY = "any"
    ENCAP_CONSOLIDATED = "consolidated"
    ENCAP_VIRTUAL = "virtual"
    ENCAP_VIRTUAL_CE = "virtual-ce"
    FORGE_MAC_ALLOW = "allow"
    FORGE_MAC_DENY = "deny"
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
    MAC_REGISTER_MODE_ALL_HOST_VLANS = "all-host-vlans"
    MAC_REGISTER_MODE_ONLY_NATIVE_VLAN = "only-native-vlan"
    MON_TRAF_DIR_BOTH = "both"
    MON_TRAF_DIR_RX = "rx"
    MON_TRAF_DIR_TX = "tx"
    OPER_STATE_ACTIVE = "active"
    OPER_STATE_ADMIN_DOWN = "admin-down"
    OPER_STATE_ERROR = "error"
    OPER_STATE_LINK_DOWN = "link-down"
    OPER_STATE_PASSIVE = "passive"
    OPER_STATE_UNKNOWN = "unknown"
    PROT_STATE_ACTIVE = "active"
    PROT_STATE_NO_PROTECTION = "no-protection"
    PROT_STATE_PASSIVE = "passive"
    QOS_POLICY_ID_NONE = "none"
    ROLE_DIAG = "diag"
    ROLE_FCOE_NAS_STORAGE = "fcoe-nas-storage"
    ROLE_FCOE_STORAGE = "fcoe-storage"
    ROLE_FCOE_UPLINK = "fcoe-uplink"
    ROLE_MGMT = "mgmt"
    ROLE_MONITOR = "monitor"
    ROLE_NAS_STORAGE = "nas-storage"
    ROLE_NETWORK = "network"
    ROLE_NETWORK_FCOE_UPLINK = "network-fcoe-uplink"
    ROLE_SERVER = "server"
    ROLE_SERVICE = "service"
    ROLE_STORAGE = "storage"
    ROLE_UNKNOWN = "unknown"
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
    UPLINK_FAIL_ACTION_LINK_DOWN = "link-down"
    UPLINK_FAIL_ACTION_WARNING = "warning"


class DcxVc(ManagedObject):
    """This is DcxVc class."""

    consts = DcxVcConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("DcxVc", "dcxVc", "vc-[id]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["read-only"], ['fabricLocale', 'fabricPath', 'swEthLanFlowMon', 'swEthMon', 'swFcMon'], ['fabricNetGroupRef', 'fabricSanGroupRef', 'faultInst', 'swCmclan', 'swNetflowMonitorRef', 'swUlan', 'swVlan', 'swVsan'], ["Get"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
        "border_aggr_port_id": MoPropertyMeta("border_aggr_port_id", "borderAggrPortId", "uint", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "border_port_id": MoPropertyMeta("border_port_id", "borderPortId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "border_slot_id": MoPropertyMeta("border_slot_id", "borderSlotId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "border_vfc_id": MoPropertyMeta("border_vfc_id", "borderVfcId", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "cdp": MoPropertyMeta("cdp", "cdp", "string", VersionMeta.Version102d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cookie": MoPropertyMeta("cookie", "cookie", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "cos": MoPropertyMeta("cos", "cos", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["any"], ["0-6", "255-255"]),
        "derived_from_id": MoPropertyMeta("derived_from_id", "derivedFromId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "encap": MoPropertyMeta("encap", "encap", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["consolidated", "virtual", "virtual-ce"], ["0-255"]),
        "fcoe_id": MoPropertyMeta("fcoe_id", "fcoeId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "forge_mac": MoPropertyMeta("forge_mac", "forgeMac", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allow", "deny"], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "inst_type": MoPropertyMeta("inst_type", "instType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["default", "dynamic", "dynamic-vf", "manual"], []),
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []),
        "link_state": MoPropertyMeta("link_state", "linkState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["admin-down", "down", "error", "offline", "unallocated", "unavailable", "unknown", "up"], []),
        "lldp": MoPropertyMeta("lldp", "lldp", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|transmit|receive|all),){0,4}(defaultValue|none|transmit|receive|all){0,1}""", [], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "mac_register_mode": MoPropertyMeta("mac_register_mode", "macRegisterMode", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all-host-vlans", "only-native-vlan"], []),
        "mon_traf_dir": MoPropertyMeta("mon_traf_dir", "monTrafDir", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["both", "rx", "tx"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_border_aggr_port_id": MoPropertyMeta("oper_border_aggr_port_id", "operBorderAggrPortId", "uint", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oper_border_port_id": MoPropertyMeta("oper_border_port_id", "operBorderPortId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oper_border_slot_id": MoPropertyMeta("oper_border_slot_id", "operBorderSlotId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "admin-down", "error", "link-down", "passive", "unknown"], []),
        "peer_id": MoPropertyMeta("peer_id", "peerId", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "prot_state": MoPropertyMeta("prot_state", "protState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "no-protection", "passive"], []),
        "qos_policy_dn": MoPropertyMeta("qos_policy_dn", "qosPolicyDn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "qos_policy_id": MoPropertyMeta("qos_policy_id", "qosPolicyId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none"], ["0-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "role": MoPropertyMeta("role", "role", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["CreatePend", "Creating", "DestroyPend", "Destroying", "ModifyPend", "Modifying", "Present", "Unknown"], []),
        "state_qual": MoPropertyMeta("state_qual", "stateQual", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "tag": MoPropertyMeta("tag", "tag", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
        "uplink_fail_action": MoPropertyMeta("uplink_fail_action", "uplinkFailAction", "string", VersionMeta.Version102d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["link-down", "warning"], []),
        "vnic": MoPropertyMeta("vnic", "vnic", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "borderAggrPortId": "border_aggr_port_id", 
        "borderPortId": "border_port_id", 
        "borderSlotId": "border_slot_id", 
        "borderVfcId": "border_vfc_id", 
        "cdp": "cdp", 
        "childAction": "child_action", 
        "cookie": "cookie", 
        "cos": "cos", 
        "derivedFromId": "derived_from_id", 
        "dn": "dn", 
        "encap": "encap", 
        "fcoeId": "fcoe_id", 
        "fltAggr": "flt_aggr", 
        "forgeMac": "forge_mac", 
        "id": "id", 
        "instType": "inst_type", 
        "lc": "lc", 
        "linkState": "link_state", 
        "lldp": "lldp", 
        "locale": "locale", 
        "macRegisterMode": "mac_register_mode", 
        "monTrafDir": "mon_traf_dir", 
        "name": "name", 
        "operBorderAggrPortId": "oper_border_aggr_port_id", 
        "operBorderPortId": "oper_border_port_id", 
        "operBorderSlotId": "oper_border_slot_id", 
        "operState": "oper_state", 
        "peerId": "peer_id", 
        "protState": "prot_state", 
        "qosPolicyDn": "qos_policy_dn", 
        "qosPolicyId": "qos_policy_id", 
        "rn": "rn", 
        "role": "role", 
        "sacl": "sacl", 
        "state": "state", 
        "stateQual": "state_qual", 
        "status": "status", 
        "switchId": "switch_id", 
        "tag": "tag", 
        "transport": "transport", 
        "type": "type", 
        "uplinkFailAction": "uplink_fail_action", 
        "vnic": "vnic", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_state = None
        self.border_aggr_port_id = None
        self.border_port_id = None
        self.border_slot_id = None
        self.border_vfc_id = None
        self.cdp = None
        self.child_action = None
        self.cookie = None
        self.cos = None
        self.derived_from_id = None
        self.encap = None
        self.fcoe_id = None
        self.flt_aggr = None
        self.forge_mac = None
        self.inst_type = None
        self.lc = None
        self.link_state = None
        self.lldp = None
        self.locale = None
        self.mac_register_mode = None
        self.mon_traf_dir = None
        self.name = None
        self.oper_border_aggr_port_id = None
        self.oper_border_port_id = None
        self.oper_border_slot_id = None
        self.oper_state = None
        self.peer_id = None
        self.prot_state = None
        self.qos_policy_dn = None
        self.qos_policy_id = None
        self.role = None
        self.sacl = None
        self.state = None
        self.state_qual = None
        self.status = None
        self.switch_id = None
        self.tag = None
        self.transport = None
        self.type = None
        self.uplink_fail_action = None
        self.vnic = None

        ManagedObject.__init__(self, "DcxVc", parent_mo_or_dn, **kwargs)
