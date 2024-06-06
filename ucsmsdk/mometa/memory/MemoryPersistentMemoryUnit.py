"""This module contains the general information for MemoryPersistentMemoryUnit ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MemoryPersistentMemoryUnitConsts:
    ADMIN_STATE_POLICY = "policy"
    ADMIN_STATE_RESET_ERRORS = "reset-errors"
    CAPACITY_UNSPECIFIED = "unspecified"
    CLOCK_UNSPECIFIED = "unspecified"
    FORM_FACTOR_DIMM = "DIMM"
    FORM_FACTOR_FB_DIMM = "FB-DIMM"
    FORM_FACTOR_OTHER = "Other"
    FORM_FACTOR_RIMM = "RIMM"
    FORM_FACTOR_SIMM = "SIMM"
    FORM_FACTOR_SODIMM = "SODIMM"
    FORM_FACTOR_SRIMM = "SRIMM"
    FORM_FACTOR_TSOP = "TSOP"
    FORM_FACTOR_UNKNOWN = "Unknown"
    FORM_FACTOR_UNDISCOVERED = "undiscovered"
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
    LATENCY_UNSPECIFIED = "unspecified"
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
    SELECTED_FALSE = "false"
    SELECTED_NO = "no"
    SELECTED_TRUE = "true"
    SELECTED_YES = "yes"
    SOCKET_ID_SOCKET_1 = "socket-1"
    SOCKET_ID_SOCKET_2 = "socket-2"
    SOCKET_ID_SOCKET_3 = "socket-3"
    SOCKET_ID_SOCKET_4 = "socket-4"
    SOCKET_LOCAL_DIMM_NUMBER_10 = "10"
    SOCKET_LOCAL_DIMM_NUMBER_11 = "11"
    SOCKET_LOCAL_DIMM_NUMBER_12 = "12"
    SOCKET_LOCAL_DIMM_NUMBER_14 = "14"
    SOCKET_LOCAL_DIMM_NUMBER_15 = "15"
    SOCKET_LOCAL_DIMM_NUMBER_16 = "16"
    SOCKET_LOCAL_DIMM_NUMBER_2 = "2"
    SOCKET_LOCAL_DIMM_NUMBER_3 = "3"
    SOCKET_LOCAL_DIMM_NUMBER_4 = "4"
    SOCKET_LOCAL_DIMM_NUMBER_6 = "6"
    SOCKET_LOCAL_DIMM_NUMBER_7 = "7"
    SOCKET_LOCAL_DIMM_NUMBER_8 = "8"
    SOCKET_LOCAL_DIMM_NUMBER_NOT_APPLICABLE = "not-applicable"
    SPEED_UNSPECIFIED = "unspecified"
    THERMAL_LOWER_CRITICAL = "lower-critical"
    THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    THERMAL_NOT_SUPPORTED = "not-supported"
    THERMAL_OK = "ok"
    THERMAL_UNKNOWN = "unknown"
    THERMAL_UPPER_CRITICAL = "upper-critical"
    THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    TYPE_3_DRAM = "3DRAM"
    TYPE_CDRAM = "CDRAM"
    TYPE_DDR = "DDR"
    TYPE_DDR2 = "DDR2"
    TYPE_DDR2_FB_DIMM = "DDR2 FB-DIMM"
    TYPE_DDR3 = "DDR3"
    TYPE_DDR4 = "DDR4"
    TYPE_DDR5 = "DDR5"
    TYPE_DRAM = "DRAM"
    TYPE_EDRAM = "EDRAM"
    TYPE_EEPROM = "EEPROM"
    TYPE_EPROM = "EPROM"
    TYPE_FBD2 = "FBD2"
    TYPE_FEPROM = "FEPROM"
    TYPE_FLASH = "FLASH"
    TYPE_LOGICAL_NON_VOLATILE_DEVICE = "Logical non-volatile device"
    TYPE_OTHER = "Other"
    TYPE_RAM = "RAM"
    TYPE_RDRAM = "RDRAM"
    TYPE_ROM = "ROM"
    TYPE_SDRAM = "SDRAM"
    TYPE_SGRAM = "SGRAM"
    TYPE_SRAM = "SRAM"
    TYPE_UNKNOWN = "Unknown"
    TYPE_VRAM = "VRAM"
    TYPE_UNDISCOVERED = "undiscovered"
    VISIBILITY_NO = "no"
    VISIBILITY_UNKNOWN = "unknown"
    VISIBILITY_YES = "yes"
    VOLTAGE_LOWER_CRITICAL = "lower-critical"
    VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
    VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    VOLTAGE_NOT_SUPPORTED = "not-supported"
    VOLTAGE_OK = "ok"
    VOLTAGE_UNKNOWN = "unknown"
    VOLTAGE_UPPER_CRITICAL = "upper-critical"
    VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
    VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    WIDTH_UNSPECIFIED = "unspecified"


class MemoryPersistentMemoryUnit(ManagedObject):
    """This is MemoryPersistentMemoryUnit class."""

    consts = MemoryPersistentMemoryUnitConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("MemoryPersistentMemoryUnit", "memoryPersistentMemoryUnit", "pmemory-[id]", VersionMeta.Version404a, "InputOutput", 0xff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['memoryArray'], ['faultInst', 'firmwareBootDefinition', 'firmwareRunning', 'memoryErrorStats', 'memoryUnitEnvStats'], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["policy", "reset-errors"], []),
        "app_direct_capacity": MoPropertyMeta("app_direct_capacity", "appDirectCapacity", "long", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([0-9]{1,15})$""", [], []),
        "array": MoPropertyMeta("array", "array", "ushort", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "bank": MoPropertyMeta("bank", "bank", "ushort", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "capacity": MoPropertyMeta("capacity", "capacity", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "clock": MoPropertyMeta("clock", "clock", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-65535"]),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "firmware_version": MoPropertyMeta("firmware_version", "firmwareVersion", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "form_factor": MoPropertyMeta("form_factor", "formFactor", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["DIMM", "FB-DIMM", "Other", "RIMM", "SIMM", "SODIMM", "SRIMM", "TSOP", "Unknown", "undiscovered"], []),
        "health_state": MoPropertyMeta("health_state", "healthState", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "hotswap_thermal": MoPropertyMeta("hotswap_thermal", "hotswapThermal", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version404a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-256"]),
        "inlet2_thermal": MoPropertyMeta("inlet2_thermal", "inlet2Thermal", "string", VersionMeta.Version423b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "latency": MoPropertyMeta("latency", "latency", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["unspecified"], ["0-4294967295"]),
        "location": MoPropertyMeta("location", "location", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "location_dn": MoPropertyMeta("location_dn", "locationDn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "memory_capacity": MoPropertyMeta("memory_capacity", "memoryCapacity", "long", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([0-9]{1,15})$""", [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "model_with_mpn": MoPropertyMeta("model_with_mpn", "modelWithMpn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "oper_qualifier": MoPropertyMeta("oper_qualifier", "operQualifier", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|uncorrectable-ecc-error|correctable-ecc-error|address-parity-error|memory-mismatch-error|dram-correctable-crc-error|dram-uncorrectable-crc-error|address-parity-error-correctable|address-parity-error-uncorrectable),){0,9}(defaultValue|none|uncorrectable-ecc-error|correctable-ecc-error|address-parity-error|memory-mismatch-error|dram-correctable-crc-error|dram-uncorrectable-crc-error|address-parity-error-correctable|address-parity-error-uncorrectable){0,1}""", [], []),
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "outlet_thermal": MoPropertyMeta("outlet_thermal", "outletThermal", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "perf": MoPropertyMeta("perf", "perf", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "persistent_memory_capacity": MoPropertyMeta("persistent_memory_capacity", "persistentMemoryCapacity", "long", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([0-9]{1,15})$""", [], []),
        "power": MoPropertyMeta("power", "power", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], []),
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-disc-error", "equipped-disc-in-progress", "equipped-disc-not-started", "equipped-disc-unknown", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []),
        "reserved_capacity": MoPropertyMeta("reserved_capacity", "reservedCapacity", "long", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([0-9]{1,15})$""", [], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "security_status": MoPropertyMeta("security_status", "securityStatus", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "selected": MoPropertyMeta("selected", "selected", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["false", "no", "true", "yes"], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "set": MoPropertyMeta("set", "set", "byte", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["socket-1", "socket-2", "socket-3", "socket-4"], []),
        "socket_local_dimm_number": MoPropertyMeta("socket_local_dimm_number", "socketLocalDimmNumber", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["10", "11", "12", "14", "15", "16", "2", "3", "4", "6", "7", "8", "not-applicable"], []),
        "speed": MoPropertyMeta("speed", "speed", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-65535"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "total_capacity": MoPropertyMeta("total_capacity", "totalCapacity", "long", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([0-9]{1,15})$""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["3DRAM", "CDRAM", "DDR", "DDR2", "DDR2 FB-DIMM", "DDR3", "DDR4", "DDR5", "DRAM", "EDRAM", "EEPROM", "EPROM", "FBD2", "FEPROM", "FLASH", "Logical non-volatile device", "Other", "RAM", "RDRAM", "ROM", "SDRAM", "SGRAM", "SRAM", "Unknown", "VRAM", "undiscovered"], []),
        "uid": MoPropertyMeta("uid", "uid", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "visibility": MoPropertyMeta("visibility", "visibility", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "unknown", "yes"], []),
        "voltage": MoPropertyMeta("voltage", "voltage", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "width": MoPropertyMeta("width", "width", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-65535"]),
    }

    prop_map = {
        "adminState": "admin_state", 
        "appDirectCapacity": "app_direct_capacity", 
        "array": "array", 
        "bank": "bank", 
        "capacity": "capacity", 
        "childAction": "child_action", 
        "clock": "clock", 
        "dn": "dn", 
        "firmwareVersion": "firmware_version", 
        "formFactor": "form_factor", 
        "healthState": "health_state", 
        "hotswapThermal": "hotswap_thermal", 
        "id": "id", 
        "inlet2Thermal": "inlet2_thermal", 
        "latency": "latency", 
        "location": "location", 
        "locationDn": "location_dn", 
        "memoryCapacity": "memory_capacity", 
        "model": "model", 
        "modelWithMpn": "model_with_mpn", 
        "operQualifier": "oper_qualifier", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "outletThermal": "outlet_thermal", 
        "perf": "perf", 
        "persistentMemoryCapacity": "persistent_memory_capacity", 
        "power": "power", 
        "presence": "presence", 
        "reservedCapacity": "reserved_capacity", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "securityStatus": "security_status", 
        "selected": "selected", 
        "serial": "serial", 
        "set": "set", 
        "socketId": "socket_id", 
        "socketLocalDimmNumber": "socket_local_dimm_number", 
        "speed": "speed", 
        "status": "status", 
        "thermal": "thermal", 
        "totalCapacity": "total_capacity", 
        "type": "type", 
        "uid": "uid", 
        "vendor": "vendor", 
        "visibility": "visibility", 
        "voltage": "voltage", 
        "width": "width", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_state = None
        self.app_direct_capacity = None
        self.array = None
        self.bank = None
        self.capacity = None
        self.child_action = None
        self.clock = None
        self.firmware_version = None
        self.form_factor = None
        self.health_state = None
        self.hotswap_thermal = None
        self.inlet2_thermal = None
        self.latency = None
        self.location = None
        self.location_dn = None
        self.memory_capacity = None
        self.model = None
        self.model_with_mpn = None
        self.oper_qualifier = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.outlet_thermal = None
        self.perf = None
        self.persistent_memory_capacity = None
        self.power = None
        self.presence = None
        self.reserved_capacity = None
        self.revision = None
        self.sacl = None
        self.security_status = None
        self.selected = None
        self.serial = None
        self.set = None
        self.socket_id = None
        self.socket_local_dimm_number = None
        self.speed = None
        self.status = None
        self.thermal = None
        self.total_capacity = None
        self.type = None
        self.uid = None
        self.vendor = None
        self.visibility = None
        self.voltage = None
        self.width = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryUnit", parent_mo_or_dn, **kwargs)
