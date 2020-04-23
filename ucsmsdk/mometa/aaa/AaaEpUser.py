"""This module contains the general information for AaaEpUser ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AaaEpUserConsts:
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_OK = "ok"
    IS_PWD_ENC_FALSE = "false"
    IS_PWD_ENC_NO = "no"
    IS_PWD_ENC_TRUE = "true"
    IS_PWD_ENC_YES = "yes"
    PRIV_ADMIN = "admin"
    PRIV_READONLY = "readonly"
    PWD_SET_FALSE = "false"
    PWD_SET_NO = "no"
    PWD_SET_TRUE = "true"
    PWD_SET_YES = "yes"


class AaaEpUser(ManagedObject):
    """This is AaaEpUser class."""

    consts = AaaEpUserConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("AaaEpUser", "aaaEpUser", "user-[name]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["aaa", "admin", "ls-security", "ls-security-policy"], ['aaaEpAuthProfile', 'computeServerUnit'], ['aaaCimcSession'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applied", "ok"], []),
        "config_status_message": MoPropertyMeta("config_status_message", "configStatusMessage", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "is_pwd_enc": MoPropertyMeta("is_pwd_enc", "isPwdEnc", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10, None, None, r"""[a-zA-Z][a-zA-Z0-9_.@-]{0,15}""", [], []),
        "priv": MoPropertyMeta("priv", "priv", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["admin", "readonly"], []),
        "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{1,20}""", [], []),
        "pwd_set": MoPropertyMeta("pwd_set", "pwdSet", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configState": "config_state", 
        "configStatusMessage": "config_status_message", 
        "descr": "descr", 
        "dn": "dn", 
        "isPwdEnc": "is_pwd_enc", 
        "name": "name", 
        "priv": "priv", 
        "pwd": "pwd", 
        "pwdSet": "pwd_set", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.config_state = None
        self.config_status_message = None
        self.descr = None
        self.is_pwd_enc = None
        self.priv = None
        self.pwd = None
        self.pwd_set = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AaaEpUser", parent_mo_or_dn, **kwargs)
