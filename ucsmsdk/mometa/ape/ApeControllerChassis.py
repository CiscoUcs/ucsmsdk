"""This module contains the general information for ApeControllerChassis ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ApeControllerChassisConsts:
    pass


class ApeControllerChassis(ManagedObject):
    """This is ApeControllerChassis class."""

    consts = ApeControllerChassisConsts()
    naming_props = set(['index'])

    mo_meta = MoMeta("ApeControllerChassis", "apeControllerChassis", "Chassis-[index]", VersionMeta.Version101e, "InputOutput", 0x3f, [], ["read-only"], ['apeControllerManager'], ['apeControllerEeprom'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "index": "index", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, index, **kwargs):
        self._dirty_mask = 0
        self.index = index
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ApeControllerChassis", parent_mo_or_dn, **kwargs)
