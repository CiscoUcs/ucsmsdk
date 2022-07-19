"""This module contains the general information for StorageFlexFlashVirtualDrive ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageFlexFlashVirtualDriveConsts:
    BLOCK_SIZE_512 = "512"
    BLOCK_SIZE_UNKNOWN = "unknown"
    CONNECTION_PROTOCOL_NVME = "NVME"
    CONNECTION_PROTOCOL_SAS = "SAS"
    CONNECTION_PROTOCOL_SATA = "SATA"
    CONNECTION_PROTOCOL_UNSPECIFIED = "unspecified"
    ID_UNSPECIFIED = "unspecified"
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
    RAID_HEALTH_FFR_HEALTH_DEGRADED = "FFR_HEALTH_DEGRADED"
    RAID_HEALTH_FFR_HEALTH_NA = "FFR_HEALTH_NA"
    RAID_HEALTH_FFR_HEALTH_NOT_REPORTING = "FFR_HEALTH_NOT_REPORTING"
    RAID_HEALTH_FFR_HEALTH_OK = "FFR_HEALTH_OK"
    RAID_STATE_FFR_STATE_DISABLED = "FFR_STATE_DISABLED"
    RAID_STATE_FFR_STATE_ENABLED_NOT_PAIRED = "FFR_STATE_ENABLED_NOT_PAIRED"
    RAID_STATE_FFR_STATE_ENABLED_PAIRED = "FFR_STATE_ENABLED_PAIRED"
    RAID_STATE_FFR_STATE_ENABLED_PAIRED_INVALID_BOTH = "FFR_STATE_ENABLED_PAIRED_INVALID_BOTH"
    RAID_STATE_FFR_STATE_ENABLED_PAIRED_INVALID_PRIMARY = "FFR_STATE_ENABLED_PAIRED_INVALID_PRIMARY"
    RAID_STATE_FFR_STATE_ENABLED_PAIRED_INVALID_SECONDARY = "FFR_STATE_ENABLED_PAIRED_INVALID_SECONDARY"
    RAID_STATE_FFR_STATE_RAID_MIRRORING_DISABLED = "FFR_STATE_RAID_MIRRORING_DISABLED"
    SIZE_NOT_APPLICABLE = "not-applicable"
    TYPE_MIRROR = "mirror"
    TYPE_MIRROR_STRIPE = "mirror-stripe"
    TYPE_RAID = "raid"
    TYPE_SIMPLE = "simple"
    TYPE_STRIPE = "stripe"
    TYPE_STRIPE_DUAL_PARITY = "stripe-dual-parity"
    TYPE_STRIPE_DUAL_PARITY_STRIPE = "stripe-dual-parity-stripe"
    TYPE_STRIPE_PARITY = "stripe-parity"
    TYPE_STRIPE_PARITY_STRIPE = "stripe-parity-stripe"
    TYPE_UNSPECIFIED = "unspecified"


class StorageFlexFlashVirtualDrive(ManagedObject):
    """This is StorageFlexFlashVirtualDrive class."""

    consts = StorageFlexFlashVirtualDriveConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("StorageFlexFlashVirtualDrive", "storageFlexFlashVirtualDrive", "vd-[id]", VersionMeta.Version221b, "InputOutput", 0x7f, [], ["read-only"], ['storageFlexFlashController'], ['faultInst'], ["Get"])

    prop_meta = {
        "block_size": MoPropertyMeta("block_size", "blockSize", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["512", "unknown"], ["0-4294967295"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "connection_protocol": MoPropertyMeta("connection_protocol", "connectionProtocol", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NVME", "SAS", "SATA", "unspecified"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x8, None, None, None, ["unspecified"], ["0-4294967295"]),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "number_of_blocks": MoPropertyMeta("number_of_blocks", "numberOfBlocks", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-18446744073709551615"]),
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "physical_block_size": MoPropertyMeta("physical_block_size", "physicalBlockSize", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["512", "unknown"], ["0-4294967295"]),
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-disc-error", "equipped-disc-in-progress", "equipped-disc-not-started", "equipped-disc-unknown", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []),
        "raid_health": MoPropertyMeta("raid_health", "raidHealth", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["FFR_HEALTH_DEGRADED", "FFR_HEALTH_NA", "FFR_HEALTH_NOT_REPORTING", "FFR_HEALTH_OK"], []),
        "raid_state": MoPropertyMeta("raid_state", "raidState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["FFR_STATE_DISABLED", "FFR_STATE_ENABLED_NOT_PAIRED", "FFR_STATE_ENABLED_PAIRED", "FFR_STATE_ENABLED_PAIRED_INVALID_BOTH", "FFR_STATE_ENABLED_PAIRED_INVALID_PRIMARY", "FFR_STATE_ENABLED_PAIRED_INVALID_SECONDARY", "FFR_STATE_RAID_MIRRORING_DISABLED"], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-18446744073709551615"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["mirror", "mirror-stripe", "raid", "simple", "stripe", "stripe-dual-parity", "stripe-dual-parity-stripe", "stripe-parity", "stripe-parity-stripe", "unspecified"], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "blockSize": "block_size", 
        "childAction": "child_action", 
        "connectionProtocol": "connection_protocol", 
        "dn": "dn", 
        "id": "id", 
        "model": "model", 
        "numberOfBlocks": "number_of_blocks", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operability": "operability", 
        "physicalBlockSize": "physical_block_size", 
        "presence": "presence", 
        "raidHealth": "raid_health", 
        "raidState": "raid_state", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "size": "size", 
        "status": "status", 
        "type": "type", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.block_size = None
        self.child_action = None
        self.connection_protocol = None
        self.model = None
        self.number_of_blocks = None
        self.oper_qualifier_reason = None
        self.operability = None
        self.physical_block_size = None
        self.presence = None
        self.raid_health = None
        self.raid_state = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.size = None
        self.status = None
        self.type = None
        self.vendor = None

        ManagedObject.__init__(self, "StorageFlexFlashVirtualDrive", parent_mo_or_dn, **kwargs)
