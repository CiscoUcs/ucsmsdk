"""This module contains the general information for AaaDefaultAuth ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AaaDefaultAuthConsts:
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_OK = "ok"
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


class AaaDefaultAuth(ManagedObject):
    """This is AaaDefaultAuth class."""

    consts = AaaDefaultAuthConsts()
    naming_props = set([])

    mo_meta = MoMeta("AaaDefaultAuth", "aaaDefaultAuth", "default-auth", VersionMeta.Version141i, "InputOutput", 0xfff, [], ["aaa", "admin"], ['aaaAuthRealm'], ['faultInst'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applied", "ok"], []),
        "config_status_message": MoPropertyMeta("config_status_message", "configStatusMessage", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_provider_group": MoPropertyMeta("oper_provider_group", "operProviderGroup", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 127, None, [], []),
        "oper_realm": MoPropertyMeta("oper_realm", "operRealm", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ldap", "local", "none", "radius", "tacacs"], []),
        "provider_group": MoPropertyMeta("provider_group", "providerGroup", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, 0, 127, None, [], []),
        "realm": MoPropertyMeta("realm", "realm", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["ldap", "local", "none", "radius", "tacacs"], []),
        "refresh_period": MoPropertyMeta("refresh_period", "refreshPeriod", "uint", VersionMeta.Version203a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["60-172800"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "session_timeout": MoPropertyMeta("session_timeout", "sessionTimeout", "uint", VersionMeta.Version203a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], ["300-172800"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "use2_factor": MoPropertyMeta("use2_factor", "use2Factor", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["false", "no", "true", "yes"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configState": "config_state", 
        "configStatusMessage": "config_status_message", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "operProviderGroup": "oper_provider_group", 
        "operRealm": "oper_realm", 
        "providerGroup": "provider_group", 
        "realm": "realm", 
        "refreshPeriod": "refresh_period", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sessionTimeout": "session_timeout", 
        "status": "status", 
        "use2Factor": "use2_factor", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.config_state = None
        self.config_status_message = None
        self.descr = None
        self.name = None
        self.oper_provider_group = None
        self.oper_realm = None
        self.provider_group = None
        self.realm = None
        self.refresh_period = None
        self.sacl = None
        self.session_timeout = None
        self.status = None
        self.use2_factor = None

        ManagedObject.__init__(self, "AaaDefaultAuth", parent_mo_or_dn, **kwargs)
