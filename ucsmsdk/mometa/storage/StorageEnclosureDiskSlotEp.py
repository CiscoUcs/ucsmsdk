"""This module contains the general information for StorageEnclosureDiskSlotEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageEnclosureDiskSlotEpConsts:
    AUTO_ZONE_CAUSE_HDD_TRAY_IN_LIEU_OF_SERVER2 = "hdd-tray-in-lieu-of-server2"
    AUTO_ZONE_CAUSE_HDDSLOT_UNASSIGNED = "hddslot-unassigned"
    AUTO_ZONE_CAUSE_HOTSPARE_UNSUPPORTED = "hotspare-unsupported"
    AUTO_ZONE_CAUSE_MEZZ_CONTROLLER_IN_IOEXPANDER = "mezz-controller-in-ioexpander"
    AUTO_ZONE_CAUSE_NONE = "none"
    AUTO_ZONE_CAUSE_SECOND_CONTROLLER_ABSENT = "second-controller-absent"
    AUTO_ZONE_CAUSE_SHARING_UNSUPPORTED = "sharing-unsupported"
    CONFIGURATION_NOT_SUPPORTED = "not-supported"
    CONFIGURATION_SUPPORTED = "supported"
    CONFIGURATION_UNKNOWN = "unknown"
    DRIVE_PATH_NONE = "NONE"
    DRIVE_PATH_PATH_0 = "PATH-0"
    DRIVE_PATH_PATH_1 = "PATH-1"
    DRIVE_PATH_PATH_BOTH = "PATH-BOTH"
    DRIVE_PATH_UNKNOWN = "UNKNOWN"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
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
    OWNERSHIP_CHASSIS_DEDICATED_SPARE = "chassis-dedicated-spare"
    OWNERSHIP_CHASSIS_GLOBAL_SPARE = "chassis-global-spare"
    OWNERSHIP_DEDICATED = "dedicated"
    OWNERSHIP_SHARED = "shared"
    OWNERSHIP_UNASSIGNED = "unassigned"
    OWNERSHIP_UNKNOWN = "unknown"
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


class StorageEnclosureDiskSlotEp(ManagedObject):
    """This is StorageEnclosureDiskSlotEp class."""

    consts = StorageEnclosureDiskSlotEpConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("StorageEnclosureDiskSlotEp", "storageEnclosureDiskSlotEp", "disk-slot-[id]", VersionMeta.Version302c, "InputOutput", 0x3f, [], ["read-only"], ['storageEnclosure'], ['faultInst', 'storageControllerRef'], ["Get"])

    prop_meta = {
        "auto_zone_cause": MoPropertyMeta("auto_zone_cause", "autoZoneCause", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["hdd-tray-in-lieu-of-server2", "hddslot-unassigned", "hotspare-unsupported", "mezz-controller-in-ioexpander", "none", "second-controller-absent", "sharing-unsupported"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "configuration": MoPropertyMeta("configuration", "configuration", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-supported", "supported", "unknown"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "drive_path": MoPropertyMeta("drive_path", "drivePath", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NONE", "PATH-0", "PATH-1", "PATH-BOTH", "UNKNOWN"], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []),
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "ownership": MoPropertyMeta("ownership", "ownership", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["chassis-dedicated-spare", "chassis-global-spare", "dedicated", "shared", "unassigned", "unknown"], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-disc-error", "equipped-disc-in-progress", "equipped-disc-not-started", "equipped-disc-unknown", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "autoZoneCause": "auto_zone_cause", 
        "childAction": "child_action", 
        "configuration": "configuration", 
        "dn": "dn", 
        "drivePath": "drive_path", 
        "id": "id", 
        "lc": "lc", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operability": "operability", 
        "ownership": "ownership", 
        "peerDn": "peer_dn", 
        "presence": "presence", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.auto_zone_cause = None
        self.child_action = None
        self.configuration = None
        self.drive_path = None
        self.lc = None
        self.oper_qualifier_reason = None
        self.operability = None
        self.ownership = None
        self.peer_dn = None
        self.presence = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "StorageEnclosureDiskSlotEp", parent_mo_or_dn, **kwargs)
