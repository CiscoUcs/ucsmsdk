"""This module contains the general information for ControllerPreferedVersionHolder ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ControllerPreferedVersionHolderConsts:
    IN_USE_FALSE = "false"
    IN_USE_NO = "no"
    IN_USE_TRUE = "true"
    IN_USE_YES = "yes"


class ControllerPreferedVersionHolder(ManagedObject):
    """This is ControllerPreferedVersionHolder class."""

    consts = ControllerPreferedVersionHolderConsts()
    naming_props = set([u'serial'])

    mo_meta = MoMeta("ControllerPreferedVersionHolder", "controllerPreferedVersionHolder", "PrefVersHolder-[serial]", VersionMeta.Version911z, "InputOutput", 0x3f, [], ["admin"], [u'controllerHaController'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version911z, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "in_use": MoPropertyMeta("in_use", "inUse", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version911z, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version911z, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "inUse": "in_use", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, serial, **kwargs):
        self._dirty_mask = 0
        self.serial = serial
        self.child_action = None
        self.in_use = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ControllerPreferedVersionHolder", parent_mo_or_dn, **kwargs)
