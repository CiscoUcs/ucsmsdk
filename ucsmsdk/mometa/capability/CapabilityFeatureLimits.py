"""This module contains the general information for CapabilityFeatureLimits ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CapabilityFeatureLimitsConsts:
    FEATURE_STATUS_SUPPORTED = "supported"
    FEATURE_STATUS_UNSUPPORTED = "unsupported"
    PLATFORM_UCS6100 = "ucs6100"
    PLATFORM_UCS6200 = "ucs6200"
    PLATFORM_UCS6300 = "ucs6300"
    PLATFORM_UCS6300_UP = "ucs6300UP"
    PLATFORM_UCS6324 = "ucs6324"
    PLATFORM_UCS6400 = "ucs6400"
    PLATFORM_UCS6500 = "ucs6500"
    PLATFORM_UCSX9100 = "ucsx9100"


class CapabilityFeatureLimits(ManagedObject):
    """This is CapabilityFeatureLimits class."""

    consts = CapabilityFeatureLimitsConsts()
    naming_props = set(['platform', 'name'])

    mo_meta = MoMeta("CapabilityFeatureLimits", "capabilityFeatureLimits", "feature-[platform]-[name]", VersionMeta.Version211a, "InputOutput", 0x7f, [], ["admin"], ['capabilityNetworkLimits', 'capabilityStorageLimits', 'capabilitySystemLimits'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "feature_status": MoPropertyMeta("feature_status", "featureStatus", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["supported", "unsupported"], []),
        "limit": MoPropertyMeta("limit", "limit", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "min_ucsm_version": MoPropertyMeta("min_ucsm_version", "minUCSMVersion", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "platform": MoPropertyMeta("platform", "platform", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x10, None, None, None, ["ucs6100", "ucs6200", "ucs6300", "ucs6300UP", "ucs6324", "ucs6400", "ucs6500", "ucsx9100"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "featureStatus": "feature_status", 
        "limit": "limit", 
        "minUCSMVersion": "min_ucsm_version", 
        "name": "name", 
        "platform": "platform", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, platform, name, **kwargs):
        self._dirty_mask = 0
        self.platform = platform
        self.name = name
        self.child_action = None
        self.descr = None
        self.feature_status = None
        self.limit = None
        self.min_ucsm_version = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "CapabilityFeatureLimits", parent_mo_or_dn, **kwargs)
