"""This module contains the general information for PkiLocale ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class PkiLocaleConsts():
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
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class PkiLocale(ManagedObject):
    """This is PkiLocale class."""

    consts = PkiLocaleConsts()
    naming_props = set([])

    mo_meta = MoMeta("PkiLocale", "pkiLocale", "pki-locale", VersionMeta.Version302a, "InputOutput", 0x7fL, [], ["read-only"], [u'storageProcessor'], [], [None])

    prop_meta = {
        "cert_status": MoPropertyMeta("cert_status", "certStatus", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["certChainTooLong", "emptyCert", "expired", "failedToVerifyWithPrivateKey", "failedToVerifyWithTp", "notYetValid", "revoked", "selfSignedCertificate", "unknown", "valid"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version302a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302a, MoPropertyMeta.CREATE_ONLY, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "certStatus": "cert_status", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
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
        self.cert_status = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PkiLocale", parent_mo_or_dn, **kwargs)

