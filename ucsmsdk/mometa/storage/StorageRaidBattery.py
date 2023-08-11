"""This module contains the general information for StorageRaidBattery ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageRaidBatteryConsts:
    BATTERY_TYPE_BATTERY = "battery"
    BATTERY_TYPE_SUPERCAP = "supercap"
    BATTERY_TYPE_UNKNOWN = "unknown"
    BBU_STATUS_FAILURE_PREDICTED = "failure-predicted"
    BBU_STATUS_LEARN_CYCLE_ACTIVE = "learn-cycle-active"
    BBU_STATUS_LEARN_CYCLE_NEEDED = "learn-cycle-needed"
    BBU_STATUS_MICROCODE_UPDATE_REQD = "microcode-update-reqd"
    BBU_STATUS_NO_FLASH_SPACE = "no-flash-space"
    BBU_STATUS_NOT_PRESENT = "not-present"
    BBU_STATUS_NOT_SUPPORTED = "not-supported"
    BBU_STATUS_OPTIMAL = "optimal"
    BBU_STATUS_PREMIUM_FEATURE_REQD = "premium-feature-reqd"
    BBU_STATUS_REPLACEMENT_NEEDED = "replacement-needed"
    BBU_STATUS_UNKNOWN = "unknown"
    BLOCK_SIZE_512 = "512"
    BLOCK_SIZE_UNKNOWN = "unknown"
    CAPACITY_PERCENTAGE_EMPTY = "empty"
    CAPACITY_PERCENTAGE_FULL = "full"
    CAPACITY_PERCENTAGE_NOT_APPLICABLE = "not-applicable"
    CONNECTION_PROTOCOL_NVME = "NVME"
    CONNECTION_PROTOCOL_SAS = "SAS"
    CONNECTION_PROTOCOL_SATA = "SATA"
    CONNECTION_PROTOCOL_UNSPECIFIED = "unspecified"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    LEARN_CYCLE_REQUESTED_FALSE = "false"
    LEARN_CYCLE_REQUESTED_TRUE = "true"
    LEARN_CYCLE_REQUESTED_UNKNOWN = "unknown"
    LEARN_MODE_AUTO = "auto"
    LEARN_MODE_DISABLED = "disabled"
    LEARN_MODE_UNKNOWN = "unknown"
    LEARN_MODE_WARN = "warn"
    NEXT_LEARN_CYCLE_TS_UNKNOWN = "unknown"
    NUMBER_OF_BLOCKS_UNKNOWN = "unknown"
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
    OPERABILITY_QUALIFIER_UNKNOWN = "unknown"
    PHYSICAL_BLOCK_SIZE_512 = "512"
    PHYSICAL_BLOCK_SIZE_UNKNOWN = "unknown"
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
    SIZE_NOT_APPLICABLE = "not-applicable"
    TEMPERATURE_NOT_APPLICABLE = "not-applicable"


class StorageRaidBattery(ManagedObject):
    """This is StorageRaidBattery class."""

    consts = StorageRaidBatteryConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageRaidBattery", "storageRaidBattery", "raid-battery", VersionMeta.Version131c, "InputOutput", 0x3ff, [], ["read-only"], ['storageController'], ['faultInst', 'storageOperation', 'storageTransportableFlashModule'], ["Get"])

    prop_meta = {
        "battery_type": MoPropertyMeta("battery_type", "batteryType", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["battery", "supercap", "unknown"], []),
        "bbu_status": MoPropertyMeta("bbu_status", "bbuStatus", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failure-predicted", "learn-cycle-active", "learn-cycle-needed", "microcode-update-reqd", "no-flash-space", "not-present", "not-supported", "optimal", "premium-feature-reqd", "replacement-needed", "unknown"], []),
        "block_size": MoPropertyMeta("block_size", "blockSize", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["512", "unknown"], ["0-4294967295"]),
        "capacity_percentage": MoPropertyMeta("capacity_percentage", "capacityPercentage", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["empty", "full", "not-applicable"], ["0-101"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x8, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "connection_protocol": MoPropertyMeta("connection_protocol", "connectionProtocol", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NVME", "SAS", "SATA", "unspecified"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []),
        "learn_cycle_requested": MoPropertyMeta("learn_cycle_requested", "learnCycleRequested", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "true", "unknown"], []),
        "learn_mode": MoPropertyMeta("learn_mode", "learnMode", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["auto", "disabled", "unknown", "warn"], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "next_learn_cycle_ts": MoPropertyMeta("next_learn_cycle_ts", "nextLearnCycleTs", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["unknown"], []),
        "number_of_blocks": MoPropertyMeta("number_of_blocks", "numberOfBlocks", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-18446744073709551615"]),
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "operability_qualifier": MoPropertyMeta("operability_qualifier", "operabilityQualifier", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["unknown"], []),
        "operability_qualifier_reason": MoPropertyMeta("operability_qualifier_reason", "operabilityQualifierReason", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "physical_block_size": MoPropertyMeta("physical_block_size", "physicalBlockSize", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["512", "unknown"], ["0-4294967295"]),
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-disc-error", "equipped-disc-in-progress", "equipped-disc-not-started", "equipped-disc-unknown", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-18446744073709551615"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "temperature": MoPropertyMeta("temperature", "temperature", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "batteryType": "battery_type", 
        "bbuStatus": "bbu_status", 
        "blockSize": "block_size", 
        "capacityPercentage": "capacity_percentage", 
        "childAction": "child_action", 
        "connectionProtocol": "connection_protocol", 
        "dn": "dn", 
        "id": "id", 
        "lc": "lc", 
        "learnCycleRequested": "learn_cycle_requested", 
        "learnMode": "learn_mode", 
        "model": "model", 
        "nextLearnCycleTs": "next_learn_cycle_ts", 
        "numberOfBlocks": "number_of_blocks", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operability": "operability", 
        "operabilityQualifier": "operability_qualifier", 
        "operabilityQualifierReason": "operability_qualifier_reason", 
        "physicalBlockSize": "physical_block_size", 
        "presence": "presence", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "size": "size", 
        "status": "status", 
        "temperature": "temperature", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.battery_type = None
        self.bbu_status = None
        self.block_size = None
        self.capacity_percentage = None
        self.child_action = None
        self.connection_protocol = None
        self.id = None
        self.lc = None
        self.learn_cycle_requested = None
        self.learn_mode = None
        self.model = None
        self.next_learn_cycle_ts = None
        self.number_of_blocks = None
        self.oper_qualifier_reason = None
        self.operability = None
        self.operability_qualifier = None
        self.operability_qualifier_reason = None
        self.physical_block_size = None
        self.presence = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.size = None
        self.status = None
        self.temperature = None
        self.vendor = None

        ManagedObject.__init__(self, "StorageRaidBattery", parent_mo_or_dn, **kwargs)
