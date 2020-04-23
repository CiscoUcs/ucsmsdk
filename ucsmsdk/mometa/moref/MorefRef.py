"""This module contains the general information for MorefRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MorefRefConsts:
    pass


class MorefRef(ManagedObject):
    """This is MorefRef class."""

    consts = MorefRefConsts()
    naming_props = set(['moRn'])

    mo_meta = MoMeta("MorefRef", "morefRef", "[mo_rn]", VersionMeta.Version227b, "InputOutput", 0x3f, [], ["admin"], ['morefFruRef', 'morefImportRoot', 'morefRef'], ['morefProp', 'morefRef'], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version227b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "mo_rn": MoPropertyMeta("mo_rn", "moRn", "string", VersionMeta.Version227b, MoPropertyMeta.NAMING, 0x8, 1, 64, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "moRn": "mo_rn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, mo_rn, **kwargs):
        self._dirty_mask = 0
        self.mo_rn = mo_rn
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MorefRef", parent_mo_or_dn, **kwargs)
