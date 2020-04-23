"""This module contains the general information for IqnpoolPool ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class IqnpoolPoolConsts:
    ASSIGNMENT_ORDER_DEFAULT = "default"
    ASSIGNMENT_ORDER_SEQUENTIAL = "sequential"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class IqnpoolPool(ManagedObject):
    """This is IqnpoolPool class."""

    consts = IqnpoolPoolConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("IqnpoolPool", "iqnpoolPool", "iqn-pool-[name]", VersionMeta.Version201m, "InputOutput", 0x3ff, [], ["admin", "ls-storage-policy"], ['orgOrg'], ['faultInst', 'iqnpoolBlock', 'iqnpoolPooled'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "assignment_order": MoPropertyMeta("assignment_order", "assignmentOrder", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["default", "sequential"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "prefix": MoPropertyMeta("prefix", "prefix", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[0-9a-zA-Z\.:-]{1,150}$""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "size": MoPropertyMeta("size", "size", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "assigned": "assigned", 
        "assignmentOrder": "assignment_order", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "prefix": "prefix", 
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
        self.policy_level = None
        self.policy_owner = None
        self.prefix = None
        self.sacl = None
        self.size = None
        self.status = None

        ManagedObject.__init__(self, "IqnpoolPool", parent_mo_or_dn, **kwargs)
