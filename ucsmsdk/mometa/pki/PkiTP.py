"""This module contains the general information for PkiTP ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PkiTPConsts:
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


class PkiTP(ManagedObject):
    """This is PkiTP class."""

    consts = PkiTPConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("PkiTP", "pkiTP", "tp-[name]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["aaa", "admin"], ['pkiEp'], ['faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "cert_chain": MoPropertyMeta("cert_chain", "certChain", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []),
        "cert_status": MoPropertyMeta("cert_status", "certStatus", "string", VersionMeta.Version203a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["certChainTooLong", "emptyCert", "expired", "failedToVerifyWithPrivateKey", "failedToVerifyWithTp", "notYetValid", "revoked", "selfSignedCertificate", "unknown", "valid"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "fp": MoPropertyMeta("fp", "fp", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "num_certs": MoPropertyMeta("num_certs", "numCerts", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "certChain": "cert_chain", 
        "certStatus": "cert_status", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "fp": "fp", 
        "intId": "int_id", 
        "name": "name", 
        "numCerts": "num_certs", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.cert_chain = None
        self.cert_status = None
        self.child_action = None
        self.descr = None
        self.fp = None
        self.int_id = None
        self.num_certs = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PkiTP", parent_mo_or_dn, **kwargs)
