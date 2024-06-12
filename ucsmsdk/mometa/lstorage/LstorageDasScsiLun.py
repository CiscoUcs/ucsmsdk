"""This module contains the general information for LstorageDasScsiLun ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LstorageDasScsiLunConsts:
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
    DEFERRED_NAMING_FALSE = "false"
    DEFERRED_NAMING_NO = "no"
    DEFERRED_NAMING_TRUE = "true"
    DEFERRED_NAMING_YES = "yes"
    EXPAND_TO_AVAIL_FALSE = "false"
    EXPAND_TO_AVAIL_NO = "no"
    EXPAND_TO_AVAIL_TRUE = "true"
    EXPAND_TO_AVAIL_YES = "yes"
    LUN_MAP_TYPE_NON_SHARED = "non-shared"
    LUN_MAP_TYPE_SHARED = "shared"
    LUN_MAP_TYPE_UNASSIGNED = "unassigned"
    OPER_STATE_COMPUTE_DEGRADED = "compute-degraded"
    OPER_STATE_COMPUTE_INOPERABLE = "compute-inoperable"
    OPER_STATE_OFFLINE = "offline"
    OPER_STATE_ONLINE = "online"
    OPER_STATE_UNDEFINED = "undefined"
    ORDER_NOT_APPLICABLE = "not-applicable"
    SIZE_UNSPECIFIED = "unspecified"
    STORAGE_CLASS_DAS = "das"
    STORAGE_CLASS_SAN = "san"


class LstorageDasScsiLun(ManagedObject):
    """This is LstorageDasScsiLun class."""

    consts = LstorageDasScsiLunConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("LstorageDasScsiLun", "lstorageDasScsiLun", "das-scsi-lun-[name]", VersionMeta.Version224b, "InputOutput", 0x7fff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage", "ls-storage-policy"], ['lstorageProfile', 'lstorageProfileDef'], ['faultInst', 'storageLocalDiskConfigDef'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["offline", "online", "undeployed"], []),
        "auto_deploy": MoPropertyMeta("auto_deploy", "autoDeploy", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["auto-deploy", "no-auto-deploy"], []),
        "boot_dev": MoPropertyMeta("boot_dev", "bootDev", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, 0x8, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|identity-assignment|unsupported-storage-capability|lun-id-conflict|missing-firmware-image|lun-capacity-exceeded|insufficient-lun-resources|lun-limit-exceeded|lun-ownership-conflict|storage-unavailable),){0,10}(defaultValue|not-applicable|identity-assignment|unsupported-storage-capability|lun-id-conflict|missing-firmware-image|lun-capacity-exceeded|insufficient-lun-resources|lun-limit-exceeded|lun-ownership-conflict|storage-unavailable){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "applying", "failed-to-apply", "ok"], []),
        "deferred_naming": MoPropertyMeta("deferred_naming", "deferredNaming", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "expand_to_avail": MoPropertyMeta("expand_to_avail", "expandToAvail", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["false", "no", "true", "yes"], []),
        "fractional_size": MoPropertyMeta("fractional_size", "fractionalSize", "ulong", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["0-1023"]),
        "local_disk_policy_name": MoPropertyMeta("local_disk_policy_name", "localDiskPolicyName", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "lun_dn": MoPropertyMeta("lun_dn", "lunDn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "lun_map_type": MoPropertyMeta("lun_map_type", "lunMapType", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["non-shared", "shared", "unassigned"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version224b, MoPropertyMeta.NAMING, 0x400, None, None, r"""[\-_a-zA-Z0-9]{1,10}""", [], []),
        "oper_local_disk_policy_name": MoPropertyMeta("oper_local_disk_policy_name", "operLocalDiskPolicyName", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["compute-degraded", "compute-inoperable", "offline", "online", "undefined"], []),
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["not-applicable"], ["0-64"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x1000, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["unspecified"], ["0-18446744073709551615"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "storage_class": MoPropertyMeta("storage_class", "storageClass", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["das", "san"], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "autoDeploy": "auto_deploy", 
        "bootDev": "boot_dev", 
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "configState": "config_state", 
        "deferredNaming": "deferred_naming", 
        "dn": "dn", 
        "expandToAvail": "expand_to_avail", 
        "fractionalSize": "fractional_size", 
        "localDiskPolicyName": "local_disk_policy_name", 
        "lunDn": "lun_dn", 
        "lunMapType": "lun_map_type", 
        "name": "name", 
        "operLocalDiskPolicyName": "oper_local_disk_policy_name", 
        "operState": "oper_state", 
        "order": "order", 
        "rn": "rn", 
        "sacl": "sacl", 
        "size": "size", 
        "status": "status", 
        "storageClass": "storage_class", 
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
        self.deferred_naming = None
        self.expand_to_avail = None
        self.fractional_size = None
        self.local_disk_policy_name = None
        self.lun_dn = None
        self.lun_map_type = None
        self.oper_local_disk_policy_name = None
        self.oper_state = None
        self.order = None
        self.sacl = None
        self.size = None
        self.status = None
        self.storage_class = None

        ManagedObject.__init__(self, "LstorageDasScsiLun", parent_mo_or_dn, **kwargs)
