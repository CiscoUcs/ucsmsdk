"""This module contains the general information for StorageUsageCounters ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageUsageCountersConsts():
    pass


class StorageUsageCounters(ManagedObject):
    """This is StorageUsageCounters class."""

    consts = StorageUsageCountersConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageUsageCounters", "storageUsageCounters", "storage-usage", VersionMeta.Version302c, "InputOutput", 0x1fL, [], ["read-only"], [u'storagePartition'], [], [None])

    prop_meta = {
        "available": MoPropertyMeta("available", "available", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "in_use": MoPropertyMeta("in_use", "inUse", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "not_in_use": MoPropertyMeta("not_in_use", "notInUse", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "orphaned": MoPropertyMeta("orphaned", "orphaned", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "replica": MoPropertyMeta("replica", "replica", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "snapshot": MoPropertyMeta("snapshot", "snapshot", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "total_configured": MoPropertyMeta("total_configured", "totalConfigured", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "total_data_protection": MoPropertyMeta("total_data_protection", "totalDataProtection", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "total_requested": MoPropertyMeta("total_requested", "totalRequested", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "available": "available", 
        "childAction": "child_action", 
        "dn": "dn", 
        "inUse": "in_use", 
        "notInUse": "not_in_use", 
        "orphaned": "orphaned", 
        "replica": "replica", 
        "rn": "rn", 
        "sacl": "sacl", 
        "snapshot": "snapshot", 
        "status": "status", 
        "totalConfigured": "total_configured", 
        "totalDataProtection": "total_data_protection", 
        "totalRequested": "total_requested", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.available = None
        self.child_action = None
        self.in_use = None
        self.not_in_use = None
        self.orphaned = None
        self.replica = None
        self.sacl = None
        self.snapshot = None
        self.status = None
        self.total_configured = None
        self.total_data_protection = None
        self.total_requested = None

        ManagedObject.__init__(self, "StorageUsageCounters", parent_mo_or_dn, **kwargs)

