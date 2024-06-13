"""This module contains the general information for MgmtUsbNicMgmtIf ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtUsbNicMgmtIfConsts:
    ACCESS_IN_BAND = "in-band"
    ACCESS_INTERNAL = "internal"
    ACCESS_OUT_OF_BAND = "out-of-band"
    ACCESS_UNSPECIFIED = "unspecified"
    ACCESS_VIRTUAL = "virtual"
    ADMIN_STATE_DISABLE = "disable"
    ADMIN_STATE_ENABLE = "enable"
    CHASSIS_ID_N_A = "N/A"
    DISCOVERY_ABSENT = "absent"
    DISCOVERY_INIT = "init"
    DISCOVERY_MIS_CONNECT = "mis-connect"
    DISCOVERY_MISSING = "missing"
    DISCOVERY_NEW = "new"
    DISCOVERY_PRESENT = "present"
    DISCOVERY_UN_INITIALIZED = "un-initialized"
    DISCOVERY_UN_SUPPORTED = "un-supported"
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
    STATE_QUAL_MISCONNECTED = "misconnected"
    STATE_QUAL_UNSPECIFIED = "unspecified"
    STATE_QUAL_VALID = "valid"
    SUBJECT_ADAPTOR = "adaptor"
    SUBJECT_BLADE = "blade"
    SUBJECT_BOARD_CONTROLLER = "board-controller"
    SUBJECT_CHASSIS = "chassis"
    SUBJECT_CMC = "cmc"
    SUBJECT_CPLD = "cpld"
    SUBJECT_INTEL_AMC = "intel-amc"
    SUBJECT_IOCARD = "iocard"
    SUBJECT_LOCAL_DISK = "local-disk"
    SUBJECT_RETIMER = "retimer"
    SUBJECT_SAS_EXPANDER = "sas-expander"
    SUBJECT_SERVER_UNIT = "server-unit"
    SUBJECT_SWITCH = "switch"
    SUBJECT_SYSTEM = "system"
    SUBJECT_UBM = "ubm"
    SUBJECT_UNKNOWN = "unknown"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    USBNIC_CONN_SIDE_FI_SIDE = "fi-side"
    USBNIC_CONN_SIDE_HOST_SIDE = "host-side"
    USBNIC_CONN_SIDE_UNSPECIFIED = "unspecified"


class MgmtUsbNicMgmtIf(ManagedObject):
    """This is MgmtUsbNicMgmtIf class."""

    consts = MgmtUsbNicMgmtIfConsts()
    naming_props = set(['usbnicConnSide', 'switchId'])

    mo_meta = MoMeta("MgmtUsbNicMgmtIf", "mgmtUsbNicMgmtIf", "usbnic-if-[usbnic_conn_side]-[switch_id]", VersionMeta.Version323a, "InputOutput", 0x3ff, [], ["admin"], ['computeHostUtilityOs', 'mgmtController'], [], ["Get"])

    prop_meta = {
        "access": MoPropertyMeta("access", "access", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["in-band", "internal", "out-of-band", "unspecified", "virtual"], []),
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disable", "enable"], []),
        "aggr_port_id": MoPropertyMeta("aggr_port_id", "aggrPortId", "uint", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version323a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "discovery": MoPropertyMeta("discovery", "discovery", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["absent", "init", "mis-connect", "missing", "new", "present", "un-initialized", "un-supported"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "ext_broadcast": MoPropertyMeta("ext_broadcast", "extBroadcast", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "ext_gw": MoPropertyMeta("ext_gw", "extGw", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "ext_ip": MoPropertyMeta("ext_ip", "extIp", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "ext_mask": MoPropertyMeta("ext_mask", "extMask", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
        "instance_id": MoPropertyMeta("instance_id", "instanceId", "uint", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-4294967295"]),
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "mac": MoPropertyMeta("mac", "mac", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "mask": MoPropertyMeta("mask", "mask", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "peer_aggr_port_id": MoPropertyMeta("peer_aggr_port_id", "peerAggrPortId", "uint", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "peer_chassis_id": MoPropertyMeta("peer_chassis_id", "peerChassisId", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "peer_port_id": MoPropertyMeta("peer_port_id", "peerPortId", "uint", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "peer_slot_id": MoPropertyMeta("peer_slot_id", "peerSlotId", "uint", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "state_qual": MoPropertyMeta("state_qual", "stateQual", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["misconnected", "unspecified", "valid"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "subject": MoPropertyMeta("subject", "subject", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["adaptor", "blade", "board-controller", "chassis", "cmc", "cpld", "intel-amc", "iocard", "local-disk", "retimer", "sas-expander", "server-unit", "switch", "system", "ubm", "unknown"], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version323a, MoPropertyMeta.NAMING, 0x100, None, None, None, ["A", "B", "NONE"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
        "usbnic_conn_side": MoPropertyMeta("usbnic_conn_side", "usbnicConnSide", "string", VersionMeta.Version323a, MoPropertyMeta.NAMING, 0x200, None, None, None, ["fi-side", "host-side", "unspecified"], []),
        "vnet": MoPropertyMeta("vnet", "vnet", "uint", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4090"]),
    }

    prop_map = {
        "access": "access", 
        "adminState": "admin_state", 
        "aggrPortId": "aggr_port_id", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "discovery": "discovery", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "extBroadcast": "ext_broadcast", 
        "extGw": "ext_gw", 
        "extIp": "ext_ip", 
        "extMask": "ext_mask", 
        "id": "id", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "instanceId": "instance_id", 
        "ip": "ip", 
        "locale": "locale", 
        "mac": "mac", 
        "mask": "mask", 
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
        "stateQual": "state_qual", 
        "status": "status", 
        "subject": "subject", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
        "usbnicConnSide": "usbnic_conn_side", 
        "vnet": "vnet", 
    }

    def __init__(self, parent_mo_or_dn, usbnic_conn_side, switch_id, **kwargs):
        self._dirty_mask = 0
        self.usbnic_conn_side = usbnic_conn_side
        self.switch_id = switch_id
        self.access = None
        self.admin_state = None
        self.aggr_port_id = None
        self.chassis_id = None
        self.child_action = None
        self.discovery = None
        self.ep_dn = None
        self.ext_broadcast = None
        self.ext_gw = None
        self.ext_ip = None
        self.ext_mask = None
        self.id = None
        self.if_role = None
        self.if_type = None
        self.instance_id = None
        self.ip = None
        self.locale = None
        self.mac = None
        self.mask = None
        self.name = None
        self.peer_aggr_port_id = None
        self.peer_chassis_id = None
        self.peer_dn = None
        self.peer_port_id = None
        self.peer_slot_id = None
        self.port_id = None
        self.sacl = None
        self.slot_id = None
        self.state_qual = None
        self.status = None
        self.subject = None
        self.transport = None
        self.type = None
        self.vnet = None

        ManagedObject.__init__(self, "MgmtUsbNicMgmtIf", parent_mo_or_dn, **kwargs)
