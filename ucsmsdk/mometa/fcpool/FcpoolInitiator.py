"""This module contains the general information for FcpoolInitiator ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FcpoolInitiatorConsts:
    ASSIGNED_FALSE = "false"
    ASSIGNED_NO = "no"
    ASSIGNED_TRUE = "true"
    ASSIGNED_YES = "yes"
    PURPOSE_DERIVED = "derived"
    PURPOSE_NODE_WWN = "node-wwn"
    PURPOSE_PORT_WWN = "port-wwn"


class FcpoolInitiator(ManagedObject):
    """This is FcpoolInitiator class."""

    consts = FcpoolInitiatorConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("FcpoolInitiator", "fcpoolInitiator", "[id]", VersionMeta.Version101e, "InputOutput", 0xff, [], ["admin", "ls-storage-policy"], ['fcpoolInitiators'], ['fcpoolBootTarget', 'fcpoolInitiatorEp'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "poolable_dn": MoPropertyMeta("poolable_dn", "poolableDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "prev_assigned_to_dn": MoPropertyMeta("prev_assigned_to_dn", "prevAssignedToDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "purpose": MoPropertyMeta("purpose", "purpose", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["derived", "node-wwn", "port-wwn"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "assigned": "assigned", 
        "assignedToDn": "assigned_to_dn", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "id": "id", 
        "name": "name", 
        "poolableDn": "poolable_dn", 
        "prevAssignedToDn": "prev_assigned_to_dn", 
        "purpose": "purpose", 
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
        self.descr = None
        self.name = None
        self.poolable_dn = None
        self.prev_assigned_to_dn = None
        self.purpose = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FcpoolInitiator", parent_mo_or_dn, **kwargs)
