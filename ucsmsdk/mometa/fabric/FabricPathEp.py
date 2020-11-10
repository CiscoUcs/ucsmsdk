"""This module contains the general information for FabricPathEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricPathEpConsts:
    C_TYPE_MUX = "mux"
    C_TYPE_MUX_ACCESS = "mux-access"
    C_TYPE_MUX_FABRIC = "mux-fabric"
    C_TYPE_MUX_FABRICPC = "mux-fabricpc"
    C_TYPE_MUX_FABRICPC_TO_CHPC = "mux-fabricpc-to-chpc"
    C_TYPE_MUX_FABRICPC_TO_HOSTPC = "mux-fabricpc-to-hostpc"
    C_TYPE_MUX_FABRICPC_TO_HOSTPORT = "mux-fabricpc-to-hostport"
    C_TYPE_MUX_FABRICPORT_TO_HOSTPC = "mux-fabricport-to-hostpc"
    C_TYPE_MUX_HOSTPC_TO_ADAPTORPC = "mux-hostpc-to-adaptorpc"
    C_TYPE_MUX_TO_APPLIANCE = "mux-to-appliance"
    C_TYPE_MUX_TO_CHASSIS = "mux-to-chassis"
    C_TYPE_MUX_TO_HOST = "mux-to-host"
    C_TYPE_SWITCH_ACCESS = "switch-access"
    C_TYPE_SWITCH_FABRIC = "switch-fabric"
    C_TYPE_SWITCH_FABRICPC = "switch-fabricpc"
    C_TYPE_SWITCH_TO_HOST = "switch-to-host"
    C_TYPE_SWITCH_TO_MUX = "switch-to-mux"
    C_TYPE_SWITCHPC_TO_HOSTPC = "switchpc-to-hostpc"
    CHASSIS_ID_N_A = "N/A"
    DIAG_LLDP_TRANSMIT_FALSE = "false"
    DIAG_LLDP_TRANSMIT_NO = "no"
    DIAG_LLDP_TRANSMIT_TRUE = "true"
    DIAG_LLDP_TRANSMIT_YES = "yes"
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
    PEER_CHASSIS_ID_N_A = "N/A"
    PORT_GROUP_ROLE_MASTER = "master"
    PORT_GROUP_ROLE_MASTER_PC = "master-pc"
    PORT_GROUP_ROLE_MEMBER = "member"
    PORT_GROUP_ROLE_NONE = "none"
    SIDE_LEFT = "left"
    SIDE_RIGHT = "right"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class FabricPathEp(ManagedObject):
    """This is FabricPathEp class."""

    consts = FabricPathEpConsts()
    naming_props = set(['cType'])

    mo_meta = MoMeta("FabricPathEp", "fabricPathEp", "ep-[c_type]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["read-only"], ['fabricPath', 'fabricPathConn'], ['portTrustMode'], ["Get"])

    prop_meta = {
        "aggr_port_id": MoPropertyMeta("aggr_port_id", "aggrPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "c_type": MoPropertyMeta("c_type", "cType", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x2, None, None, None, ["mux", "mux-access", "mux-fabric", "mux-fabricpc", "mux-fabricpc-to-chpc", "mux-fabricpc-to-hostpc", "mux-fabricpc-to-hostport", "mux-fabricport-to-hostpc", "mux-hostpc-to-adaptorpc", "mux-to-appliance", "mux-to-chassis", "mux-to-host", "switch-access", "switch-fabric", "switch-fabricpc", "switch-to-host", "switch-to-mux", "switchpc-to-hostpc"], ["0-255"]),
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "diag_lldp_transmit": MoPropertyMeta("diag_lldp_transmit", "diagLldpTransmit", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "peer_aggr_port_id": MoPropertyMeta("peer_aggr_port_id", "peerAggrPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "peer_chassis_id": MoPropertyMeta("peer_chassis_id", "peerChassisId", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "peer_mac": MoPropertyMeta("peer_mac", "peerMac", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "peer_port_id": MoPropertyMeta("peer_port_id", "peerPortId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "peer_slot_id": MoPropertyMeta("peer_slot_id", "peerSlotId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "port_group_role": MoPropertyMeta("port_group_role", "portGroupRole", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["master", "master-pc", "member", "none"], ["0-255"]),
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "side": MoPropertyMeta("side", "side", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["left", "right"], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "aggrPortId": "aggr_port_id", 
        "cType": "c_type", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "diagLldpTransmit": "diag_lldp_transmit", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "locale": "locale", 
        "name": "name", 
        "peerAggrPortId": "peer_aggr_port_id", 
        "peerChassisId": "peer_chassis_id", 
        "peerDn": "peer_dn", 
        "peerMac": "peer_mac", 
        "peerPortId": "peer_port_id", 
        "peerSlotId": "peer_slot_id", 
        "portGroupRole": "port_group_role", 
        "portId": "port_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "side": "side", 
        "slotId": "slot_id", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, c_type, **kwargs):
        self._dirty_mask = 0
        self.c_type = c_type
        self.aggr_port_id = None
        self.chassis_id = None
        self.child_action = None
        self.diag_lldp_transmit = None
        self.ep_dn = None
        self.if_role = None
        self.if_type = None
        self.locale = None
        self.name = None
        self.peer_aggr_port_id = None
        self.peer_chassis_id = None
        self.peer_dn = None
        self.peer_mac = None
        self.peer_port_id = None
        self.peer_slot_id = None
        self.port_group_role = None
        self.port_id = None
        self.sacl = None
        self.side = None
        self.slot_id = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "FabricPathEp", parent_mo_or_dn, **kwargs)
