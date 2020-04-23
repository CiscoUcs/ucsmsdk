"""This module contains the general information for FabricEthEstcPc ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricEthEstcPcConsts:
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
    PORT_MODE_ACCESS = "access"
    PORT_MODE_TRUNK = "trunk"
    PRIO_BEST_EFFORT = "best-effort"
    PRIO_BRONZE = "bronze"
    PRIO_FC = "fc"
    PRIO_GOLD = "gold"
    PRIO_PLATINUM = "platinum"
    PRIO_SILVER = "silver"
    PROTOCOL_LACP = "lacp"
    PROTOCOL_STATIC = "static"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class FabricEthEstcPc(ManagedObject):
    """This is FabricEthEstcPc class."""

    consts = FabricEthEstcPcConsts()
    naming_props = set(['portId'])

    mo_meta = MoMeta("FabricEthEstcPc", "fabricEthEstcPc", "pc-[port_id]", VersionMeta.Version141i, "InputOutput", 0x3ffff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricEthEstc'], ['etherErrStats', 'etherLossStats', 'etherPauseStats', 'etherRxStats', 'etherTxStats', 'fabricEthEstcPcEp', 'fabricEthMonSrcEp', 'fabricEthTargetEp', 'fabricSubGroup', 'fabricVlanEp', 'faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_speed": MoPropertyMeta("admin_speed", "adminSpeed", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["100gbps", "10gbps", "1gbps", "20gbps", "25gbps", "40gbps", "auto", "indeterminate"], []),
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x8, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "flow_ctrl_policy": MoPropertyMeta("flow_ctrl_policy", "flowCtrlPolicy", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
        "lacp_policy_name": MoPropertyMeta("lacp_policy_name", "lacpPolicyName", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "nw_ctrl_policy_name": MoPropertyMeta("nw_ctrl_policy_name", "nwCtrlPolicyName", "string", VersionMeta.Version142b, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_lacp_policy_name": MoPropertyMeta("oper_lacp_policy_name", "operLacpPolicyName", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_nw_ctrl_policy_name": MoPropertyMeta("oper_nw_ctrl_policy_name", "operNwCtrlPolicyName", "string", VersionMeta.Version142b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_speed": MoPropertyMeta("oper_speed", "operSpeed", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["100gbps", "10gbps", "1gbps", "20gbps", "25gbps", "40gbps", "auto", "indeterminate"], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["admin-down", "down", "error-disabled", "failed", "hardware-failure", "indeterminate", "link-down", "link-up", "no-license", "sfp-not-present", "software-failure", "udld-aggr-down", "up"], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "pin_group_name": MoPropertyMeta("pin_group_name", "pinGroupName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x800, 0, 510, None, [], []),
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x1000, None, None, None, [], ["1-256"]),
        "port_mode": MoPropertyMeta("port_mode", "portMode", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["access", "trunk"], []),
        "prio": MoPropertyMeta("prio", "prio", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["best-effort", "bronze", "fc", "gold", "platinum", "silver"], []),
        "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version142b, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["lacp", "static"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10000, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "state_qual": MoPropertyMeta("state_qual", "stateQual", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
        "warnings": MoPropertyMeta("warnings", "warnings", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|fc-zoning-enabled|configuration-error),){0,3}(defaultValue|none|fc-zoning-enabled|configuration-error){0,1}""", [], []),
    }

    prop_map = {
        "adminSpeed": "admin_speed", 
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "flowCtrlPolicy": "flow_ctrl_policy", 
        "fltAggr": "flt_aggr", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "lacpPolicyName": "lacp_policy_name", 
        "locale": "locale", 
        "name": "name", 
        "nwCtrlPolicyName": "nw_ctrl_policy_name", 
        "operLacpPolicyName": "oper_lacp_policy_name", 
        "operNwCtrlPolicyName": "oper_nw_ctrl_policy_name", 
        "operSpeed": "oper_speed", 
        "operState": "oper_state", 
        "peerDn": "peer_dn", 
        "pinGroupName": "pin_group_name", 
        "portId": "port_id", 
        "portMode": "port_mode", 
        "prio": "prio", 
        "protocol": "protocol", 
        "rn": "rn", 
        "sacl": "sacl", 
        "stateQual": "state_qual", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
        "warnings": "warnings", 
    }

    def __init__(self, parent_mo_or_dn, port_id, **kwargs):
        self._dirty_mask = 0
        self.port_id = port_id
        self.admin_speed = None
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.ep_dn = None
        self.flow_ctrl_policy = None
        self.flt_aggr = None
        self.if_role = None
        self.if_type = None
        self.lacp_policy_name = None
        self.locale = None
        self.name = None
        self.nw_ctrl_policy_name = None
        self.oper_lacp_policy_name = None
        self.oper_nw_ctrl_policy_name = None
        self.oper_speed = None
        self.oper_state = None
        self.peer_dn = None
        self.pin_group_name = None
        self.port_mode = None
        self.prio = None
        self.protocol = None
        self.sacl = None
        self.state_qual = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None
        self.warnings = None

        ManagedObject.__init__(self, "FabricEthEstcPc", parent_mo_or_dn, **kwargs)
