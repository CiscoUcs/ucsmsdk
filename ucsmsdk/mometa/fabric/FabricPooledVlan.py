"""This module contains the general information for FabricPooledVlan ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricPooledVlanConsts:
    ASSIGNED_FALSE = "false"
    ASSIGNED_NO = "no"
    ASSIGNED_TRUE = "true"
    ASSIGNED_YES = "yes"


class FabricPooledVlan(ManagedObject):
    """This is FabricPooledVlan class."""

    consts = FabricPooledVlanConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricPooledVlan", "fabricPooledVlan", "net-[name]", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricNetGroup'], ['faultInst'], ["Add", "Get", "Remove"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_issues": MoPropertyMeta("config_issues", "configIssues", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|named-vlan-unresolved),){0,2}(defaultValue|not-applicable|named-vlan-unresolved){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "poolable_dn": MoPropertyMeta("poolable_dn", "poolableDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "prev_assigned_to_dn": MoPropertyMeta("prev_assigned_to_dn", "prevAssignedToDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "assigned": "assigned", 
        "assignedToDn": "assigned_to_dn", 
        "childAction": "child_action", 
        "configIssues": "config_issues", 
        "dn": "dn", 
        "name": "name", 
        "peerDn": "peer_dn", 
        "poolableDn": "poolable_dn", 
        "prevAssignedToDn": "prev_assigned_to_dn", 
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
        self.config_issues = None
        self.peer_dn = None
        self.poolable_dn = None
        self.prev_assigned_to_dn = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FabricPooledVlan", parent_mo_or_dn, **kwargs)
