"""This module contains the general information for EquipmentLocalDiskControllerTypeDef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentLocalDiskControllerTypeDefConsts():
    IS_FLASH_LIFE_LEFT_SUPPORTED_FALSE = "false"
    IS_FLASH_LIFE_LEFT_SUPPORTED_NO = "no"
    IS_FLASH_LIFE_LEFT_SUPPORTED_TRUE = "true"
    IS_FLASH_LIFE_LEFT_SUPPORTED_YES = "yes"


class EquipmentLocalDiskControllerTypeDef(ManagedObject):
    """This is EquipmentLocalDiskControllerTypeDef class."""

    consts = EquipmentLocalDiskControllerTypeDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentLocalDiskControllerTypeDef", "equipmentLocalDiskControllerTypeDef", "controller-type", VersionMeta.Version224a, "InputOutput", 0x1fL, [], [""], [u'equipmentLocalDiskControllerCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "is_flash_life_left_supported": MoPropertyMeta("is_flash_life_left_supported", "isFlashLifeLeftSupported", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "isFlashLifeLeftSupported": "is_flash_life_left_supported", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.is_flash_life_left_supported = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentLocalDiskControllerTypeDef", parent_mo_or_dn, **kwargs)

