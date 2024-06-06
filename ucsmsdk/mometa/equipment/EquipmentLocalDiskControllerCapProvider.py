"""This module contains the general information for EquipmentLocalDiskControllerCapProvider ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentLocalDiskControllerCapProviderConsts:
    CARD_TYPE_FLASH = "FLASH"
    CARD_TYPE_M2 = "M2"
    CARD_TYPE_NVME = "NVME"
    CARD_TYPE_PT = "PT"
    CARD_TYPE_SAS = "SAS"
    CARD_TYPE_SD = "SD"
    CONTAINMENT_METHOD_CHASSIS_ENCLOSURE = "chassis-enclosure"
    CONTAINMENT_METHOD_COMPUTE_ENCLOSURE = "compute-enclosure"
    CONTAINMENT_METHOD_CONTROLLER = "controller"
    CONTROLLER_MODE_AHCI = "AHCI"
    CONTROLLER_MODE_HBA = "HBA"
    CONTROLLER_MODE_M2_HWRAID = "M2HWRAID"
    CONTROLLER_MODE_NVME = "NVME"
    CONTROLLER_MODE_PHBA = "PHBA"
    CONTROLLER_MODE_PRAID = "PRAID"
    CONTROLLER_MODE_RAID = "RAID"
    CONTROLLER_MODE_SAS4 = "SAS4"
    CONTROLLER_MODE_SWRAID = "SWRAID"
    CONTROLLER_MODE_XSDS = "XSDS"
    CONTROLLER_MODE_UNKNOWN = "unknown"
    CONTROLLER_TYPE_EXTERNAL = "external"
    CONTROLLER_TYPE_INTERNAL = "internal"
    DELETED_FALSE = "false"
    DELETED_NO = "no"
    DELETED_TRUE = "true"
    DELETED_YES = "yes"
    DEPRECATED_FALSE = "false"
    DEPRECATED_NO = "no"
    DEPRECATED_TRUE = "true"
    DEPRECATED_YES = "yes"
    FORM_EMBEDDED = "embedded"
    FORM_MEZZANINE = "mezzanine"
    FORM_NONE = "none"
    FORM_ON_BOARD = "on-board"
    FORM_PCI = "pci"
    ON_BOARD_MEMORY_SIZE_UNKNOWN = "unknown"


class EquipmentLocalDiskControllerCapProvider(ManagedObject):
    """This is EquipmentLocalDiskControllerCapProvider class."""

    consts = EquipmentLocalDiskControllerCapProviderConsts()
    naming_props = set(['vendor', 'model', 'revision'])

    mo_meta = MoMeta("EquipmentLocalDiskControllerCapProvider", "equipmentLocalDiskControllerCapProvider", "manufacturer-[vendor]-model-[model]-revision-[revision]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], [""], ['capabilityCatalogue', 'equipmentHwCapDerivativeProvider'], ['adaptorFamilyTypeDef', 'equipmentDriveSecCap', 'equipmentDriveSupportedStripSizes', 'equipmentEmbeddedStorageDef', 'equipmentFirmwareUpdateRestriction', 'equipmentFlashLife', 'equipmentFruVariant', 'equipmentLocalDiskControllerDef', 'equipmentLocalDiskControllerTypeDef', 'equipmentManufacturingDef', 'equipmentOnboardDeviceDef', 'equipmentPciDef', 'equipmentPhysicalDef', 'equipmentPicture', 'equipmentRaidDef', 'equipmentServiceDef', 'equipmentSlotArrayRef', 'equipmentStorageLimitCap', 'firmwareType', 'firmwareUpgradeConstraint'], ["Get"])

    prop_meta = {
        "card_type": MoPropertyMeta("card_type", "cardType", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["FLASH", "M2", "NVME", "PT", "SAS", "SD"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "containment_method": MoPropertyMeta("containment_method", "containmentMethod", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["chassis-enclosure", "compute-enclosure", "controller"], []),
        "controller_mode": MoPropertyMeta("controller_mode", "controllerMode", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["AHCI", "HBA", "M2HWRAID", "NVME", "PHBA", "PRAID", "RAID", "SAS4", "SWRAID", "XSDS", "unknown"], []),
        "controller_type": MoPropertyMeta("controller_type", "controllerType", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["external", "internal"], []),
        "deleted": MoPropertyMeta("deleted", "deleted", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "deprecated": MoPropertyMeta("deprecated", "deprecated", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "element_load_failures": MoPropertyMeta("element_load_failures", "elementLoadFailures", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "elements_loaded": MoPropertyMeta("elements_loaded", "elementsLoaded", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "form": MoPropertyMeta("form", "form", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["embedded", "mezzanine", "none", "on-board", "pci"], []),
        "gencount": MoPropertyMeta("gencount", "gencount", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "internalports": MoPropertyMeta("internalports", "internalports", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "load_errors": MoPropertyMeta("load_errors", "loadErrors", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_warnings": MoPropertyMeta("load_warnings", "loadWarnings", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mgmt_plane_ver": MoPropertyMeta("mgmt_plane_ver", "mgmtPlaneVer", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "num_controllers": MoPropertyMeta("num_controllers", "numControllers", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "on_board_memory_size": MoPropertyMeta("on_board_memory_size", "onBoardMemorySize", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-18446744073709551615"]),
        "prom_card_type": MoPropertyMeta("prom_card_type", "promCardType", "ushort", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, 1, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x100, 1, 510, None, [], []),
    }

    prop_map = {
        "cardType": "card_type", 
        "childAction": "child_action", 
        "containmentMethod": "containment_method", 
        "controllerMode": "controller_mode", 
        "controllerType": "controller_type", 
        "deleted": "deleted", 
        "deprecated": "deprecated", 
        "dn": "dn", 
        "elementLoadFailures": "element_load_failures", 
        "elementsLoaded": "elements_loaded", 
        "form": "form", 
        "gencount": "gencount", 
        "internalports": "internalports", 
        "loadErrors": "load_errors", 
        "loadWarnings": "load_warnings", 
        "mgmtPlaneVer": "mgmt_plane_ver", 
        "model": "model", 
        "numControllers": "num_controllers", 
        "onBoardMemorySize": "on_board_memory_size", 
        "promCardType": "prom_card_type", 
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
        self.card_type = None
        self.child_action = None
        self.containment_method = None
        self.controller_mode = None
        self.controller_type = None
        self.deleted = None
        self.deprecated = None
        self.element_load_failures = None
        self.elements_loaded = None
        self.form = None
        self.gencount = None
        self.internalports = None
        self.load_errors = None
        self.load_warnings = None
        self.mgmt_plane_ver = None
        self.num_controllers = None
        self.on_board_memory_size = None
        self.prom_card_type = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentLocalDiskControllerCapProvider", parent_mo_or_dn, **kwargs)
