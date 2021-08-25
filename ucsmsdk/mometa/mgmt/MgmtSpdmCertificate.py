"""This module contains the general information for MgmtSpdmCertificate ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtSpdmCertificateConsts:
    CERT_TYPE_PEM = "pem"


class MgmtSpdmCertificate(ManagedObject):
    """This is MgmtSpdmCertificate class."""

    consts = MgmtSpdmCertificateConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("MgmtSpdmCertificate", "mgmtSpdmCertificate", "spdm-cert-[name]", VersionMeta.Version421a, "InputOutput", 0x1ff, [], ["admin"], ['mgmtSpdmCertificatePolicy'], [], [None])

    prop_meta = {
        "cert_content": MoPropertyMeta("cert_content", "certContent", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []),
        "cert_hash_key": MoPropertyMeta("cert_hash_key", "certHashKey", "uint", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []),
        "cert_type": MoPropertyMeta("cert_type", "certType", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["pem"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, 0x10, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version421a, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "certContent": "cert_content", 
        "certHashKey": "cert_hash_key", 
        "certType": "cert_type", 
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.cert_content = None
        self.cert_hash_key = None
        self.cert_type = None
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtSpdmCertificate", parent_mo_or_dn, **kwargs)
