"""This module contains the general information for StorageItem ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageItemConsts:
    ALARM_TYPE_MAJOR = "major"
    ALARM_TYPE_MINOR = "minor"
    OPER_STATE_CLEAN = "clean"
    OPER_STATE_CLEAN_WITH_ERRORS = "clean-with-errors"
    OPER_STATE_MOUNTED = "mounted"
    OPER_STATE_NOT_CLEAN = "not-clean"
    OPER_STATE_UNKNOWN = "unknown"
    OPER_STATE_UNMOUNTED = "unmounted"
    SIZE_NOTHING = "nothing"
    USED_EMPTY = "empty"
    USED_FULL = "full"
    USED_NOT_APPLICABLE = "not-applicable"


class StorageItem(ManagedObject):
    """This is StorageItem class."""

    consts = StorageItemConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("StorageItem", "storageItem", "stor-part-[name]", VersionMeta.Version101e, "InputOutput", 0x3f, [], ["read-only"], ['networkElement'], ['faultInst'], ["Get"])

    prop_meta = {
        "alarm_type": MoPropertyMeta("alarm_type", "alarmType", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["major", "minor"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["clean", "clean-with-errors", "mounted", "not-clean", "unknown", "unmounted"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["nothing"], ["0-18446744073709551615"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "used": MoPropertyMeta("used", "used", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "full", "not-applicable"], ["0-101"]),
    }

    prop_map = {
        "alarmType": "alarm_type", 
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "operState": "oper_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "size": "size", 
        "status": "status", 
        "used": "used", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.alarm_type = None
        self.child_action = None
        self.oper_state = None
        self.sacl = None
        self.size = None
        self.status = None
        self.used = None

        ManagedObject.__init__(self, "StorageItem", parent_mo_or_dn, **kwargs)
