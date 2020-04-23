"""This module contains the general information for EquipmentStorageSasExpanderCapRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentStorageSasExpanderCapRefConsts:
    pass


class EquipmentStorageSasExpanderCapRef(ManagedObject):
    """This is EquipmentStorageSasExpanderCapRef class."""

    consts = EquipmentStorageSasExpanderCapRefConsts()
    naming_props = set(['vendor', 'model', 'revision'])

    mo_meta = MoMeta("EquipmentStorageSasExpanderCapRef", "equipmentStorageSasExpanderCapRef", "manufacturer-[vendor]-model-[model]-revision-[revision]", VersionMeta.Version226c, "InputOutput", 0xff, [], [""], ['equipmentRackUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version226c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "min_boot_fw_cimc_version": MoPropertyMeta("min_boot_fw_cimc_version", "minBootFwCimcVersion", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "min_cimc_version": MoPropertyMeta("min_cimc_version", "minCimcVersion", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version226c, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version226c, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version226c, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version226c, MoPropertyMeta.NAMING, 0x80, 1, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "minBootFwCimcVersion": "min_boot_fw_cimc_version", 
        "minCimcVersion": "min_cimc_version", 
        "model": "model", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, vendor, model, revision, **kwargs):
        self._dirty_mask = 0
        self.vendor = vendor
        self.model = model
        self.revision = revision
        self.child_action = None
        self.min_boot_fw_cimc_version = None
        self.min_cimc_version = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentStorageSasExpanderCapRef", parent_mo_or_dn, **kwargs)
