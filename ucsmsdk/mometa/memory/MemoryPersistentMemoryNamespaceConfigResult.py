"""This module contains the general information for MemoryPersistentMemoryNamespaceConfigResult ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MemoryPersistentMemoryNamespaceConfigResultConsts:
    SOCKET_ID_SOCKET_1 = "socket-1"
    SOCKET_ID_SOCKET_2 = "socket-2"
    SOCKET_ID_SOCKET_3 = "socket-3"
    SOCKET_ID_SOCKET_4 = "socket-4"
    SOCKET_LOCAL_DIMM_NUMBER_10 = "10"
    SOCKET_LOCAL_DIMM_NUMBER_11 = "11"
    SOCKET_LOCAL_DIMM_NUMBER_12 = "12"
    SOCKET_LOCAL_DIMM_NUMBER_14 = "14"
    SOCKET_LOCAL_DIMM_NUMBER_15 = "15"
    SOCKET_LOCAL_DIMM_NUMBER_16 = "16"
    SOCKET_LOCAL_DIMM_NUMBER_2 = "2"
    SOCKET_LOCAL_DIMM_NUMBER_3 = "3"
    SOCKET_LOCAL_DIMM_NUMBER_4 = "4"
    SOCKET_LOCAL_DIMM_NUMBER_6 = "6"
    SOCKET_LOCAL_DIMM_NUMBER_7 = "7"
    SOCKET_LOCAL_DIMM_NUMBER_8 = "8"
    SOCKET_LOCAL_DIMM_NUMBER_NOT_APPLICABLE = "not-applicable"


class MemoryPersistentMemoryNamespaceConfigResult(ManagedObject):
    """This is MemoryPersistentMemoryNamespaceConfigResult class."""

    consts = MemoryPersistentMemoryNamespaceConfigResultConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("MemoryPersistentMemoryNamespaceConfigResult", "memoryPersistentMemoryNamespaceConfigResult", "nscr-[name]", VersionMeta.Version404a, "InputOutput", 0x3f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['memoryPersistentMemoryConfigResult'], ['faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_status": MoPropertyMeta("config_status", "configStatus", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version404a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["socket-1", "socket-2", "socket-3", "socket-4"], []),
        "socket_local_dimm_number": MoPropertyMeta("socket_local_dimm_number", "socketLocalDimmNumber", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["10", "11", "12", "14", "15", "16", "2", "3", "4", "6", "7", "8", "not-applicable"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configStatus": "config_status", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "socketId": "socket_id", 
        "socketLocalDimmNumber": "socket_local_dimm_number", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.config_status = None
        self.sacl = None
        self.socket_id = None
        self.socket_local_dimm_number = None
        self.status = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryNamespaceConfigResult", parent_mo_or_dn, **kwargs)
