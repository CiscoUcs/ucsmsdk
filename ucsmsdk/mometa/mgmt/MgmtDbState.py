"""This module contains the general information for MgmtDbState ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtDbStateConsts:
    pass


class MgmtDbState(ManagedObject):
    """This is MgmtDbState class."""

    consts = MgmtDbStateConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtDbState", "mgmtDbState", "mgmt-db-state", VersionMeta.Version321d, "InputOutput", 0x3f, [], ["read-only"], ['networkElement'], ['faultInst'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "corrupted_count": MoPropertyMeta("corrupted_count", "corruptedCount", "ulong", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "last_occurrence_time": MoPropertyMeta("last_occurrence_time", "lastOccurrenceTime", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "corruptedCount": "corrupted_count", 
        "dn": "dn", 
        "lastOccurrenceTime": "last_occurrence_time", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.corrupted_count = None
        self.last_occurrence_time = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtDbState", parent_mo_or_dn, **kwargs)
