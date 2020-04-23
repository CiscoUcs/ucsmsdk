"""This module contains the general information for EtherSwitchIntFIoPcEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EtherSwitchIntFIoPcEpConsts:
    ACK_STATE_ACK_IN_PROGRESS = "ack-in-progress"
    ACK_STATE_ACKNOWLEDGED = "acknowledged"
    ACK_STATE_AUTO_ACK = "auto-ack"
    ACK_STATE_EVALUATION = "evaluation"
    ACK_STATE_OK = "ok"
    ACK_STATE_REMOVING = "removing"
    ACK_STATE_UN_ACKNOWLEDGED = "un-acknowledged"
    ACK_STATE_UN_INITIALIZED = "un-initialized"
    ACK_STATE_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    CHASSIS_ID_N_A = "N/A"
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
    MEMBERSHIP_DOWN = "down"
    MEMBERSHIP_HOT_STANDBY = "hot-standby"
    MEMBERSHIP_INCOMPATIBLE_SPEED = "incompatible-speed"
    MEMBERSHIP_INDIVIDUAL = "individual"
    MEMBERSHIP_MODULE_REMOVED = "module-removed"
    MEMBERSHIP_SUSPENDED = "suspended"
    MEMBERSHIP_UNKNOWN = "unknown"
    MEMBERSHIP_UP = "up"
    PEER_CHASSIS_ID_N_A = "N/A"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class EtherSwitchIntFIoPcEp(ManagedObject):
    """This is EtherSwitchIntFIoPcEp class."""

    consts = EtherSwitchIntFIoPcEpConsts()
    naming_props = set(['slotId', 'portId'])

    mo_meta = MoMeta("EtherSwitchIntFIoPcEp", "etherSwitchIntFIoPcEp", "ep-slot-[slot_id]-port-[port_id]", VersionMeta.Version201m, "InputOutput", 0x1ff, [], ["admin", "ext-lan-config", "ext-lan-policy", "pn-equipment", "pn-maintenance"], ['etherSwitchIntFIoPc'], [], ["Get"])

    prop_meta = {
        "ack_state": MoPropertyMeta("ack_state", "ackState", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ack-in-progress", "acknowledged", "auto-ack", "evaluation", "ok", "removing", "un-acknowledged", "un-initialized", "unsupported-connectivity"], []),
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "aggr_port_id": MoPropertyMeta("aggr_port_id", "aggrPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "membership": MoPropertyMeta("membership", "membership", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["down", "hot-standby", "incompatible-speed", "individual", "module-removed", "suspended", "unknown", "up"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "peer_aggr_port_id": MoPropertyMeta("peer_aggr_port_id", "peerAggrPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "peer_chassis_id": MoPropertyMeta("peer_chassis_id", "peerChassisId", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "peer_port_id": MoPropertyMeta("peer_port_id", "peerPortId", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "peer_slot_id": MoPropertyMeta("peer_slot_id", "peerSlotId", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x20, None, None, None, [], ["1-32"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x80, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "status_change_ts": MoPropertyMeta("status_change_ts", "statusChangeTs", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "ackState": "ack_state", 
        "adminState": "admin_state", 
        "aggrPortId": "aggr_port_id", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "locale": "locale", 
        "membership": "membership", 
        "name": "name", 
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
        "statusChangeTs": "status_change_ts", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, slot_id, port_id, **kwargs):
        self._dirty_mask = 0
        self.slot_id = slot_id
        self.port_id = port_id
        self.ack_state = None
        self.admin_state = None
        self.aggr_port_id = None
        self.chassis_id = None
        self.child_action = None
        self.ep_dn = None
        self.if_role = None
        self.if_type = None
        self.locale = None
        self.membership = None
        self.name = None
        self.peer_aggr_port_id = None
        self.peer_chassis_id = None
        self.peer_dn = None
        self.peer_port_id = None
        self.peer_slot_id = None
        self.sacl = None
        self.status = None
        self.status_change_ts = None
        self.switch_id = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "EtherSwitchIntFIoPcEp", parent_mo_or_dn, **kwargs)
