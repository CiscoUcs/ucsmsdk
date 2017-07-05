"""This module contains the general information for FirmwareSecondControllerChassisConstraint ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareSecondControllerChassisConstraintConsts:
    pass


class FirmwareSecondControllerChassisConstraint(ManagedObject):
    """This is FirmwareSecondControllerChassisConstraint class."""

    consts = FirmwareSecondControllerChassisConstraintConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareSecondControllerChassisConstraint", "firmwareSecondControllerChassisConstraint", "second-controller-chassis-constraint", None, "InputOutput", 0x1f, [], ["read-only"], [u'firmwareConstraints'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "min_cmc_version": MoPropertyMeta("min_cmc_version", "minCmcVersion", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "minCmcVersion": "min_cmc_version", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.min_cmc_version = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareSecondControllerChassisConstraint", parent_mo_or_dn, **kwargs)
