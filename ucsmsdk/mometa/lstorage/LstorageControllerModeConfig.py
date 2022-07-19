"""This module contains the general information for LstorageControllerModeConfig ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LstorageControllerModeConfigConsts:
    PROTECT_CONFIG_FALSE = "false"
    PROTECT_CONFIG_NO = "no"
    PROTECT_CONFIG_TRUE = "true"
    PROTECT_CONFIG_YES = "yes"
    RAID_MODE_ANY_CONFIGURATION = "any-configuration"
    RAID_MODE_BEST_EFFORT_MIRRORED = "best-effort-mirrored"
    RAID_MODE_BEST_EFFORT_MIRRORED_STRIPED = "best-effort-mirrored-striped"
    RAID_MODE_BEST_EFFORT_STRIPED = "best-effort-striped"
    RAID_MODE_BEST_EFFORT_STRIPED_DUAL_PARITY = "best-effort-striped-dual-parity"
    RAID_MODE_BEST_EFFORT_STRIPED_PARITY = "best-effort-striped-parity"
    RAID_MODE_DISABLE_LOCAL_STORAGE = "disable-local-storage"
    RAID_MODE_DUAL_DISK = "dual-disk"
    RAID_MODE_NO_LOCAL_STORAGE = "no-local-storage"
    RAID_MODE_NO_RAID = "no-raid"
    RAID_MODE_RAID_MIRRORED = "raid-mirrored"
    RAID_MODE_RAID_MIRRORED_STRIPED = "raid-mirrored-striped"
    RAID_MODE_RAID_STRIPED = "raid-striped"
    RAID_MODE_RAID_STRIPED_DUAL_PARITY = "raid-striped-dual-parity"
    RAID_MODE_RAID_STRIPED_DUAL_PARITY_STRIPED = "raid-striped-dual-parity-striped"
    RAID_MODE_RAID_STRIPED_PARITY = "raid-striped-parity"
    RAID_MODE_RAID_STRIPED_PARITY_STRIPED = "raid-striped-parity-striped"
    RAID_MODE_SINGLE_DISK = "single-disk"


class LstorageControllerModeConfig(ManagedObject):
    """This is LstorageControllerModeConfig class."""

    consts = LstorageControllerModeConfigConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageControllerModeConfig", "lstorageControllerModeConfig", "controller-mode-config", VersionMeta.Version227b, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-storage", "ls-storage-policy"], ['lstorageControllerDef'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version227b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "protect_config": MoPropertyMeta("protect_config", "protectConfig", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["false", "no", "true", "yes"], []),
        "raid_mode": MoPropertyMeta("raid_mode", "raidMode", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["any-configuration", "best-effort-mirrored", "best-effort-mirrored-striped", "best-effort-striped", "best-effort-striped-dual-parity", "best-effort-striped-parity", "disable-local-storage", "dual-disk", "no-local-storage", "no-raid", "raid-mirrored", "raid-mirrored-striped", "raid-striped", "raid-striped-dual-parity", "raid-striped-dual-parity-striped", "raid-striped-parity", "raid-striped-parity-striped", "single-disk"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "protectConfig": "protect_config", 
        "raidMode": "raid_mode", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.protect_config = None
        self.raid_mode = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageControllerModeConfig", parent_mo_or_dn, **kwargs)
