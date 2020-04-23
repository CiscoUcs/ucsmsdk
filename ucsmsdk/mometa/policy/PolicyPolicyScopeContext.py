"""This module contains the general information for PolicyPolicyScopeContext ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PolicyPolicyScopeContextConsts:
    pass


class PolicyPolicyScopeContext(ManagedObject):
    """This is PolicyPolicyScopeContext class."""

    consts = PolicyPolicyScopeContextConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("PolicyPolicyScopeContext", "policyPolicyScopeContext", "context-[name]", VersionMeta.Version211a, "InputOutput", 0x7f, [], ["admin"], ['policyPolicyScopeCont'], ['policyPolicyScope'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "context": MoPropertyMeta("context", "context", "string", VersionMeta.Version211a, MoPropertyMeta.CREATE_ONLY, 0x4, 0, 256, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "context": "context", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.context = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PolicyPolicyScopeContext", parent_mo_or_dn, **kwargs)
