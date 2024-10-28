"""This module contains the general information for SecurityDeployedAesEncryption ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SecurityDeployedAesEncryptionConsts:
    CONFIG_PENDING_FALSE = "false"
    CONFIG_PENDING_NO = "no"
    CONFIG_PENDING_TRUE = "true"
    CONFIG_PENDING_YES = "yes"
    IS_PRIMARY_KEY_SET_FALSE = "false"
    IS_PRIMARY_KEY_SET_NO = "no"
    IS_PRIMARY_KEY_SET_TRUE = "true"
    IS_PRIMARY_KEY_SET_YES = "yes"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class SecurityDeployedAesEncryption(ManagedObject):
    """This is SecurityDeployedAesEncryption class."""

    consts = SecurityDeployedAesEncryptionConsts()
    naming_props = set(['switchId'])

    mo_meta = MoMeta("SecurityDeployedAesEncryption", "securityDeployedAesEncryption", "deployed-aes-[switch_id]", VersionMeta.Version435a, "InputOutput", 0x3f, [], ["aaa", "admin"], ['securityEncryptionEp'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version435a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_pending": MoPropertyMeta("config_pending", "configPending", "string", VersionMeta.Version435a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version435a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "is_primary_key_set": MoPropertyMeta("is_primary_key_set", "isPrimaryKeySet", "string", VersionMeta.Version435a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "primary_key": MoPropertyMeta("primary_key", "primaryKey", "string", VersionMeta.Version435a, MoPropertyMeta.READ_ONLY, None, 16, 64, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version435a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version435a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version435a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version435a, MoPropertyMeta.NAMING, 0x20, None, None, None, ["A", "B", "NONE"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configPending": "config_pending", 
        "dn": "dn", 
        "isPrimaryKeySet": "is_primary_key_set", 
        "primaryKey": "primary_key", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
    }

    def __init__(self, parent_mo_or_dn, switch_id, **kwargs):
        self._dirty_mask = 0
        self.switch_id = switch_id
        self.child_action = None
        self.config_pending = None
        self.is_primary_key_set = None
        self.primary_key = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "SecurityDeployedAesEncryption", parent_mo_or_dn, **kwargs)
