"""This module contains the general information for AaaLoginProfile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AaaLoginProfileConsts:
    ADMIN_STATE_DISABLE = "disable"
    ADMIN_STATE_ENABLE = "enable"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class AaaLoginProfile(ManagedObject):
    """This is AaaLoginProfile class."""

    consts = AaaLoginProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AaaLoginProfile", "aaaLoginProfile", "login-profile", VersionMeta.Version401a, "InputOutput", 0xfff, [], ["aaa", "admin"], ['aaaUserEp'], [], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disable", "enable"], []),
        "attempted_within": MoPropertyMeta("attempted_within", "attemptedWithin", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1-65535"]),
        "block_login": MoPropertyMeta("block_login", "blockLogin", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-65535"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, 0x10, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "failed_attempts": MoPropertyMeta("failed_attempts", "failedAttempts", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["1-65535"]),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version401a, MoPropertyMeta.CREATE_ONLY, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "attemptedWithin": "attempted_within", 
        "blockLogin": "block_login", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "failedAttempts": "failed_attempts", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.attempted_within = None
        self.block_login = None
        self.child_action = None
        self.descr = None
        self.failed_attempts = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AaaLoginProfile", parent_mo_or_dn, **kwargs)
