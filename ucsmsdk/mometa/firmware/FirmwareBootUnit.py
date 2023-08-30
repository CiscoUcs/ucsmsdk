"""This module contains the general information for FirmwareBootUnit ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareBootUnitConsts:
    ADMIN_STATE_FORCE_TRIGGER = "force-trigger"
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"
    IGNORE_COMP_CHECK_FALSE = "false"
    IGNORE_COMP_CHECK_NO = "no"
    IGNORE_COMP_CHECK_TRUE = "true"
    IGNORE_COMP_CHECK_YES = "yes"
    IMAGE_BACKUP = "backup"
    IMAGE_RUNNING = "running"
    MODE_INSTALL = "install"
    MODE_UPGRADE = "upgrade"
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
    RESET_ON_ACTIVATE_FALSE = "false"
    RESET_ON_ACTIVATE_NO = "no"
    RESET_ON_ACTIVATE_TRUE = "true"
    RESET_ON_ACTIVATE_YES = "yes"
    SKIP_VALIDATION_FALSE = "false"
    SKIP_VALIDATION_NO = "no"
    SKIP_VALIDATION_TRUE = "true"
    SKIP_VALIDATION_YES = "yes"


class FirmwareBootUnit(ManagedObject):
    """This is FirmwareBootUnit class."""

    consts = FirmwareBootUnitConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("FirmwareBootUnit", "firmwareBootUnit", "bootunit-[type]", VersionMeta.Version101e, "InputOutput", 0xfff, [], ["admin"], ['firmwareBootDefinition'], ['faultInst', 'firmwareInstallable', 'firmwareServicePack'], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["force-trigger", "trigger", "triggered"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "ignore_comp_check": MoPropertyMeta("ignore_comp_check", "ignoreCompCheck", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []),
        "image": MoPropertyMeta("image", "image", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["backup", "running"], []),
        "inv_tag": MoPropertyMeta("inv_tag", "invTag", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["install", "upgrade"], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "auto-activating", "auto-updating", "bad-image", "downgrade-not-supported", "download-error", "failed", "faulty-state", "operation-not-supported", "pending-next-boot", "pending-power-cycle", "ready", "rebooting", "rebuilding", "scheduled", "set-startup", "throttled", "updating", "upgrading", "vessel-not-found", "vessel-validate-error", "waiting"], []),
        "prev_version": MoPropertyMeta("prev_version", "prevVersion", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "reset_on_activate": MoPropertyMeta("reset_on_activate", "resetOnActivate", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "skip_validation": MoPropertyMeta("skip_validation", "skipValidation", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["false", "no", "true", "yes"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x400, None, None, r"""((kernel|system|combined|boot-loader|service-pack),){0,4}(kernel|system|combined|boot-loader|service-pack){0,1}""", [], []),
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800, 0, 510, None, [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "ignoreCompCheck": "ignore_comp_check", 
        "image": "image", 
        "invTag": "inv_tag", 
        "mode": "mode", 
        "operState": "oper_state", 
        "prevVersion": "prev_version", 
        "resetOnActivate": "reset_on_activate", 
        "rn": "rn", 
        "sacl": "sacl", 
        "skipValidation": "skip_validation", 
        "status": "status", 
        "type": "type", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.admin_state = None
        self.child_action = None
        self.ignore_comp_check = None
        self.image = None
        self.inv_tag = None
        self.mode = None
        self.oper_state = None
        self.prev_version = None
        self.reset_on_activate = None
        self.sacl = None
        self.skip_validation = None
        self.status = None
        self.version = None

        ManagedObject.__init__(self, "FirmwareBootUnit", parent_mo_or_dn, **kwargs)
