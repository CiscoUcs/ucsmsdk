"""This module contains the general information for FabricEthLanPc ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricEthLanPcConsts:
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
    AUTO_NEGOTIATE_FALSE = "false"
    AUTO_NEGOTIATE_NO = "no"
    AUTO_NEGOTIATE_TRUE = "true"
    AUTO_NEGOTIATE_YES = "yes"
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
    IS_UPLINK_PEER_PORT_STP_FALSE = "false"
    IS_UPLINK_PEER_PORT_STP_NO = "no"
    IS_UPLINK_PEER_PORT_STP_TRUE = "true"
    IS_UPLINK_PEER_PORT_STP_YES = "yes"
    OPER_SPEED_100GBPS = "100gbps"
    OPER_SPEED_10GBPS = "10gbps"
    OPER_SPEED_1GBPS = "1gbps"
    OPER_SPEED_20GBPS = "20gbps"
    OPER_SPEED_25GBPS = "25gbps"
    OPER_SPEED_40GBPS = "40gbps"
    OPER_SPEED_AUTO = "auto"
    OPER_SPEED_INDETERMINATE = "indeterminate"
    OPER_STATE_ADMIN_DOWN = "admin-down"
    OPER_STATE_DOWN = "down"
    OPER_STATE_ERROR_DISABLED = "error-disabled"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_HARDWARE_FAILURE = "hardware-failure"
    OPER_STATE_INDETERMINATE = "indeterminate"
    OPER_STATE_LINK_DOWN = "link-down"
    OPER_STATE_LINK_UP = "link-up"
    OPER_STATE_NO_LICENSE = "no-license"
    OPER_STATE_SFP_NOT_PRESENT = "sfp-not-present"
    OPER_STATE_SOFTWARE_FAILURE = "software-failure"
    OPER_STATE_UDLD_AGGR_DOWN = "udld-aggr-down"
    OPER_STATE_UP = "up"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    VLAN_STATUS_MISSING_PRIMARY = "missing-primary"
    VLAN_STATUS_OK = "ok"


class FabricEthLanPc(ManagedObject):
    """This is FabricEthLanPc class."""

    consts = FabricEthLanPcConsts()
    naming_props = set(['portId'])

    mo_meta = MoMeta("FabricEthLanPc", "fabricEthLanPc", "pc-[port_id]", VersionMeta.Version101e, "InputOutput", 0x3fff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricEthLan'], ['etherErrStats', 'etherLossStats', 'etherPauseStats', 'etherRxStats', 'etherTxStats', 'fabricEthLanPcEp', 'fabricEthMonSrcEp', 'fabricSubGroup', 'faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_speed": MoPropertyMeta("admin_speed", "adminSpeed", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["100gbps", "10gbps", "1gbps", "20gbps", "25gbps", "40gbps", "auto", "indeterminate"], []),
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["disabled", "enabled"], []),
        "auto_negotiate": MoPropertyMeta("auto_negotiate", "autoNegotiate", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["false", "no", "true", "yes"], []),
        "bandwidth": MoPropertyMeta("bandwidth", "bandwidth", "uint", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x10, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "flow_ctrl_policy": MoPropertyMeta("flow_ctrl_policy", "flowCtrlPolicy", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
        "is_uplink_peer_port_stp": MoPropertyMeta("is_uplink_peer_port_stp", "isUplinkPeerPortStp", "string", VersionMeta.Version423b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "lacp_policy_name": MoPropertyMeta("lacp_policy_name", "lacpPolicyName", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_lacp_policy_name": MoPropertyMeta("oper_lacp_policy_name", "operLacpPolicyName", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_speed": MoPropertyMeta("oper_speed", "operSpeed", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["100gbps", "10gbps", "1gbps", "20gbps", "25gbps", "40gbps", "auto", "indeterminate"], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["admin-down", "down", "error-disabled", "failed", "hardware-failure", "indeterminate", "link-down", "link-up", "no-license", "sfp-not-present", "software-failure", "udld-aggr-down", "up"], []),
        "overlapping_vlans": MoPropertyMeta("overlapping_vlans", "overlappingVlans", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x800, None, None, None, [], ["1-256"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x1000, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "state_qual": MoPropertyMeta("state_qual", "stateQual", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
        "vlan_status": MoPropertyMeta("vlan_status", "vlanStatus", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["missing-primary", "ok"], []),
        "warnings": MoPropertyMeta("warnings", "warnings", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|fc-zoning-enabled|configuration-error),){0,3}(defaultValue|none|fc-zoning-enabled|configuration-error){0,1}""", [], []),
    }

    prop_map = {
        "adminSpeed": "admin_speed", 
        "adminState": "admin_state", 
        "autoNegotiate": "auto_negotiate", 
        "bandwidth": "bandwidth", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "flowCtrlPolicy": "flow_ctrl_policy", 
        "fltAggr": "flt_aggr", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "isUplinkPeerPortStp": "is_uplink_peer_port_stp", 
        "lacpPolicyName": "lacp_policy_name", 
        "locale": "locale", 
        "name": "name", 
        "operLacpPolicyName": "oper_lacp_policy_name", 
        "operSpeed": "oper_speed", 
        "operState": "oper_state", 
        "overlappingVlans": "overlapping_vlans", 
        "peerDn": "peer_dn", 
        "portId": "port_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "stateQual": "state_qual", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
        "vlanStatus": "vlan_status", 
        "warnings": "warnings", 
    }

    def __init__(self, parent_mo_or_dn, port_id, **kwargs):
        self._dirty_mask = 0
        self.port_id = port_id
        self.admin_speed = None
        self.admin_state = None
        self.auto_negotiate = None
        self.bandwidth = None
        self.child_action = None
        self.descr = None
        self.ep_dn = None
        self.flow_ctrl_policy = None
        self.flt_aggr = None
        self.if_role = None
        self.if_type = None
        self.is_uplink_peer_port_stp = None
        self.lacp_policy_name = None
        self.locale = None
        self.name = None
        self.oper_lacp_policy_name = None
        self.oper_speed = None
        self.oper_state = None
        self.overlapping_vlans = None
        self.peer_dn = None
        self.sacl = None
        self.state_qual = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None
        self.vlan_status = None
        self.warnings = None

        ManagedObject.__init__(self, "FabricEthLanPc", parent_mo_or_dn, **kwargs)
