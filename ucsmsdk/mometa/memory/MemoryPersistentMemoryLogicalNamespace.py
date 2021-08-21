"""This module contains the general information for MemoryPersistentMemoryLogicalNamespace ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MemoryPersistentMemoryLogicalNamespaceConsts:
    MODE_BLOCK = "block"
    MODE_RAW = "raw"
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


class MemoryPersistentMemoryLogicalNamespace(ManagedObject):
    """This is MemoryPersistentMemoryLogicalNamespace class."""

    consts = MemoryPersistentMemoryLogicalNamespaceConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("MemoryPersistentMemoryLogicalNamespace", "memoryPersistentMemoryLogicalNamespace", "lns-[name]", VersionMeta.Version404a, "InputOutput", 0x3ff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], ['memoryPersistentMemoryPolicy'], [], [None])

    prop_meta = {
        "capacity": MoPropertyMeta("capacity", "capacity", "long", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["1-9223372036854775807"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["block", "raw"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version404a, MoPropertyMeta.NAMING, 0x20, None, None, r"""[a-zA-Z0-9#_-][a-zA-Z0-9#_ -]{0,62}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["socket-1", "socket-2", "socket-3", "socket-4"], []),
        "socket_local_dimm_number": MoPropertyMeta("socket_local_dimm_number", "socketLocalDimmNumber", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["10", "11", "12", "14", "15", "16", "2", "3", "4", "6", "7", "8", "not-applicable"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "capacity": "capacity", 
        "childAction": "child_action", 
        "dn": "dn", 
        "mode": "mode", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "socketId": "socket_id", 
        "socketLocalDimmNumber": "socket_local_dimm_number", 
        "status": "status", 
        "uuid": "uuid", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.capacity = None
        self.child_action = None
        self.mode = None
        self.sacl = None
        self.socket_id = None
        self.socket_local_dimm_number = None
        self.status = None
        self.uuid = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryLogicalNamespace", parent_mo_or_dn, **kwargs)
