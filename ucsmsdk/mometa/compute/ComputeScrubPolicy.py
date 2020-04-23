"""This module contains the general information for ComputeScrubPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeScrubPolicyConsts:
    BIOS_SETTINGS_SCRUB_NO = "no"
    BIOS_SETTINGS_SCRUB_YES = "yes"
    DISK_SCRUB_NO = "no"
    DISK_SCRUB_YES = "yes"
    FLEX_FLASH_SCRUB_NO = "no"
    FLEX_FLASH_SCRUB_YES = "yes"
    INT_ID_NONE = "none"
    PERSISTENT_MEMORY_SCRUB_NO = "no"
    PERSISTENT_MEMORY_SCRUB_YES = "yes"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class ComputeScrubPolicy(ManagedObject):
    """This is ComputeScrubPolicy class."""

    consts = ComputeScrubPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("ComputeScrubPolicy", "computeScrubPolicy", "scrub-[name]", VersionMeta.Version101e, "InputOutput", 0xfff, [], ["admin", "pn-policy"], ['computeBlade', 'computeRackUnit', 'computeServerUnit', 'orgOrg'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "bios_settings_scrub": MoPropertyMeta("bios_settings_scrub", "biosSettingsScrub", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["no", "yes"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "disk_scrub": MoPropertyMeta("disk_scrub", "diskScrub", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["no", "yes"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "flex_flash_scrub": MoPropertyMeta("flex_flash_scrub", "flexFlashScrub", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["no", "yes"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "persistent_memory_scrub": MoPropertyMeta("persistent_memory_scrub", "persistentMemoryScrub", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["no", "yes"], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "biosSettingsScrub": "bios_settings_scrub", 
        "childAction": "child_action", 
        "descr": "descr", 
        "diskScrub": "disk_scrub", 
        "dn": "dn", 
        "flexFlashScrub": "flex_flash_scrub", 
        "intId": "int_id", 
        "name": "name", 
        "persistentMemoryScrub": "persistent_memory_scrub", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.bios_settings_scrub = None
        self.child_action = None
        self.descr = None
        self.disk_scrub = None
        self.flex_flash_scrub = None
        self.int_id = None
        self.persistent_memory_scrub = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputeScrubPolicy", parent_mo_or_dn, **kwargs)
