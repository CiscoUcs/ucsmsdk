"""This module contains the general information for EquipmentDiscoveryCap ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentDiscoveryCapConsts():
    OPER_POWER_REQUIREMENT_FULL = "full"
    OPER_POWER_REQUIREMENT_NONE = "none"
    OPER_POWER_REQUIREMENT_STANDBY = "standby"


class EquipmentDiscoveryCap(ManagedObject):
    """This is EquipmentDiscoveryCap class."""

    consts = EquipmentDiscoveryCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentDiscoveryCap", "equipmentDiscoveryCap", "disccap", VersionMeta.Version142b, "InputOutput", 0x3fL, [], ["read-only"], [u'equipmentBladeCapProvider', u'equipmentRackUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version142b, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version142b, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "oper_power_requirement": MoPropertyMeta("oper_power_requirement", "operPowerRequirement", "string", VersionMeta.Version142b, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["full", "none", "standby"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version142b, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version142b, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "operPowerRequirement": "oper_power_requirement", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.oper_power_requirement = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentDiscoveryCap", parent_mo_or_dn, **kwargs)

