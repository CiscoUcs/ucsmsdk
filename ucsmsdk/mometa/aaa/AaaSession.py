"""This module contains the general information for AaaSession ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AaaSessionConsts:
    INT_DEL_FALSE = "false"
    INT_DEL_NO = "no"
    INT_DEL_TRUE = "true"
    INT_DEL_YES = "yes"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    UI_EP = "ep"
    UI_KVM = "kvm"
    UI_NONE = "none"
    UI_SHELL = "shell"
    UI_SOL = "sol"
    UI_VMEDIA = "vmedia"
    UI_WEB = "web"


class AaaSession(ManagedObject):
    """This is AaaSession class."""

    consts = AaaSessionConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AaaSession", "aaaSession", "term-[id]", VersionMeta.Version101e, "InputOutput", 0x3f, [], ["aaa", "admin"], ['aaaRemoteUser', 'aaaUser'], [], ["Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "host": MoPropertyMeta("host", "host", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, 1, 32, None, [], []),
        "int_del": MoPropertyMeta("int_del", "intDel", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "login_time": MoPropertyMeta("login_time", "loginTime", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "pid": MoPropertyMeta("pid", "pid", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "refresh_period": MoPropertyMeta("refresh_period", "refreshPeriod", "uint", VersionMeta.Version203a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "session_timeout": MoPropertyMeta("session_timeout", "sessionTimeout", "uint", VersionMeta.Version203a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "term": MoPropertyMeta("term", "term", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 16, None, [], []),
        "ui": MoPropertyMeta("ui", "ui", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ep", "kvm", "none", "shell", "sol", "vmedia", "web"], []),
        "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "host": "host", 
        "id": "id", 
        "intDel": "int_del", 
        "loginTime": "login_time", 
        "pid": "pid", 
        "refreshPeriod": "refresh_period", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sessionTimeout": "session_timeout", 
        "status": "status", 
        "switchId": "switch_id", 
        "term": "term", 
        "ui": "ui", 
        "user": "user", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.host = None
        self.int_del = None
        self.login_time = None
        self.pid = None
        self.refresh_period = None
        self.sacl = None
        self.session_timeout = None
        self.status = None
        self.switch_id = None
        self.term = None
        self.ui = None
        self.user = None

        ManagedObject.__init__(self, "AaaSession", parent_mo_or_dn, **kwargs)
