"""This module contains the general information for MemoryPersistentMemoryConfiguration ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MemoryPersistentMemoryConfigurationConsts:
    ADMIN_ACTION_CANCEL_ALL = "cancel-all"
    ADMIN_ACTION_DISABLE_SECURITY = "disable-security"
    ADMIN_ACTION_ENABLE_SECURITY = "enable-security"
    ADMIN_ACTION_MODIFY_PASSPHRASE = "modify-passphrase"
    ADMIN_ACTION_NO_OP = "no-op"
    ADMIN_ACTION_RESET_FACTORY_DEFAULT = "reset-factory-default"
    ADMIN_ACTION_SECURE_ERASE = "secure-erase"
    ADMIN_ACTION_UNLOCK_DIMMS = "unlock-dimms"
    ADMIN_STATE_CONFIGURE = "configure"
    ADMIN_STATE_DELETE = "delete"
    ADMIN_STATE_FORCE_CONFIGURE = "force-configure"
    ADMIN_STATE_FORCE_DELETE = "force-delete"
    ADMIN_STATE_FORCE_FLAG = "force-flag"
    ADMIN_STATE_INIT = "init"
    ADMIN_STATE_MATCHING = "matching"
    ADMIN_STATE_NOT_MATCHING = "not-matching"
    CFGD_MEMORY_PERCENTAGE_UNKNOWN = "unknown"
    NS_ADMIN_STATE_CONFIGURE = "configure"
    NS_ADMIN_STATE_DELETE = "delete"
    NS_ADMIN_STATE_FORCE_CONFIGURE = "force-configure"
    NS_ADMIN_STATE_FORCE_DELETE = "force-delete"
    NS_ADMIN_STATE_FORCE_FLAG = "force-flag"
    NS_ADMIN_STATE_INIT = "init"
    NS_ADMIN_STATE_MATCHING = "matching"
    NS_ADMIN_STATE_NOT_MATCHING = "not-matching"
    POLICY_OPERATION_DISABLE_SECURITY = "disable-security"
    POLICY_OPERATION_ENABLE_SECURITY = "enable-security"
    POLICY_OPERATION_FAILED = "failed"
    POLICY_OPERATION_HOST_MANAGED = "host-managed"
    POLICY_OPERATION_MODIFY_PASSPHRASE = "modify-passphrase"
    POLICY_OPERATION_NO_OP = "no-op"
    POLICY_OPERATION_POLICY_CHANGED = "policy-changed"


class MemoryPersistentMemoryConfiguration(ManagedObject):
    """This is MemoryPersistentMemoryConfiguration class."""

    consts = MemoryPersistentMemoryConfigurationConsts()
    naming_props = set([])

    mo_meta = MoMeta("MemoryPersistentMemoryConfiguration", "memoryPersistentMemoryConfiguration", "pmemory-config", VersionMeta.Version404a, "InputOutput", 0x7f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['computeBoard', 'lsServer'], ['faultInst', 'memoryPersistentMemoryConfigResult', 'memoryPersistentMemoryRegion'], [None])

    prop_meta = {
        "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["cancel-all", "disable-security", "enable-security", "modify-passphrase", "no-op", "reset-factory-default", "secure-erase", "unlock-dimms"], []),
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["configure", "delete", "force-configure", "force-delete", "force-flag", "init", "matching", "not-matching"], []),
        "cfgd_memory_percentage": MoPropertyMeta("cfgd_memory_percentage", "cfgdMemoryPercentage", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["1-100"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "deployed_secure_passphrase": MoPropertyMeta("deployed_secure_passphrase", "deployedSecurePassphrase", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 32, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "inaccessible_capacity": MoPropertyMeta("inaccessible_capacity", "inaccessibleCapacity", "long", VersionMeta.Version411a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([0-9]{1,15})$""", [], []),
        "memory_capacity": MoPropertyMeta("memory_capacity", "memoryCapacity", "long", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([0-9]{1,15})$""", [], []),
        "ns_admin_state": MoPropertyMeta("ns_admin_state", "nsAdminState", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["configure", "delete", "force-configure", "force-delete", "force-flag", "init", "matching", "not-matching"], []),
        "num_of_dimms": MoPropertyMeta("num_of_dimms", "numOfDimms", "uint", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "num_of_regions": MoPropertyMeta("num_of_regions", "numOfRegions", "uint", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "persistent_memory_capacity": MoPropertyMeta("persistent_memory_capacity", "persistentMemoryCapacity", "long", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([0-9]{1,15})$""", [], []),
        "policy_operation": MoPropertyMeta("policy_operation", "policyOperation", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disable-security", "enable-security", "failed", "host-managed", "modify-passphrase", "no-op", "policy-changed"], []),
        "reserved_capacity": MoPropertyMeta("reserved_capacity", "reservedCapacity", "long", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([0-9]{1,15})$""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "secure_passphrase": MoPropertyMeta("secure_passphrase", "securePassphrase", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x20, 0, 32, None, [], []),
        "security_state": MoPropertyMeta("security_state", "securityState", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "total_capacity": MoPropertyMeta("total_capacity", "totalCapacity", "long", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([0-9]{1,15})$""", [], []),
        "unconfigured_capacity": MoPropertyMeta("unconfigured_capacity", "unconfiguredCapacity", "long", VersionMeta.Version411a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([0-9]{1,15})$""", [], []),
    }

    prop_map = {
        "adminAction": "admin_action", 
        "adminState": "admin_state", 
        "cfgdMemoryPercentage": "cfgd_memory_percentage", 
        "childAction": "child_action", 
        "deployedSecurePassphrase": "deployed_secure_passphrase", 
        "dn": "dn", 
        "inaccessibleCapacity": "inaccessible_capacity", 
        "memoryCapacity": "memory_capacity", 
        "nsAdminState": "ns_admin_state", 
        "numOfDimms": "num_of_dimms", 
        "numOfRegions": "num_of_regions", 
        "persistentMemoryCapacity": "persistent_memory_capacity", 
        "policyOperation": "policy_operation", 
        "reservedCapacity": "reserved_capacity", 
        "rn": "rn", 
        "sacl": "sacl", 
        "securePassphrase": "secure_passphrase", 
        "securityState": "security_state", 
        "status": "status", 
        "totalCapacity": "total_capacity", 
        "unconfiguredCapacity": "unconfigured_capacity", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.admin_state = None
        self.cfgd_memory_percentage = None
        self.child_action = None
        self.deployed_secure_passphrase = None
        self.inaccessible_capacity = None
        self.memory_capacity = None
        self.ns_admin_state = None
        self.num_of_dimms = None
        self.num_of_regions = None
        self.persistent_memory_capacity = None
        self.policy_operation = None
        self.reserved_capacity = None
        self.sacl = None
        self.secure_passphrase = None
        self.security_state = None
        self.status = None
        self.total_capacity = None
        self.unconfigured_capacity = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryConfiguration", parent_mo_or_dn, **kwargs)
