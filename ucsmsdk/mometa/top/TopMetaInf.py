"""This module contains the general information for TopMetaInf ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class TopMetaInfConsts:
    pass


class TopMetaInf(ManagedObject):
    """This is TopMetaInf class."""

    consts = TopMetaInfConsts()
    naming_props = set([])

    mo_meta = MoMeta("TopMetaInf", "topMetaInf", "meta", VersionMeta.Version111j, "InputOutput", 0x7f, [], ["read-only"], ['topRoot'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ecode": MoPropertyMeta("ecode", "ecode", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, 0, 8, None, [], []),
        "everi": MoPropertyMeta("everi", "everi", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[a-zA-Z][a-zA-Z0-9-]{0,29}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ecode": "ecode", 
        "everi": "everi", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.ecode = None
        self.everi = None
        self.name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "TopMetaInf", **kwargs)
