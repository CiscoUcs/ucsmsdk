"""This module contains the general information for EquipmentHwRevisionModifier ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentHwRevisionModifierConsts:
    HW_TYPE_LOCAL_DISK = "local-disk"
    HW_TYPE_STORAGE_CONTROLLER = "storage-controller"


class EquipmentHwRevisionModifier(ManagedObject):
    """This is EquipmentHwRevisionModifier class."""

    consts = EquipmentHwRevisionModifierConsts()
    naming_props = set(['hwType'])

    mo_meta = MoMeta("EquipmentHwRevisionModifier", "equipmentHwRevisionModifier", "hw-rev-modifier-[hw_type]", VersionMeta.Version312b, "InputOutput", 0x3f, [], [""], ['equipmentBladeCapProvider', 'equipmentRackUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "hw_type": MoPropertyMeta("hw_type", "hwType", "string", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x8, None, None, None, ["local-disk", "storage-controller"], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "hwType": "hw_type", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, hw_type, **kwargs):
        self._dirty_mask = 0
        self.hw_type = hw_type
        self.child_action = None
        self.revision = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentHwRevisionModifier", parent_mo_or_dn, **kwargs)
