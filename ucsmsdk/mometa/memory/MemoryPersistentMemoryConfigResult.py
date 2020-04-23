"""This module contains the general information for MemoryPersistentMemoryConfigResult ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MemoryPersistentMemoryConfigResultConsts:
    pass


class MemoryPersistentMemoryConfigResult(ManagedObject):
    """This is MemoryPersistentMemoryConfigResult class."""

    consts = MemoryPersistentMemoryConfigResultConsts()
    naming_props = set([])

    mo_meta = MoMeta("MemoryPersistentMemoryConfigResult", "memoryPersistentMemoryConfigResult", "cfg-result", VersionMeta.Version404a, "InputOutput", 0x1f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['memoryPersistentMemoryConfiguration'], ['faultInst', 'memoryPersistentMemoryNamespaceConfigResult'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_error_desc": MoPropertyMeta("config_error_desc", "configErrorDesc", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "config_result": MoPropertyMeta("config_result", "configResult", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "config_sequence_no": MoPropertyMeta("config_sequence_no", "configSequenceNo", "uint", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configErrorDesc": "config_error_desc", 
        "configResult": "config_result", 
        "configSequenceNo": "config_sequence_no", 
        "configState": "config_state", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.config_error_desc = None
        self.config_result = None
        self.config_sequence_no = None
        self.config_state = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryConfigResult", parent_mo_or_dn, **kwargs)
