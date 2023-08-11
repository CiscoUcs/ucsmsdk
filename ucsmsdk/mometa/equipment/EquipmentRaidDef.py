"""This module contains the general information for EquipmentRaidDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentRaidDefConsts:
    INT_ID_NONE = "none"
    LEVEL_ANY_CONFIGURATION = "any-configuration"
    LEVEL_BEST_EFFORT_MIRRORED = "best-effort-mirrored"
    LEVEL_BEST_EFFORT_MIRRORED_STRIPED = "best-effort-mirrored-striped"
    LEVEL_BEST_EFFORT_STRIPED = "best-effort-striped"
    LEVEL_BEST_EFFORT_STRIPED_DUAL_PARITY = "best-effort-striped-dual-parity"
    LEVEL_BEST_EFFORT_STRIPED_PARITY = "best-effort-striped-parity"
    LEVEL_DISABLE_LOCAL_STORAGE = "disable-local-storage"
    LEVEL_DUAL_DISK = "dual-disk"
    LEVEL_NO_LOCAL_STORAGE = "no-local-storage"
    LEVEL_NO_RAID = "no-raid"
    LEVEL_RAID_MIRRORED = "raid-mirrored"
    LEVEL_RAID_MIRRORED_STRIPED = "raid-mirrored-striped"
    LEVEL_RAID_STRIPED = "raid-striped"
    LEVEL_RAID_STRIPED_DUAL_PARITY = "raid-striped-dual-parity"
    LEVEL_RAID_STRIPED_DUAL_PARITY_STRIPED = "raid-striped-dual-parity-striped"
    LEVEL_RAID_STRIPED_PARITY = "raid-striped-parity"
    LEVEL_RAID_STRIPED_PARITY_STRIPED = "raid-striped-parity-striped"
    LEVEL_SINGLE_DISK = "single-disk"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentRaidDef(ManagedObject):
    """This is EquipmentRaidDef class."""

    consts = EquipmentRaidDefConsts()
    naming_props = set(['level'])

    mo_meta = MoMeta("EquipmentRaidDef", "equipmentRaidDef", "[level]", VersionMeta.Version141i, "InputOutput", 0x1ff, [], [""], ['equipmentLocalDiskControllerCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "level": MoPropertyMeta("level", "level", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x10, None, None, None, ["any-configuration", "best-effort-mirrored", "best-effort-mirrored-striped", "best-effort-striped", "best-effort-striped-dual-parity", "best-effort-striped-parity", "disable-local-storage", "dual-disk", "no-local-storage", "no-raid", "raid-mirrored", "raid-mirrored-striped", "raid-striped", "raid-striped-dual-parity", "raid-striped-dual-parity-striped", "raid-striped-parity", "raid-striped-parity-striped", "single-disk"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "level": "level", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, level, **kwargs):
        self._dirty_mask = 0
        self.level = level
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentRaidDef", parent_mo_or_dn, **kwargs)
