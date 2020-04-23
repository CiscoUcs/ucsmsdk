"""This module contains the general information for LicenseFeatureCapProvider ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LicenseFeatureCapProviderConsts:
    DELETED_FALSE = "false"
    DELETED_NO = "no"
    DELETED_TRUE = "true"
    DELETED_YES = "yes"
    DEPRECATED_FALSE = "false"
    DEPRECATED_NO = "no"
    DEPRECATED_TRUE = "true"
    DEPRECATED_YES = "yes"
    TYPE_BOOLEAN = "boolean"
    TYPE_COUNTED = "counted"


class LicenseFeatureCapProvider(ManagedObject):
    """This is LicenseFeatureCapProvider class."""

    consts = LicenseFeatureCapProviderConsts()
    naming_props = set(['featureName', 'licVendor', 'licVersion', 'vendor', 'model', 'revision'])

    mo_meta = MoMeta("LicenseFeatureCapProvider", "licenseFeatureCapProvider", "feature-[feature_name]-[lic_vendor]|[lic_version]manufacturer-[vendor]-model-[model]-revision-[revision]", VersionMeta.Version141i, "InputOutput", 0x3fff, [], [""], ['capabilityCatalogue'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "def_quant": MoPropertyMeta("def_quant", "defQuant", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["0-4294967295"]),
        "deleted": MoPropertyMeta("deleted", "deleted", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "deprecated": MoPropertyMeta("deprecated", "deprecated", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "element_load_failures": MoPropertyMeta("element_load_failures", "elementLoadFailures", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "elements_loaded": MoPropertyMeta("elements_loaded", "elementsLoaded", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "feature_name": MoPropertyMeta("feature_name", "featureName", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x10, 1, 64, None, [], []),
        "gencount": MoPropertyMeta("gencount", "gencount", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "grace_period": MoPropertyMeta("grace_period", "gracePeriod", "ulong", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
        "lic_vendor": MoPropertyMeta("lic_vendor", "licVendor", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x40, 1, 510, None, [], []),
        "lic_version": MoPropertyMeta("lic_version", "licVersion", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x80, 1, 510, None, [], []),
        "load_errors": MoPropertyMeta("load_errors", "loadErrors", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_warnings": MoPropertyMeta("load_warnings", "loadWarnings", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mgmt_plane_ver": MoPropertyMeta("mgmt_plane_ver", "mgmtPlaneVer", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x100, 1, 510, None, [], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x200, 1, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sku": MoPropertyMeta("sku", "sku", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["boolean", "counted"], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x2000, 1, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "defQuant": "def_quant", 
        "deleted": "deleted", 
        "deprecated": "deprecated", 
        "dn": "dn", 
        "elementLoadFailures": "element_load_failures", 
        "elementsLoaded": "elements_loaded", 
        "featureName": "feature_name", 
        "gencount": "gencount", 
        "gracePeriod": "grace_period", 
        "licVendor": "lic_vendor", 
        "licVersion": "lic_version", 
        "loadErrors": "load_errors", 
        "loadWarnings": "load_warnings", 
        "mgmtPlaneVer": "mgmt_plane_ver", 
        "model": "model", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sku": "sku", 
        "status": "status", 
        "type": "type", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, feature_name, lic_vendor, lic_version, vendor, model, revision, **kwargs):
        self._dirty_mask = 0
        self.feature_name = feature_name
        self.lic_vendor = lic_vendor
        self.lic_version = lic_version
        self.vendor = vendor
        self.model = model
        self.revision = revision
        self.child_action = None
        self.def_quant = None
        self.deleted = None
        self.deprecated = None
        self.element_load_failures = None
        self.elements_loaded = None
        self.gencount = None
        self.grace_period = None
        self.load_errors = None
        self.load_warnings = None
        self.mgmt_plane_ver = None
        self.sacl = None
        self.sku = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LicenseFeatureCapProvider", parent_mo_or_dn, **kwargs)
