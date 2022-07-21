"""This module contains the general information for StorageVDMemberEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageVDMemberEpConsts:
    CONFIG_QUAL_ADD = "add"
    CONFIG_QUAL_NO_ACTION = "no-action"
    CONFIG_QUAL_REMOVE = "remove"
    CONFIG_STATE_N_A = "N/A"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLY_FAILED = "apply-failed"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_NOT_IN_USE = "not-in-use"
    CONFIG_STATE_ORPHANED = "orphaned"
    CONFIG_STATE_UNKNOWN = "unknown"
    DEPLOY_ACTION_ABORT_REPLICATION = "abort-replication"
    DEPLOY_ACTION_CREATE = "create"
    DEPLOY_ACTION_DELETE = "delete"
    DEPLOY_ACTION_MODIFY = "modify"
    DEPLOY_ACTION_NO_ACTION = "no-action"
    DEPLOY_ACTION_REPLACE = "replace"
    DEPLOY_ACTION_RESTORE = "restore"
    DEPLOY_ACTION_SET_OFFLINE = "set-offline"
    DEPLOY_ACTION_SET_ONLINE = "set-online"
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
    ROLE_DED_HOT_SPARE = "ded-hot-spare"
    ROLE_GLOB_HOT_SPARE = "glob-hot-spare"
    ROLE_NORMAL = "normal"
    ROLE_UNKNOWN = "unknown"
    SPAN_ID_UNSPECIFIED = "unspecified"


class StorageVDMemberEp(ManagedObject):
    """This is StorageVDMemberEp class."""

    consts = StorageVDMemberEpConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("StorageVDMemberEp", "storageVDMemberEp", "member-[id]", VersionMeta.Version224b, "InputOutput", 0x3f, [], ["read-only"], ['storageVirtualDrive'], ['faultInst'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_qual": MoPropertyMeta("config_qual", "configQual", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["add", "no-action", "remove"], []),
        "config_qualifier_reason": MoPropertyMeta("config_qualifier_reason", "configQualifierReason", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A", "applied", "apply-failed", "applying", "not-applied", "not-in-use", "orphaned", "unknown"], []),
        "deploy_action": MoPropertyMeta("deploy_action", "deployAction", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["abort-replication", "create", "delete", "modify", "no-action", "replace", "restore", "set-offline", "set-online"], []),
        "disk_dn": MoPropertyMeta("disk_dn", "diskDn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version224b, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-disc-error", "equipped-disc-in-progress", "equipped-disc-not-started", "equipped-disc-unknown", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "role": MoPropertyMeta("role", "role", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ded-hot-spare", "glob-hot-spare", "normal", "unknown"], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "span_id": MoPropertyMeta("span_id", "spanId", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-8"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configQual": "config_qual", 
        "configQualifierReason": "config_qualifier_reason", 
        "configState": "config_state", 
        "deployAction": "deploy_action", 
        "diskDn": "disk_dn", 
        "dn": "dn", 
        "id": "id", 
        "model": "model", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operability": "operability", 
        "presence": "presence", 
        "revision": "revision", 
        "rn": "rn", 
        "role": "role", 
        "sacl": "sacl", 
        "serial": "serial", 
        "spanId": "span_id", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.config_qual = None
        self.config_qualifier_reason = None
        self.config_state = None
        self.deploy_action = None
        self.disk_dn = None
        self.model = None
        self.oper_qualifier_reason = None
        self.operability = None
        self.presence = None
        self.revision = None
        self.role = None
        self.sacl = None
        self.serial = None
        self.span_id = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "StorageVDMemberEp", parent_mo_or_dn, **kwargs)
