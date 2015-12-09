"""This module contains the general information for StorageLunCounters ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageLunCountersConsts():
    pass


class StorageLunCounters(ManagedObject):
    """This is StorageLunCounters class."""

    consts = StorageLunCountersConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageLunCounters", "storageLunCounters", "lun-counters", VersionMeta.Version302c, "InputOutput", 0x1fL, [], ["read-only"], [u'storagePartition'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "lun_count_in_use": MoPropertyMeta("lun_count_in_use", "lunCountInUse", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lun_count_not_in_use": MoPropertyMeta("lun_count_not_in_use", "lunCountNotInUse", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lun_count_orphaned": MoPropertyMeta("lun_count_orphaned", "lunCountOrphaned", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lun_replica_count": MoPropertyMeta("lun_replica_count", "lunReplicaCount", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lun_snapshot_count": MoPropertyMeta("lun_snapshot_count", "lunSnapshotCount", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "lunCountInUse": "lun_count_in_use", 
        "lunCountNotInUse": "lun_count_not_in_use", 
        "lunCountOrphaned": "lun_count_orphaned", 
        "lunReplicaCount": "lun_replica_count", 
        "lunSnapshotCount": "lun_snapshot_count", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.lun_count_in_use = None
        self.lun_count_not_in_use = None
        self.lun_count_orphaned = None
        self.lun_replica_count = None
        self.lun_snapshot_count = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "StorageLunCounters", parent_mo_or_dn, **kwargs)

