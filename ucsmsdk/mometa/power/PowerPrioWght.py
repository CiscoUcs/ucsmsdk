"""This module contains the general information for PowerPrioWght ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PowerPrioWghtConsts:
    PRIO_NO_CAP = "no-cap"
    PRIO_UTILITY = "utility"


class PowerPrioWght(ManagedObject):
    """This is PowerPrioWght class."""

    consts = PowerPrioWghtConsts()
    naming_props = set(['prio'])

    mo_meta = MoMeta("PowerPrioWght", "powerPrioWght", "weight-[prio]", VersionMeta.Version141i, "InputOutput", 0x7f, [], ["admin", "power-mgmt"], ['powerEp'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prio": MoPropertyMeta("prio", "prio", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8, None, None, None, ["no-cap", "utility"], ["1-10"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "weight": MoPropertyMeta("weight", "weight", "byte", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["0-200"]),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "prio": "prio", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "weight": "weight", 
    }

    def __init__(self, parent_mo_or_dn, prio, **kwargs):
        self._dirty_mask = 0
        self.prio = prio
        self.child_action = None
        self.sacl = None
        self.status = None
        self.weight = None

        ManagedObject.__init__(self, "PowerPrioWght", parent_mo_or_dn, **kwargs)
