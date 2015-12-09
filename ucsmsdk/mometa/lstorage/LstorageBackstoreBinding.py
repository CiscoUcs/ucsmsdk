"""This module contains the general information for LstorageBackstoreBinding ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageBackstoreBindingConsts():
    pass


class LstorageBackstoreBinding(ManagedObject):
    """This is LstorageBackstoreBinding class."""

    consts = LstorageBackstoreBindingConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageBackstoreBinding", "lstorageBackstoreBinding", "backstore", VersionMeta.Version302c, "InputOutput", 0xffL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage", "ls-storage-policy", "read-only"], [u'lstorageSanScsiLun'], [], [None])

    prop_meta = {
        "array_name": MoPropertyMeta("array_name", "arrayName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x2L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []), 
        "backstore_dn": MoPropertyMeta("backstore_dn", "backstoreDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "partition_name": MoPropertyMeta("partition_name", "partitionName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "volume_name": MoPropertyMeta("volume_name", "volumeName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,32}""", [], []), 
    }

    prop_map = {
        "arrayName": "array_name", 
        "backstoreDn": "backstore_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "partitionName": "partition_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "volumeName": "volume_name", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.array_name = None
        self.backstore_dn = None
        self.child_action = None
        self.name = None
        self.partition_name = None
        self.sacl = None
        self.status = None
        self.volume_name = None

        ManagedObject.__init__(self, "LstorageBackstoreBinding", parent_mo_or_dn, **kwargs)

