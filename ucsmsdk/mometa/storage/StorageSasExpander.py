"""This module contains the general information for StorageSasExpander ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageSasExpanderConsts:
    CONNECTION_MANAGEMENT_DEFAULT = "default"
    CONNECTION_MANAGEMENT_DISABLED = "disabled"
    CONNECTION_MANAGEMENT_ENABLED = "enabled"
    CONNECTION_MANAGEMENT_UNKNOWN = "unknown"
    EXPANDER_STATE_DEGRADED = "degraded"
    EXPANDER_STATE_DISCOVERY = "discovery"
    EXPANDER_STATE_INOPERABLE = "inoperable"
    EXPANDER_STATE_NOT_READY = "not-ready"
    EXPANDER_STATE_OPERABLE = "operable"
    EXPANDER_STATE_REBOOT_PENDING = "reboot-pending"
    EXPANDER_STATE_RESOURCE_UNAVAILABLE = "resource-unavailable"
    EXPANDER_STATE_UNKNOWN = "unknown"
    EXPANDER_STATE_UNREACHABLE = "unreachable"
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
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
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
    TEMPERATURE_NOT_APPLICABLE = "not-applicable"
    THERMAL_LOWER_CRITICAL = "lower-critical"
    THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    THERMAL_NOT_SUPPORTED = "not-supported"
    THERMAL_OK = "ok"
    THERMAL_UNKNOWN = "unknown"
    THERMAL_UPPER_CRITICAL = "upper-critical"
    THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    UPLINK_STATE_MISCONNECT = "misconnect"
    UPLINK_STATE_OPTIMAL = "optimal"
    UPLINK_STATE_SUB_OPTIMAL = "sub-optimal"
    UPLINK_STATE_UNKNOWN = "unknown"
    VOLTAGE_LOWER_CRITICAL = "lower-critical"
    VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
    VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    VOLTAGE_NOT_SUPPORTED = "not-supported"
    VOLTAGE_OK = "ok"
    VOLTAGE_UNKNOWN = "unknown"
    VOLTAGE_UPPER_CRITICAL = "upper-critical"
    VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
    VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"


class StorageSasExpander(ManagedObject):
    """This is StorageSasExpander class."""

    consts = StorageSasExpanderConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("StorageSasExpander", "storageSasExpander", "sas-expander-[id]", VersionMeta.Version226c, "InputOutput", 0x3f, [], ["read-only"], ['computeBoard', 'equipmentChassis'], ['faultInst', 'firmwareBootDefinition', 'firmwareRunning', 'mgmtController', 'storageOnboardDevice', 'storageSasUpLink'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version226c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_check_point": MoPropertyMeta("config_check_point", "configCheckPoint", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|firmware-inventory-reported),){0,2}(defaultValue|unknown|firmware-inventory-reported){0,1}""", [], []),
        "connection_management": MoPropertyMeta("connection_management", "connectionManagement", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["default", "disabled", "enabled", "unknown"], []),
        "current_epfb": MoPropertyMeta("current_epfb", "currentEPFB", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "elid": MoPropertyMeta("elid", "elid", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "expander_state": MoPropertyMeta("expander_state", "expanderState", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "discovery", "inoperable", "not-ready", "operable", "reboot-pending", "resource-unavailable", "unknown", "unreachable"], []),
        "fw_region_one": MoPropertyMeta("fw_region_one", "fwRegionOne", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "fw_region_two": MoPropertyMeta("fw_region_two", "fwRegionTwo", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "fw_running_region": MoPropertyMeta("fw_running_region", "fwRunningRegion", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "hotswap_thermal": MoPropertyMeta("hotswap_thermal", "hotswapThermal", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version226c, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["0-4294967295"]),
        "inlet2_thermal": MoPropertyMeta("inlet2_thermal", "inlet2Thermal", "string", VersionMeta.Version423b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []),
        "location_dn": MoPropertyMeta("location_dn", "locationDn", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "mfg_major_rev": MoPropertyMeta("mfg_major_rev", "mfgMajorRev", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "mfg_minor_rev": MoPropertyMeta("mfg_minor_rev", "mfgMinorRev", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "mfg_platform_id": MoPropertyMeta("mfg_platform_id", "mfgPlatformId", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "outlet_thermal": MoPropertyMeta("outlet_thermal", "outletThermal", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "perf": MoPropertyMeta("perf", "perf", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "persisted_epfb": MoPropertyMeta("persisted_epfb", "persistedEPFB", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "power": MoPropertyMeta("power", "power", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], []),
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-disc-error", "equipped-disc-in-progress", "equipped-disc-not-started", "equipped-disc-unknown", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sas_address": MoPropertyMeta("sas_address", "sasAddress", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "start_slot_num": MoPropertyMeta("start_slot_num", "startSlotNum", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version226c, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "temperature": MoPropertyMeta("temperature", "temperature", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "total_slots": MoPropertyMeta("total_slots", "totalSlots", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "uplink_state": MoPropertyMeta("uplink_state", "uplinkState", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["misconnect", "optimal", "sub-optimal", "unknown"], []),
        "uplink_state_reason": MoPropertyMeta("uplink_state_reason", "uplinkStateReason", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "voltage": MoPropertyMeta("voltage", "voltage", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configCheckPoint": "config_check_point", 
        "connectionManagement": "connection_management", 
        "currentEPFB": "current_epfb", 
        "dn": "dn", 
        "elid": "elid", 
        "expanderState": "expander_state", 
        "fwRegionOne": "fw_region_one", 
        "fwRegionTwo": "fw_region_two", 
        "fwRunningRegion": "fw_running_region", 
        "hotswapThermal": "hotswap_thermal", 
        "id": "id", 
        "inlet2Thermal": "inlet2_thermal", 
        "lc": "lc", 
        "locationDn": "location_dn", 
        "mfgMajorRev": "mfg_major_rev", 
        "mfgMinorRev": "mfg_minor_rev", 
        "mfgPlatformId": "mfg_platform_id", 
        "model": "model", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "outletThermal": "outlet_thermal", 
        "perf": "perf", 
        "persistedEPFB": "persisted_epfb", 
        "power": "power", 
        "presence": "presence", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sasAddress": "sas_address", 
        "serial": "serial", 
        "startSlotNum": "start_slot_num", 
        "status": "status", 
        "temperature": "temperature", 
        "thermal": "thermal", 
        "totalSlots": "total_slots", 
        "uplinkState": "uplink_state", 
        "uplinkStateReason": "uplink_state_reason", 
        "vendor": "vendor", 
        "voltage": "voltage", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.config_check_point = None
        self.connection_management = None
        self.current_epfb = None
        self.elid = None
        self.expander_state = None
        self.fw_region_one = None
        self.fw_region_two = None
        self.fw_running_region = None
        self.hotswap_thermal = None
        self.inlet2_thermal = None
        self.lc = None
        self.location_dn = None
        self.mfg_major_rev = None
        self.mfg_minor_rev = None
        self.mfg_platform_id = None
        self.model = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.outlet_thermal = None
        self.perf = None
        self.persisted_epfb = None
        self.power = None
        self.presence = None
        self.revision = None
        self.sacl = None
        self.sas_address = None
        self.serial = None
        self.start_slot_num = None
        self.status = None
        self.temperature = None
        self.thermal = None
        self.total_slots = None
        self.uplink_state = None
        self.uplink_state_reason = None
        self.vendor = None
        self.voltage = None

        ManagedObject.__init__(self, "StorageSasExpander", parent_mo_or_dn, **kwargs)
