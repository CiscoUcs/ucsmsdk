"""This module contains the general information for ControllerMgmtDbCheckPol ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ControllerMgmtDbCheckPolConsts:
    RESET_CORRUPT_COUNT_FALSE = "false"
    RESET_CORRUPT_COUNT_NO = "no"
    RESET_CORRUPT_COUNT_TRUE = "true"
    RESET_CORRUPT_COUNT_YES = "yes"
    TRIGGER_HEALTH_CHECK_FALSE = "false"
    TRIGGER_HEALTH_CHECK_NO = "no"
    TRIGGER_HEALTH_CHECK_TRUE = "true"
    TRIGGER_HEALTH_CHECK_YES = "yes"


class ControllerMgmtDbCheckPol(ManagedObject):
    """This is ControllerMgmtDbCheckPol class."""

    consts = ControllerMgmtDbCheckPolConsts()
    naming_props = set([])

    mo_meta = MoMeta("ControllerMgmtDbCheckPol", "controllerMgmtDbCheckPol", "MgmtDbCheckPol", VersionMeta.Version321d, "InputOutput", 0x1ff, [], ["admin"], ['topSystem'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "health_check_interval": MoPropertyMeta("health_check_interval", "healthCheckInterval", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-168"]),
        "internal_backup_interval": MoPropertyMeta("internal_backup_interval", "internalBackupInterval", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-60"]),
        "last_integrity_check_time": MoPropertyMeta("last_integrity_check_time", "lastIntegrityCheckTime", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "last_internal_backup_time": MoPropertyMeta("last_internal_backup_time", "lastInternalBackupTime", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "reset_corrupt_count": MoPropertyMeta("reset_corrupt_count", "resetCorruptCount", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "trigger_health_check": MoPropertyMeta("trigger_health_check", "triggerHealthCheck", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["false", "no", "true", "yes"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "healthCheckInterval": "health_check_interval", 
        "internalBackupInterval": "internal_backup_interval", 
        "lastIntegrityCheckTime": "last_integrity_check_time", 
        "lastInternalBackupTime": "last_internal_backup_time", 
        "resetCorruptCount": "reset_corrupt_count", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "triggerHealthCheck": "trigger_health_check", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.health_check_interval = None
        self.internal_backup_interval = None
        self.last_integrity_check_time = None
        self.last_internal_backup_time = None
        self.reset_corrupt_count = None
        self.sacl = None
        self.status = None
        self.trigger_health_check = None

        ManagedObject.__init__(self, "ControllerMgmtDbCheckPol", parent_mo_or_dn, **kwargs)
