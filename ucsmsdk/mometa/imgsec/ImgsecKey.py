"""This module contains the general information for ImgsecKey ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ImgsecKeyConsts:
    TYPE_PRIVATE = "private"
    TYPE_PUBLIC = "public"
    TYPE_SHARED = "shared"


class ImgsecKey(ManagedObject):
    """This is ImgsecKey class."""

    consts = ImgsecKeyConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("ImgsecKey", "imgsecKey", "key-[type]", VersionMeta.Version141i, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server"], ['imgprovTarget', 'imgsecPolicy'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x20, None, None, None, ["private", "public", "shared"], []),
        "value": MoPropertyMeta("value", "value", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
        "value": "value", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.sacl = None
        self.status = None
        self.value = None

        ManagedObject.__init__(self, "ImgsecKey", parent_mo_or_dn, **kwargs)
