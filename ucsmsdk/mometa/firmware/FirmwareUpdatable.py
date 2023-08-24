"""This module contains the general information for FirmwareUpdatable ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareUpdatableConsts:
    ADMIN_STATE_FORCE_TRIGGER = "force-trigger"
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"
    DEPLOYMENT_BACKUP = "backup"
    DEPLOYMENT_UNSPECIFIED = "unspecified"
    OPER_STATE_ACTIVATING = "activating"
    OPER_STATE_AUTO_ACTIVATING = "auto-activating"
    OPER_STATE_AUTO_UPDATING = "auto-updating"
    OPER_STATE_BAD_IMAGE = "bad-image"
    OPER_STATE_DOWNGRADE_NOT_SUPPORTED = "downgrade-not-supported"
    OPER_STATE_DOWNLOAD_ERROR = "download-error"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_FAULTY_STATE = "faulty-state"
    OPER_STATE_OPERATION_NOT_SUPPORTED = "operation-not-supported"
    OPER_STATE_PENDING_NEXT_BOOT = "pending-next-boot"
    OPER_STATE_PENDING_POWER_CYCLE = "pending-power-cycle"
    OPER_STATE_READY = "ready"
    OPER_STATE_REBOOTING = "rebooting"
    OPER_STATE_REBUILDING = "rebuilding"
    OPER_STATE_SCHEDULED = "scheduled"
    OPER_STATE_SET_STARTUP = "set-startup"
    OPER_STATE_THROTTLED = "throttled"
    OPER_STATE_UPDATING = "updating"
    OPER_STATE_UPGRADING = "upgrading"
    OPER_STATE_VESSEL_NOT_FOUND = "vessel-not-found"
    OPER_STATE_VESSEL_VALIDATE_ERROR = "vessel-validate-error"
    OPER_STATE_WAITING = "waiting"
    OPER_STATE_QUAL_BOOT_CONF_MISSING = "boot-conf-missing"
    OPER_STATE_QUAL_CHECKSUM_FAILURE = "checksum-failure"
    OPER_STATE_QUAL_CRC_FAILURE = "crc-failure"
    OPER_STATE_QUAL_FILESYSTEM_ERROR = "filesystem-error"
    OPER_STATE_QUAL_MGMT_CONNECT_ERROR = "mgmt-connect-error"
    OPER_STATE_QUAL_NONE = "none"
    OPER_STATE_QUAL_REBUILDING = "rebuilding"
    OPER_STATE_QUAL_UNKNOWN_ERROR = "unknown-error"


class FirmwareUpdatable(ManagedObject):
    """This is FirmwareUpdatable class."""

    consts = FirmwareUpdatableConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareUpdatable", "firmwareUpdatable", "fw-updatable", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["admin"], ['biosUnit', 'equipmentPsu', 'mgmtController', 'storageOnboardDevice'], ['faultInst', 'firmwareInstallable'], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["force-trigger", "trigger", "triggered"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "deployment": MoPropertyMeta("deployment", "deployment", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["backup", "unspecified"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "auto-activating", "auto-updating", "bad-image", "downgrade-not-supported", "download-error", "failed", "faulty-state", "operation-not-supported", "pending-next-boot", "pending-power-cycle", "ready", "rebooting", "rebuilding", "scheduled", "set-startup", "throttled", "updating", "upgrading", "vessel-not-found", "vessel-validate-error", "waiting"], []),
        "oper_state_qual": MoPropertyMeta("oper_state_qual", "operStateQual", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["boot-conf-missing", "checksum-failure", "crc-failure", "filesystem-error", "mgmt-connect-error", "none", "rebuilding", "unknown-error"], []),
        "prev_version": MoPropertyMeta("prev_version", "prevVersion", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "deployment": "deployment", 
        "dn": "dn", 
        "operState": "oper_state", 
        "operStateQual": "oper_state_qual", 
        "prevVersion": "prev_version", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.deployment = None
        self.oper_state = None
        self.oper_state_qual = None
        self.prev_version = None
        self.sacl = None
        self.status = None
        self.version = None

        ManagedObject.__init__(self, "FirmwareUpdatable", parent_mo_or_dn, **kwargs)
