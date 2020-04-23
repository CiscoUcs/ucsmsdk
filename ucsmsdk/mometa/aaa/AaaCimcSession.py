"""This module contains the general information for AaaCimcSession ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AaaCimcSessionConsts:
    ADMIN_STATE_ACTIVE = "active"
    ADMIN_STATE_INACTIVE = "inactive"
    INT_DEL_FALSE = "false"
    INT_DEL_NO = "no"
    INT_DEL_TRUE = "true"
    INT_DEL_YES = "yes"
    IS_DELETE_NO = "no"
    IS_DELETE_YES = "yes"
    TYPE_ALL = "all"
    TYPE_KVM = "kvm"
    TYPE_SOL = "sol"
    TYPE_VMEDIA = "vmedia"


class AaaCimcSession(ManagedObject):
    """This is AaaCimcSession class."""

    consts = AaaCimcSessionConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AaaCimcSession", "aaaCimcSession", "cimc-term-[id]", VersionMeta.Version212a, "InputOutput", 0x7f, [], ["admin"], ['aaaEpUser', 'aaaRemoteUser', 'aaaUser', 'commSnmpUser', 'storageEpUser'], [], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "inactive"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version212a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cimc_addr": MoPropertyMeta("cimc_addr", "cimcAddr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version212a, MoPropertyMeta.NAMING, 0x8, 1, 32, None, [], []),
        "int_del": MoPropertyMeta("int_del", "intDel", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "is_delete": MoPropertyMeta("is_delete", "isDelete", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["no", "yes"], []),
        "last_updated_time": MoPropertyMeta("last_updated_time", "lastUpdatedTime", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "login_time": MoPropertyMeta("login_time", "loginTime", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "ls_dn": MoPropertyMeta("ls_dn", "lsDn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "pid": MoPropertyMeta("pid", "pid", "uint", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pn_dn": MoPropertyMeta("pn_dn", "pnDn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "priv": MoPropertyMeta("priv", "priv", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "source_addr": MoPropertyMeta("source_addr", "sourceAddr", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "kvm", "sol", "vmedia"], []),
        "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "cimcAddr": "cimc_addr", 
        "dn": "dn", 
        "id": "id", 
        "intDel": "int_del", 
        "isDelete": "is_delete", 
        "lastUpdatedTime": "last_updated_time", 
        "loginTime": "login_time", 
        "lsDn": "ls_dn", 
        "pid": "pid", 
        "pnDn": "pn_dn", 
        "priv": "priv", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sourceAddr": "source_addr", 
        "status": "status", 
        "type": "type", 
        "user": "user", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_state = None
        self.child_action = None
        self.cimc_addr = None
        self.int_del = None
        self.is_delete = None
        self.last_updated_time = None
        self.login_time = None
        self.ls_dn = None
        self.pid = None
        self.pn_dn = None
        self.priv = None
        self.sacl = None
        self.source_addr = None
        self.status = None
        self.type = None
        self.user = None

        ManagedObject.__init__(self, "AaaCimcSession", parent_mo_or_dn, **kwargs)
