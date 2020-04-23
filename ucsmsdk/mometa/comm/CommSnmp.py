"""This module contains the general information for CommSnmp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CommSnmpConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_OK = "ok"
    INT_ID_NONE = "none"
    IS_SET_SNMP_SECURE_FALSE = "false"
    IS_SET_SNMP_SECURE_NO = "no"
    IS_SET_SNMP_SECURE_TRUE = "true"
    IS_SET_SNMP_SECURE_YES = "yes"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PROTO_ALL = "all"
    PROTO_NONE = "none"
    PROTO_TCP = "tcp"
    PROTO_UDP = "udp"
    PROTOCOL_ALL = "all"
    PROTOCOL_NONE = "none"
    PROTOCOL_TCP = "tcp"
    PROTOCOL_UDP = "udp"
    SNMP_OPER_STATE_DISABLED = "disabled"
    SNMP_OPER_STATE_ENABLED = "enabled"


class CommSnmp(ManagedObject):
    """This is CommSnmp class."""

    consts = CommSnmpConsts()
    naming_props = set([])

    mo_meta = MoMeta("CommSnmp", "commSnmp", "snmp-svc", VersionMeta.Version101e, "InputOutput", 0x3fff, [], ["aaa", "admin"], ['commSvcEp'], ['commSnmpTrap', 'commSnmpUser', 'faultInst'], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "community": MoPropertyMeta("community", "community", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[!#$%\)\*\+,\-\./:<=\[\]\^_\{\}~a-zA-Z0-9]{0,32}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applied", "ok"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "is_set_snmp_secure": MoPropertyMeta("is_set_snmp_secure", "isSetSnmpSecure", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["false", "no", "true", "yes"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.CREATE_ONLY, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_port": MoPropertyMeta("oper_port", "operPort", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["local", "pending-policy", "policy"], []),
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], []),
        "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["all", "none", "tcp", "udp"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "snmp_oper_state": MoPropertyMeta("snmp_oper_state", "snmpOperState", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "sys_contact": MoPropertyMeta("sys_contact", "sysContact", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x1000, 0, 255, None, [], []),
        "sys_location": MoPropertyMeta("sys_location", "sysLocation", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x2000, 0, 510, None, [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "community": "community", 
        "configState": "config_state", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "isSetSnmpSecure": "is_set_snmp_secure", 
        "name": "name", 
        "operPort": "oper_port", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "port": "port", 
        "proto": "proto", 
        "protocol": "protocol", 
        "rn": "rn", 
        "sacl": "sacl", 
        "snmpOperState": "snmp_oper_state", 
        "status": "status", 
        "sysContact": "sys_contact", 
        "sysLocation": "sys_location", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.community = None
        self.config_state = None
        self.descr = None
        self.int_id = None
        self.is_set_snmp_secure = None
        self.name = None
        self.oper_port = None
        self.policy_level = None
        self.policy_owner = None
        self.port = None
        self.proto = None
        self.protocol = None
        self.sacl = None
        self.snmp_oper_state = None
        self.status = None
        self.sys_contact = None
        self.sys_location = None

        ManagedObject.__init__(self, "CommSnmp", parent_mo_or_dn, **kwargs)
