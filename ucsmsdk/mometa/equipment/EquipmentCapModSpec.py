"""This module contains the general information for EquipmentCapModSpec ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentCapModSpecConsts:
    pass


class EquipmentCapModSpec(ManagedObject):
    """This is EquipmentCapModSpec class."""

    consts = EquipmentCapModSpecConsts()
    naming_props = set(['path'])

    mo_meta = MoMeta("EquipmentCapModSpec", "equipmentCapModSpec", "modspec-[path]", VersionMeta.Version227b, "InputOutput", 0x3f, [], [""], ['equipmentHwCapDerivativeProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version227b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "path": MoPropertyMeta("path", "path", "string", VersionMeta.Version227b, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "path": "path", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, path, **kwargs):
        self._dirty_mask = 0
        self.path = path
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentCapModSpec", parent_mo_or_dn, **kwargs)
