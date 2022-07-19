"""This module contains the general information for StorageFlexFlashDrive ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageFlexFlashDriveConsts:
    RWTYPE_READ_ONLY = "read_only"
    RWTYPE_READ_WRITE = "read_write"
    BLOCK_SIZE_512 = "512"
    BLOCK_SIZE_UNKNOWN = "unknown"
    CONNECTION_PROTOCOL_NVME = "NVME"
    CONNECTION_PROTOCOL_SAS = "SAS"
    CONNECTION_PROTOCOL_SATA = "SATA"
    CONNECTION_PROTOCOL_UNSPECIFIED = "unspecified"
    DRIVE_STATE_NONRAID = "NONRAID"
    DRIVE_STATE_RAID = "RAID"
    DRIVE_TYPE_DRIVERS = "Drivers"
    DRIVE_TYPE_HUU = "HUU"
    DRIVE_TYPE_HV = "HV"
    DRIVE_TYPE_SCU = "SCU"
    DRIVE_TYPE_UNKNOWN = "Unknown"
    LAST_OPERATION_PARTITION_MIRRORED = "PARTITION_MIRRORED"
    LAST_OPERATION_PARTITION_MIRRORED_ERASING = "PARTITION_MIRRORED_ERASING"
    LAST_OPERATION_PARTITION_MIRRORED_ERASING_FAIL = "PARTITION_MIRRORED_ERASING_FAIL"
    LAST_OPERATION_PARTITION_MIRRORED_ERASING_SUCCESS = "PARTITION_MIRRORED_ERASING_SUCCESS"
    LAST_OPERATION_PARTITION_MIRRORED_SYNCING = "PARTITION_MIRRORED_SYNCING"
    LAST_OPERATION_PARTITION_MIRRORED_SYNCING_FAIL = "PARTITION_MIRRORED_SYNCING_FAIL"
    LAST_OPERATION_PARTITION_MIRRORED_SYNCING_SUCCESS = "PARTITION_MIRRORED_SYNCING_SUCCESS"
    LAST_OPERATION_PARTITION_MIRRORED_UPDATING = "PARTITION_MIRRORED_UPDATING"
    LAST_OPERATION_PARTITION_MIRRORED_UPDATING_FAIL = "PARTITION_MIRRORED_UPDATING_FAIL"
    LAST_OPERATION_PARTITION_MIRRORED_UPDATING_SUCCESS = "PARTITION_MIRRORED_UPDATING_SUCCESS"
    LAST_OPERATION_PARTITION_NON_MIRRORED = "PARTITION_NON_MIRRORED"
    LAST_OPERATION_PARTITION_NON_MIRRORED_ERASING = "PARTITION_NON_MIRRORED_ERASING"
    LAST_OPERATION_PARTITION_NON_MIRRORED_ERASING_FAIL = "PARTITION_NON_MIRRORED_ERASING_FAIL"
    LAST_OPERATION_PARTITION_NON_MIRRORED_ERASING_SUCCESS = "PARTITION_NON_MIRRORED_ERASING_SUCCESS"
    LAST_OPERATION_PARTITION_NON_MIRRORED_UPDATING = "PARTITION_NON_MIRRORED_UPDATING"
    LAST_OPERATION_PARTITION_NON_MIRRORED_UPDATING_FAIL = "PARTITION_NON_MIRRORED_UPDATING_FAIL"
    LAST_OPERATION_PARTITION_NON_MIRRORED_UPDATING_SUCCESS = "PARTITION_NON_MIRRORED_UPDATING_SUCCESS"
    LAST_OPERATION_UNKNOWN = "unknown"
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
    OPERATION_STATE_PARTITION_MIRRORED = "PARTITION_MIRRORED"
    OPERATION_STATE_PARTITION_MIRRORED_ERASING = "PARTITION_MIRRORED_ERASING"
    OPERATION_STATE_PARTITION_MIRRORED_ERASING_FAIL = "PARTITION_MIRRORED_ERASING_FAIL"
    OPERATION_STATE_PARTITION_MIRRORED_ERASING_SUCCESS = "PARTITION_MIRRORED_ERASING_SUCCESS"
    OPERATION_STATE_PARTITION_MIRRORED_SYNCING = "PARTITION_MIRRORED_SYNCING"
    OPERATION_STATE_PARTITION_MIRRORED_SYNCING_FAIL = "PARTITION_MIRRORED_SYNCING_FAIL"
    OPERATION_STATE_PARTITION_MIRRORED_SYNCING_SUCCESS = "PARTITION_MIRRORED_SYNCING_SUCCESS"
    OPERATION_STATE_PARTITION_MIRRORED_UPDATING = "PARTITION_MIRRORED_UPDATING"
    OPERATION_STATE_PARTITION_MIRRORED_UPDATING_FAIL = "PARTITION_MIRRORED_UPDATING_FAIL"
    OPERATION_STATE_PARTITION_MIRRORED_UPDATING_SUCCESS = "PARTITION_MIRRORED_UPDATING_SUCCESS"
    OPERATION_STATE_PARTITION_NON_MIRRORED = "PARTITION_NON_MIRRORED"
    OPERATION_STATE_PARTITION_NON_MIRRORED_ERASING = "PARTITION_NON_MIRRORED_ERASING"
    OPERATION_STATE_PARTITION_NON_MIRRORED_ERASING_FAIL = "PARTITION_NON_MIRRORED_ERASING_FAIL"
    OPERATION_STATE_PARTITION_NON_MIRRORED_ERASING_SUCCESS = "PARTITION_NON_MIRRORED_ERASING_SUCCESS"
    OPERATION_STATE_PARTITION_NON_MIRRORED_UPDATING = "PARTITION_NON_MIRRORED_UPDATING"
    OPERATION_STATE_PARTITION_NON_MIRRORED_UPDATING_FAIL = "PARTITION_NON_MIRRORED_UPDATING_FAIL"
    OPERATION_STATE_PARTITION_NON_MIRRORED_UPDATING_SUCCESS = "PARTITION_NON_MIRRORED_UPDATING_SUCCESS"
    OPERATION_STATE_UNKNOWN = "unknown"
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
    REMOVABLE_NA = "NA"
    REMOVABLE_NO = "no"
    REMOVABLE_NO_CHANGE = "no-change"
    REMOVABLE_YES = "yes"
    SIZE_NOT_APPLICABLE = "not-applicable"
    VISIBLE_NO = "no"
    VISIBLE_YES = "yes"


class StorageFlexFlashDrive(ManagedObject):
    """This is StorageFlexFlashDrive class."""

    consts = StorageFlexFlashDriveConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("StorageFlexFlashDrive", "storageFlexFlashDrive", "drive-[name]", VersionMeta.Version221b, "InputOutput", 0x7f, [], ["read-only"], ['storageFlexFlashCard'], ['faultInst'], ["Get"])

    prop_meta = {
        "rw_type": MoPropertyMeta("rw_type", "RWType", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["read_only", "read_write"], []),
        "block_size": MoPropertyMeta("block_size", "blockSize", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["512", "unknown"], ["0-4294967295"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "connection_protocol": MoPropertyMeta("connection_protocol", "connectionProtocol", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NVME", "SAS", "SATA", "unspecified"], []),
        "controller_index": MoPropertyMeta("controller_index", "controllerIndex", "ushort", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "drive_state": MoPropertyMeta("drive_state", "driveState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NONRAID", "RAID"], []),
        "drive_type": MoPropertyMeta("drive_type", "driveType", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Drivers", "HUU", "HV", "SCU", "Unknown"], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
        "last_operation": MoPropertyMeta("last_operation", "lastOperation", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["PARTITION_MIRRORED", "PARTITION_MIRRORED_ERASING", "PARTITION_MIRRORED_ERASING_FAIL", "PARTITION_MIRRORED_ERASING_SUCCESS", "PARTITION_MIRRORED_SYNCING", "PARTITION_MIRRORED_SYNCING_FAIL", "PARTITION_MIRRORED_SYNCING_SUCCESS", "PARTITION_MIRRORED_UPDATING", "PARTITION_MIRRORED_UPDATING_FAIL", "PARTITION_MIRRORED_UPDATING_SUCCESS", "PARTITION_NON_MIRRORED", "PARTITION_NON_MIRRORED_ERASING", "PARTITION_NON_MIRRORED_ERASING_FAIL", "PARTITION_NON_MIRRORED_ERASING_SUCCESS", "PARTITION_NON_MIRRORED_UPDATING", "PARTITION_NON_MIRRORED_UPDATING_FAIL", "PARTITION_NON_MIRRORED_UPDATING_SUCCESS", "unknown"], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []),
        "number_of_blocks": MoPropertyMeta("number_of_blocks", "numberOfBlocks", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-18446744073709551615"]),
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "operation_state": MoPropertyMeta("operation_state", "operationState", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["PARTITION_MIRRORED", "PARTITION_MIRRORED_ERASING", "PARTITION_MIRRORED_ERASING_FAIL", "PARTITION_MIRRORED_ERASING_SUCCESS", "PARTITION_MIRRORED_SYNCING", "PARTITION_MIRRORED_SYNCING_FAIL", "PARTITION_MIRRORED_SYNCING_SUCCESS", "PARTITION_MIRRORED_UPDATING", "PARTITION_MIRRORED_UPDATING_FAIL", "PARTITION_MIRRORED_UPDATING_SUCCESS", "PARTITION_NON_MIRRORED", "PARTITION_NON_MIRRORED_ERASING", "PARTITION_NON_MIRRORED_ERASING_FAIL", "PARTITION_NON_MIRRORED_ERASING_SUCCESS", "PARTITION_NON_MIRRORED_UPDATING", "PARTITION_NON_MIRRORED_UPDATING_FAIL", "PARTITION_NON_MIRRORED_UPDATING_SUCCESS", "unknown"], []),
        "physical_block_size": MoPropertyMeta("physical_block_size", "physicalBlockSize", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["512", "unknown"], ["0-4294967295"]),
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-disc-error", "equipped-disc-in-progress", "equipped-disc-not-started", "equipped-disc-unknown", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []),
        "removable": MoPropertyMeta("removable", "removable", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "no", "no-change", "yes"], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-18446744073709551615"]),
        "slot_number": MoPropertyMeta("slot_number", "slotNumber", "ushort", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "visible": MoPropertyMeta("visible", "visible", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
    }

    prop_map = {
        "RWType": "rw_type", 
        "blockSize": "block_size", 
        "childAction": "child_action", 
        "connectionProtocol": "connection_protocol", 
        "controllerIndex": "controller_index", 
        "dn": "dn", 
        "driveState": "drive_state", 
        "driveType": "drive_type", 
        "id": "id", 
        "lastOperation": "last_operation", 
        "model": "model", 
        "name": "name", 
        "numberOfBlocks": "number_of_blocks", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operability": "operability", 
        "operationState": "operation_state", 
        "physicalBlockSize": "physical_block_size", 
        "presence": "presence", 
        "removable": "removable", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "size": "size", 
        "slotNumber": "slot_number", 
        "status": "status", 
        "vendor": "vendor", 
        "visible": "visible", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.rw_type = None
        self.block_size = None
        self.child_action = None
        self.connection_protocol = None
        self.controller_index = None
        self.drive_state = None
        self.drive_type = None
        self.id = None
        self.last_operation = None
        self.model = None
        self.number_of_blocks = None
        self.oper_qualifier_reason = None
        self.operability = None
        self.operation_state = None
        self.physical_block_size = None
        self.presence = None
        self.removable = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.size = None
        self.slot_number = None
        self.status = None
        self.vendor = None
        self.visible = None

        ManagedObject.__init__(self, "StorageFlexFlashDrive", parent_mo_or_dn, **kwargs)
