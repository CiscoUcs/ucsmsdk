"""This module contains the general information for FirmwareBundleTypeCapProvider ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareBundleTypeCapProviderConsts:
    DELETED_FALSE = "false"
    DELETED_NO = "no"
    DELETED_TRUE = "true"
    DELETED_YES = "yes"
    DEPRECATED_FALSE = "false"
    DEPRECATED_NO = "no"
    DEPRECATED_TRUE = "true"
    DEPRECATED_YES = "yes"
    PLATFORM_TYPE_UCS = "UCS"
    PLATFORM_TYPE_UCS_6300 = "UCS-6300"
    PLATFORM_TYPE_UCS_6400 = "UCS-6400"
    PLATFORM_TYPE_UCS_6500 = "UCS-6500"
    PLATFORM_TYPE_UCS_MINI = "UCS-MINI"
    PLATFORM_TYPE_UCSX_9100 = "UCSX-9100"


class FirmwareBundleTypeCapProvider(ManagedObject):
    """This is FirmwareBundleTypeCapProvider class."""

    consts = FirmwareBundleTypeCapProviderConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareBundleTypeCapProvider", "firmwareBundleTypeCapProvider", "bundle-type-cap", VersionMeta.Version141i, "InputOutput", 0x1f, [], [""], ['capabilityCatalogue'], ['firmwareBundleType', 'firmwareChassisComponentSpec', 'firmwareComponentSpec'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "deleted": MoPropertyMeta("deleted", "deleted", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "deprecated": MoPropertyMeta("deprecated", "deprecated", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "element_load_failures": MoPropertyMeta("element_load_failures", "elementLoadFailures", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "elements_loaded": MoPropertyMeta("elements_loaded", "elementsLoaded", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "gencount": MoPropertyMeta("gencount", "gencount", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "load_errors": MoPropertyMeta("load_errors", "loadErrors", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_warnings": MoPropertyMeta("load_warnings", "loadWarnings", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mgmt_plane_ver": MoPropertyMeta("mgmt_plane_ver", "mgmtPlaneVer", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "platform_type": MoPropertyMeta("platform_type", "platformType", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["UCS", "UCS-6300", "UCS-6400", "UCS-6500", "UCS-MINI", "UCSX-9100"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "deleted": "deleted", 
        "deprecated": "deprecated", 
        "dn": "dn", 
        "elementLoadFailures": "element_load_failures", 
        "elementsLoaded": "elements_loaded", 
        "gencount": "gencount", 
        "loadErrors": "load_errors", 
        "loadWarnings": "load_warnings", 
        "mgmtPlaneVer": "mgmt_plane_ver", 
        "model": "model", 
        "platformType": "platform_type", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.deleted = None
        self.deprecated = None
        self.element_load_failures = None
        self.elements_loaded = None
        self.gencount = None
        self.load_errors = None
        self.load_warnings = None
        self.mgmt_plane_ver = None
        self.model = None
        self.platform_type = None
        self.sacl = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "FirmwareBundleTypeCapProvider", parent_mo_or_dn, **kwargs)
