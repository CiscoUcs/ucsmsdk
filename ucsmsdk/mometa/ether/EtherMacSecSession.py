"""This module contains the general information for EtherMacSecSession ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EtherMacSecSessionConsts:
    AUTH_MODE_FALLBACK_PSK = "fallback-psk"
    AUTH_MODE_PRIMARY_PSK = "primary-psk"
    AUTH_MODE_UNKNOWN = "unknown"
    CIPHER_SUITE_GCM_AES_128 = "GCM-AES-128"
    CIPHER_SUITE_GCM_AES_256 = "GCM-AES-256"
    CIPHER_SUITE_GCM_AES_XPN_128 = "GCM-AES-XPN-128"
    CIPHER_SUITE_GCM_AES_XPN_256 = "GCM-AES-XPN-256"
    CONF_OFFSET_CONF_OFFSET_0 = "conf-offset-0"
    CONF_OFFSET_CONF_OFFSET_30 = "conf-offset-30"
    CONF_OFFSET_CONF_OFFSET_50 = "conf-offset-50"
    KEY_SERVER_NO = "no"
    KEY_SERVER_UNKNOWN = "unknown"
    KEY_SERVER_YES = "yes"
    STATE_INIT = "init"
    STATE_PENDING = "pending"
    STATE_REKEYED = "rekeyed"
    STATE_SECURED = "secured"
    STATE_UNKNOWN = "unknown"


class EtherMacSecSession(ManagedObject):
    """This is EtherMacSecSession class."""

    consts = EtherMacSecSessionConsts()
    naming_props = set(['authMode'])

    mo_meta = MoMeta("EtherMacSecSession", "etherMacSecSession", "macsec-session-[auth_mode]", VersionMeta.Version434a, "InputOutput", 0x3f, [], ["read-only"], ['etherPIo'], ['faultInst'], [None])

    prop_meta = {
        "auth_mode": MoPropertyMeta("auth_mode", "authMode", "string", VersionMeta.Version434a, MoPropertyMeta.NAMING, 0x2, None, None, None, ["fallback-psk", "primary-psk", "unknown"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cipher_suite": MoPropertyMeta("cipher_suite", "cipherSuite", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["GCM-AES-128", "GCM-AES-256", "GCM-AES-XPN-128", "GCM-AES-XPN-256"], []),
        "conf_offset": MoPropertyMeta("conf_offset", "confOffset", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conf-offset-0", "conf-offset-30", "conf-offset-50"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "key_server": MoPropertyMeta("key_server", "keyServer", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "unknown", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["init", "pending", "rekeyed", "secured", "unknown"], []),
        "state_reason": MoPropertyMeta("state_reason", "stateReason", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "authMode": "auth_mode", 
        "childAction": "child_action", 
        "cipherSuite": "cipher_suite", 
        "confOffset": "conf_offset", 
        "dn": "dn", 
        "keyServer": "key_server", 
        "rn": "rn", 
        "sacl": "sacl", 
        "state": "state", 
        "stateReason": "state_reason", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, auth_mode, **kwargs):
        self._dirty_mask = 0
        self.auth_mode = auth_mode
        self.child_action = None
        self.cipher_suite = None
        self.conf_offset = None
        self.key_server = None
        self.sacl = None
        self.state = None
        self.state_reason = None
        self.status = None

        ManagedObject.__init__(self, "EtherMacSecSession", parent_mo_or_dn, **kwargs)
