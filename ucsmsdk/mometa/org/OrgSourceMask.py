"""This module contains the general information for OrgSourceMask ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class OrgSourceMaskConsts:
    pass


class OrgSourceMask(ManagedObject):
    """This is OrgSourceMask class."""

    consts = OrgSourceMaskConsts()
    naming_props = set([])

    mo_meta = MoMeta("OrgSourceMask", "orgSourceMask", "src-mask", VersionMeta.Version212a, "InputOutput", 0x1f, [], ["read-only"], ['orgOrg'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version212a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "mask": MoPropertyMeta("mask", "mask", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|local|global),){0,2}(defaultValue|local|global){0,1}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "mask": "mask", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.mask = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "OrgSourceMask", parent_mo_or_dn, **kwargs)
