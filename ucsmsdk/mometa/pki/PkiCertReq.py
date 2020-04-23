"""This module contains the general information for PkiCertReq ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PkiCertReqConsts:
    pass


class PkiCertReq(ManagedObject):
    """This is PkiCertReq class."""

    consts = PkiCertReqConsts()
    naming_props = set([])

    mo_meta = MoMeta("PkiCertReq", "pkiCertReq", "certreq", VersionMeta.Version101e, "InputOutput", 0xfffff, [], ["aaa", "admin"], ['pkiKeyRing'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "country": MoPropertyMeta("country", "country", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""^([A-Z]{2})?$""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "dns": MoPropertyMeta("dns", "dns", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,255}""", [], []),
        "email": MoPropertyMeta("email", "email", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,40}""", [], []),
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "ip_a": MoPropertyMeta("ip_a", "ipA", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x80, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "ip_b": MoPropertyMeta("ip_b", "ipB", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x100, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "ipv6": MoPropertyMeta("ipv6", "ipv6", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x200, 0, 256, None, [], []),
        "ipv6_a": MoPropertyMeta("ipv6_a", "ipv6A", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x400, 0, 256, None, [], []),
        "ipv6_b": MoPropertyMeta("ipv6_b", "ipv6B", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x800, 0, 256, None, [], []),
        "locality": MoPropertyMeta("locality", "locality", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,64}""", [], []),
        "org_name": MoPropertyMeta("org_name", "orgName", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,64}""", [], []),
        "org_unit_name": MoPropertyMeta("org_unit_name", "orgUnitName", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,64}""", [], []),
        "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, [], []),
        "req": MoPropertyMeta("req", "req", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10000, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x20000, None, None, r"""[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,64}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "subj_name": MoPropertyMeta("subj_name", "subjName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80000, 0, 64, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "country": "country", 
        "dn": "dn", 
        "dns": "dns", 
        "email": "email", 
        "ip": "ip", 
        "ipA": "ip_a", 
        "ipB": "ip_b", 
        "ipv6": "ipv6", 
        "ipv6A": "ipv6_a", 
        "ipv6B": "ipv6_b", 
        "locality": "locality", 
        "orgName": "org_name", 
        "orgUnitName": "org_unit_name", 
        "pwd": "pwd", 
        "req": "req", 
        "rn": "rn", 
        "sacl": "sacl", 
        "state": "state", 
        "status": "status", 
        "subjName": "subj_name", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.country = None
        self.dns = None
        self.email = None
        self.ip = None
        self.ip_a = None
        self.ip_b = None
        self.ipv6 = None
        self.ipv6_a = None
        self.ipv6_b = None
        self.locality = None
        self.org_name = None
        self.org_unit_name = None
        self.pwd = None
        self.req = None
        self.sacl = None
        self.state = None
        self.status = None
        self.subj_name = None

        ManagedObject.__init__(self, "PkiCertReq", parent_mo_or_dn, **kwargs)
