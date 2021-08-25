"""This module contains the general information for MgmtSpdmCertificateData ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtSpdmCertificateDataConsts:
    CERT_TYPE_PEM = "pem"


class MgmtSpdmCertificateData(ManagedObject):
    """This is MgmtSpdmCertificateData class."""

    consts = MgmtSpdmCertificateDataConsts()
    naming_props = set(['certId'])

    mo_meta = MoMeta("MgmtSpdmCertificateData", "mgmtSpdmCertificateData", "spdm-cert-[cert_id]", VersionMeta.Version421a, "InputOutput", 0xffffff, [], ["admin"], ['mgmtSpdmCertificateInventory'], [], [None])

    prop_meta = {
        "cert_content": MoPropertyMeta("cert_content", "certContent", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []),
        "cert_id": MoPropertyMeta("cert_id", "certId", "ushort", VersionMeta.Version421a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []),
        "cert_type": MoPropertyMeta("cert_type", "certType", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["pem"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, 0x10, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "common_name": MoPropertyMeta("common_name", "commonName", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "country_code": MoPropertyMeta("country_code", "countryCode", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "is_user_uploaded": MoPropertyMeta("is_user_uploaded", "isUserUploaded", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "issuer_common_name": MoPropertyMeta("issuer_common_name", "issuerCommonName", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "issuer_country_code": MoPropertyMeta("issuer_country_code", "issuerCountryCode", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "issuer_locality": MoPropertyMeta("issuer_locality", "issuerLocality", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "issuer_org_name": MoPropertyMeta("issuer_org_name", "issuerOrgName", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "issuer_org_unit_name": MoPropertyMeta("issuer_org_unit_name", "issuerOrgUnitName", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "issuer_state": MoPropertyMeta("issuer_state", "issuerState", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "locality": MoPropertyMeta("locality", "locality", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "org_name": MoPropertyMeta("org_name", "orgName", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "org_unit_name": MoPropertyMeta("org_unit_name", "orgUnitName", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x20000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, 0x40000, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial_number": MoPropertyMeta("serial_number", "serialNumber", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x80000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x100000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x200000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "valid_from": MoPropertyMeta("valid_from", "validFrom", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x400000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "valid_to": MoPropertyMeta("valid_to", "validTo", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x800000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
    }

    prop_map = {
        "certContent": "cert_content", 
        "certId": "cert_id", 
        "certType": "cert_type", 
        "childAction": "child_action", 
        "commonName": "common_name", 
        "countryCode": "country_code", 
        "dn": "dn", 
        "isUserUploaded": "is_user_uploaded", 
        "issuerCommonName": "issuer_common_name", 
        "issuerCountryCode": "issuer_country_code", 
        "issuerLocality": "issuer_locality", 
        "issuerOrgName": "issuer_org_name", 
        "issuerOrgUnitName": "issuer_org_unit_name", 
        "issuerState": "issuer_state", 
        "locality": "locality", 
        "orgName": "org_name", 
        "orgUnitName": "org_unit_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serialNumber": "serial_number", 
        "state": "state", 
        "status": "status", 
        "validFrom": "valid_from", 
        "validTo": "valid_to", 
    }

    def __init__(self, parent_mo_or_dn, cert_id, **kwargs):
        self._dirty_mask = 0
        self.cert_id = cert_id
        self.cert_content = None
        self.cert_type = None
        self.child_action = None
        self.common_name = None
        self.country_code = None
        self.is_user_uploaded = None
        self.issuer_common_name = None
        self.issuer_country_code = None
        self.issuer_locality = None
        self.issuer_org_name = None
        self.issuer_org_unit_name = None
        self.issuer_state = None
        self.locality = None
        self.org_name = None
        self.org_unit_name = None
        self.sacl = None
        self.serial_number = None
        self.state = None
        self.status = None
        self.valid_from = None
        self.valid_to = None

        ManagedObject.__init__(self, "MgmtSpdmCertificateData", parent_mo_or_dn, **kwargs)
