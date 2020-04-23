"""This module contains the general information for PolicyScope ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PolicyScopeConsts:
    RESOLVE_TYPE_NAME = "name"
    RESOLVE_TYPE_RN = "rn"


class PolicyScope(ManagedObject):
    """This is PolicyScope class."""

    consts = PolicyScopeConsts()
    naming_props = set(['policyType', 'resolveType', 'policyName'])

    mo_meta = MoMeta("PolicyScope", "policyScope", "scope-[policy_type]-[resolve_type]-[policy_name]", VersionMeta.Version321d, "InputOutput", 0xff, [], ["read-only"], ['policyContext'], ['policyPolicyDestClass', 'policyRequestor'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "policy_name": MoPropertyMeta("policy_name", "policyName", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "policy_type": MoPropertyMeta("policy_type", "policyType", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []),
        "resolve_type": MoPropertyMeta("resolve_type", "resolveType", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x20, None, None, None, ["name", "rn"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "policyName": "policy_name", 
        "policyType": "policy_type", 
        "resolveType": "resolve_type", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, policy_type, resolve_type, policy_name, **kwargs):
        self._dirty_mask = 0
        self.policy_type = policy_type
        self.resolve_type = resolve_type
        self.policy_name = policy_name
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PolicyScope", parent_mo_or_dn, **kwargs)
