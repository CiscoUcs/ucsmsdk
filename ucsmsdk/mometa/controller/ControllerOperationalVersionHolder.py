"""This module contains the general information for ControllerOperationalVersionHolder ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ControllerOperationalVersionHolderConsts:
    pass


class ControllerOperationalVersionHolder(ManagedObject):
    """This is ControllerOperationalVersionHolder class."""

    consts = ControllerOperationalVersionHolderConsts()
    naming_props = set(['serial'])

    mo_meta = MoMeta("ControllerOperationalVersionHolder", "controllerOperationalVersionHolder", "OpVersHolder-[serial]", VersionMeta.Version312b, "InputOutput", 0x3f, [], ["read-only"], ['controllerHaController'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, serial, **kwargs):
        self._dirty_mask = 0
        self.serial = serial
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ControllerOperationalVersionHolder", parent_mo_or_dn, **kwargs)
