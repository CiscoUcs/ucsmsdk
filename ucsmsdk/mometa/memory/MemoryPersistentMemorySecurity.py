"""This module contains the general information for MemoryPersistentMemorySecurity ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MemoryPersistentMemorySecurityConsts:
    pass


class MemoryPersistentMemorySecurity(ManagedObject):
    """This is MemoryPersistentMemorySecurity class."""

    consts = MemoryPersistentMemorySecurityConsts()
    naming_props = set([])

    mo_meta = MoMeta("MemoryPersistentMemorySecurity", "memoryPersistentMemorySecurity", "security", VersionMeta.Version404a, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server"], ['memoryPersistentMemoryPolicy'], ['memoryPersistentMemoryLocalSecurity'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MemoryPersistentMemorySecurity", parent_mo_or_dn, **kwargs)
