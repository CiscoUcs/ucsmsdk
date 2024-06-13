"""This module contains the general information for MgmtAccessPolicyItem ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtAccessPolicyItemConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SUBJECT_ADAPTOR = "adaptor"
    SUBJECT_BLADE = "blade"
    SUBJECT_BOARD_CONTROLLER = "board-controller"
    SUBJECT_CHASSIS = "chassis"
    SUBJECT_CMC = "cmc"
    SUBJECT_CPLD = "cpld"
    SUBJECT_INTEL_AMC = "intel-amc"
    SUBJECT_IOCARD = "iocard"
    SUBJECT_LOCAL_DISK = "local-disk"
    SUBJECT_RETIMER = "retimer"
    SUBJECT_SAS_EXPANDER = "sas-expander"
    SUBJECT_SERVER_UNIT = "server-unit"
    SUBJECT_SWITCH = "switch"
    SUBJECT_SYSTEM = "system"
    SUBJECT_UBM = "ubm"
    SUBJECT_UNKNOWN = "unknown"


class MgmtAccessPolicyItem(ManagedObject):
    """This is MgmtAccessPolicyItem class."""

    consts = MgmtAccessPolicyItemConsts()
    naming_props = set(['subject'])

    mo_meta = MoMeta("MgmtAccessPolicyItem", "mgmtAccessPolicyItem", "item-[subject]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["read-only"], ['mgmtAccessPolicy'], ['mgmtAccessPort'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "ip_pool_name": MoPropertyMeta("ip_pool_name", "ipPoolName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "subject": MoPropertyMeta("subject", "subject", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x100, None, None, None, ["adaptor", "blade", "board-controller", "chassis", "cmc", "cpld", "intel-amc", "iocard", "local-disk", "retimer", "sas-expander", "server-unit", "switch", "system", "ubm", "unknown"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "ipPoolName": "ip_pool_name", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "subject": "subject", 
    }

    def __init__(self, parent_mo_or_dn, subject, **kwargs):
        self._dirty_mask = 0
        self.subject = subject
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.ip_pool_name = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtAccessPolicyItem", parent_mo_or_dn, **kwargs)
