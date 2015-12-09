"""This module contains the general information for LstorageSanScsiLun ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageSanScsiLunConsts():
    ADMIN_STATE_OFFLINE = "offline"
    ADMIN_STATE_ONLINE = "online"
    ADMIN_STATE_UNDEPLOYED = "undeployed"
    AUTO_DEPLOY_AUTO_DEPLOY = "auto-deploy"
    AUTO_DEPLOY_NO_AUTO_DEPLOY = "no-auto-deploy"
    BOOT_DEV_DISABLED = "disabled"
    BOOT_DEV_ENABLED = "enabled"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_FAILED_TO_APPLY = "failed-to-apply"
    CONFIG_STATE_OK = "ok"
    LUN_MAP_TYPE_NON_SHARED = "non-shared"
    LUN_MAP_TYPE_SHARED = "shared"
    MODE_ANY_CONFIGURATION = "any-configuration"
    MODE_RAID_MIRRORED = "raid-mirrored"
    MODE_RAID_MIRRORED_STRIPED = "raid-mirrored-striped"
    MODE_RAID_STRIPED = "raid-striped"
    MODE_RAID_STRIPED_DUAL_PARITY = "raid-striped-dual-parity"
    MODE_RAID_STRIPED_DUAL_PARITY_STRIPED = "raid-striped-dual-parity-striped"
    MODE_RAID_STRIPED_PARITY = "raid-striped-parity"
    MODE_RAID_STRIPED_PARITY_STRIPED = "raid-striped-parity-striped"
    OPER_STATE_CLUSTER_DEGRADED = "cluster-degraded"
    OPER_STATE_COMPUTE_DEGRADED = "compute-degraded"
    OPER_STATE_COMPUTE_INOPERABLE = "compute-inoperable"
    OPER_STATE_OFFLINE = "offline"
    OPER_STATE_ONLINE = "online"
    OPER_STATE_UNDEFINED = "undefined"
    STORAGE_CLASS_DAS = "das"
    STORAGE_CLASS_SAN = "san"
    STPL_FCP = "fcp"
    STPL_ISCSI = "iscsi"
    STPL_SAS = "sas"
    STPL_SCSI_PARALLEL = "scsi-parallel"
    STPL_SSA = "ssa"
    STPL_UAS = "uas"
    STPL_UNSPECIFIED = "unspecified"
    VDAS_NATIVE = "native"
    VDAS_UNSPECIFIED = "unspecified"
    VDAS_VDAS = "vdas"


class LstorageSanScsiLun(ManagedObject):
    """This is LstorageSanScsiLun class."""

    consts = LstorageSanScsiLunConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("LstorageSanScsiLun", "lstorageSanScsiLun", "san-scsi-lun-[name]", VersionMeta.Version302c, "InputOutput", 0x7fffL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage", "ls-storage-policy"], [u'lstorageProfile', u'lstorageProfileDef'], [u'faultInst', u'lstorageBackstoreBinding', u'lstorageBackstoreRequirement', u'lstorageLunClone'], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["offline", "online", "undeployed"], []), 
        "auto_deploy": MoPropertyMeta("auto_deploy", "autoDeploy", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["auto-deploy", "no-auto-deploy"], []), 
        "boot_dev": MoPropertyMeta("boot_dev", "bootDev", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x8L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|identity-assignment|unsupported-storage-capability|lun-id-conflict|missing-firmware-image|lun-capacity-exceeded|insufficient-lun-resources|lun-limit-exceeded|lun-ownership-conflict|storage-unavailable),){0,10}(defaultValue|not-applicable|identity-assignment|unsupported-storage-capability|lun-id-conflict|missing-firmware-image|lun-capacity-exceeded|insufficient-lun-resources|lun-limit-exceeded|lun-ownership-conflict|storage-unavailable){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "applying", "failed-to-apply", "ok"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "lun_dn": MoPropertyMeta("lun_dn", "lunDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "lun_map_type": MoPropertyMeta("lun_map_type", "lunMapType", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["non-shared", "shared"], []), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["any-configuration", "raid-mirrored", "raid-mirrored-striped", "raid-striped", "raid-striped-dual-parity", "raid-striped-dual-parity-striped", "raid-striped-parity", "raid-striped-parity-striped"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x80L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "oper_replication_policy_name": MoPropertyMeta("oper_replication_policy_name", "operReplicationPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_snapshot_policy_name": MoPropertyMeta("oper_snapshot_policy_name", "operSnapshotPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cluster-degraded", "compute-degraded", "compute-inoperable", "offline", "online", "undefined"], []), 
        "replication_policy_name": MoPropertyMeta("replication_policy_name", "replicationPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x100L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x200L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "size": MoPropertyMeta("size", "size", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, [], ["1-10240"]), 
        "snapshot_policy_name": MoPropertyMeta("snapshot_policy_name", "snapshotPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x800L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "storage_class": MoPropertyMeta("storage_class", "storageClass", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["das", "san"], []), 
        "stpl": MoPropertyMeta("stpl", "stpl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, ["fcp", "iscsi", "sas", "scsi-parallel", "ssa", "uas", "unspecified"], []), 
        "vdas": MoPropertyMeta("vdas", "vdas", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, None, ["native", "unspecified", "vdas"], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "autoDeploy": "auto_deploy", 
        "bootDev": "boot_dev", 
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "configState": "config_state", 
        "dn": "dn", 
        "lunDn": "lun_dn", 
        "lunMapType": "lun_map_type", 
        "mode": "mode", 
        "name": "name", 
        "operReplicationPolicyName": "oper_replication_policy_name", 
        "operSnapshotPolicyName": "oper_snapshot_policy_name", 
        "operState": "oper_state", 
        "replicationPolicyName": "replication_policy_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "size": "size", 
        "snapshotPolicyName": "snapshot_policy_name", 
        "status": "status", 
        "storageClass": "storage_class", 
        "stpl": "stpl", 
        "vdas": "vdas", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_state = None
        self.auto_deploy = None
        self.boot_dev = None
        self.child_action = None
        self.config_qualifier = None
        self.config_state = None
        self.lun_dn = None
        self.lun_map_type = None
        self.mode = None
        self.oper_replication_policy_name = None
        self.oper_snapshot_policy_name = None
        self.oper_state = None
        self.replication_policy_name = None
        self.sacl = None
        self.size = None
        self.snapshot_policy_name = None
        self.status = None
        self.storage_class = None
        self.stpl = None
        self.vdas = None

        ManagedObject.__init__(self, "LstorageSanScsiLun", parent_mo_or_dn, **kwargs)

