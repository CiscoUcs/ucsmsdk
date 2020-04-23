"""This module contains the general information for AaaTacacsPlusProvider ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AaaTacacsPlusProviderConsts:
    KEY_SET_FALSE = "false"
    KEY_SET_NO = "no"
    KEY_SET_TRUE = "true"
    KEY_SET_YES = "yes"
    ORDER_LOWEST_AVAILABLE = "lowest-available"


class AaaTacacsPlusProvider(ManagedObject):
    """This is AaaTacacsPlusProvider class."""

    consts = AaaTacacsPlusProviderConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("AaaTacacsPlusProvider", "aaaTacacsPlusProvider", "provider-[name]", VersionMeta.Version101e, "InputOutput", 0x1fff, [], ["aaa", "admin"], ['aaaTacacsPlusEp'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "enc_key": MoPropertyMeta("enc_key", "encKey", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, 0, 63, None, [], []),
        "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[!""#$%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,63}""", [], []),
        "key_set": MoPropertyMeta("key_set", "keySet", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, r"""^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,63}$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], []),
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["lowest-available"], ["0-16"]),
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["1-65535"]),
        "retries": MoPropertyMeta("retries", "retries", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], ["0-5"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], ["0-60"]),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "encKey": "enc_key", 
        "key": "key", 
        "keySet": "key_set", 
        "name": "name", 
        "order": "order", 
        "port": "port", 
        "retries": "retries", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "timeout": "timeout", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.enc_key = None
        self.key = None
        self.key_set = None
        self.order = None
        self.port = None
        self.retries = None
        self.sacl = None
        self.status = None
        self.timeout = None

        ManagedObject.__init__(self, "AaaTacacsPlusProvider", parent_mo_or_dn, **kwargs)
