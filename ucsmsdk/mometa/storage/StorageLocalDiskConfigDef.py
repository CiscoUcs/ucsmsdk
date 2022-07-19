"""This module contains the general information for StorageLocalDiskConfigDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageLocalDiskConfigDefConsts:
    FLEX_FLASH_RAIDREPORTING_STATE_DISABLE = "disable"
    FLEX_FLASH_RAIDREPORTING_STATE_ENABLE = "enable"
    FLEX_FLASH_REMOVABLE_STATE_NA = "NA"
    FLEX_FLASH_REMOVABLE_STATE_NO = "no"
    FLEX_FLASH_REMOVABLE_STATE_NO_CHANGE = "no-change"
    FLEX_FLASH_REMOVABLE_STATE_YES = "yes"
    FLEX_FLASH_STATE_DISABLE = "disable"
    FLEX_FLASH_STATE_ENABLE = "enable"
    INT_ID_NONE = "none"
    MODE_ANY_CONFIGURATION = "any-configuration"
    MODE_BEST_EFFORT_MIRRORED = "best-effort-mirrored"
    MODE_BEST_EFFORT_MIRRORED_STRIPED = "best-effort-mirrored-striped"
    MODE_BEST_EFFORT_STRIPED = "best-effort-striped"
    MODE_BEST_EFFORT_STRIPED_DUAL_PARITY = "best-effort-striped-dual-parity"
    MODE_BEST_EFFORT_STRIPED_PARITY = "best-effort-striped-parity"
    MODE_DISABLE_LOCAL_STORAGE = "disable-local-storage"
    MODE_DUAL_DISK = "dual-disk"
    MODE_NO_LOCAL_STORAGE = "no-local-storage"
    MODE_NO_RAID = "no-raid"
    MODE_RAID_MIRRORED = "raid-mirrored"
    MODE_RAID_MIRRORED_STRIPED = "raid-mirrored-striped"
    MODE_RAID_STRIPED = "raid-striped"
    MODE_RAID_STRIPED_DUAL_PARITY = "raid-striped-dual-parity"
    MODE_RAID_STRIPED_DUAL_PARITY_STRIPED = "raid-striped-dual-parity-striped"
    MODE_RAID_STRIPED_PARITY = "raid-striped-parity"
    MODE_RAID_STRIPED_PARITY_STRIPED = "raid-striped-parity-striped"
    MODE_SINGLE_DISK = "single-disk"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PROTECT_CONFIG_FALSE = "false"
    PROTECT_CONFIG_NO = "no"
    PROTECT_CONFIG_TRUE = "true"
    PROTECT_CONFIG_YES = "yes"


class StorageLocalDiskConfigDef(ManagedObject):
    """This is StorageLocalDiskConfigDef class."""

    consts = StorageLocalDiskConfigDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageLocalDiskConfigDef", "storageLocalDiskConfigDef", "local-disk-config", VersionMeta.Version101e, "InputOutput", 0x1fff, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-storage", "ls-storage-policy"], ['lsServer', 'lstorageDasScsiLun', 'storageController', 'storageFlexFlashController'], ['lstorageSecurity', 'storageLocalDiskPartition'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "flex_flash_raid_reporting_state": MoPropertyMeta("flex_flash_raid_reporting_state", "flexFlashRAIDReportingState", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disable", "enable"], []),
        "flex_flash_removable_state": MoPropertyMeta("flex_flash_removable_state", "flexFlashRemovableState", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["NA", "no", "no-change", "yes"], []),
        "flex_flash_state": MoPropertyMeta("flex_flash_state", "flexFlashState", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["disable", "enable"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["any-configuration", "best-effort-mirrored", "best-effort-mirrored-striped", "best-effort-striped", "best-effort-striped-dual-parity", "best-effort-striped-parity", "disable-local-storage", "dual-disk", "no-local-storage", "no-raid", "raid-mirrored", "raid-mirrored-striped", "raid-striped", "raid-striped-dual-parity", "raid-striped-dual-parity-striped", "raid-striped-parity", "raid-striped-parity-striped", "single-disk"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["local", "pending-policy", "policy"], []),
        "protect_config": MoPropertyMeta("protect_config", "protectConfig", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x800, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "flexFlashRAIDReportingState": "flex_flash_raid_reporting_state", 
        "flexFlashRemovableState": "flex_flash_removable_state", 
        "flexFlashState": "flex_flash_state", 
        "intId": "int_id", 
        "mode": "mode", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "protectConfig": "protect_config", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.flex_flash_raid_reporting_state = None
        self.flex_flash_removable_state = None
        self.flex_flash_state = None
        self.int_id = None
        self.mode = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.protect_config = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "StorageLocalDiskConfigDef", parent_mo_or_dn, **kwargs)
