"""This module contains the general information for BiosSettingRef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class BiosSettingRefConsts():
    IS_DEFAULT_NO = "no"
    IS_DEFAULT_YES = "yes"
    IS_SUPPORTED_NO = "no"
    IS_SUPPORTED_YES = "yes"


class BiosSettingRef(ManagedObject):
    """This is BiosSettingRef class."""

    consts = BiosSettingRefConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("BiosSettingRef", "biosSettingRef", "setting-ref-[name]", VersionMeta.Version131c, "InputOutput", 0x3fL, [], [""], [u'biosParameterRef'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "constant_name": MoPropertyMeta("constant_name", "constantName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "is_default": MoPropertyMeta("is_default", "isDefault", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "is_supported": MoPropertyMeta("is_supported", "isSupported", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131c, MoPropertyMeta.NAMING, 0x8L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,256}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "constantName": "constant_name", 
        "dn": "dn", 
        "isDefault": "is_default", 
        "isSupported": "is_supported", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.constant_name = None
        self.is_default = None
        self.is_supported = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "BiosSettingRef", parent_mo_or_dn, **kwargs)

