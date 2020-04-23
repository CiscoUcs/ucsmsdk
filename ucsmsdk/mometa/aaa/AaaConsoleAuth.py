"""This module contains the general information for AaaConsoleAuth ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AaaConsoleAuthConsts:
    OPER_REALM_LDAP = "ldap"
    OPER_REALM_LOCAL = "local"
    OPER_REALM_NONE = "none"
    OPER_REALM_RADIUS = "radius"
    OPER_REALM_TACACS = "tacacs"
    REALM_LDAP = "ldap"
    REALM_LOCAL = "local"
    REALM_NONE = "none"
    REALM_RADIUS = "radius"
    REALM_TACACS = "tacacs"
    USE2_FACTOR_FALSE = "false"
    USE2_FACTOR_NO = "no"
    USE2_FACTOR_TRUE = "true"
    USE2_FACTOR_YES = "yes"


class AaaConsoleAuth(ManagedObject):
    """This is AaaConsoleAuth class."""

    consts = AaaConsoleAuthConsts()
    naming_props = set([])

    mo_meta = MoMeta("AaaConsoleAuth", "aaaConsoleAuth", "console-auth", VersionMeta.Version141i, "InputOutput", 0x3ff, [], ["aaa", "admin"], ['aaaAuthRealm'], ['faultInst'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_provider_group": MoPropertyMeta("oper_provider_group", "operProviderGroup", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 127, None, [], []),
        "oper_realm": MoPropertyMeta("oper_realm", "operRealm", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ldap", "local", "none", "radius", "tacacs"], []),
        "provider_group": MoPropertyMeta("provider_group", "providerGroup", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, 0, 127, None, [], []),
        "realm": MoPropertyMeta("realm", "realm", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["ldap", "local", "none", "radius", "tacacs"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "use2_factor": MoPropertyMeta("use2_factor", "use2Factor", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["false", "no", "true", "yes"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "operProviderGroup": "oper_provider_group", 
        "operRealm": "oper_realm", 
        "providerGroup": "provider_group", 
        "realm": "realm", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "use2Factor": "use2_factor", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.name = None
        self.oper_provider_group = None
        self.oper_realm = None
        self.provider_group = None
        self.realm = None
        self.sacl = None
        self.status = None
        self.use2_factor = None

        ManagedObject.__init__(self, "AaaConsoleAuth", parent_mo_or_dn, **kwargs)
