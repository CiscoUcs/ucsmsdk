"""This module contains the general information for PkiKeyRing ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PkiKeyRingConsts:
    ADMIN_STATE_COMPLETED = "completed"
    ADMIN_STATE_CREATED = "created"
    ADMIN_STATE_REQ_CREATED = "reqCreated"
    ADMIN_STATE_STARTED = "started"
    ADMIN_STATE_TP_SET = "tpSet"
    CERT_STATUS_CERT_CHAIN_TOO_LONG = "certChainTooLong"
    CERT_STATUS_EMPTY_CERT = "emptyCert"
    CERT_STATUS_EXPIRED = "expired"
    CERT_STATUS_FAILED_TO_VERIFY_WITH_PRIVATE_KEY = "failedToVerifyWithPrivateKey"
    CERT_STATUS_FAILED_TO_VERIFY_WITH_TP = "failedToVerifyWithTp"
    CERT_STATUS_NOT_YET_VALID = "notYetValid"
    CERT_STATUS_REVOKED = "revoked"
    CERT_STATUS_SELF_SIGNED_CERTIFICATE = "selfSignedCertificate"
    CERT_STATUS_UNKNOWN = "unknown"
    CERT_STATUS_VALID = "valid"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_OK = "ok"
    INT_ID_NONE = "none"
    MODULUS_MOD2048 = "mod2048"
    MODULUS_MOD2560 = "mod2560"
    MODULUS_MOD3072 = "mod3072"
    MODULUS_MOD3584 = "mod3584"
    MODULUS_MOD4096 = "mod4096"
    MODULUS_MODINVALID = "modinvalid"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    REGEN_FALSE = "false"
    REGEN_NO = "no"
    REGEN_TRUE = "true"
    REGEN_YES = "yes"
    RESTART_WEB_SERVICE_FALSE = "false"
    RESTART_WEB_SERVICE_NO = "no"
    RESTART_WEB_SERVICE_TRUE = "true"
    RESTART_WEB_SERVICE_YES = "yes"


class PkiKeyRing(ManagedObject):
    """This is PkiKeyRing class."""

    consts = PkiKeyRingConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("PkiKeyRing", "pkiKeyRing", "keyring-[name]", VersionMeta.Version101e, "InputOutput", 0xfff, [], ["aaa", "admin"], ['pkiEp'], ['faultInst', 'pkiCertReq'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["completed", "created", "reqCreated", "started", "tpSet"], []),
        "cert": MoPropertyMeta("cert", "cert", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []),
        "cert_status": MoPropertyMeta("cert_status", "certStatus", "string", VersionMeta.Version203a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["certChainTooLong", "emptyCert", "expired", "failedToVerifyWithPrivateKey", "failedToVerifyWithTp", "notYetValid", "revoked", "selfSignedCertificate", "unknown", "valid"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applied", "ok"], []),
        "config_status_message": MoPropertyMeta("config_status_message", "configStatusMessage", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "modulus": MoPropertyMeta("modulus", "modulus", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["mod2048", "mod2560", "mod3072", "mod3584", "mod4096", "modinvalid"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "regen": MoPropertyMeta("regen", "regen", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["false", "no", "true", "yes"], []),
        "restart_web_service": MoPropertyMeta("restart_web_service", "restartWebService", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "tp": MoPropertyMeta("tp", "tp", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "cert": "cert", 
        "certStatus": "cert_status", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "configStatusMessage": "config_status_message", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "key": "key", 
        "modulus": "modulus", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "regen": "regen", 
        "restartWebService": "restart_web_service", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "tp": "tp", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_state = None
        self.cert = None
        self.cert_status = None
        self.child_action = None
        self.config_state = None
        self.config_status_message = None
        self.descr = None
        self.int_id = None
        self.key = None
        self.modulus = None
        self.policy_level = None
        self.policy_owner = None
        self.regen = None
        self.restart_web_service = None
        self.sacl = None
        self.status = None
        self.tp = None

        ManagedObject.__init__(self, "PkiKeyRing", parent_mo_or_dn, **kwargs)
