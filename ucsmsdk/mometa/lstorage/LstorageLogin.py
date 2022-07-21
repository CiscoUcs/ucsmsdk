"""This module contains the general information for LstorageLogin ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LstorageLoginConsts:
    PWD_SET_FALSE = "false"
    PWD_SET_NO = "no"
    PWD_SET_TRUE = "true"
    PWD_SET_YES = "yes"


class LstorageLogin(ManagedObject):
    """This is LstorageLogin class."""

    consts = LstorageLoginConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageLogin", "lstorageLogin", "login", VersionMeta.Version321d, "InputOutput", 0xff, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-storage", "ls-storage-policy"], ['lstorageRemote', 'lstorageRemoteDef'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,255}""", [], []),
        "pwd_set": MoPropertyMeta("pwd_set", "pwdSet", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "user_name": MoPropertyMeta("user_name", "userName", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[a-zA-Z][a-zA-Z0-9_.-]{0,255}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "password": "password", 
        "pwdSet": "pwd_set", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "userName": "user_name", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.password = None
        self.pwd_set = None
        self.sacl = None
        self.status = None
        self.user_name = None

        ManagedObject.__init__(self, "LstorageLogin", parent_mo_or_dn, **kwargs)
