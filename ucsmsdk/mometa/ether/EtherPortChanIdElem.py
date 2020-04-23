"""This module contains the general information for EtherPortChanIdElem ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EtherPortChanIdElemConsts:
    RESERVED_FALSE = "false"
    RESERVED_NO = "no"
    RESERVED_TRUE = "true"
    RESERVED_YES = "yes"


class EtherPortChanIdElem(ManagedObject):
    """This is EtherPortChanIdElem class."""

    consts = EtherPortChanIdElemConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EtherPortChanIdElem", "etherPortChanIdElem", "pchanid-[id]", VersionMeta.Version201m, "InputOutput", 0x3f, [], ["read-only"], ['etherPortChanIdUniverse'], [], ["Get"])

    prop_meta = {
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "prev_assigned_to_dn": MoPropertyMeta("prev_assigned_to_dn", "prevAssignedToDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "reserved": MoPropertyMeta("reserved", "reserved", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "assignedToDn": "assigned_to_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "prevAssignedToDn": "prev_assigned_to_dn", 
        "reserved": "reserved", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.assigned_to_dn = None
        self.child_action = None
        self.prev_assigned_to_dn = None
        self.reserved = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EtherPortChanIdElem", parent_mo_or_dn, **kwargs)
