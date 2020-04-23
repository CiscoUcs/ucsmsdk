"""This module contains the general information for ComputePnuOSImage ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePnuOSImageConsts:
    pass


class ComputePnuOSImage(ManagedObject):
    """This is ComputePnuOSImage class."""

    consts = ComputePnuOSImageConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputePnuOSImage", "computePnuOSImage", "pnuos", VersionMeta.Version202m, "InputOutput", 0x1f, [], ["read-only"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202m, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "img_loc": MoPropertyMeta("img_loc", "imgLoc", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "img_name": MoPropertyMeta("img_name", "imgName", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "imgLoc": "img_loc", 
        "imgName": "img_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.img_loc = None
        self.img_name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputePnuOSImage", parent_mo_or_dn, **kwargs)
