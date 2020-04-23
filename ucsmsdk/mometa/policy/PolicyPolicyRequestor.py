"""This module contains the general information for PolicyPolicyRequestor ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PolicyPolicyRequestorConsts:
    pass


class PolicyPolicyRequestor(ManagedObject):
    """This is PolicyPolicyRequestor class."""

    consts = PolicyPolicyRequestorConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("PolicyPolicyRequestor", "policyPolicyRequestor", "requestor-[name]", VersionMeta.Version211a, "InputOutput", 0x7f, [], ["admin"], ['policyPolicyScope'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "on_behalf_of_ident": MoPropertyMeta("on_behalf_of_ident", "onBehalfOfIdent", "string", VersionMeta.Version211a, MoPropertyMeta.CREATE_ONLY, 0x10, 0, 510, None, [], []),
        "on_behalf_of_type": MoPropertyMeta("on_behalf_of_type", "onBehalfOfType", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "resolved_class_type": MoPropertyMeta("resolved_class_type", "resolvedClassType", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "onBehalfOfIdent": "on_behalf_of_ident", 
        "onBehalfOfType": "on_behalf_of_type", 
        "resolvedClassType": "resolved_class_type", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.on_behalf_of_ident = None
        self.on_behalf_of_type = None
        self.resolved_class_type = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PolicyPolicyRequestor", parent_mo_or_dn, **kwargs)
