"""This module contains the general information for AaaSessionInfo ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AaaSessionInfoConsts:
    TYPE_ALL = "all"
    TYPE_KVM = "kvm"
    TYPE_SOL = "sol"
    TYPE_VMEDIA = "vmedia"
    USER_TYPE_IPMI = "ipmi"
    USER_TYPE_LOCAL = "local"
    USER_TYPE_REMOTE = "remote"


class AaaSessionInfo(ManagedObject):
    """This is AaaSessionInfo class."""

    consts = AaaSessionInfoConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AaaSessionInfo", "aaaSessionInfo", "term-[id]", VersionMeta.Version212a, "InputOutput", 0x1fff, [], ["aaa", "admin"], ['aaaSessionInfoTable'], [], [None])

    prop_meta = {
        "address": MoPropertyMeta("address", "address", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version212a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dest_ip": MoPropertyMeta("dest_ip", "destIp", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "etime": MoPropertyMeta("etime", "etime", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version212a, MoPropertyMeta.NAMING, 0x40, 1, 510, None, [], []),
        "priv": MoPropertyMeta("priv", "priv", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["all", "kvm", "sol", "vmedia"], []),
        "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x800, 0, 510, None, [], []),
        "user_type": MoPropertyMeta("user_type", "userType", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["ipmi", "local", "remote"], []),
    }

    prop_map = {
        "address": "address", 
        "childAction": "child_action", 
        "destIp": "dest_ip", 
        "dn": "dn", 
        "etime": "etime", 
        "id": "id", 
        "priv": "priv", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
        "user": "user", 
        "userType": "user_type", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.address = None
        self.child_action = None
        self.dest_ip = None
        self.etime = None
        self.priv = None
        self.sacl = None
        self.status = None
        self.type = None
        self.user = None
        self.user_type = None

        ManagedObject.__init__(self, "AaaSessionInfo", parent_mo_or_dn, **kwargs)
