"""This module contains the general information for PolicyConfigError ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PolicyConfigErrorConsts:
    pass


class PolicyConfigError(ManagedObject):
    """This is PolicyConfigError class."""

    consts = PolicyConfigErrorConsts()
    naming_props = set([])

    mo_meta = MoMeta("PolicyConfigError", "policyConfigError", "policy-error", VersionMeta.Version321d, "InputOutput", 0x1f, [], ["read-only"], ['policyPolicyScopeCont'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "error_code": MoPropertyMeta("error_code", "errorCode", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "error_descr": MoPropertyMeta("error_descr", "errorDescr", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "error_location": MoPropertyMeta("error_location", "errorLocation", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "timestamp": MoPropertyMeta("timestamp", "timestamp", "ulong", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "errorCode": "error_code", 
        "errorDescr": "error_descr", 
        "errorLocation": "error_location", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "timestamp": "timestamp", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.error_code = None
        self.error_descr = None
        self.error_location = None
        self.sacl = None
        self.status = None
        self.timestamp = None

        ManagedObject.__init__(self, "PolicyConfigError", parent_mo_or_dn, **kwargs)
