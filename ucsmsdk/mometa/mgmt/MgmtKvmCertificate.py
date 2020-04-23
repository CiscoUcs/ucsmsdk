"""This module contains the general information for MgmtKvmCertificate ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtKvmCertificateConsts:
    INT_ID_NONE = "none"
    OPER_STATUS_EMPTY_PARAMS = "empty-params"
    OPER_STATUS_NONE = "none"
    OPER_STATUS_UNSUPPORTED = "unsupported"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class MgmtKvmCertificate(ManagedObject):
    """This is MgmtKvmCertificate class."""

    consts = MgmtKvmCertificateConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtKvmCertificate", "mgmtKvmCertificate", "cert", VersionMeta.Version323a, "InputOutput", 0x3ff, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server", "ls-server-oper"], ['computeKvmMgmtPolicy', 'mgmtController'], ['faultInst'], [None])

    prop_meta = {
        "certificate": MoPropertyMeta("certificate", "certificate", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version323a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version323a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_status": MoPropertyMeta("oper_status", "operStatus", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty-params", "none", "unsupported"], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "certificate": "certificate", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "key": "key", 
        "name": "name", 
        "operStatus": "oper_status", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.certificate = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.key = None
        self.name = None
        self.oper_status = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtKvmCertificate", parent_mo_or_dn, **kwargs)
