"""This module contains the general information for FabricMacSecPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricMacSecPolicyConsts:
    CIPHER_SUITE_GCM_AES_128 = "GCM-AES-128"
    CIPHER_SUITE_GCM_AES_256 = "GCM-AES-256"
    CIPHER_SUITE_GCM_AES_XPN_128 = "GCM-AES-XPN-128"
    CIPHER_SUITE_GCM_AES_XPN_256 = "GCM-AES-XPN-256"
    CONF_OFFSET_CONF_OFFSET_0 = "conf-offset-0"
    CONF_OFFSET_CONF_OFFSET_30 = "conf-offset-30"
    CONF_OFFSET_CONF_OFFSET_50 = "conf-offset-50"
    INCLUDE_ICV_PARAM_NO = "no"
    INCLUDE_ICV_PARAM_YES = "yes"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SECURITY_POLICY_MUST_SECURE = "must-secure"
    SECURITY_POLICY_SHOULD_SECURE = "should-secure"


class FabricMacSecPolicy(ManagedObject):
    """This is FabricMacSecPolicy class."""

    consts = FabricMacSecPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricMacSecPolicy", "fabricMacSecPolicy", "macsec-policy-[name]", VersionMeta.Version434a, "InputOutput", 0x7fff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricMacSec'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cipher_suite": MoPropertyMeta("cipher_suite", "cipherSuite", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["GCM-AES-128", "GCM-AES-256", "GCM-AES-XPN-128", "GCM-AES-XPN-256"], []),
        "conf_offset": MoPropertyMeta("conf_offset", "confOffset", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["conf-offset-0", "conf-offset-30", "conf-offset-50"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "include_icv_param": MoPropertyMeta("include_icv_param", "includeIcvParam", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["no", "yes"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "key_server_priority": MoPropertyMeta("key_server_priority", "keyServerPriority", "ushort", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["0-255"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version434a, MoPropertyMeta.NAMING, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["local", "pending-policy", "policy"], []),
        "replay_window_size": MoPropertyMeta("replay_window_size", "replayWindowSize", "uint", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], ["0-596000000"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x800, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sak_expiry_time": MoPropertyMeta("sak_expiry_time", "sakExpiryTime", "uint", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], ["60-2592000"]),
        "security_policy": MoPropertyMeta("security_policy", "securityPolicy", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["must-secure", "should-secure"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "cipherSuite": "cipher_suite", 
        "confOffset": "conf_offset", 
        "descr": "descr", 
        "dn": "dn", 
        "includeIcvParam": "include_icv_param", 
        "intId": "int_id", 
        "keyServerPriority": "key_server_priority", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "replayWindowSize": "replay_window_size", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sakExpiryTime": "sak_expiry_time", 
        "securityPolicy": "security_policy", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.cipher_suite = None
        self.conf_offset = None
        self.descr = None
        self.include_icv_param = None
        self.int_id = None
        self.key_server_priority = None
        self.policy_level = None
        self.policy_owner = None
        self.replay_window_size = None
        self.sacl = None
        self.sak_expiry_time = None
        self.security_policy = None
        self.status = None

        ManagedObject.__init__(self, "FabricMacSecPolicy", parent_mo_or_dn, **kwargs)
