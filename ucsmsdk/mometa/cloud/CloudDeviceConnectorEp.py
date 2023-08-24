"""This module contains the general information for CloudDeviceConnectorEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CloudDeviceConnectorEpConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    ADMIN_STATE_UNKNOWN = "unknown"
    CLAIM_STATE_CLAIMED = "claimed"
    CLAIM_STATE_NONE = "none"
    CLAIM_STATE_UNCLAIMED = "unclaimed"
    INT_ID_NONE = "none"
    IS_IISLICENSE_REQUIRED_FALSE = "false"
    IS_IISLICENSE_REQUIRED_NO = "no"
    IS_IISLICENSE_REQUIRED_TRUE = "true"
    IS_IISLICENSE_REQUIRED_YES = "yes"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class CloudDeviceConnectorEp(ManagedObject):
    """This is CloudDeviceConnectorEp class."""

    consts = CloudDeviceConnectorEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("CloudDeviceConnectorEp", "cloudDeviceConnectorEp", "device-connector", VersionMeta.Version402a, "InputOutput", 0x7ff, [], ["aaa", "admin"], ['cloudMgmtSvc'], ['faultInst'], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled", "unknown"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version402a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "claim_state": MoPropertyMeta("claim_state", "claimState", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["claimed", "none", "unclaimed"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version402a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "is_iis_license_required": MoPropertyMeta("is_iis_license_required", "isIISLicenseRequired", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version402a, MoPropertyMeta.CREATE_ONLY, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "claimState": "claim_state", 
        "descr": "descr", 
        "description": "description", 
        "dn": "dn", 
        "intId": "int_id", 
        "isIISLicenseRequired": "is_iis_license_required", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.claim_state = None
        self.descr = None
        self.description = None
        self.int_id = None
        self.is_iis_license_required = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "CloudDeviceConnectorEp", parent_mo_or_dn, **kwargs)
