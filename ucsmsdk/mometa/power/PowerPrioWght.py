"""This module contains the general information for PowerPrioWght ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class PowerPrioWghtConsts():
    PRIO_NO_CAP = "no-cap"
    PRIO_UTILITY = "utility"


class PowerPrioWght(ManagedObject):
    """This is PowerPrioWght class."""

    consts = PowerPrioWghtConsts()
    naming_props = set([u'prio'])

    mo_meta = MoMeta("PowerPrioWght", "powerPrioWght", "weight-[prio]", VersionMeta.Version141i, "InputOutput", 0x7fL, [], ["admin", "power-mgmt"], [u'powerEp'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "prio": MoPropertyMeta("prio", "prio", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8L, None, None, None, ["no-cap", "utility"], ["1-10"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "weight": MoPropertyMeta("weight", "weight", "byte", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], ["0-200"]), 
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

