"""This module contains the general information for LstoragePooledArrayVolume ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstoragePooledArrayVolumeConsts():
    ASSIGNED_FALSE = "false"
    ASSIGNED_NO = "no"
    ASSIGNED_TRUE = "true"
    ASSIGNED_YES = "yes"
    OWNER_MANAGEMENT = "management"
    OWNER_POLICY = "policy"


class LstoragePooledArrayVolume(ManagedObject):
    """This is LstoragePooledArrayVolume class."""

    consts = LstoragePooledArrayVolumeConsts()
    naming_props = set([u'arrayName', u'partitionName', u'volumeName'])

    mo_meta = MoMeta("LstoragePooledArrayVolume", "lstoragePooledArrayVolume", "array-[array_name]-part-[partition_name]-vol-[volume_name]", VersionMeta.Version302c, "InputOutput", 0xffL, [], ["admin", "ls-storage", "read-only"], [u'lstorageBackstorePool'], [], [None])

    prop_meta = {
        "array_name": MoPropertyMeta("array_name", "arrayName", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x2L, 1, 32, None, [], []), 
        "assigned": MoPropertyMeta("assigned", "assigned", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["management", "policy"], []), 
        "partition_name": MoPropertyMeta("partition_name", "partitionName", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x10L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "poolable_dn": MoPropertyMeta("poolable_dn", "poolableDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "prev_assigned_to_dn": MoPropertyMeta("prev_assigned_to_dn", "prevAssignedToDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "volume_name": MoPropertyMeta("volume_name", "volumeName", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x80L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []), 
    }

    prop_map = {
        "arrayName": "array_name", 
        "assigned": "assigned", 
        "assignedToDn": "assigned_to_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "owner": "owner", 
        "partitionName": "partition_name", 
        "poolableDn": "poolable_dn", 
        "prevAssignedToDn": "prev_assigned_to_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "volumeName": "volume_name", 
    }

    def __init__(self, parent_mo_or_dn, array_name, partition_name, volume_name, **kwargs):
        self._dirty_mask = 0
        self.array_name = array_name
        self.partition_name = partition_name
        self.volume_name = volume_name
        self.assigned = None
        self.assigned_to_dn = None
        self.child_action = None
        self.owner = None
        self.poolable_dn = None
        self.prev_assigned_to_dn = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstoragePooledArrayVolume", parent_mo_or_dn, **kwargs)

