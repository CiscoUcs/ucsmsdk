"""This module contains the general information for ComputeExtBoard ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeExtBoardConsts:
    BOARD_AGGREGATION_ROLE_MULTI_MASTER = "multi-master"
    BOARD_AGGREGATION_ROLE_MULTI_SLAVE = "multi-slave"
    BOARD_AGGREGATION_ROLE_NONE = "none"
    BOARD_AGGREGATION_ROLE_SINGLE = "single"
    CMOS_VOLTAGE_LOWER_CRITICAL = "lower-critical"
    CMOS_VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
    CMOS_VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    CMOS_VOLTAGE_NOT_SUPPORTED = "not-supported"
    CMOS_VOLTAGE_OK = "ok"
    CMOS_VOLTAGE_UNKNOWN = "unknown"
    CMOS_VOLTAGE_UPPER_CRITICAL = "upper-critical"
    CMOS_VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
    CMOS_VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    HOTSWAP_THERMAL_LOWER_CRITICAL = "lower-critical"
    HOTSWAP_THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    HOTSWAP_THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    HOTSWAP_THERMAL_NOT_SUPPORTED = "not-supported"
    HOTSWAP_THERMAL_OK = "ok"
    HOTSWAP_THERMAL_UNKNOWN = "unknown"
    HOTSWAP_THERMAL_UPPER_CRITICAL = "upper-critical"
    HOTSWAP_THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    HOTSWAP_THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    INLET2_THERMAL_LOWER_CRITICAL = "lower-critical"
    INLET2_THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    INLET2_THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    INLET2_THERMAL_NOT_SUPPORTED = "not-supported"
    INLET2_THERMAL_OK = "ok"
    INLET2_THERMAL_UNKNOWN = "unknown"
    INLET2_THERMAL_UPPER_CRITICAL = "upper-critical"
    INLET2_THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    INLET2_THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    MANAGING_INST_A = "A"
    MANAGING_INST_B = "B"
    MANAGING_INST_NONE = "NONE"
    OPER_POWER_DEGRADED = "degraded"
    OPER_POWER_ERROR = "error"
    OPER_POWER_FAILED = "failed"
    OPER_POWER_NOT_SUPPORTED = "not-supported"
    OPER_POWER_OFF = "off"
    OPER_POWER_OFFDUTY = "offduty"
    OPER_POWER_OFFLINE = "offline"
    OPER_POWER_OK = "ok"
    OPER_POWER_ON = "on"
    OPER_POWER_ONLINE = "online"
    OPER_POWER_POWER_SAVE = "power-save"
    OPER_POWER_TEST = "test"
    OPER_POWER_UNKNOWN = "unknown"
    OPER_STATE_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPER_STATE_AUTO_UPGRADE = "auto-upgrade"
    OPER_STATE_BACKPLANE_PORT_PROBLEM = "backplane-port-problem"
    OPER_STATE_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPER_STATE_CHASSIS_INTRUSION = "chassis-intrusion"
    OPER_STATE_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPER_STATE_CONFIG = "config"
    OPER_STATE_DECOMISSIONING = "decomissioning"
    OPER_STATE_DEGRADED = "degraded"
    OPER_STATE_DIMM_DISABLED = "dimm-disabled"
    OPER_STATE_DISABLED = "disabled"
    OPER_STATE_DISCOVERY = "discovery"
    OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    OPER_STATE_EQUIPMENT_PROBLEM = "equipment-problem"
    OPER_STATE_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    OPER_STATE_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    OPER_STATE_IDENTIFY = "identify"
    OPER_STATE_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    OPER_STATE_INOPERABLE = "inoperable"
    OPER_STATE_LINK_ACTIVATE_BLOCKED = "link-activate-blocked"
    OPER_STATE_MALFORMED_FRU = "malformed-fru"
    OPER_STATE_NON_OPTIMAL = "non-optimal"
    OPER_STATE_NON_OPTIMAL_SEVERE = "non-optimal-severe"
    OPER_STATE_NOT_SUPPORTED = "not-supported"
    OPER_STATE_OPERABLE = "operable"
    OPER_STATE_PEER_COMM_PROBLEM = "peer-comm-problem"
    OPER_STATE_PEER_DIMM_DISABLED = "peer-dimm-disabled"
    OPER_STATE_PERFORMANCE_PROBLEM = "performance-problem"
    OPER_STATE_POST_FAILURE = "post-failure"
    OPER_STATE_POWER_PROBLEM = "power-problem"
    OPER_STATE_POWERED_OFF = "powered-off"
    OPER_STATE_REMOVED = "removed"
    OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    OPER_STATE_UNKNOWN = "unknown"
    OPER_STATE_UNSUPPORTED_CONFIG = "unsupported-config"
    OPER_STATE_UPGRADE_PROBLEM = "upgrade-problem"
    OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
    OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
    OPERABILITY_BACKPLANE_PORT_PROBLEM = "backplane-port-problem"
    OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPERABILITY_CHASSIS_INTRUSION = "chassis-intrusion"
    OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPERABILITY_CONFIG = "config"
    OPERABILITY_DECOMISSIONING = "decomissioning"
    OPERABILITY_DEGRADED = "degraded"
    OPERABILITY_DIMM_DISABLED = "dimm-disabled"
    OPERABILITY_DISABLED = "disabled"
    OPERABILITY_DISCOVERY = "discovery"
    OPERABILITY_DISCOVERY_FAILED = "discovery-failed"
    OPERABILITY_EQUIPMENT_PROBLEM = "equipment-problem"
    OPERABILITY_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    OPERABILITY_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    OPERABILITY_IDENTIFY = "identify"
    OPERABILITY_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    OPERABILITY_INOPERABLE = "inoperable"
    OPERABILITY_LINK_ACTIVATE_BLOCKED = "link-activate-blocked"
    OPERABILITY_MALFORMED_FRU = "malformed-fru"
    OPERABILITY_NON_OPTIMAL = "non-optimal"
    OPERABILITY_NON_OPTIMAL_SEVERE = "non-optimal-severe"
    OPERABILITY_NOT_SUPPORTED = "not-supported"
    OPERABILITY_OPERABLE = "operable"
    OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
    OPERABILITY_PEER_DIMM_DISABLED = "peer-dimm-disabled"
    OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
    OPERABILITY_POST_FAILURE = "post-failure"
    OPERABILITY_POWER_PROBLEM = "power-problem"
    OPERABILITY_POWERED_OFF = "powered-off"
    OPERABILITY_REMOVED = "removed"
    OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
    OPERABILITY_UNKNOWN = "unknown"
    OPERABILITY_UNSUPPORTED_CONFIG = "unsupported-config"
    OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
    OUTLET_THERMAL_LOWER_CRITICAL = "lower-critical"
    OUTLET_THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    OUTLET_THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    OUTLET_THERMAL_NOT_SUPPORTED = "not-supported"
    OUTLET_THERMAL_OK = "ok"
    OUTLET_THERMAL_UNKNOWN = "unknown"
    OUTLET_THERMAL_UPPER_CRITICAL = "upper-critical"
    OUTLET_THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    OUTLET_THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    PERF_LOWER_CRITICAL = "lower-critical"
    PERF_LOWER_NON_CRITICAL = "lower-non-critical"
    PERF_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    PERF_NOT_SUPPORTED = "not-supported"
    PERF_OK = "ok"
    PERF_UNKNOWN = "unknown"
    PERF_UPPER_CRITICAL = "upper-critical"
    PERF_UPPER_NON_CRITICAL = "upper-non-critical"
    PERF_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    POWER_DEGRADED = "degraded"
    POWER_ERROR = "error"
    POWER_FAILED = "failed"
    POWER_NOT_SUPPORTED = "not-supported"
    POWER_OFF = "off"
    POWER_OFFDUTY = "offduty"
    POWER_OFFLINE = "offline"
    POWER_OK = "ok"
    POWER_ON = "on"
    POWER_ONLINE = "online"
    POWER_POWER_SAVE = "power-save"
    POWER_TEST = "test"
    POWER_UNKNOWN = "unknown"
    POWER_USAGE_LOWER_CRITICAL = "lower-critical"
    POWER_USAGE_LOWER_NON_CRITICAL = "lower-non-critical"
    POWER_USAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    POWER_USAGE_NOT_SUPPORTED = "not-supported"
    POWER_USAGE_OK = "ok"
    POWER_USAGE_UNKNOWN = "unknown"
    POWER_USAGE_UPPER_CRITICAL = "upper-critical"
    POWER_USAGE_UPPER_NON_CRITICAL = "upper-non-critical"
    POWER_USAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
    PRESENCE_EQUIPPED_DEPRECATED = "equipped-deprecated"
    PRESENCE_EQUIPPED_DISC_ERROR = "equipped-disc-error"
    PRESENCE_EQUIPPED_DISC_IN_PROGRESS = "equipped-disc-in-progress"
    PRESENCE_EQUIPPED_DISC_NOT_STARTED = "equipped-disc-not-started"
    PRESENCE_EQUIPPED_DISC_UNKNOWN = "equipped-disc-unknown"
    PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    PRESENCE_EQUIPPED_SLAVE = "equipped-slave"
    PRESENCE_EQUIPPED_UNSUPPORTED = "equipped-unsupported"
    PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    PRESENCE_INACCESSIBLE = "inaccessible"
    PRESENCE_MISMATCH = "mismatch"
    PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    PRESENCE_MISMATCH_SLAVE = "mismatch-slave"
    PRESENCE_MISSING = "missing"
    PRESENCE_MISSING_SLAVE = "missing-slave"
    PRESENCE_NOT_SUPPORTED = "not-supported"
    PRESENCE_UNAUTHORIZED = "unauthorized"
    PRESENCE_UNKNOWN = "unknown"
    THERMAL_LOWER_CRITICAL = "lower-critical"
    THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    THERMAL_NOT_SUPPORTED = "not-supported"
    THERMAL_OK = "ok"
    THERMAL_UNKNOWN = "unknown"
    THERMAL_UPPER_CRITICAL = "upper-critical"
    THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    VOLTAGE_LOWER_CRITICAL = "lower-critical"
    VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
    VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    VOLTAGE_NOT_SUPPORTED = "not-supported"
    VOLTAGE_OK = "ok"
    VOLTAGE_UNKNOWN = "unknown"
    VOLTAGE_UPPER_CRITICAL = "upper-critical"
    VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
    VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"


class ComputeExtBoard(ManagedObject):
    """This is ComputeExtBoard class."""

    consts = ComputeExtBoardConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ComputeExtBoard", "computeExtBoard", "ext-board-[id]", VersionMeta.Version222c, "InputOutput", 0x3f, [], ["read-only"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], ['biosUnit', 'computeBoardController', 'computeMbPowerStats', 'computeMbTempStats', 'equipmentHealthLed', 'equipmentLocatorLed', 'faultInst', 'mgmtController', 'powerBudget'], ["Get"])

    prop_meta = {
        "board_aggregation_role": MoPropertyMeta("board_aggregation_role", "boardAggregationRole", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["multi-master", "multi-slave", "none", "single"], []),
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "uint", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cmos_voltage": MoPropertyMeta("cmos_voltage", "cmosVoltage", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "conn_path": MoPropertyMeta("conn_path", "connPath", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []),
        "conn_status": MoPropertyMeta("conn_status", "connStatus", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []),
        "discovery_status": MoPropertyMeta("discovery_status", "discoveryStatus", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "fault_qualifier": MoPropertyMeta("fault_qualifier", "faultQualifier", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "hotswap_thermal": MoPropertyMeta("hotswap_thermal", "hotswapThermal", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version222c, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "inlet2_thermal": MoPropertyMeta("inlet2_thermal", "inlet2Thermal", "string", VersionMeta.Version423b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "location_dn": MoPropertyMeta("location_dn", "locationDn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "managing_inst": MoPropertyMeta("managing_inst", "managingInst", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "oper_power": MoPropertyMeta("oper_power", "operPower", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], []),
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "outlet_thermal": MoPropertyMeta("outlet_thermal", "outletThermal", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "perf": MoPropertyMeta("perf", "perf", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "power": MoPropertyMeta("power", "power", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], []),
        "power_usage": MoPropertyMeta("power_usage", "powerUsage", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-disc-error", "equipped-disc-in-progress", "equipped-disc-not-started", "equipped-disc-unknown", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "voltage": MoPropertyMeta("voltage", "voltage", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
    }

    prop_map = {
        "boardAggregationRole": "board_aggregation_role", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "cmosVoltage": "cmos_voltage", 
        "connPath": "conn_path", 
        "connStatus": "conn_status", 
        "discoveryStatus": "discovery_status", 
        "dn": "dn", 
        "faultQualifier": "fault_qualifier", 
        "hotswapThermal": "hotswap_thermal", 
        "id": "id", 
        "inlet2Thermal": "inlet2_thermal", 
        "locationDn": "location_dn", 
        "managingInst": "managing_inst", 
        "model": "model", 
        "operPower": "oper_power", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "outletThermal": "outlet_thermal", 
        "perf": "perf", 
        "power": "power", 
        "powerUsage": "power_usage", 
        "presence": "presence", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "slotId": "slot_id", 
        "status": "status", 
        "thermal": "thermal", 
        "vendor": "vendor", 
        "voltage": "voltage", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.board_aggregation_role = None
        self.chassis_id = None
        self.child_action = None
        self.cmos_voltage = None
        self.conn_path = None
        self.conn_status = None
        self.discovery_status = None
        self.fault_qualifier = None
        self.hotswap_thermal = None
        self.inlet2_thermal = None
        self.location_dn = None
        self.managing_inst = None
        self.model = None
        self.oper_power = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.outlet_thermal = None
        self.perf = None
        self.power = None
        self.power_usage = None
        self.presence = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.slot_id = None
        self.status = None
        self.thermal = None
        self.vendor = None
        self.voltage = None

        ManagedObject.__init__(self, "ComputeExtBoard", parent_mo_or_dn, **kwargs)
