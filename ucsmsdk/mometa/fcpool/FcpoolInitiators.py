"""This module contains the general information for FcpoolInitiators ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FcpoolInitiatorsConsts:
    ASSIGNMENT_ORDER_DEFAULT = "default"
    ASSIGNMENT_ORDER_SEQUENTIAL = "sequential"
    INT_ID_NONE = "none"
    MAX_PORTS_PER_NODE_UPTO15 = "upto15"
    MAX_PORTS_PER_NODE_UPTO3 = "upto3"
    MAX_PORTS_PER_NODE_UPTO31 = "upto31"
    MAX_PORTS_PER_NODE_UPTO63 = "upto63"
    MAX_PORTS_PER_NODE_UPTO7 = "upto7"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PURPOSE_NODE_AND_PORT_WWN_ASSIGNMENT = "node-and-port-wwn-assignment"
    PURPOSE_NODE_WWN_ASSIGNMENT = "node-wwn-assignment"
    PURPOSE_PORT_WWN_ASSIGNMENT = "port-wwn-assignment"


class FcpoolInitiators(ManagedObject):
    """This is FcpoolInitiators class."""

    consts = FcpoolInitiatorsConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FcpoolInitiators", "fcpoolInitiators", "wwn-pool-[name]", VersionMeta.Version101e, "InputOutput", 0x7ff, [], ["admin", "ls-storage-policy"], ['orgOrg'], ['faultInst', 'fcpoolBlock', 'fcpoolInitiator'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "assignment_order": MoPropertyMeta("assignment_order", "assignmentOrder", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["default", "sequential"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "max_ports_per_node": MoPropertyMeta("max_ports_per_node", "maxPortsPerNode", "string", VersionMeta.Version211a, MoPropertyMeta.CREATE_ONLY, 0x20, None, None, None, ["upto15", "upto3", "upto31", "upto63", "upto7"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "purpose": MoPropertyMeta("purpose", "purpose", "string", VersionMeta.Version101e, MoPropertyMeta.CREATE_ONLY, 0x100, None, None, None, ["node-and-port-wwn-assignment", "node-wwn-assignment", "port-wwn-assignment"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "size": MoPropertyMeta("size", "size", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "assigned": "assigned", 
        "assignmentOrder": "assignment_order", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "maxPortsPerNode": "max_ports_per_node", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "purpose": "purpose", 
        "rn": "rn", 
        "sacl": "sacl", 
        "size": "size", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.assigned = None
        self.assignment_order = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.max_ports_per_node = None
        self.policy_level = None
        self.policy_owner = None
        self.purpose = None
        self.sacl = None
        self.size = None
        self.status = None

        ManagedObject.__init__(self, "FcpoolInitiators", parent_mo_or_dn, **kwargs)
