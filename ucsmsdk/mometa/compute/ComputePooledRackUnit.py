"""This module contains the general information for ComputePooledRackUnit ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePooledRackUnitConsts:
    ASSIGNED_FALSE = "false"
    ASSIGNED_NO = "no"
    ASSIGNED_TRUE = "true"
    ASSIGNED_YES = "yes"
    OWNER_MANAGEMENT = "management"
    OWNER_POLICY = "policy"


class ComputePooledRackUnit(ManagedObject):
    """This is ComputePooledRackUnit class."""

    consts = ComputePooledRackUnitConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ComputePooledRackUnit", "computePooledRackUnit", "rack-[id]", VersionMeta.Version141i, "InputOutput", 0x3f, [], ["admin", "pn-policy"], ['computePool'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-255"]),
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["management", "policy"], []),
        "poolable_dn": MoPropertyMeta("poolable_dn", "poolableDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "prev_assigned_to_dn": MoPropertyMeta("prev_assigned_to_dn", "prevAssignedToDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "assigned": "assigned", 
        "assignedToDn": "assigned_to_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "owner": "owner", 
        "poolableDn": "poolable_dn", 
        "prevAssignedToDn": "prev_assigned_to_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.assigned = None
        self.assigned_to_dn = None
        self.child_action = None
        self.owner = None
        self.poolable_dn = None
        self.prev_assigned_to_dn = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputePooledRackUnit", parent_mo_or_dn, **kwargs)
