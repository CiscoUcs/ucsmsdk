"""This module contains the general information for PolicyIdResolvePolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PolicyIdResolvePolicyConsts:
    ID_ASSIGNMENT_MODE_LOOSE_DUPLICATE_CHECK = "loose-duplicate-check"
    ID_ASSIGNMENT_MODE_NO_DUPLICATE_CHECK = "no-duplicate-check"
    ID_ASSIGNMENT_MODE_STRICT_DUPLICATE_CHECK = "strict-duplicate-check"


class PolicyIdResolvePolicy(ManagedObject):
    """This is PolicyIdResolvePolicy class."""

    consts = PolicyIdResolvePolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("PolicyIdResolvePolicy", "policyIdResolvePolicy", "id-policy", VersionMeta.Version223a, "InputOutput", 0x3f, [], ["admin", "operations"], ['policyControlEp'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id_assignment_mode": MoPropertyMeta("id_assignment_mode", "idAssignmentMode", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["loose-duplicate-check", "no-duplicate-check", "strict-duplicate-check"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "idAssignmentMode": "id_assignment_mode", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.id_assignment_mode = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PolicyIdResolvePolicy", parent_mo_or_dn, **kwargs)
