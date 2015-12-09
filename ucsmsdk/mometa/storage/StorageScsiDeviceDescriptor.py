"""This module contains the general information for StorageScsiDeviceDescriptor ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageScsiDeviceDescriptorConsts():
    TYPE_EUI_64 = "eui-64"
    TYPE_MD5 = "md5"
    TYPE_NAA = "naa"
    TYPE_SCSI_NAME = "scsi-name"
    TYPE_T10 = "t10"


class StorageScsiDeviceDescriptor(ManagedObject):
    """This is StorageScsiDeviceDescriptor class."""

    consts = StorageScsiDeviceDescriptorConsts()
    naming_props = set([u'type'])

    mo_meta = MoMeta("StorageScsiDeviceDescriptor", "storageScsiDeviceDescriptor", "scsi-descriptor-[type]", VersionMeta.Version302c, "InputOutput", 0x3fL, [], ["read-only"], [u'storageScsiLun'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x20L, None, None, None, ["eui-64", "md5", "naa", "scsi-name", "t10"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.id = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "StorageScsiDeviceDescriptor", parent_mo_or_dn, **kwargs)

