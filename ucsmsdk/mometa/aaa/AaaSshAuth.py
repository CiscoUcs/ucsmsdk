"""This module contains the general information for AaaSshAuth ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AaaSshAuthConsts:
    INTERNAL_KEY_STATUS_FALSE = "false"
    INTERNAL_KEY_STATUS_NO = "no"
    INTERNAL_KEY_STATUS_TRUE = "true"
    INTERNAL_KEY_STATUS_YES = "yes"
    OLD_STR_TYPE_KEY = "key"
    OLD_STR_TYPE_NONE = "none"
    REGEN_FALSE = "false"
    REGEN_NO = "no"
    REGEN_TRUE = "true"
    REGEN_YES = "yes"
    STR_TYPE_KEY = "key"
    STR_TYPE_NONE = "none"


class AaaSshAuth(ManagedObject):
    """This is AaaSshAuth class."""

    consts = AaaSshAuthConsts()
    naming_props = set([])

    mo_meta = MoMeta("AaaSshAuth", "aaaSshAuth", "sshauth", VersionMeta.Version101e, "InputOutput", 0xff, [], ["aaa", "admin"], ['aaaUser'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "data": MoPropertyMeta("data", "data", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\n\r \+\-\./=@_a-zA-Z0-9]{0,16384}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "internal_key_status": MoPropertyMeta("internal_key_status", "internalKeyStatus", "string", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "old_str_type": MoPropertyMeta("old_str_type", "oldStrType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["key", "none"], []),
        "private_key": MoPropertyMeta("private_key", "privateKey", "string", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\n\r \+\-\./=@_a-zA-Z0-9]{0,16384}""", [], []),
        "public_key": MoPropertyMeta("public_key", "publicKey", "string", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\n\r \+\-\./=@_a-zA-Z0-9]{0,16384}""", [], []),
        "regen": MoPropertyMeta("regen", "regen", "string", VersionMeta.Version601b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "str_type": MoPropertyMeta("str_type", "strType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["key", "none"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "data": "data", 
        "dn": "dn", 
        "internalKeyStatus": "internal_key_status", 
        "oldStrType": "old_str_type", 
        "privateKey": "private_key", 
        "publicKey": "public_key", 
        "regen": "regen", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "strType": "str_type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.data = None
        self.internal_key_status = None
        self.old_str_type = None
        self.private_key = None
        self.public_key = None
        self.regen = None
        self.sacl = None
        self.status = None
        self.str_type = None

        ManagedObject.__init__(self, "AaaSshAuth", parent_mo_or_dn, **kwargs)
