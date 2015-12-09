"""This module contains the general information for FirmwareBundleInfoDigest ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FirmwareBundleInfoDigestConsts():
    TYPE_B_SERIES_BUNDLE = "b-series-bundle"
    TYPE_C_SERIES_BUNDLE = "c-series-bundle"
    TYPE_CATALOG = "catalog"
    TYPE_FULL_BUNDLE = "full-bundle"
    TYPE_IMAGE = "image"
    TYPE_INFRASTRUCTURE_BUNDLE = "infrastructure-bundle"
    TYPE_M_SERIES_BUNDLE = "m-series-bundle"
    TYPE_S_SERIES_BUNDLE = "s-series-bundle"
    TYPE_UNKNOWN = "unknown"


class FirmwareBundleInfoDigest(ManagedObject):
    """This is FirmwareBundleInfoDigest class."""

    consts = FirmwareBundleInfoDigestConsts()
    naming_props = set([u'type', u'version'])

    mo_meta = MoMeta("FirmwareBundleInfoDigest", "firmwareBundleInfoDigest", "bundleinfo-[type]-version-[version]", VersionMeta.Version211a, "InputOutput", 0x7fL, [], ["read-only"], [], [], [None])

    prop_meta = {
        "bundle_name": MoPropertyMeta("bundle_name", "bundleName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x20L, None, None, None, ["b-series-bundle", "c-series-bundle", "catalog", "full-bundle", "image", "infrastructure-bundle", "m-series-bundle", "s-series-bundle", "unknown"], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x40L, 1, 510, None, [], []), 
    }

    prop_map = {
        "bundleName": "bundle_name", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, type, version, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.version = version
        self.bundle_name = None
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareBundleInfoDigest", parent_mo_or_dn, **kwargs)

