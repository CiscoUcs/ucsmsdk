"""This module contains the general information for MemoryPersistentMemoryGoal ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MemoryPersistentMemoryGoalConsts:
    PERSISTENT_MEMORY_TYPE_APP_DIRECT = "app-direct"
    PERSISTENT_MEMORY_TYPE_APP_DIRECT_NON_INTERLEAVED = "app-direct-non-interleaved"
    SOCKET_ID_ALL_SOCKETS = "all-sockets"


class MemoryPersistentMemoryGoal(ManagedObject):
    """This is MemoryPersistentMemoryGoal class."""

    consts = MemoryPersistentMemoryGoalConsts()
    naming_props = set(['socketId'])

    mo_meta = MoMeta("MemoryPersistentMemoryGoal", "memoryPersistentMemoryGoal", "goal-[socket_id]", VersionMeta.Version404a, "InputOutput", 0xff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], ['memoryPersistentMemoryPolicy'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "memory_mode_percentage": MoPropertyMeta("memory_mode_percentage", "memoryModePercentage", "byte", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-100"]),
        "persistent_memory_type": MoPropertyMeta("persistent_memory_type", "persistentMemoryType", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["app-direct", "app-direct-non-interleaved"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "socket_id": MoPropertyMeta("socket_id", "socketId", "string", VersionMeta.Version404a, MoPropertyMeta.NAMING, 0x40, None, None, None, ["all-sockets"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "memoryModePercentage": "memory_mode_percentage", 
        "persistentMemoryType": "persistent_memory_type", 
        "rn": "rn", 
        "sacl": "sacl", 
        "socketId": "socket_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, socket_id, **kwargs):
        self._dirty_mask = 0
        self.socket_id = socket_id
        self.child_action = None
        self.memory_mode_percentage = None
        self.persistent_memory_type = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryGoal", parent_mo_or_dn, **kwargs)
