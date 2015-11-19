"""This module contains the general information for CapabilityFeatureLimits ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class CapabilityFeatureLimitsConsts():
    FEATURE_STATUS_SUPPORTED = "supported"
    FEATURE_STATUS_UNSUPPORTED = "unsupported"
    PLATFORM_UCS6100 = "ucs6100"
    PLATFORM_UCS6200 = "ucs6200"
    PLATFORM_UCS6324 = "ucs6324"


class CapabilityFeatureLimits(ManagedObject):
    """This is CapabilityFeatureLimits class."""

    consts = CapabilityFeatureLimitsConsts()
    naming_props = set([u'platform', u'name'])

    mo_meta = MoMeta("CapabilityFeatureLimits", "capabilityFeatureLimits", "feature-[platform]-[name]", VersionMeta.Version211a, "InputOutput", 0x3fL, [], ["admin"], [u'capabilityNetworkLimits', u'capabilityStorageLimits', u'capabilitySystemLimits'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "feature_status": MoPropertyMeta("feature_status", "featureStatus", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["supported", "unsupported"], []), 
        "limit": MoPropertyMeta("limit", "limit", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x4L, 1, 510, None, [], []), 
        "platform": MoPropertyMeta("platform", "platform", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8L, None, None, None, ["ucs6100", "ucs6200", "ucs6324"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "featureStatus": "feature_status", 
        "limit": "limit", 
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
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "CapabilityFeatureLimits", parent_mo_or_dn, **kwargs)

