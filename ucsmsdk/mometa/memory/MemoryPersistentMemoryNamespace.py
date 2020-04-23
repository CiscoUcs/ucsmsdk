"""This module contains the general information for MemoryPersistentMemoryNamespace ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MemoryPersistentMemoryNamespaceConsts:
    ADMIN_STATE_CONFIGURE = "configure"
    ADMIN_STATE_DELETE = "delete"
    ADMIN_STATE_FORCE_CONFIGURE = "force-configure"
    ADMIN_STATE_FORCE_DELETE = "force-delete"
    ADMIN_STATE_FORCE_FLAG = "force-flag"
    ADMIN_STATE_INIT = "init"
    ADMIN_STATE_MATCHING = "matching"
    ADMIN_STATE_NOT_MATCHING = "not-matching"


class MemoryPersistentMemoryNamespace(ManagedObject):
    """This is MemoryPersistentMemoryNamespace class."""

    consts = MemoryPersistentMemoryNamespaceConsts()
    naming_props = set(['uuid'])

    mo_meta = MoMeta("MemoryPersistentMemoryNamespace", "memoryPersistentMemoryNamespace", "ns-[uuid]", VersionMeta.Version404a, "InputOutput", 0x7f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['memoryPersistentMemoryRegion'], ['faultInst'], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["configure", "delete", "force-configure", "force-delete", "force-flag", "init", "matching", "not-matching"], []),
        "capacity": MoPropertyMeta("capacity", "capacity", "long", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([0-9]{1,15})$""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "health_state": MoPropertyMeta("health_state", "healthState", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "label_version": MoPropertyMeta("label_version", "labelVersion", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[a-zA-Z0-9#_-][a-zA-Z0-9#_ -]{0,62}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version404a, MoPropertyMeta.NAMING, 0x40, 1, 510, None, [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "capacity": "capacity", 
        "childAction": "child_action", 
        "dn": "dn", 
        "healthState": "health_state", 
        "labelVersion": "label_version", 
        "mode": "mode", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "uuid": "uuid", 
    }

    def __init__(self, parent_mo_or_dn, uuid, **kwargs):
        self._dirty_mask = 0
        self.uuid = uuid
        self.admin_state = None
        self.capacity = None
        self.child_action = None
        self.health_state = None
        self.label_version = None
        self.mode = None
        self.name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryNamespace", parent_mo_or_dn, **kwargs)
