"""This module contains the general information for EquipmentPcieSlotOrientation ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentPcieSlotOrientationConsts:
    ORIENTATION_DOWN = "down"
    ORIENTATION_LEFT = "left"
    ORIENTATION_RIGHT = "right"
    ORIENTATION_UP = "up"


class EquipmentPcieSlotOrientation(ManagedObject):
    """This is EquipmentPcieSlotOrientation class."""

    consts = EquipmentPcieSlotOrientationConsts()
    naming_props = set(['slotNumber'])

    mo_meta = MoMeta("EquipmentPcieSlotOrientation", "equipmentPcieSlotOrientation", "pcie-slot-orientation-[slot_number]", VersionMeta.Version323a, "InputOutput", 0x7f, [], [""], ['equipmentRackUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version323a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "orientation": MoPropertyMeta("orientation", "orientation", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["down", "left", "right", "up"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_number": MoPropertyMeta("slot_number", "slotNumber", "ushort", VersionMeta.Version323a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "orientation": "orientation", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotNumber": "slot_number", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, slot_number, **kwargs):
        self._dirty_mask = 0
        self.slot_number = slot_number
        self.child_action = None
        self.orientation = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPcieSlotOrientation", parent_mo_or_dn, **kwargs)
