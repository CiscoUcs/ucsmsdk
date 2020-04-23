"""This module contains the general information for EquipmentPciSlotSubOEMIdEntry ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentPciSlotSubOEMIdEntryConsts:
    SUB_OEM_ID_UNDEFINED = "undefined"


class EquipmentPciSlotSubOEMIdEntry(ManagedObject):
    """This is EquipmentPciSlotSubOEMIdEntry class."""

    consts = EquipmentPciSlotSubOEMIdEntryConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("EquipmentPciSlotSubOEMIdEntry", "equipmentPciSlotSubOEMIdEntry", "pci-slot-suboemid-entry-[name]", VersionMeta.Version312b, "InputOutput", 0x3f, [], [""], ['equipmentStorageControllerConfig'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "sub_oem_id": MoPropertyMeta("sub_oem_id", "subOemId", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["undefined"], ["0-65535"]),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "subOemId": "sub_oem_id", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.sacl = None
        self.status = None
        self.sub_oem_id = None

        ManagedObject.__init__(self, "EquipmentPciSlotSubOEMIdEntry", parent_mo_or_dn, **kwargs)
