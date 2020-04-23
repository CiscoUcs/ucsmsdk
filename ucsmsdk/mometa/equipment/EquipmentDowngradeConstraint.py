"""This module contains the general information for EquipmentDowngradeConstraint ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentDowngradeConstraintConsts:
    pass


class EquipmentDowngradeConstraint(ManagedObject):
    """This is EquipmentDowngradeConstraint class."""

    consts = EquipmentDowngradeConstraintConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentDowngradeConstraint", "equipmentDowngradeConstraint", "fw-dngrd-constr", VersionMeta.Version213a, "InputOutput", 0x1f, [], [""], ['equipmentBoardControllerDef'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version213a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "min_ver": MoPropertyMeta("min_ver", "minVer", "string", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version213a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "minVer": "min_ver", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.min_ver = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentDowngradeConstraint", parent_mo_or_dn, **kwargs)
