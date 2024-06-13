"""This module contains the general information for CommHttps ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CommHttpsConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    ALLOWED_SSLPROTOCOLS_ALL = "all"
    ALLOWED_SSLPROTOCOLS_TLSV1_2 = "tlsv1_2"
    ALLOWED_SSLPROTOCOLS_TLSV1_3 = "tlsv1_3"
    CIPHER_SUITE_MODE_CUSTOM = "custom"
    CIPHER_SUITE_MODE_HIGH_STRENGTH = "high-strength"
    CIPHER_SUITE_MODE_LOW_STRENGTH = "low-strength"
    CIPHER_SUITE_MODE_MEDIUM_STRENGTH = "medium-strength"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PROTO_ALL = "all"
    PROTO_NONE = "none"
    PROTO_TCP = "tcp"
    PROTO_UDP = "udp"


class CommHttps(ManagedObject):
    """This is CommHttps class."""

    consts = CommHttpsConsts()
    naming_props = set([])

    mo_meta = MoMeta("CommHttps", "commHttps", "https-svc", VersionMeta.Version101e, "InputOutput", 0x3fff, [], ["aaa", "admin"], ['commSvcEp'], [], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "allowed_ssl_protocols": MoPropertyMeta("allowed_ssl_protocols", "allowedSSLProtocols", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["all", "tlsv1_2", "tlsv1_3"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x8, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cipher_suite": MoPropertyMeta("cipher_suite", "cipherSuite", "string", VersionMeta.Version203a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[!\+,\-\./:;<=>\?@\[\\a-zA-Z0-9]{0,256}""", [], []),
        "cipher_suite_mode": MoPropertyMeta("cipher_suite_mode", "cipherSuiteMode", "string", VersionMeta.Version203a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["custom", "high-strength", "low-strength", "medium-strength"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "key_ring": MoPropertyMeta("key_ring", "keyRing", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.CREATE_ONLY, 0x200, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_port": MoPropertyMeta("oper_port", "operPort", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["local", "pending-policy", "policy"], []),
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, [], ["1-65535"]),
        "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x1000, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "allowedSSLProtocols": "allowed_ssl_protocols", 
        "childAction": "child_action", 
        "cipherSuite": "cipher_suite", 
        "cipherSuiteMode": "cipher_suite_mode", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "keyRing": "key_ring", 
        "name": "name", 
        "operPort": "oper_port", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "port": "port", 
        "proto": "proto", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.allowed_ssl_protocols = None
        self.child_action = None
        self.cipher_suite = None
        self.cipher_suite_mode = None
        self.descr = None
        self.int_id = None
        self.key_ring = None
        self.name = None
        self.oper_port = None
        self.policy_level = None
        self.policy_owner = None
        self.port = None
        self.proto = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "CommHttps", parent_mo_or_dn, **kwargs)
