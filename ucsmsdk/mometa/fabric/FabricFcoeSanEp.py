"""This module contains the general information for FabricFcoeSanEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricFcoeSanEpConsts:
    ADMIN_SPEED_100GBPS = "100gbps"
    ADMIN_SPEED_10GBPS = "10gbps"
    ADMIN_SPEED_1GBPS = "1gbps"
    ADMIN_SPEED_20GBPS = "20gbps"
    ADMIN_SPEED_25GBPS = "25gbps"
    ADMIN_SPEED_40GBPS = "40gbps"
    ADMIN_SPEED_AUTO = "auto"
    ADMIN_SPEED_INDETERMINATE = "indeterminate"
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    AUTO_NEGOTIATE_DISABLED = "disabled"
    AUTO_NEGOTIATE_ENABLED = "enabled"
    CHASSIS_ID_N_A = "N/A"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_INCONSISTENT = "inconsistent"
    FCOE_STATE_ADMIN_DOWN = "admin-down"
    FCOE_STATE_DOWN = "down"
    FCOE_STATE_ERROR_DISABLED = "error-disabled"
    FCOE_STATE_FAILED = "failed"
    FCOE_STATE_HARDWARE_FAILURE = "hardware-failure"
    FCOE_STATE_INDETERMINATE = "indeterminate"
    FCOE_STATE_LINK_DOWN = "link-down"
    FCOE_STATE_LINK_UP = "link-up"
    FCOE_STATE_NO_LICENSE = "no-license"
    FCOE_STATE_SFP_NOT_PRESENT = "sfp-not-present"
    FCOE_STATE_SOFTWARE_FAILURE = "software-failure"
    FCOE_STATE_UDLD_AGGR_DOWN = "udld-aggr-down"
    FCOE_STATE_UP = "up"
    FEC_AUTO = "auto"
    FEC_CL74 = "cl74"
    FEC_CL91 = "cl91"
    FEC_OFF = "off"
    FEC_RS_CONS16 = "rs-cons16"
    FEC_RS_IEEE = "rs-ieee"
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
    LIC_STATE_LICENSE_EXPIRED = "license-expired"
    LIC_STATE_LICENSE_GRACEPERIOD = "license-graceperiod"
    LIC_STATE_LICENSE_INSUFFICIENT = "license-insufficient"
    LIC_STATE_LICENSE_OK = "license-ok"
    LIC_STATE_NOT_APPLICABLE = "not-applicable"
    LIC_STATE_UNKNOWN = "unknown"
    OPER_STATE_DOWN = "down"
    OPER_STATE_ERROR_MISCONFIGURED = "error-misconfigured"
    OPER_STATE_ERROR_UNSUPPORTED_MINI_SERVER_PORT = "error-unsupported-mini-server-port"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_UNKNOWN = "unknown"
    OPER_STATE_UP = "up"
    PEER_CHASSIS_ID_N_A = "N/A"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    UDLD_OPER_STATE_ADMIN_DISABLED = "admin-disabled"
    UDLD_OPER_STATE_BIDIRECTIONAL = "bidirectional"
    UDLD_OPER_STATE_ECHO_EMPTY = "echo-empty"
    UDLD_OPER_STATE_MISMATCH = "mismatch"
    UDLD_OPER_STATE_TX_RX_LOOP = "tx-rx-loop"
    UDLD_OPER_STATE_UNIDIRECTIONAL = "unidirectional"
    UDLD_OPER_STATE_UNKNOWN = "unknown"


class FabricFcoeSanEp(ManagedObject):
    """This is FabricFcoeSanEp class."""

    consts = FabricFcoeSanEpConsts()
    naming_props = set(['slotId', 'portId'])

    mo_meta = MoMeta("FabricFcoeSanEp", "fabricFcoeSanEp", "phys-fcoesanep-slot-[slot_id]-port-[port_id]", VersionMeta.Version211a, "InputOutput", 0x3fff, [], ["admin", "ext-san-config", "ext-san-policy"], ['fabricFcSan', 'fabricSubGroup'], ['etherFcoeInterfaceStats', 'fabricEthMonSrcEp', 'fabricVsanEp', 'fabricVsanMembership', 'faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_speed": MoPropertyMeta("admin_speed", "adminSpeed", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["100gbps", "10gbps", "1gbps", "20gbps", "25gbps", "40gbps", "auto", "indeterminate"], []),
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["disabled", "enabled"], []),
        "aggr_port_id": MoPropertyMeta("aggr_port_id", "aggrPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "auto_negotiate": MoPropertyMeta("auto_negotiate", "autoNegotiate", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["disabled", "enabled"], []),
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x10, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "inconsistent"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "eth_link_profile_name": MoPropertyMeta("eth_link_profile_name", "ethLinkProfileName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "fcoe_state": MoPropertyMeta("fcoe_state", "fcoeState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["admin-down", "down", "error-disabled", "failed", "hardware-failure", "indeterminate", "link-down", "link-up", "no-license", "sfp-not-present", "software-failure", "udld-aggr-down", "up"], []),
        "fcoe_state_reason": MoPropertyMeta("fcoe_state_reason", "fcoeStateReason", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "fec": MoPropertyMeta("fec", "fec", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["auto", "cl74", "cl91", "off", "rs-cons16", "rs-ieee"], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
        "lic_gp": MoPropertyMeta("lic_gp", "licGP", "ulong", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "lic_state": MoPropertyMeta("lic_state", "licState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["license-expired", "license-graceperiod", "license-insufficient", "license-ok", "not-applicable", "unknown"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_eth_link_profile_name": MoPropertyMeta("oper_eth_link_profile_name", "operEthLinkProfileName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["down", "error-misconfigured", "error-unsupported-mini-server-port", "failed", "unknown", "up"], []),
        "oper_state_reason": MoPropertyMeta("oper_state_reason", "operStateReason", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "peer_aggr_port_id": MoPropertyMeta("peer_aggr_port_id", "peerAggrPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "peer_chassis_id": MoPropertyMeta("peer_chassis_id", "peerChassisId", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "peer_port_id": MoPropertyMeta("peer_port_id", "peerPortId", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "peer_slot_id": MoPropertyMeta("peer_slot_id", "peerSlotId", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x200, None, None, None, [], ["1-108"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x800, None, None, None, [], ["1-5"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
        "udld_oper_state": MoPropertyMeta("udld_oper_state", "udldOperState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["admin-disabled", "bidirectional", "echo-empty", "mismatch", "tx-rx-loop", "unidirectional", "unknown"], []),
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []),
        "warnings": MoPropertyMeta("warnings", "warnings", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|fc-zoning-enabled|configuration-error),){0,3}(defaultValue|none|fc-zoning-enabled|configuration-error){0,1}""", [], []),
    }

    prop_map = {
        "adminSpeed": "admin_speed", 
        "adminState": "admin_state", 
        "aggrPortId": "aggr_port_id", 
        "autoNegotiate": "auto_negotiate", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "ethLinkProfileName": "eth_link_profile_name", 
        "fcoeState": "fcoe_state", 
        "fcoeStateReason": "fcoe_state_reason", 
        "fec": "fec", 
        "fltAggr": "flt_aggr", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "licGP": "lic_gp", 
        "licState": "lic_state", 
        "locale": "locale", 
        "name": "name", 
        "operEthLinkProfileName": "oper_eth_link_profile_name", 
        "operState": "oper_state", 
        "operStateReason": "oper_state_reason", 
        "peerAggrPortId": "peer_aggr_port_id", 
        "peerChassisId": "peer_chassis_id", 
        "peerDn": "peer_dn", 
        "peerPortId": "peer_port_id", 
        "peerSlotId": "peer_slot_id", 
        "portId": "port_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotId": "slot_id", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
        "udldOperState": "udld_oper_state", 
        "usrLbl": "usr_lbl", 
        "warnings": "warnings", 
    }

    def __init__(self, parent_mo_or_dn, slot_id, port_id, **kwargs):
        self._dirty_mask = 0
        self.slot_id = slot_id
        self.port_id = port_id
        self.admin_speed = None
        self.admin_state = None
        self.aggr_port_id = None
        self.auto_negotiate = None
        self.chassis_id = None
        self.child_action = None
        self.config_state = None
        self.ep_dn = None
        self.eth_link_profile_name = None
        self.fcoe_state = None
        self.fcoe_state_reason = None
        self.fec = None
        self.flt_aggr = None
        self.if_role = None
        self.if_type = None
        self.lic_gp = None
        self.lic_state = None
        self.locale = None
        self.name = None
        self.oper_eth_link_profile_name = None
        self.oper_state = None
        self.oper_state_reason = None
        self.peer_aggr_port_id = None
        self.peer_chassis_id = None
        self.peer_dn = None
        self.peer_port_id = None
        self.peer_slot_id = None
        self.sacl = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None
        self.udld_oper_state = None
        self.usr_lbl = None
        self.warnings = None

        ManagedObject.__init__(self, "FabricFcoeSanEp", parent_mo_or_dn, **kwargs)
