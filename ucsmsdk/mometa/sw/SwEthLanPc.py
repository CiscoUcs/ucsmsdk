"""This module contains the general information for SwEthLanPc ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwEthLanPcConsts:
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
    LACP_FAST_TIMER_FALSE = "false"
    LACP_FAST_TIMER_NO = "no"
    LACP_FAST_TIMER_TRUE = "true"
    LACP_FAST_TIMER_YES = "yes"
    LACP_SUSPEND_INDIVIDUAL_FALSE = "false"
    LACP_SUSPEND_INDIVIDUAL_NO = "no"
    LACP_SUSPEND_INDIVIDUAL_TRUE = "true"
    LACP_SUSPEND_INDIVIDUAL_YES = "yes"
    MON_TRAF_DIR_BOTH = "both"
    MON_TRAF_DIR_RX = "rx"
    MON_TRAF_DIR_TX = "tx"
    PRIORITY_FLOW_CTRL_AUTO = "auto"
    PRIORITY_FLOW_CTRL_ON = "on"
    RECV_FLOW_CTRL_OFF = "off"
    RECV_FLOW_CTRL_ON = "on"
    SEND_FLOW_CTRL_OFF = "off"
    SEND_FLOW_CTRL_ON = "on"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class SwEthLanPc(ManagedObject):
    """This is SwEthLanPc class."""

    consts = SwEthLanPcConsts()
    naming_props = set(['portId'])

    mo_meta = MoMeta("SwEthLanPc", "swEthLanPc", "pc-[port_id]", VersionMeta.Version101e, "InputOutput", 0xff, [], ["read-only"], ['swEthLanBorder', 'swEthMon'], ['swVlan'], ["Get"])

    prop_meta = {
        "admin_speed": MoPropertyMeta("admin_speed", "adminSpeed", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["100gbps", "10gbps", "1gbps", "20gbps", "25gbps", "40gbps", "auto", "indeterminate"], []),
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
        "lacp_fast_timer": MoPropertyMeta("lacp_fast_timer", "lacpFastTimer", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "lacp_suspend_individual": MoPropertyMeta("lacp_suspend_individual", "lacpSuspendIndividual", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "mon_traf_dir": MoPropertyMeta("mon_traf_dir", "monTrafDir", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["both", "rx", "tx"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []),
        "priority_flow_ctrl": MoPropertyMeta("priority_flow_ctrl", "priorityFlowCtrl", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["auto", "on"], []),
        "recv_flow_ctrl": MoPropertyMeta("recv_flow_ctrl", "recvFlowCtrl", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["off", "on"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "send_flow_ctrl": MoPropertyMeta("send_flow_ctrl", "sendFlowCtrl", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["off", "on"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "adminSpeed": "admin_speed", 
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "lacpFastTimer": "lacp_fast_timer", 
        "lacpSuspendIndividual": "lacp_suspend_individual", 
        "locale": "locale", 
        "monTrafDir": "mon_traf_dir", 
        "name": "name", 
        "peerDn": "peer_dn", 
        "portId": "port_id", 
        "priorityFlowCtrl": "priority_flow_ctrl", 
        "recvFlowCtrl": "recv_flow_ctrl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sendFlowCtrl": "send_flow_ctrl", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, port_id, **kwargs):
        self._dirty_mask = 0
        self.port_id = port_id
        self.admin_speed = None
        self.admin_state = None
        self.child_action = None
        self.ep_dn = None
        self.if_role = None
        self.if_type = None
        self.lacp_fast_timer = None
        self.lacp_suspend_individual = None
        self.locale = None
        self.mon_traf_dir = None
        self.name = None
        self.peer_dn = None
        self.priority_flow_ctrl = None
        self.recv_flow_ctrl = None
        self.sacl = None
        self.send_flow_ctrl = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "SwEthLanPc", parent_mo_or_dn, **kwargs)
