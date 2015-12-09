"""This module contains the general information for FirmwareStoragePackModImpact ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FirmwareStoragePackModImpactConsts():
    pass


class FirmwareStoragePackModImpact(ManagedObject):
    """This is FirmwareStoragePackModImpact class."""

    consts = FirmwareStoragePackModImpactConsts()
    naming_props = set([u'keyDn'])

    mo_meta = MoMeta("FirmwareStoragePackModImpact", "firmwareStoragePackModImpact", "fw-sys-StoragePackModImpact-[key_dn]", VersionMeta.Version302c, "InputOutput", 0x3fL, [], ["admin", "ls-config-policy", "ls-server-policy"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "key_dn": MoPropertyMeta("key_dn", "keyDn", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x8L, 1, 510, None, [], []), 
        "maint_policy_dn": MoPropertyMeta("maint_policy_dn", "maintPolicyDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "pn_dn": MoPropertyMeta("pn_dn", "pnDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "reboot_policy": MoPropertyMeta("reboot_policy", "rebootPolicy", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "storage_array_profile_dn": MoPropertyMeta("storage_array_profile_dn", "storageArrayProfileDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "keyDn": "key_dn", 
        "maintPolicyDn": "maint_policy_dn", 
        "pnDn": "pn_dn", 
        "rebootPolicy": "reboot_policy", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "storageArrayProfileDn": "storage_array_profile_dn", 
    }

    def __init__(self, parent_mo_or_dn, key_dn, **kwargs):
        self._dirty_mask = 0
        self.key_dn = key_dn
        self.child_action = None
        self.maint_policy_dn = None
        self.pn_dn = None
        self.reboot_policy = None
        self.sacl = None
        self.status = None
        self.storage_array_profile_dn = None

        ManagedObject.__init__(self, "FirmwareStoragePackModImpact", parent_mo_or_dn, **kwargs)

