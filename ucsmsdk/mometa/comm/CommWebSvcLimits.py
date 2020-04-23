"""This module contains the general information for CommWebSvcLimits ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CommWebSvcLimitsConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class CommWebSvcLimits(ManagedObject):
    """This is CommWebSvcLimits class."""

    consts = CommWebSvcLimitsConsts()
    naming_props = set([])

    mo_meta = MoMeta("CommWebSvcLimits", "commWebSvcLimits", "web-svc-limits", VersionMeta.Version141i, "InputOutput", 0x7ff, [], ["aaa", "admin"], ['commSvcEp'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "max_event_interval": MoPropertyMeta("max_event_interval", "maxEventInterval", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["120-3600"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.CREATE_ONLY, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sessions_per_user": MoPropertyMeta("sessions_per_user", "sessionsPerUser", "ushort", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["1-256"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "total_sessions": MoPropertyMeta("total_sessions", "totalSessions", "ushort", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], ["1-256"]),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "maxEventInterval": "max_event_interval", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sessionsPerUser": "sessions_per_user", 
        "status": "status", 
        "totalSessions": "total_sessions", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.max_event_interval = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.sessions_per_user = None
        self.status = None
        self.total_sessions = None

        ManagedObject.__init__(self, "CommWebSvcLimits", parent_mo_or_dn, **kwargs)
