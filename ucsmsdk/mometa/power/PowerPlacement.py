"""This module contains the general information for PowerPlacement ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PowerPlacementConsts:
    INT_ID_NONE = "none"
    PEER_REQ_CONFLICT_FAIL_PLACEMENT = "fail-placement"
    PEER_REQ_CONFLICT_IGNORE = "ignore"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PRIO_SHARE_HIGHEST_PRIO_IN_CHASSIS = "highest-prio-in-chassis"
    PRIO_SHARE_HIGHEST_PRIO_IN_POWER_GROUP = "highest-prio-in-power-group"
    PRIO_SHARE_NO_PREFERENCE = "no-preference"
    SELF_REQ_CONFLICT_FAIL_PLACEMENT = "fail-placement"
    SELF_REQ_CONFLICT_IGNORE = "ignore"


class PowerPlacement(ManagedObject):
    """This is PowerPlacement class."""

    consts = PowerPlacementConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("PowerPlacement", "powerPlacement", "placement-[name]", VersionMeta.Version141i, "InputOutput", 0xfff, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy"], ['orgOrg'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "peer_req_conflict": MoPropertyMeta("peer_req_conflict", "peerReqConflict", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["fail-placement", "ignore"], []),
        "pg_name": MoPropertyMeta("pg_name", "pgName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "prio_share": MoPropertyMeta("prio_share", "prioShare", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["highest-prio-in-chassis", "highest-prio-in-power-group", "no-preference"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "self_req_conflict": MoPropertyMeta("self_req_conflict", "selfReqConflict", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["fail-placement", "ignore"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "peerReqConflict": "peer_req_conflict", 
        "pgName": "pg_name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "prioShare": "prio_share", 
        "rn": "rn", 
        "sacl": "sacl", 
        "selfReqConflict": "self_req_conflict", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.peer_req_conflict = None
        self.pg_name = None
        self.policy_level = None
        self.policy_owner = None
        self.prio_share = None
        self.sacl = None
        self.self_req_conflict = None
        self.status = None

        ManagedObject.__init__(self, "PowerPlacement", parent_mo_or_dn, **kwargs)
