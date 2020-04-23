"""This module contains the general information for EquipmentStorageControllerSlotDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentStorageControllerSlotDefConsts:
    pass


class EquipmentStorageControllerSlotDef(ManagedObject):
    """This is EquipmentStorageControllerSlotDef class."""

    consts = EquipmentStorageControllerSlotDefConsts()
    naming_props = set(['slotNum'])

    mo_meta = MoMeta("EquipmentStorageControllerSlotDef", "equipmentStorageControllerSlotDef", "controller-slot-def-[slot_num]", VersionMeta.Version224b, "InputOutput", 0x3f, [], ["read-only"], ['equipmentBladeCapProvider', 'equipmentRackUnitCapProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "num_slots": MoPropertyMeta("num_slots", "numSlots", "ushort", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_num": MoPropertyMeta("slot_num", "slotNum", "ushort", VersionMeta.Version224b, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "numSlots": "num_slots", 
        "order": "order", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotNum": "slot_num", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, slot_num, **kwargs):
        self._dirty_mask = 0
        self.slot_num = slot_num
        self.child_action = None
        self.num_slots = None
        self.order = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentStorageControllerSlotDef", parent_mo_or_dn, **kwargs)
