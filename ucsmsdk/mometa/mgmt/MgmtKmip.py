"""This module contains the general information for MgmtKmip ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtKmipConsts:
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


class MgmtKmip(ManagedObject):
    """This is MgmtKmip class."""

    consts = MgmtKmipConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtKmip", "mgmtKmip", "kmip", VersionMeta.Version321d, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-storage", "ls-storage-policy"], ['mgmtSecurity'], [], ["Get", "Set"])

    prop_meta = {
        "ca_certificate": MoPropertyMeta("ca_certificate", "caCertificate", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []),
        "cert_sign_request": MoPropertyMeta("cert_sign_request", "certSignRequest", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "cert_status": MoPropertyMeta("cert_status", "certStatus", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["certChainTooLong", "emptyCert", "expired", "failedToVerifyWithPrivateKey", "failedToVerifyWithTp", "notYetValid", "revoked", "selfSignedCertificate", "unknown", "valid"], []),
        "certificate": MoPropertyMeta("certificate", "certificate", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "pri_conn_status": MoPropertyMeta("pri_conn_status", "priConnStatus", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sec_conn_status": MoPropertyMeta("sec_conn_status", "secConnStatus", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "caCertificate": "ca_certificate", 
        "certSignRequest": "cert_sign_request", 
        "certStatus": "cert_status", 
        "certificate": "certificate", 
        "childAction": "child_action", 
        "dn": "dn", 
        "priConnStatus": "pri_conn_status", 
        "rn": "rn", 
        "sacl": "sacl", 
        "secConnStatus": "sec_conn_status", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.ca_certificate = None
        self.cert_sign_request = None
        self.cert_status = None
        self.certificate = None
        self.child_action = None
        self.pri_conn_status = None
        self.sacl = None
        self.sec_conn_status = None
        self.status = None

        ManagedObject.__init__(self, "MgmtKmip", parent_mo_or_dn, **kwargs)
