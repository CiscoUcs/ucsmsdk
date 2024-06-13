"""This module contains the general information for FabricLifeTime ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricLifeTimeConsts:
    TIMEZONE_UTC = "UTC"
    TIMEZONE_LOCAL = "local"


class FabricLifeTime(ManagedObject):
    """This is FabricLifeTime class."""

    consts = FabricLifeTimeConsts()
    naming_props = set([])

    mo_meta = MoMeta("FabricLifeTime", "fabricLifeTime", "lifetime", VersionMeta.Version434a, "InputOutput", 0x1ff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricMacSecKey'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "duration": MoPropertyMeta("duration", "duration", "uint", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-2147483646"]),
        "end_date_time": MoPropertyMeta("end_date_time", "endDateTime", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "start_date_time": MoPropertyMeta("start_date_time", "startDateTime", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "timezone": MoPropertyMeta("timezone", "timezone", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["UTC", "local"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "duration": "duration", 
        "endDateTime": "end_date_time", 
        "rn": "rn", 
        "sacl": "sacl", 
        "startDateTime": "start_date_time", 
        "status": "status", 
        "timezone": "timezone", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.duration = None
        self.end_date_time = None
        self.sacl = None
        self.start_date_time = None
        self.status = None
        self.timezone = None

        ManagedObject.__init__(self, "FabricLifeTime", parent_mo_or_dn, **kwargs)
