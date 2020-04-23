"""This module contains the general information for ApeParam ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ApeParamConsts:
    pass


class ApeParam(ManagedObject):
    """This is ApeParam class."""

    consts = ApeParamConsts()
    naming_props = set(['key'])

    mo_meta = MoMeta("ApeParam", "apeParam", "param-[key]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["read-only"], ['apeMcTable'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "key": MoPropertyMeta("key", "key", "ushort", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "value": MoPropertyMeta("value", "value", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "key": "key", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "value": "value", 
    }

    def __init__(self, parent_mo_or_dn, key, **kwargs):
        self._dirty_mask = 0
        self.key = key
        self.child_action = None
        self.sacl = None
        self.status = None
        self.value = None

        ManagedObject.__init__(self, "ApeParam", parent_mo_or_dn, **kwargs)
