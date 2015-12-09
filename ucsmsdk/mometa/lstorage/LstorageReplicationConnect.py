"""This module contains the general information for LstorageReplicationConnect ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageReplicationConnectConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class LstorageReplicationConnect(ManagedObject):
    """This is LstorageReplicationConnect class."""

    consts = LstorageReplicationConnectConsts()
    naming_props = set([u'hostname'])

    mo_meta = MoMeta("LstorageReplicationConnect", "lstorageReplicationConnect", "repl-connect-[hostname]", VersionMeta.Version302c, "InputOutput", 0xfffL, [], ["admin", "ls-storage", "ls-storage-policy"], [u'lstorageLunReplicationPolicy'], [], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x20L, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.CREATE_ONLY, 0x40L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "owner_policy": MoPropertyMeta("owner_policy", "ownerPolicy", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x100L, 0, 64, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x200L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x400L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x800L, 0, 510, None, [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "hostname": "hostname", 
        "intId": "int_id", 
        "name": "name", 
        "ownerPolicy": "owner_policy", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "pwd": "pwd", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "user": "user", 
    }

    def __init__(self, parent_mo_or_dn, hostname, **kwargs):
        self._dirty_mask = 0
        self.hostname = hostname
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.owner_policy = None
        self.policy_level = None
        self.policy_owner = None
        self.pwd = None
        self.sacl = None
        self.status = None
        self.user = None

        ManagedObject.__init__(self, "LstorageReplicationConnect", parent_mo_or_dn, **kwargs)

