"""This module contains the general information for AaaSshAuth ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class AaaSshAuthConsts():
    OLD_STR_TYPE_KEY = "key"
    OLD_STR_TYPE_NONE = "none"
    STR_TYPE_KEY = "key"
    STR_TYPE_NONE = "none"


class AaaSshAuth(ManagedObject):
    """This is AaaSshAuth class."""

    consts = AaaSshAuthConsts()
    naming_props = set([])

    mo_meta = MoMeta("AaaSshAuth", "aaaSshAuth", "sshauth", VersionMeta.Version101e, "InputOutput", 0x7fL, [], ["aaa", "admin"], [u'aaaUser'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "data": MoPropertyMeta("data", "data", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, r"""[\n\r \+\-\./=@_a-zA-Z0-9]{0,16384}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "old_str_type": MoPropertyMeta("old_str_type", "oldStrType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["key", "none"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "str_type": MoPropertyMeta("str_type", "strType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["key", "none"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "data": "data", 
        "dn": "dn", 
        "oldStrType": "old_str_type", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "strType": "str_type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.data = None
        self.old_str_type = None
        self.sacl = None
        self.status = None
        self.str_type = None

        ManagedObject.__init__(self, "AaaSshAuth", parent_mo_or_dn, **kwargs)

