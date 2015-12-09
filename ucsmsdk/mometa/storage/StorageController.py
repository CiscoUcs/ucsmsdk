"""This module contains the general information for StorageController ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageControllerConsts():
    ADMIN_ACTION_CLEAR_FOREIGN_CONFIGURATION = "clear-foreign-configuration"
    ADMIN_ACTION_IMPORT_FOREIGN_CONFIGURATION = "import-foreign-configuration"
    ADMIN_ACTION_UNPIN_CACHE_ALL = "unpin-cache-all"
    ADMIN_ACTION_UNSPECIFIED = "unspecified"
    ADMIN_ACTION_TRIGGER_CANCELED = "canceled"
    ADMIN_ACTION_TRIGGER_IDLE = "idle"
    ADMIN_ACTION_TRIGGER_TRIGGERED = "triggered"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLY_FAILED = "apply-failed"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_NOT_IN_USE = "not-in-use"
    CONFIG_STATE_ORPHANED = "orphaned"
    CONTROLLER_STATUS_FAILED = "failed"
    CONTROLLER_STATUS_OPTIMAL = "optimal"
    CONTROLLER_STATUS_UNKNOWN = "unknown"
    CONTROLLER_STATUS_UNRESPONSIVE = "unresponsive"
    FAULT_MONITORING_NOT_SUPPORTED = "notSupported"
    FAULT_MONITORING_SUPPORTED = "supported"
    ID_COUNT_MIN = "min"
    ID_COUNT_UNKNOWN = "unknown"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    OOB_CONTROLLER_ID_NOT_APPLICABLE = "not-applicable"
    OOB_INTERFACE_SUPPORTED_FALSE = "false"
    OOB_INTERFACE_SUPPORTED_NO = "no"
    OOB_INTERFACE_SUPPORTED_TRUE = "true"
    OOB_INTERFACE_SUPPORTED_YES = "yes"
    OPER_STATE_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPER_STATE_AUTO_UPGRADE = "auto-upgrade"
    OPER_STATE_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPER_STATE_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPER_STATE_CONFIG = "config"
    OPER_STATE_DECOMISSIONING = "decomissioning"
    OPER_STATE_DEGRADED = "degraded"
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
    OPER_STATE_NOT_SUPPORTED = "not-supported"
    OPER_STATE_OPERABLE = "operable"
    OPER_STATE_PEER_COMM_PROBLEM = "peer-comm-problem"
    OPER_STATE_PERFORMANCE_PROBLEM = "performance-problem"
    OPER_STATE_POST_FAILURE = "post-failure"
    OPER_STATE_POWER_PROBLEM = "power-problem"
    OPER_STATE_POWERED_OFF = "powered-off"
    OPER_STATE_REMOVED = "removed"
    OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    OPER_STATE_UNKNOWN = "unknown"
    OPER_STATE_UPGRADE_PROBLEM = "upgrade-problem"
    OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
    OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
    OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPERABILITY_CONFIG = "config"
    OPERABILITY_DECOMISSIONING = "decomissioning"
    OPERABILITY_DEGRADED = "degraded"
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
    OPERABILITY_NOT_SUPPORTED = "not-supported"
    OPERABILITY_OPERABLE = "operable"
    OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
    OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
    OPERABILITY_POST_FAILURE = "post-failure"
    OPERABILITY_POWER_PROBLEM = "power-problem"
    OPERABILITY_POWERED_OFF = "powered-off"
    OPERABILITY_REMOVED = "removed"
    OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
    OPERABILITY_UNKNOWN = "unknown"
    OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
    OPROM_BOOT_STATUS_DISABLED = "disabled"
    OPROM_BOOT_STATUS_ENABLED = "enabled"
    OPROM_BOOT_STATUS_UNKNOWN = "unknown"
    PERF_LOWER_CRITICAL = "lower-critical"
    PERF_LOWER_NON_CRITICAL = "lower-non-critical"
    PERF_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    PERF_NOT_SUPPORTED = "not-supported"
    PERF_OK = "ok"
    PERF_UNKNOWN = "unknown"
    PERF_UPPER_CRITICAL = "upper-critical"
    PERF_UPPER_NON_CRITICAL = "upper-non-critical"
    PERF_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    PINNED_CACHE_STATUS_DISABLED = "disabled"
    PINNED_CACHE_STATUS_ENABLED = "enabled"
    PINNED_CACHE_STATUS_UNKNOWN = "unknown"
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
    REBUILD_RATE_NOT_APPLICABLE = "not-applicable"
    REBUILD_RATE_UNKNOWN = "unknown"
    THERMAL_LOWER_CRITICAL = "lower-critical"
    THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    THERMAL_NOT_SUPPORTED = "not-supported"
    THERMAL_OK = "ok"
    THERMAL_UNKNOWN = "unknown"
    THERMAL_UPPER_CRITICAL = "upper-critical"
    THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    TYPE_FLASH = "FLASH"
    TYPE_NVME = "NVME"
    TYPE_PCH = "PCH"
    TYPE_PT = "PT"
    TYPE_SAS = "SAS"
    TYPE_SATA = "SATA"
    TYPE_SD = "SD"
    TYPE_EXTERNAL = "external"
    TYPE_UNKNOWN = "unknown"
    VOLTAGE_LOWER_CRITICAL = "lower-critical"
    VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
    VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    VOLTAGE_NOT_SUPPORTED = "not-supported"
    VOLTAGE_OK = "ok"
    VOLTAGE_UNKNOWN = "unknown"
    VOLTAGE_UPPER_CRITICAL = "upper-critical"
    VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
    VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"


class StorageController(ManagedObject):
    """This is StorageController class."""

    consts = StorageControllerConsts()
    naming_props = set([u'type', u'id'])

    mo_meta = MoMeta("StorageController", "storageController", "storage-[type]-[id]", VersionMeta.Version101e, "InputOutput", 0x1ffL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], [u'computeBoard', u'equipmentChassis'], [u'faultInst', u'firmwareBootDefinition', u'firmwareRunning', u'lstorageControllerDef', u'mgmtController', u'storageDeviceBridge', u'storageDrive', u'storageEnclosure', u'storageLocalDisk', u'storageLocalDiskConfigDef', u'storageLocalDiskEp', u'storageLocalLun', u'storageMezzFlashLife', u'storageOperation', u'storageRaidBattery', u'storageVirtualDrive'], ["Get"])

    prop_meta = {
        "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["clear-foreign-configuration", "import-foreign-configuration", "unpin-cache-all", "unspecified"], []), 
        "admin_action_trigger": MoPropertyMeta("admin_action_trigger", "adminActionTrigger", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["canceled", "idle", "triggered"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x8L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "apply-failed", "applying", "not-applied", "not-in-use", "orphaned"], []), 
        "controller_status": MoPropertyMeta("controller_status", "controllerStatus", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed", "optimal", "unknown", "unresponsive"], []), 
        "device_raid_support": MoPropertyMeta("device_raid_support", "deviceRaidSupport", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "fault_monitoring": MoPropertyMeta("fault_monitoring", "faultMonitoring", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["notSupported", "supported"], []), 
        "hw_revision": MoPropertyMeta("hw_revision", "hwRevision", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20L, None, None, None, [], ["1-64"]), 
        "id_count": MoPropertyMeta("id_count", "idCount", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["min", "unknown"], ["0-4294967295"]), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "location_dn": MoPropertyMeta("location_dn", "locationDn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oob_controller_id": MoPropertyMeta("oob_controller_id", "oobControllerId", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "oob_interface_supported": MoPropertyMeta("oob_interface_supported", "oobInterfaceSupported", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "oprom_boot_status": MoPropertyMeta("oprom_boot_status", "opromBootStatus", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled", "unknown"], []), 
        "part_number": MoPropertyMeta("part_number", "partNumber", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pci_addr": MoPropertyMeta("pci_addr", "pciAddr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pci_slot_raw_name": MoPropertyMeta("pci_slot_raw_name", "pciSlotRawName", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "perf": MoPropertyMeta("perf", "perf", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "pinned_cache_status": MoPropertyMeta("pinned_cache_status", "pinnedCacheStatus", "string", VersionMeta.Version252a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled", "unknown"], []), 
        "power": MoPropertyMeta("power", "power", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "raid_support": MoPropertyMeta("raid_support", "raidSupport", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rebuild_rate": MoPropertyMeta("rebuild_rate", "rebuildRate", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable", "unknown"], ["0-101"]), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x100L, None, None, None, ["FLASH", "NVME", "PCH", "PT", "SAS", "SATA", "SD", "external", "unknown"], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "vid": MoPropertyMeta("vid", "vid", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "voltage": MoPropertyMeta("voltage", "voltage", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
    }

    prop_map = {
        "adminAction": "admin_action", 
        "adminActionTrigger": "admin_action_trigger", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "controllerStatus": "controller_status", 
        "deviceRaidSupport": "device_raid_support", 
        "dn": "dn", 
        "faultMonitoring": "fault_monitoring", 
        "hwRevision": "hw_revision", 
        "id": "id", 
        "idCount": "id_count", 
        "lc": "lc", 
        "locationDn": "location_dn", 
        "model": "model", 
        "oobControllerId": "oob_controller_id", 
        "oobInterfaceSupported": "oob_interface_supported", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "opromBootStatus": "oprom_boot_status", 
        "partNumber": "part_number", 
        "pciAddr": "pci_addr", 
        "pciSlot": "pci_slot", 
        "pciSlotRawName": "pci_slot_raw_name", 
        "perf": "perf", 
        "pinnedCacheStatus": "pinned_cache_status", 
        "power": "power", 
        "presence": "presence", 
        "raidSupport": "raid_support", 
        "rebuildRate": "rebuild_rate", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "status": "status", 
        "thermal": "thermal", 
        "type": "type", 
        "vendor": "vendor", 
        "vid": "vid", 
        "voltage": "voltage", 
    }

    def __init__(self, parent_mo_or_dn, type, id, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.id = id
        self.admin_action = None
        self.admin_action_trigger = None
        self.child_action = None
        self.config_state = None
        self.controller_status = None
        self.device_raid_support = None
        self.fault_monitoring = None
        self.hw_revision = None
        self.id_count = None
        self.lc = None
        self.location_dn = None
        self.model = None
        self.oob_controller_id = None
        self.oob_interface_supported = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.oprom_boot_status = None
        self.part_number = None
        self.pci_addr = None
        self.pci_slot = None
        self.pci_slot_raw_name = None
        self.perf = None
        self.pinned_cache_status = None
        self.power = None
        self.presence = None
        self.raid_support = None
        self.rebuild_rate = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.status = None
        self.thermal = None
        self.vendor = None
        self.vid = None
        self.voltage = None

        ManagedObject.__init__(self, "StorageController", parent_mo_or_dn, **kwargs)

