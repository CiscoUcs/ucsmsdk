"""This module contains the general information for CommSnmpUser ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CommSnmpUserConsts:
    AUTH_MD5 = "md5"
    AUTH_SHA = "sha"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_OK = "ok"
    PRIV_PWD_SET_FALSE = "false"
    PRIV_PWD_SET_NO = "no"
    PRIV_PWD_SET_TRUE = "true"
    PRIV_PWD_SET_YES = "yes"
    PWD_SET_FALSE = "false"
    PWD_SET_NO = "no"
    PWD_SET_TRUE = "true"
    PWD_SET_YES = "yes"
    USE_AES_FALSE = "false"
    USE_AES_NO = "no"
    USE_AES_TRUE = "true"
    USE_AES_YES = "yes"


class CommSnmpUser(ManagedObject):
    """This is CommSnmpUser class."""

    consts = CommSnmpUserConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("CommSnmpUser", "commSnmpUser", "snmpv3-user-[name]", VersionMeta.Version101e, "InputOutput", 0x7ff, [], ["aaa", "admin"], ['commSnmp'], ['aaaCimcSession', 'faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "auth": MoPropertyMeta("auth", "auth", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["md5", "sha"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applied", "ok"], []),
        "config_status_message": MoPropertyMeta("config_status_message", "configStatusMessage", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, None, None, r"""[a-zA-Z][a-zA-Z0-9_.@-]{0,31}""", [], []),
        "priv_pwd_set": MoPropertyMeta("priv_pwd_set", "privPwdSet", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "privpwd": MoPropertyMeta("privpwd", "privpwd", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,127}""", [], []),
        "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,127}""", [], []),
        "pwd_set": MoPropertyMeta("pwd_set", "pwdSet", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "use_aes": MoPropertyMeta("use_aes", "useAes", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["false", "no", "true", "yes"], []),
    }

    prop_map = {
        "auth": "auth", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "configStatusMessage": "config_status_message", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "privPwdSet": "priv_pwd_set", 
        "privpwd": "privpwd", 
        "pwd": "pwd", 
        "pwdSet": "pwd_set", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "useAes": "use_aes", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.auth = None
        self.child_action = None
        self.config_state = None
        self.config_status_message = None
        self.descr = None
        self.priv_pwd_set = None
        self.privpwd = None
        self.pwd = None
        self.pwd_set = None
        self.sacl = None
        self.status = None
        self.use_aes = None

        ManagedObject.__init__(self, "CommSnmpUser", parent_mo_or_dn, **kwargs)
