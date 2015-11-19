"""This module contains the general information for StorageScsiLunMask ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageScsiLunMaskConsts():
    pass


class StorageScsiLunMask(ManagedObject):
    """This is StorageScsiLunMask class."""

    consts = StorageScsiLunMaskConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("StorageScsiLunMask", "storageScsiLunMask", "lunmask-[name]", VersionMeta.Version302a, "InputOutput", 0x1fL, [], ["read-only"], [u'storageLunMaskGroup'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ushort", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-255"]), 
        "lun_dn": MoPropertyMeta("lun_dn", "lunDn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302a, MoPropertyMeta.NAMING, 0x4L, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "lunDn": "lun_dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.id = None
        self.lun_dn = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "StorageScsiLunMask", parent_mo_or_dn, **kwargs)

