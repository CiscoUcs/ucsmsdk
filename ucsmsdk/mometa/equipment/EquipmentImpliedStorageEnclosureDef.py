"""This module contains the general information for EquipmentImpliedStorageEnclosureDef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentImpliedStorageEnclosureDefConsts():
    pass


class EquipmentImpliedStorageEnclosureDef(ManagedObject):
    """This is EquipmentImpliedStorageEnclosureDef class."""

    consts = EquipmentImpliedStorageEnclosureDefConsts()
    naming_props = set([u'enclosureId'])

    mo_meta = MoMeta("EquipmentImpliedStorageEnclosureDef", "equipmentImpliedStorageEnclosureDef", "enclosure-def-[enclosure_id]", VersionMeta.Version302c, "InputOutput", 0x3fL, [], [""], [u'equipmentStorageProcessorCap'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "enclosure_id": MoPropertyMeta("enclosure_id", "enclosureId", "ushort", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x8L, None, None, None, [], []), 
        "first_slot_idx": MoPropertyMeta("first_slot_idx", "firstSlotIdx", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "num_slots": MoPropertyMeta("num_slots", "numSlots", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "description": "description", 
        "dn": "dn", 
        "enclosureId": "enclosure_id", 
        "firstSlotIdx": "first_slot_idx", 
        "model": "model", 
        "numSlots": "num_slots", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, enclosure_id, **kwargs):
        self._dirty_mask = 0
        self.enclosure_id = enclosure_id
        self.child_action = None
        self.description = None
        self.first_slot_idx = None
        self.model = None
        self.num_slots = None
        self.sacl = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "EquipmentImpliedStorageEnclosureDef", parent_mo_or_dn, **kwargs)

