"""This module contains the general information for FabricMacSecKey ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricMacSecKeyConsts:
    CRYPTOGRAPHIC_ALGORITHM_AES_128_CMAC = "AES-128-CMAC"
    CRYPTOGRAPHIC_ALGORITHM_AES_256_CMAC = "AES-256-CMAC"
    ENCRYPT_TYPE_TYPE_7 = "type-7"
    ENCRYPT_TYPE_UNENCRYPTED = "unencrypted"
    IS_KEY_HEX_STR_UPDATED_FALSE = "false"
    IS_KEY_HEX_STR_UPDATED_NO = "no"
    IS_KEY_HEX_STR_UPDATED_TRUE = "true"
    IS_KEY_HEX_STR_UPDATED_YES = "yes"


class FabricMacSecKey(ManagedObject):
    """This is FabricMacSecKey class."""

    consts = FabricMacSecKeyConsts()
    naming_props = set(['keyId'])

    mo_meta = MoMeta("FabricMacSecKey", "fabricMacSecKey", "macsec-key-[key_id]", VersionMeta.Version434a, "InputOutput", 0x1ff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricMacSecKeyChain'], ['fabricLifeTime'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cryptographic_algorithm": MoPropertyMeta("cryptographic_algorithm", "cryptographicAlgorithm", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["AES-128-CMAC", "AES-256-CMAC"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "encrypt_type": MoPropertyMeta("encrypt_type", "encryptType", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["type-7", "unencrypted"], []),
        "is_key_hex_str_updated": MoPropertyMeta("is_key_hex_str_updated", "isKeyHexStrUpdated", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "key_hex_string": MoPropertyMeta("key_hex_string", "keyHexString", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{32,144}""", [], []),
        "key_id": MoPropertyMeta("key_id", "keyId", "string", VersionMeta.Version434a, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{2,64}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "cryptographicAlgorithm": "cryptographic_algorithm", 
        "dn": "dn", 
        "encryptType": "encrypt_type", 
        "isKeyHexStrUpdated": "is_key_hex_str_updated", 
        "keyHexString": "key_hex_string", 
        "keyId": "key_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, key_id, **kwargs):
        self._dirty_mask = 0
        self.key_id = key_id
        self.child_action = None
        self.cryptographic_algorithm = None
        self.encrypt_type = None
        self.is_key_hex_str_updated = None
        self.key_hex_string = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FabricMacSecKey", parent_mo_or_dn, **kwargs)
