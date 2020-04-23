"""This module contains the general information for ComputePowerSyncPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePowerSyncPolicyConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SYNC_OPTION_ALWAYS_SYNC = "always-sync"
    SYNC_OPTION_DEFAULT = "default"
    SYNC_OPTION_INITIAL_ONLY_SYNC = "initial-only-sync"


class ComputePowerSyncPolicy(ManagedObject):
    """This is ComputePowerSyncPolicy class."""

    consts = ComputePowerSyncPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("ComputePowerSyncPolicy", "computePowerSyncPolicy", "power-sync-[name]", VersionMeta.Version312b, "InputOutput", 0x1ff, [], ["admin", "ls-compute", "ls-config-policy", "ls-server", "ls-server-policy"], ['orgOrg'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "sync_option": MoPropertyMeta("sync_option", "syncOption", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["always-sync", "default", "initial-only-sync"], []),
    }

    prop_map = {
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
        "syncOption": "sync_option", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.sync_option = None

        ManagedObject.__init__(self, "ComputePowerSyncPolicy", parent_mo_or_dn, **kwargs)
