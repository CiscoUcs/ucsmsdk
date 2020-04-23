"""This module contains the general information for EquipmentBladeCapProviderTypeDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentBladeCapProviderTypeDefConsts:
    pass


class EquipmentBladeCapProviderTypeDef(ManagedObject):
    """This is EquipmentBladeCapProviderTypeDef class."""

    consts = EquipmentBladeCapProviderTypeDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentBladeCapProviderTypeDef", "equipmentBladeCapProviderTypeDef", "blade-provider-type", VersionMeta.Version224b, "InputOutput", 0x7f, [], [""], ['equipmentBladeCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "num_adapter_slots": MoPropertyMeta("num_adapter_slots", "numAdapterSlots", "ushort", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
        "num_slots": MoPropertyMeta("num_slots", "numSlots", "ushort", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "numAdapterSlots": "num_adapter_slots", 
        "numSlots": "num_slots", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.num_adapter_slots = None
        self.num_slots = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentBladeCapProviderTypeDef", parent_mo_or_dn, **kwargs)
