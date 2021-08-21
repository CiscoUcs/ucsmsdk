"""This module contains the general information for AaaPwdProfile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AaaPwdProfileConsts:
    CHANGE_DURING_INTERVAL_DISABLE = "disable"
    CHANGE_DURING_INTERVAL_ENABLE = "enable"
    ENABLE_PWDEXPIRY_FALSE = "false"
    ENABLE_PWDEXPIRY_NO = "no"
    ENABLE_PWDEXPIRY_TRUE = "true"
    ENABLE_PWDEXPIRY_YES = "yes"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class AaaPwdProfile(ManagedObject):
    """This is AaaPwdProfile class."""

    consts = AaaPwdProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AaaPwdProfile", "aaaPwdProfile", "pwd-profile", VersionMeta.Version201m, "InputOutput", 0x1ffff, [], ["aaa", "admin"], ['aaaUserEp'], [], ["Get", "Set"])

    prop_meta = {
        "change_count": MoPropertyMeta("change_count", "changeCount", "byte", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-10"]),
        "change_during_interval": MoPropertyMeta("change_during_interval", "changeDuringInterval", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["disable", "enable"], []),
        "change_interval": MoPropertyMeta("change_interval", "changeInterval", "ushort", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-745"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x10, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "enable_pwd_expiry": MoPropertyMeta("enable_pwd_expiry", "enablePWDExpiry", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["false", "no", "true", "yes"], []),
        "expiration_period": MoPropertyMeta("expiration_period", "expirationPeriod", "byte", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["1-180"]),
        "expiration_warn_time": MoPropertyMeta("expiration_warn_time", "expirationWarnTime", "byte", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], ["0-30"]),
        "history_count": MoPropertyMeta("history_count", "historyCount", "byte", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], ["0-15"]),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "min_passphrase_len": MoPropertyMeta("min_passphrase_len", "minPassphraseLen", "byte", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, [], ["6-80"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201m, MoPropertyMeta.CREATE_ONLY, 0x1000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "no_change_interval": MoPropertyMeta("no_change_interval", "noChangeInterval", "ushort", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, [], ["1-745"]),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x8000, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x10000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "changeCount": "change_count", 
        "changeDuringInterval": "change_during_interval", 
        "changeInterval": "change_interval", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "enablePWDExpiry": "enable_pwd_expiry", 
        "expirationPeriod": "expiration_period", 
        "expirationWarnTime": "expiration_warn_time", 
        "historyCount": "history_count", 
        "intId": "int_id", 
        "minPassphraseLen": "min_passphrase_len", 
        "name": "name", 
        "noChangeInterval": "no_change_interval", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.change_count = None
        self.change_during_interval = None
        self.change_interval = None
        self.child_action = None
        self.descr = None
        self.enable_pwd_expiry = None
        self.expiration_period = None
        self.expiration_warn_time = None
        self.history_count = None
        self.int_id = None
        self.min_passphrase_len = None
        self.name = None
        self.no_change_interval = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AaaPwdProfile", parent_mo_or_dn, **kwargs)
