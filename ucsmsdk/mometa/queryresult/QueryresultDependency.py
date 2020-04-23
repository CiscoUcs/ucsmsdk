"""This module contains the general information for QueryresultDependency ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class QueryresultDependencyConsts:
    IS_IMPORTABLE_FALSE = "false"
    IS_IMPORTABLE_NO = "no"
    IS_IMPORTABLE_TRUE = "true"
    IS_IMPORTABLE_YES = "yes"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class QueryresultDependency(ManagedObject):
    """This is QueryresultDependency class."""

    consts = QueryresultDependencyConsts()
    naming_props = set(['refConvertedDn'])

    mo_meta = MoMeta("QueryresultDependency", "queryresultDependency", "dependency-[ref_converted_dn]", VersionMeta.Version221b, "InputOutput", 0x3f, [], ["admin"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "class_type": MoPropertyMeta("class_type", "classType", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "is_importable": MoPropertyMeta("is_importable", "isImportable", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy"], []),
        "ref_converted_dn": MoPropertyMeta("ref_converted_dn", "refConvertedDn", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "ref_dn": MoPropertyMeta("ref_dn", "refDn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "ref_name": MoPropertyMeta("ref_name", "refName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "classType": "class_type", 
        "dn": "dn", 
        "isImportable": "is_importable", 
        "policyOwner": "policy_owner", 
        "refConvertedDn": "ref_converted_dn", 
        "refDn": "ref_dn", 
        "refName": "ref_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, ref_converted_dn, **kwargs):
        self._dirty_mask = 0
        self.ref_converted_dn = ref_converted_dn
        self.child_action = None
        self.class_type = None
        self.is_importable = None
        self.policy_owner = None
        self.ref_dn = None
        self.ref_name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "QueryresultDependency", parent_mo_or_dn, **kwargs)
