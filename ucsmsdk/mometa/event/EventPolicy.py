"""This module contains the general information for EventPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EventPolicyConsts:
    INT_ID_NONE = "none"
    PINNING_EXPIRATION_INTERVAL_FOREVER = "forever"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    RETENTION_INTERVAL_FOREVER = "forever"
    SIZE_LIMIT_MAX = "max"


class EventPolicy(ManagedObject):
    """This is EventPolicy class."""

    consts = EventPolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("EventPolicy", "eventPolicy", "event-policy", VersionMeta.Version101e, "InputOutput", 0x7ff, [], ["admin", "read-only"], ['eventHolder'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "pinning_expiration_interval": MoPropertyMeta("pinning_expiration_interval", "pinningExpirationInterval", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", ["forever"], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "retention_interval": MoPropertyMeta("retention_interval", "retentionInterval", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", ["forever"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "size_limit": MoPropertyMeta("size_limit", "sizeLimit", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["max"], ["0-20000"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "pinningExpirationInterval": "pinning_expiration_interval", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "retentionInterval": "retention_interval", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sizeLimit": "size_limit", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.pinning_expiration_interval = None
        self.policy_level = None
        self.policy_owner = None
        self.retention_interval = None
        self.sacl = None
        self.size_limit = None
        self.status = None

        ManagedObject.__init__(self, "EventPolicy", parent_mo_or_dn, **kwargs)
