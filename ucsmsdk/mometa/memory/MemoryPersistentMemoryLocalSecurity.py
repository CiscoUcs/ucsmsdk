"""This module contains the general information for MemoryPersistentMemoryLocalSecurity ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MemoryPersistentMemoryLocalSecurityConsts:
    DEPLOYED_KEY_FLAG_FALSE = "false"
    DEPLOYED_KEY_FLAG_NO = "no"
    DEPLOYED_KEY_FLAG_TRUE = "true"
    DEPLOYED_KEY_FLAG_YES = "yes"


class MemoryPersistentMemoryLocalSecurity(ManagedObject):
    """This is MemoryPersistentMemoryLocalSecurity class."""

    consts = MemoryPersistentMemoryLocalSecurityConsts()
    naming_props = set([])

    mo_meta = MoMeta("MemoryPersistentMemoryLocalSecurity", "memoryPersistentMemoryLocalSecurity", "local", VersionMeta.Version404a, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server"], ['memoryPersistentMemorySecurity'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "deployed_key_flag": MoPropertyMeta("deployed_key_flag", "deployedKeyFlag", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "deployed_secure_passphrase": MoPropertyMeta("deployed_secure_passphrase", "deployedSecurePassphrase", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x4, 0, 32, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version404a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "secure_passphrase": MoPropertyMeta("secure_passphrase", "securePassphrase", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[a-zA-Z0-9=!&#$%+^@_*-]{8,32}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "deployedKeyFlag": "deployed_key_flag", 
        "deployedSecurePassphrase": "deployed_secure_passphrase", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "securePassphrase": "secure_passphrase", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.deployed_key_flag = None
        self.deployed_secure_passphrase = None
        self.sacl = None
        self.secure_passphrase = None
        self.status = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryLocalSecurity", parent_mo_or_dn, **kwargs)
