"""This module contains the general information for MgmtMgmtDbState ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtMgmtDbStateConsts:
    pass


class MgmtMgmtDbState(ManagedObject):
    """This is MgmtMgmtDbState class."""

    consts = MgmtMgmtDbStateConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtMgmtDbState", "mgmtMgmtDbState", "mgmt-db-state", VersionMeta.Version227b, "InputOutput", 0x1f, [], ["read-only"], [u'networkElement'], [u'faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version227b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "corrupted_count": MoPropertyMeta("corrupted_count", "corruptedCount", "ulong", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "last_occurence_time": MoPropertyMeta("last_occurence_time", "lastOccurenceTime", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "corruptedCount": "corrupted_count", 
        "dn": "dn", 
        "lastOccurenceTime": "last_occurence_time", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.corrupted_count = None
        self.last_occurence_time = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtMgmtDbState", parent_mo_or_dn, **kwargs)
