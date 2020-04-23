"""This module contains the general information for IqnpoolAddr ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class IqnpoolAddrConsts:
    ASSIGNED_FALSE = "false"
    ASSIGNED_NO = "no"
    ASSIGNED_TRUE = "true"
    ASSIGNED_YES = "yes"
    OWNER_END_POINT = "end-point"
    OWNER_POOL = "pool"


class IqnpoolAddr(ManagedObject):
    """This is IqnpoolAddr class."""

    consts = IqnpoolAddrConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("IqnpoolAddr", "iqnpoolAddr", "[name]", VersionMeta.Version201m, "InputOutput", 0x3f, [], ["read-only"], ['iqnpoolUniverse'], ['faultInst', 'iqnpoolPoolable'], ["Get"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "global_assigned_cnt": MoPropertyMeta("global_assigned_cnt", "globalAssignedCnt", "uint", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "global_defined_cnt": MoPropertyMeta("global_defined_cnt", "globalDefinedCnt", "uint", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["end-point", "pool"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "assigned": "assigned", 
        "assignedToDn": "assigned_to_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "globalAssignedCnt": "global_assigned_cnt", 
        "globalDefinedCnt": "global_defined_cnt", 
        "name": "name", 
        "owner": "owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.assigned = None
        self.assigned_to_dn = None
        self.child_action = None
        self.global_assigned_cnt = None
        self.global_defined_cnt = None
        self.owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "IqnpoolAddr", parent_mo_or_dn, **kwargs)
