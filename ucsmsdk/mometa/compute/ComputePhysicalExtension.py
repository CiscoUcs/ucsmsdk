"""This module contains the general information for ComputePhysicalExtension ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePhysicalExtensionConsts:
    pass


class ComputePhysicalExtension(ManagedObject):
    """This is ComputePhysicalExtension class."""

    consts = ComputePhysicalExtensionConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputePhysicalExtension", "computePhysicalExtension", "phys-extension", VersionMeta.Version321d, "InputOutput", 0x1f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], ['faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "hw_inventory_status": MoPropertyMeta("hw_inventory_status", "hwInventoryStatus", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|ok|pci-config-mismatch|mismatch|insertion|persistent-memory-detection|removal|replacement),){0,7}(defaultValue|ok|pci-config-mismatch|mismatch|insertion|persistent-memory-detection|removal|replacement){0,1}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "hwInventoryStatus": "hw_inventory_status", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.hw_inventory_status = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputePhysicalExtension", parent_mo_or_dn, **kwargs)
