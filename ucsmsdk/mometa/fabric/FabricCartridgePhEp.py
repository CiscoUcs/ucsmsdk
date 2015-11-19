"""This module contains the general information for FabricCartridgePhEp ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FabricCartridgePhEpConsts():
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
    LC_IN_SERVICE = "in-service"
    LC_MIGRATE = "migrate"
    LC_OUT_OF_SERVICE = "out-of-service"
    LC_OUT_OF_SERVICE_SLAVE = "out-of-service-slave"
    LIC_STATE_LICENSE_EXPIRED = "license-expired"
    LIC_STATE_LICENSE_GRACEPERIOD = "license-graceperiod"
    LIC_STATE_LICENSE_INSUFFICIENT = "license-insufficient"
    LIC_STATE_LICENSE_OK = "license-ok"
    LIC_STATE_NOT_APPLICABLE = "not-applicable"
    LIC_STATE_UNKNOWN = "unknown"
    OPER_STATE_DOWN = "down"
    OPER_STATE_ERROR_MISCONFIGURED = "error-misconfigured"
    OPER_STATE_UNKNOWN = "unknown"
    OPER_STATE_UP = "up"
    PEER_CHASSIS_ID_N_A = "N/A"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class FabricCartridgePhEp(ManagedObject):
    """This is FabricCartridgePhEp class."""

    consts = FabricCartridgePhEpConsts()
    naming_props = set([u'vendor', u'model', u'serial'])

    mo_meta = MoMeta("FabricCartridgePhEp", "fabricCartridgePhEp", "cart-ep-ven-[vendor]-mod-[model]-ser-[serial]", VersionMeta.Version251a, "InputOutput", 0x3ffL, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], [u'fabricDceSrv'], [u'fabricLastAckedSlot', u'faultInst'], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["disabled", "enabled"], []), 
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["N/A"], ["1-255"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, 0x4L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []), 
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["in-service", "migrate", "out-of-service", "out-of-service-slave"], []), 
        "lic_gp": MoPropertyMeta("lic_gp", "licGP", "ulong", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lic_state": MoPropertyMeta("lic_state", "licState", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["license-expired", "license-graceperiod", "license-insufficient", "license-ok", "not-applicable", "unknown"], []), 
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, """((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x10L, 1, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["down", "error-misconfigured", "unknown", "up"], []), 
        "oper_state_reason": MoPropertyMeta("oper_state_reason", "operStateReason", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "peer_chassis_id": MoPropertyMeta("peer_chassis_id", "peerChassisId", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]), 
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "peer_port_id": MoPropertyMeta("peer_port_id", "peerPortId", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "peer_slot_id": MoPropertyMeta("peer_slot_id", "peerSlotId", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-48"]), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x80L, 1, 510, None, [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []), 
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, """((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, """((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x200L, 1, 510, None, [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "fltAggr": "flt_aggr", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "lc": "lc", 
        "licGP": "lic_gp", 
        "licState": "lic_state", 
        "locale": "locale", 
        "model": "model", 
        "name": "name", 
        "operState": "oper_state", 
        "operStateReason": "oper_state_reason", 
        "peerChassisId": "peer_chassis_id", 
        "peerDn": "peer_dn", 
        "peerPortId": "peer_port_id", 
        "peerSlotId": "peer_slot_id", 
        "portId": "port_id", 
        "revision": "revision", 
        "rn": "rn", 
        "serial": "serial", 
        "slotId": "slot_id", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, vendor, model, serial, **kwargs):
        self._dirty_mask = 0
        self.vendor = vendor
        self.model = model
        self.serial = serial
        self.admin_state = None
        self.chassis_id = None
        self.child_action = None
        self.ep_dn = None
        self.flt_aggr = None
        self.if_role = None
        self.if_type = None
        self.lc = None
        self.lic_gp = None
        self.lic_state = None
        self.locale = None
        self.name = None
        self.oper_state = None
        self.oper_state_reason = None
        self.peer_chassis_id = None
        self.peer_dn = None
        self.peer_port_id = None
        self.peer_slot_id = None
        self.port_id = None
        self.revision = None
        self.slot_id = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "FabricCartridgePhEp", parent_mo_or_dn, **kwargs)

