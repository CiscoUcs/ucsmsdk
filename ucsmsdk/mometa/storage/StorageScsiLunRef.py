"""This module contains the general information for StorageScsiLunRef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageScsiLunRefConsts():
    pass


class StorageScsiLunRef(ManagedObject):
    """This is StorageScsiLunRef class."""

    consts = StorageScsiLunRefConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("StorageScsiLunRef", "storageScsiLunRef", "scsi-lun-ref-[id]", VersionMeta.Version224a, "InputOutput", 0x1fL, [], ["read-only"], [u'storageLunReplica', u'storageLunSnapshot', u'storageScsiLun', u'storageVirtualDrive'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version224a, MoPropertyMeta.NAMING, 0x4L, None, None, None, [], []), 
        "ls_dn": MoPropertyMeta("ls_dn", "lsDn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "lun_name": MoPropertyMeta("lun_name", "lunName", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "profile_dn": MoPropertyMeta("profile_dn", "profileDn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "lsDn": "ls_dn", 
        "lunName": "lun_name", 
        "profileDn": "profile_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.ls_dn = None
        self.lun_name = None
        self.profile_dn = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "StorageScsiLunRef", parent_mo_or_dn, **kwargs)

