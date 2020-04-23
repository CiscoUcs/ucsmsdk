"""This module contains the general information for CommDateTime ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CommDateTimeConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    CONFIG_STATE_FAILURE = "failure"
    CONFIG_STATE_SUCCESS = "success"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PROTO_ALL = "all"
    PROTO_NONE = "none"
    PROTO_TCP = "tcp"
    PROTO_UDP = "udp"


class CommDateTime(ManagedObject):
    """This is CommDateTime class."""

    consts = CommDateTimeConsts()
    naming_props = set([])

    mo_meta = MoMeta("CommDateTime", "commDateTime", "datetime-svc", VersionMeta.Version101e, "InputOutput", 0x7ff, [], ["admin", "ext-lan-config", "ext-lan-security", "operations"], ['commLocale', 'commSvcEp', 'commSvcPolicy'], ['commNtpProvider', 'faultInst'], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failure", "success"], []),
        "date": MoPropertyMeta("date", "date", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.CREATE_ONLY, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_port": MoPropertyMeta("oper_port", "operPort", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "oper_timezone": MoPropertyMeta("oper_timezone", "operTimezone", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["0-65535"]),
        "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "timezone": MoPropertyMeta("timezone", "timezone", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, None, [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "date": "date", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "operPort": "oper_port", 
        "operTimezone": "oper_timezone", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "port": "port", 
        "proto": "proto", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "timezone": "timezone", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.config_state = None
        self.date = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.oper_port = None
        self.oper_timezone = None
        self.policy_level = None
        self.policy_owner = None
        self.port = None
        self.proto = None
        self.sacl = None
        self.status = None
        self.timezone = None

        ManagedObject.__init__(self, "CommDateTime", parent_mo_or_dn, **kwargs)
