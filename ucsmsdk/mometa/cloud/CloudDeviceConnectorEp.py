"""This module contains the general information for CloudDeviceConnectorEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CloudDeviceConnectorEpConsts:
    CLAIM_STATE_CLAIMED = "claimed"
    CLAIM_STATE_NONE = "none"
    CLAIM_STATE_UNCLAIMED = "unclaimed"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class CloudDeviceConnectorEp(ManagedObject):
    """This is CloudDeviceConnectorEp class."""

    consts = CloudDeviceConnectorEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("CloudDeviceConnectorEp", "cloudDeviceConnectorEp", "device-connector", VersionMeta.Version402a, "InputOutput", 0x3ff, [], ["aaa", "admin"], ['cloudMgmtSvc'], ['faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version402a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "claim_state": MoPropertyMeta("claim_state", "claimState", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["claimed", "none", "unclaimed"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version402a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version402a, MoPropertyMeta.CREATE_ONLY, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "claimState": "claim_state", 
        "descr": "descr", 
        "description": "description", 
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
        self.child_action = None
        self.claim_state = None
        self.descr = None
        self.description = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "CloudDeviceConnectorEp", parent_mo_or_dn, **kwargs)
