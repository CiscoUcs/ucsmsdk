"""This module contains the general information for FirmwareServicePack ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareServicePackConsts:
    LAST_KNOWN_STATUS_ACTIVE = "active"
    LAST_KNOWN_STATUS_ACTIVE_COMMITTED = "active-committed"
    LAST_KNOWN_STATUS_ACTIVE_COMMITTED_ON_RELOAD = "active-committed-on-reload"
    LAST_KNOWN_STATUS_ACTIVE_ON_RELOAD = "active-on-reload"
    LAST_KNOWN_STATUS_FAILED = "failed"
    LAST_KNOWN_STATUS_INACTIVE = "inactive"
    LAST_KNOWN_STATUS_INACTIVE_COMMITTED = "inactive-committed"
    LAST_KNOWN_STATUS_INACTIVE_COMMITTED_ON_RELOAD = "inactive-committed-on-reload"
    LAST_KNOWN_STATUS_INACTIVE_ON_RELOAD = "inactive-on-reload"
    LAST_KNOWN_STATUS_NOT_INSTALLED = "not-installed"
    LAST_KNOWN_STATUS_READY = "ready"
    LAST_KNOWN_STATUS_TRANSIENT = "transient"
    LAST_KNOWN_STATUS_UNKNOWN = "unknown"
    LAST_KNOWN_STATUS_UNKNOWN_INSTALLER_BUSY = "unknown-installer-busy"


class FirmwareServicePack(ManagedObject):
    """This is FirmwareServicePack class."""

    consts = FirmwareServicePackConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareServicePack", "firmwareServicePack", "servicepack", VersionMeta.Version321d, "InputOutput", 0x3f, [], ["admin"], ['firmwareBootUnit', 'firmwareRunning'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "default_sp_version": MoPropertyMeta("default_sp_version", "defaultSpVersion", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "last_known_status": MoPropertyMeta("last_known_status", "lastKnownStatus", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "active-committed", "active-committed-on-reload", "active-on-reload", "failed", "inactive", "inactive-committed", "inactive-committed-on-reload", "inactive-on-reload", "not-installed", "ready", "transient", "unknown", "unknown-installer-busy"], []),
        "modules": MoPropertyMeta("modules", "modules", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "defaultSpVersion": "default_sp_version", 
        "dn": "dn", 
        "lastKnownStatus": "last_known_status", 
        "modules": "modules", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.default_sp_version = None
        self.last_known_status = None
        self.modules = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareServicePack", parent_mo_or_dn, **kwargs)
