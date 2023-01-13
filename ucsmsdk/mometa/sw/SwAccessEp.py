"""This module contains the general information for SwAccessEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwAccessEpConsts:
    SPEED_100GBPS = "100gbps"
    SPEED_10GBPS = "10gbps"
    SPEED_1GBPS = "1gbps"
    SPEED_20GBPS = "20gbps"
    SPEED_25GBPS = "25gbps"
    SPEED_40GBPS = "40gbps"
    SPEED_AUTO = "auto"
    SPEED_INDETERMINATE = "indeterminate"
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    AUTO_NEG_DISABLED = "disabled"
    AUTO_NEG_ENABLED = "enabled"
    CHASSIS_ID_N_A = "N/A"
    ENCAP_CONSOLIDATED = "consolidated"
    ENCAP_VIRTUAL = "virtual"
    ENCAP_VIRTUAL_CE = "virtual-ce"
    FEC_AUTO = "auto"
    FEC_CL74 = "cl74"
    FEC_CL91 = "cl91"
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
    LC_PENDING = "pending"
    LC_REPURPOSED = "repurposed"
    PEER_CHASSIS_ID_N_A = "N/A"
    PRIORITY_FLOW_CTRL_AUTO = "auto"
    PRIORITY_FLOW_CTRL_ON = "on"
    RECV_FLOW_CTRL_OFF = "off"
    RECV_FLOW_CTRL_ON = "on"
    SEND_FLOW_CTRL_OFF = "off"
    SEND_FLOW_CTRL_ON = "on"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class SwAccessEp(ManagedObject):
    """This is SwAccessEp class."""

    consts = SwAccessEpConsts()
    naming_props = set(['slotId', 'portId'])

    mo_meta = MoMeta("SwAccessEp", "swAccessEp", "ep-slot-[slot_id]port-[port_id]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["read-only"], ['swAccessDomain', 'swSubGroup'], ['portTrustMode', 'swUlan'], ["Get"])

    prop_meta = {
        "speed": MoPropertyMeta("speed", "Speed", "string", VersionMeta.Version422d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["100gbps", "10gbps", "1gbps", "20gbps", "25gbps", "40gbps", "auto", "indeterminate"], []),
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "aggr_port_id": MoPropertyMeta("aggr_port_id", "aggrPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "auto_neg": MoPropertyMeta("auto_neg", "autoNeg", "string", VersionMeta.Version422d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "encap": MoPropertyMeta("encap", "encap", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["consolidated", "virtual", "virtual-ce"], ["0-255"]),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "fec": MoPropertyMeta("fec", "fec", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["auto", "cl74", "cl91"], []),
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "pending", "repurposed"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "ns_size": MoPropertyMeta("ns_size", "nsSize", "ushort", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "peer_aggr_port_id": MoPropertyMeta("peer_aggr_port_id", "peerAggrPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "peer_chassis_id": MoPropertyMeta("peer_chassis_id", "peerChassisId", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "peer_port_id": MoPropertyMeta("peer_port_id", "peerPortId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "peer_slot_id": MoPropertyMeta("peer_slot_id", "peerSlotId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []),
        "priority_flow_ctrl": MoPropertyMeta("priority_flow_ctrl", "priorityFlowCtrl", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["auto", "on"], []),
        "recv_flow_ctrl": MoPropertyMeta("recv_flow_ctrl", "recvFlowCtrl", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["off", "on"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "send_flow_ctrl": MoPropertyMeta("send_flow_ctrl", "sendFlowCtrl", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["off", "on"], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x80, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "Speed": "speed", 
        "adminState": "admin_state", 
        "aggrPortId": "aggr_port_id", 
        "autoNeg": "auto_neg", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "encap": "encap", 
        "epDn": "ep_dn", 
        "fec": "fec", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "lc": "lc", 
        "locale": "locale", 
        "name": "name", 
        "nsSize": "ns_size", 
        "peerAggrPortId": "peer_aggr_port_id", 
        "peerChassisId": "peer_chassis_id", 
        "peerDn": "peer_dn", 
        "peerPortId": "peer_port_id", 
        "peerSlotId": "peer_slot_id", 
        "portId": "port_id", 
        "priorityFlowCtrl": "priority_flow_ctrl", 
        "recvFlowCtrl": "recv_flow_ctrl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sendFlowCtrl": "send_flow_ctrl", 
        "slotId": "slot_id", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, slot_id, port_id, **kwargs):
        self._dirty_mask = 0
        self.slot_id = slot_id
        self.port_id = port_id
        self.speed = None
        self.admin_state = None
        self.aggr_port_id = None
        self.auto_neg = None
        self.chassis_id = None
        self.child_action = None
        self.encap = None
        self.ep_dn = None
        self.fec = None
        self.if_role = None
        self.if_type = None
        self.lc = None
        self.locale = None
        self.name = None
        self.ns_size = None
        self.peer_aggr_port_id = None
        self.peer_chassis_id = None
        self.peer_dn = None
        self.peer_port_id = None
        self.peer_slot_id = None
        self.priority_flow_ctrl = None
        self.recv_flow_ctrl = None
        self.sacl = None
        self.send_flow_ctrl = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "SwAccessEp", parent_mo_or_dn, **kwargs)
