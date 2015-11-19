"""This module contains the general information for ComputeScrubPolicy ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ComputeScrubPolicyConsts():
    BIOS_SETTINGS_SCRUB_NO = "no"
    BIOS_SETTINGS_SCRUB_YES = "yes"
    DISK_SCRUB_NO = "no"
    DISK_SCRUB_YES = "yes"
    FLEX_FLASH_SCRUB_NO = "no"
    FLEX_FLASH_SCRUB_YES = "yes"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class ComputeScrubPolicy(ManagedObject):
    """This is ComputeScrubPolicy class."""

    consts = ComputeScrubPolicyConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("ComputeScrubPolicy", "computeScrubPolicy", "scrub-[name]", VersionMeta.Version101e, "InputOutput", 0x3ffL, [], ["admin", "pn-policy"], [u'computeBlade', u'computeRackUnit', u'computeServerUnit', u'orgOrg'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "bios_settings_scrub": MoPropertyMeta("bios_settings_scrub", "biosSettingsScrub", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["no", "yes"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "disk_scrub": MoPropertyMeta("disk_scrub", "diskScrub", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["no", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "flex_flash_scrub": MoPropertyMeta("flex_flash_scrub", "flexFlashScrub", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["no", "yes"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x100L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
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
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputeScrubPolicy", parent_mo_or_dn, **kwargs)

