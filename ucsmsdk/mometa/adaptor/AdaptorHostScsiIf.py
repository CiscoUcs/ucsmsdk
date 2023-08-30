"""This module contains the general information for AdaptorHostScsiIf ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorHostScsiIfConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_DISABLED_ACTIVE = "disabled-active"
    ADMIN_STATE_DISABLED_PASSIVE = "disabled-passive"
    ADMIN_STATE_ENABLED = "enabled"
    ADMIN_STATE_ENABLED_ACTIVE = "enabled-active"
    ADMIN_STATE_ENABLED_PASSIVE = "enabled-passive"
    ADMIN_STATE_RESET_CONNECTIVITY = "reset-connectivity"
    ADMIN_STATE_RESET_CONNECTIVITY_ACTIVE = "reset-connectivity-active"
    ADMIN_STATE_RESET_CONNECTIVITY_PASSIVE = "reset-connectivity-passive"
    BOOT_DEV_DISABLED = "disabled"
    BOOT_DEV_ENABLED = "enabled"
    CHASSIS_ID_N_A = "N/A"
    DISCOVERY_ABSENT = "absent"
    DISCOVERY_INIT = "init"
    DISCOVERY_MIS_CONNECT = "mis-connect"
    DISCOVERY_MISSING = "missing"
    DISCOVERY_NEW = "new"
    DISCOVERY_PRESENT = "present"
    DISCOVERY_UN_INITIALIZED = "un-initialized"
    DISCOVERY_UN_SUPPORTED = "un-supported"
    HOTSWAP_THERMAL_LOWER_CRITICAL = "lower-critical"
    HOTSWAP_THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    HOTSWAP_THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    HOTSWAP_THERMAL_NOT_SUPPORTED = "not-supported"
    HOTSWAP_THERMAL_OK = "ok"
    HOTSWAP_THERMAL_UNKNOWN = "unknown"
    HOTSWAP_THERMAL_UPPER_CRITICAL = "upper-critical"
    HOTSWAP_THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    HOTSWAP_THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
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
    LINK_STATE_ADMIN_DOWN = "admin-down"
    LINK_STATE_DOWN = "down"
    LINK_STATE_ERROR = "error"
    LINK_STATE_OFFLINE = "offline"
    LINK_STATE_UNALLOCATED = "unallocated"
    LINK_STATE_UNAVAILABLE = "unavailable"
    LINK_STATE_UNKNOWN = "unknown"
    LINK_STATE_UP = "up"
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
    ORDER_UNSPECIFIED = "unspecified"
    OUTLET_THERMAL_LOWER_CRITICAL = "lower-critical"
    OUTLET_THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    OUTLET_THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    OUTLET_THERMAL_NOT_SUPPORTED = "not-supported"
    OUTLET_THERMAL_OK = "ok"
    OUTLET_THERMAL_UNKNOWN = "unknown"
    OUTLET_THERMAL_UPPER_CRITICAL = "upper-critical"
    OUTLET_THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    OUTLET_THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    PEER_CHASSIS_ID_N_A = "N/A"
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
    PURPOSE_CROSSLINK = "crosslink"
    PURPOSE_GENERAL = "general"
    PURPOSE_MANAGEMENT = "management"
    PURPOSE_OVERLAY = "overlay"
    PURPOSE_UNUSED = "unused"
    PURPOSE_UTILITY = "utility"
    SIDE_LEFT = "left"
    SIDE_RIGHT = "right"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
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


class AdaptorHostScsiIf(ManagedObject):
    """This is AdaptorHostScsiIf class."""

    consts = AdaptorHostScsiIfConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorHostScsiIf", "adaptorHostScsiIf", "host-scsi-[id]", VersionMeta.Version251a, "InputOutput", 0x1ff, [], ["admin", "ext-lan-config", "ext-lan-policy", "pn-equipment", "pn-maintenance", "read-only"], ['adaptorUnit'], ['adaptorHostScsiLunRef', 'adaptorVnicStats', 'faultInst', 'networkIfStats'], ["Get"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "disabled-active", "disabled-passive", "enabled", "enabled-active", "enabled-passive", "reset-connectivity", "reset-connectivity-active", "reset-connectivity-passive"], []),
        "boot_dev": MoPropertyMeta("boot_dev", "bootDev", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["disabled", "enabled"], []),
        "cdn_name": MoPropertyMeta("cdn_name", "cdnName", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, 0x8, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "discovery": MoPropertyMeta("discovery", "discovery", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["absent", "init", "mis-connect", "missing", "new", "present", "un-initialized", "un-supported"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "hotswap_thermal": MoPropertyMeta("hotswap_thermal", "hotswapThermal", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []),
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
        "inlet2_thermal": MoPropertyMeta("inlet2_thermal", "inlet2Thermal", "string", VersionMeta.Version423b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []),
        "link_state": MoPropertyMeta("link_state", "linkState", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["admin-down", "down", "error", "offline", "unallocated", "unavailable", "unknown", "up"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["unspecified"], ["0-65535"]),
        "outlet_thermal": MoPropertyMeta("outlet_thermal", "outletThermal", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "pci_addr": MoPropertyMeta("pci_addr", "pciAddr", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "pci_func": MoPropertyMeta("pci_func", "pciFunc", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "peer_chassis_id": MoPropertyMeta("peer_chassis_id", "peerChassisId", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "peer_port_id": MoPropertyMeta("peer_port_id", "peerPortId", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "peer_slot_id": MoPropertyMeta("peer_slot_id", "peerSlotId", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "perf": MoPropertyMeta("perf", "perf", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "power": MoPropertyMeta("power", "power", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], []),
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-disc-error", "equipped-disc-in-progress", "equipped-disc-not-started", "equipped-disc-unknown", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []),
        "purpose": MoPropertyMeta("purpose", "purpose", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["crosslink", "general", "management", "overlay", "unused", "utility"], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "side": MoPropertyMeta("side", "side", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["left", "right"], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "vnic_dn": MoPropertyMeta("vnic_dn", "vnicDn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "voltage": MoPropertyMeta("voltage", "voltage", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "bootDev": "boot_dev", 
        "cdnName": "cdn_name", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "discovery": "discovery", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "fltAggr": "flt_aggr", 
        "hotswapThermal": "hotswap_thermal", 
        "id": "id", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "inlet2Thermal": "inlet2_thermal", 
        "lc": "lc", 
        "linkState": "link_state", 
        "locale": "locale", 
        "model": "model", 
        "name": "name", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "order": "order", 
        "outletThermal": "outlet_thermal", 
        "pciAddr": "pci_addr", 
        "pciFunc": "pci_func", 
        "pciSlot": "pci_slot", 
        "peerChassisId": "peer_chassis_id", 
        "peerDn": "peer_dn", 
        "peerPortId": "peer_port_id", 
        "peerSlotId": "peer_slot_id", 
        "perf": "perf", 
        "portId": "port_id", 
        "power": "power", 
        "presence": "presence", 
        "purpose": "purpose", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "side": "side", 
        "slotId": "slot_id", 
        "status": "status", 
        "switchId": "switch_id", 
        "thermal": "thermal", 
        "transport": "transport", 
        "type": "type", 
        "vendor": "vendor", 
        "vnicDn": "vnic_dn", 
        "voltage": "voltage", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_state = None
        self.boot_dev = None
        self.cdn_name = None
        self.chassis_id = None
        self.child_action = None
        self.discovery = None
        self.ep_dn = None
        self.flt_aggr = None
        self.hotswap_thermal = None
        self.if_role = None
        self.if_type = None
        self.inlet2_thermal = None
        self.lc = None
        self.link_state = None
        self.locale = None
        self.model = None
        self.name = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.order = None
        self.outlet_thermal = None
        self.pci_addr = None
        self.pci_func = None
        self.pci_slot = None
        self.peer_chassis_id = None
        self.peer_dn = None
        self.peer_port_id = None
        self.peer_slot_id = None
        self.perf = None
        self.port_id = None
        self.power = None
        self.presence = None
        self.purpose = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.side = None
        self.slot_id = None
        self.status = None
        self.switch_id = None
        self.thermal = None
        self.transport = None
        self.type = None
        self.vendor = None
        self.vnic_dn = None
        self.voltage = None

        ManagedObject.__init__(self, "AdaptorHostScsiIf", parent_mo_or_dn, **kwargs)
