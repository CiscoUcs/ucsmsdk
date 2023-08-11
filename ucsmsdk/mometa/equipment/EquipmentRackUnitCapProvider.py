"""This module contains the general information for EquipmentRackUnitCapProvider ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentRackUnitCapProviderConsts:
    DELETED_FALSE = "false"
    DELETED_NO = "no"
    DELETED_TRUE = "true"
    DELETED_YES = "yes"
    DEPRECATED_FALSE = "false"
    DEPRECATED_NO = "no"
    DEPRECATED_TRUE = "true"
    DEPRECATED_YES = "yes"
    FORM_ENCLOSURE_MOUNT = "enclosure-mount"
    FORM_RACK_MOUNT = "rack-mount"


class EquipmentRackUnitCapProvider(ManagedObject):
    """This is EquipmentRackUnitCapProvider class."""

    consts = EquipmentRackUnitCapProviderConsts()
    naming_props = set(['vendor', 'model', 'revision'])

    mo_meta = MoMeta("EquipmentRackUnitCapProvider", "equipmentRackUnitCapProvider", "manufacturer-[vendor]-model-[model]-revision-[revision]", VersionMeta.Version141i, "InputOutput", 0x1ff, [], [""], ['capabilityCatalogue', 'equipmentHwCapDerivativeProvider'], ['adaptorFruCapRef', 'computeConstraintDef', 'computeMemoryUnitConstraintDef', 'computePciCap', 'computeServerTypeCap', 'equipmentAdvancedBootOrder', 'equipmentAutoConfigMode', 'equipmentBiosDef', 'equipmentBiosPasswordReset', 'equipmentBiosTokenOverride', 'equipmentBladeAGLibrary', 'equipmentBoardControllerDef', 'equipmentBootDeviceConstraints', 'equipmentCimcVmedia', 'equipmentCiscoOsOpenGate', 'equipmentDiagFeatureSupport', 'equipmentDimmMapping', 'equipmentDiscoveryCap', 'equipmentDriveSecCap', 'equipmentEmbeddedControllerConfig', 'equipmentFanAggressiveCoolingCap', 'equipmentFlexFlashNonRemovable', 'equipmentFruVariant', 'equipmentGraphicsCardCapRef', 'equipmentHostMgmtControllerCap', 'equipmentHwRevisionModifier', 'equipmentHxCap', 'equipmentInbandMgmtCap', 'equipmentKvmMgmtCap', 'equipmentLocalDiskControllerCapRef', 'equipmentManufacturingDef', 'equipmentNvmeDef', 'equipmentPciSlotIdMapping', 'equipmentPcieSlotOrientation', 'equipmentPersonality', 'equipmentPhysicalDef', 'equipmentPicture', 'equipmentPnuosBootMode', 'equipmentPowerCapDef', 'equipmentRackFanModuleDef', 'equipmentSecureBoot', 'equipmentServerCorrectUuidBehavior', 'equipmentServerFeatureCap', 'equipmentServiceDef', 'equipmentSlotArray', 'equipmentSlotArrayRef', 'equipmentSpdmCertificateCap', 'equipmentStorageControllerConfig', 'equipmentStorageControllerSlotDef', 'equipmentStorageSasExpanderCapRef', 'equipmentUuidFeatureCap', 'firmwareConstraints', 'firmwareType', 'firmwareUpgradeConstraint', 'storageEnclosureCap'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "deleted": MoPropertyMeta("deleted", "deleted", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "deprecated": MoPropertyMeta("deprecated", "deprecated", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "element_load_failures": MoPropertyMeta("element_load_failures", "elementLoadFailures", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "elements_loaded": MoPropertyMeta("elements_loaded", "elementsLoaded", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "form": MoPropertyMeta("form", "form", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["enclosure-mount", "rack-mount"], []),
        "gencount": MoPropertyMeta("gencount", "gencount", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "generation": MoPropertyMeta("generation", "generation", "ushort", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_errors": MoPropertyMeta("load_errors", "loadErrors", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_warnings": MoPropertyMeta("load_warnings", "loadWarnings", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "max_local_disks": MoPropertyMeta("max_local_disks", "maxLocalDisks", "ushort", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mgmt_plane_ver": MoPropertyMeta("mgmt_plane_ver", "mgmtPlaneVer", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "prom_card_type": MoPropertyMeta("prom_card_type", "promCardType", "ushort", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x20, 1, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x100, 1, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "deleted": "deleted", 
        "deprecated": "deprecated", 
        "dn": "dn", 
        "elementLoadFailures": "element_load_failures", 
        "elementsLoaded": "elements_loaded", 
        "form": "form", 
        "gencount": "gencount", 
        "generation": "generation", 
        "loadErrors": "load_errors", 
        "loadWarnings": "load_warnings", 
        "maxLocalDisks": "max_local_disks", 
        "mgmtPlaneVer": "mgmt_plane_ver", 
        "model": "model", 
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
        self.child_action = None
        self.deleted = None
        self.deprecated = None
        self.element_load_failures = None
        self.elements_loaded = None
        self.form = None
        self.gencount = None
        self.generation = None
        self.load_errors = None
        self.load_warnings = None
        self.max_local_disks = None
        self.mgmt_plane_ver = None
        self.prom_card_type = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentRackUnitCapProvider", parent_mo_or_dn, **kwargs)
