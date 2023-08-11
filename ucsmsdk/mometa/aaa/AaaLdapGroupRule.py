"""This module contains the general information for AaaLdapGroupRule ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AaaLdapGroupRuleConsts:
    AUTHORIZATION_DISABLE = "disable"
    AUTHORIZATION_ENABLE = "enable"
    TRAVERSAL_NON_RECURSIVE = "non-recursive"
    TRAVERSAL_RECURSIVE = "recursive"
    USE_PRIMARY_GROUP_FALSE = "false"
    USE_PRIMARY_GROUP_NO = "no"
    USE_PRIMARY_GROUP_TRUE = "true"
    USE_PRIMARY_GROUP_YES = "yes"


class AaaLdapGroupRule(ManagedObject):
    """This is AaaLdapGroupRule class."""

    consts = AaaLdapGroupRuleConsts()
    naming_props = set([])

    mo_meta = MoMeta("AaaLdapGroupRule", "aaaLdapGroupRule", "ldapgroup-rule", VersionMeta.Version141i, "InputOutput", 0x7ff, [], ["aaa", "admin"], ['aaaLdapEp', 'aaaLdapProvider'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "authorization": MoPropertyMeta("authorization", "authorization", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disable", "enable"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "target_attr": MoPropertyMeta("target_attr", "targetAttr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[ !#$%&\(\)\*\+,\-\.:;=\?@\[\]_\{\|\}~a-zA-Z0-9]{0,63}""", [], []),
        "traversal": MoPropertyMeta("traversal", "traversal", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["non-recursive", "recursive"], []),
        "use_primary_group": MoPropertyMeta("use_primary_group", "usePrimaryGroup", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["false", "no", "true", "yes"], []),
    }

    prop_map = {
        "authorization": "authorization", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "targetAttr": "target_attr", 
        "traversal": "traversal", 
        "usePrimaryGroup": "use_primary_group", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.authorization = None
        self.child_action = None
        self.descr = None
        self.name = None
        self.sacl = None
        self.status = None
        self.target_attr = None
        self.traversal = None
        self.use_primary_group = None

        ManagedObject.__init__(self, "AaaLdapGroupRule", parent_mo_or_dn, **kwargs)
