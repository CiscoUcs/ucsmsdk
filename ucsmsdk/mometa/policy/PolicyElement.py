"""This module contains the general information for PolicyElement ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PolicyElementConsts:
    OWNERSHIP_LOCAL = "local"
    OWNERSHIP_PENDING_POLICY = "pending-policy"
    OWNERSHIP_POLICY = "policy"


class PolicyElement(ManagedObject):
    """This is PolicyElement class."""

    consts = PolicyElementConsts()
    naming_props = set(['convertedDn'])

    mo_meta = MoMeta("PolicyElement", "policyElement", "element-[converted_dn]", VersionMeta.Version212a, "InputOutput", 0x3f, [], ["admin"], ['policyLocalMap'], ['policyRefReq'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version212a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "class_type": MoPropertyMeta("class_type", "classType", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "converted_dn": MoPropertyMeta("converted_dn", "convertedDn", "string", VersionMeta.Version212a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "ownership": MoPropertyMeta("ownership", "ownership", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy"], []),
        "policy_dn": MoPropertyMeta("policy_dn", "policyDn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "classType": "class_type", 
        "convertedDn": "converted_dn", 
        "dn": "dn", 
        "ownership": "ownership", 
        "policyDn": "policy_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, converted_dn, **kwargs):
        self._dirty_mask = 0
        self.converted_dn = converted_dn
        self.child_action = None
        self.class_type = None
        self.ownership = None
        self.policy_dn = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PolicyElement", parent_mo_or_dn, **kwargs)
