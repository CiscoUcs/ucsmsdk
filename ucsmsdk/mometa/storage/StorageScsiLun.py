"""This module contains the general information for StorageScsiLun ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageScsiLunConsts():
    ADMIN_STATE_DELETE = "delete"
    ADMIN_STATE_OFFLINE = "offline"
    ADMIN_STATE_ONLINE = "online"
    ADMIN_STATE_RESTORE = "restore"
    ADMIN_STATE_UNDEFINED = "undefined"
    BLOCK_SIZE_UNKNOWN = "unknown"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLY_FAILED = "apply-failed"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_NOT_IN_USE = "not-in-use"
    CONFIG_STATE_ORPHANED = "orphaned"
    CONNECTION_PROTOCOL_SAS = "SAS"
    CONNECTION_PROTOCOL_SATA = "SATA"
    CONNECTION_PROTOCOL_UNSPECIFIED = "unspecified"
    DEPLOY_ACTION_ABORT_REPLICATION = "abort-replication"
    DEPLOY_ACTION_CREATE = "create"
    DEPLOY_ACTION_DELETE = "delete"
    DEPLOY_ACTION_MODIFY = "modify"
    DEPLOY_ACTION_NO_ACTION = "no-action"
    DEPLOY_ACTION_REPLACE = "replace"
    DEPLOY_ACTION_RESTORE = "restore"
    DEPLOY_ACTION_SET_OFFLINE = "set-offline"
    DEPLOY_ACTION_SET_ONLINE = "set-online"
    LUN_MAP_TYPE_NON_SHARED = "non-shared"
    LUN_MAP_TYPE_SHARED = "shared"
    NUMBER_OF_BLOCKS_UNKNOWN = "unknown"
    OPER_STATE_CLUSTER_DEGRADED = "cluster-degraded"
    OPER_STATE_COMPUTE_DEGRADED = "compute-degraded"
    OPER_STATE_COMPUTE_INOPERABLE = "compute-inoperable"
    OPER_STATE_OFFLINE = "offline"
    OPER_STATE_ONLINE = "online"
    OPER_STATE_UNDEFINED = "undefined"
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
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
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
    SNAPSHOT_ADMIN_STATE_ABORT_REPLICATION = "abort-replication"
    SNAPSHOT_ADMIN_STATE_CREATE = "create"
    SNAPSHOT_ADMIN_STATE_CREATE_LUN_REPLICA = "create-lun-replica"
    SNAPSHOT_ADMIN_STATE_REPLICATION_RESTORE = "replication-restore"
    SNAPSHOT_ADMIN_STATE_SET_REPLICATION_OFFLINE = "set-replication-offline"
    SNAPSHOT_ADMIN_STATE_SET_REPLICATION_ONLINE = "set-replication-online"
    SNAPSHOT_ADMIN_STATE_UNDEFINED = "undefined"
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


class StorageScsiLun(ManagedObject):
    """This is StorageScsiLun class."""

    consts = StorageScsiLunConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("StorageScsiLun", "storageScsiLun", "lun-[name]", VersionMeta.Version302c, "InputOutput", 0x3ffL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], [u'storagePartition'], [u'faultInst', u'storageInitiatorRef', u'storageReplicaRestoreProfile', u'storageReplicationProfile', u'storageScsiDeviceDescriptor', u'storageScsiLunRef', u'storageSnapshotProfile'], [None])

    prop_meta = {
        "actual_size": MoPropertyMeta("actual_size", "actualSize", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["delete", "offline", "online", "restore", "undefined"], []), 
        "block_size": MoPropertyMeta("block_size", "blockSize", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_qualifier_reason": MoPropertyMeta("config_qualifier_reason", "configQualifierReason", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "apply-failed", "applying", "not-applied", "not-in-use", "orphaned"], []), 
        "connection_protocol": MoPropertyMeta("connection_protocol", "connectionProtocol", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["SAS", "SATA", "unspecified"], []), 
        "deploy_action": MoPropertyMeta("deploy_action", "deployAction", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["abort-replication", "create", "delete", "modify", "no-action", "replace", "restore", "set-offline", "set-online"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "device_id": MoPropertyMeta("device_id", "deviceId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], []), 
        "last_snapshot_id": MoPropertyMeta("last_snapshot_id", "lastSnapshotId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "lun_map_type": MoPropertyMeta("lun_map_type", "lunMapType", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["non-shared", "shared"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x20L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []), 
        "number_of_blocks": MoPropertyMeta("number_of_blocks", "numberOfBlocks", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cluster-degraded", "compute-degraded", "compute-inoperable", "offline", "online", "undefined"], []), 
        "oper_volume_name": MoPropertyMeta("oper_volume_name", "operVolumeName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "parent_lun_name": MoPropertyMeta("parent_lun_name", "parentLunName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "size": MoPropertyMeta("size", "size", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "snapshot_admin_state": MoPropertyMeta("snapshot_admin_state", "snapshotAdminState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["abort-replication", "create", "create-lun-replica", "replication-restore", "set-replication-offline", "set-replication-online", "undefined"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x100L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["mirror", "mirror-stripe", "raid", "simple", "stripe", "stripe-dual-parity", "stripe-dual-parity-stripe", "stripe-parity", "stripe-parity-stripe", "unspecified"], []), 
        "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "vendor_uuid": MoPropertyMeta("vendor_uuid", "vendorUuid", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []), 
        "volume_name": MoPropertyMeta("volume_name", "volumeName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
    }

    prop_map = {
        "actualSize": "actual_size", 
        "adminState": "admin_state", 
        "blockSize": "block_size", 
        "childAction": "child_action", 
        "configQualifierReason": "config_qualifier_reason", 
        "configState": "config_state", 
        "connectionProtocol": "connection_protocol", 
        "deployAction": "deploy_action", 
        "descr": "descr", 
        "deviceId": "device_id", 
        "dn": "dn", 
        "id": "id", 
        "lastSnapshotId": "last_snapshot_id", 
        "locale": "locale", 
        "lunMapType": "lun_map_type", 
        "model": "model", 
        "name": "name", 
        "numberOfBlocks": "number_of_blocks", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operVolumeName": "oper_volume_name", 
        "operability": "operability", 
        "parentLunName": "parent_lun_name", 
        "presence": "presence", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "size": "size", 
        "snapshotAdminState": "snapshot_admin_state", 
        "status": "status", 
        "type": "type", 
        "uuid": "uuid", 
        "vendor": "vendor", 
        "vendorUuid": "vendor_uuid", 
        "volumeName": "volume_name", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.actual_size = None
        self.admin_state = None
        self.block_size = None
        self.child_action = None
        self.config_qualifier_reason = None
        self.config_state = None
        self.connection_protocol = None
        self.deploy_action = None
        self.descr = None
        self.device_id = None
        self.id = None
        self.last_snapshot_id = None
        self.locale = None
        self.lun_map_type = None
        self.model = None
        self.number_of_blocks = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.oper_volume_name = None
        self.operability = None
        self.parent_lun_name = None
        self.presence = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.size = None
        self.snapshot_admin_state = None
        self.status = None
        self.type = None
        self.uuid = None
        self.vendor = None
        self.vendor_uuid = None
        self.volume_name = None

        ManagedObject.__init__(self, "StorageScsiLun", parent_mo_or_dn, **kwargs)

