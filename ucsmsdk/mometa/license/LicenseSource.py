"""This module contains the general information for LicenseSource ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LicenseSourceConsts:
    ALWAYS_USE_FALSE = "false"
    ALWAYS_USE_NO = "no"
    ALWAYS_USE_TRUE = "true"
    ALWAYS_USE_YES = "yes"


class LicenseSource(ManagedObject):
    """This is LicenseSource class."""

    consts = LicenseSourceConsts()
    naming_props = set([])

    mo_meta = MoMeta("LicenseSource", "licenseSource", "source", VersionMeta.Version141i, "InputOutput", 0x1f, [], ["read-only"], ['licenseFile'], [], ["Get"])

    prop_meta = {
        "always_use": MoPropertyMeta("always_use", "alwaysUse", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "host_id": MoPropertyMeta("host_id", "hostId", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "host_name": MoPropertyMeta("host_name", "hostName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sku": MoPropertyMeta("sku", "sku", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vendor_daemon_path": MoPropertyMeta("vendor_daemon_path", "vendorDaemonPath", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "alwaysUse": "always_use", 
        "childAction": "child_action", 
        "dn": "dn", 
        "hostId": "host_id", 
        "hostName": "host_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sku": "sku", 
        "status": "status", 
        "vendorDaemonPath": "vendor_daemon_path", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.always_use = None
        self.child_action = None
        self.host_id = None
        self.host_name = None
        self.sacl = None
        self.sku = None
        self.status = None
        self.vendor_daemon_path = None

        ManagedObject.__init__(self, "LicenseSource", parent_mo_or_dn, **kwargs)
