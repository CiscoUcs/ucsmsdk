"""This module contains the general information for FirmwareStatus ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareStatusConsts:
    BACK_UP_HOLDER_OPER_STATE_ACTIVATING = "activating"
    BACK_UP_HOLDER_OPER_STATE_AUTO_ACTIVATING = "auto-activating"
    BACK_UP_HOLDER_OPER_STATE_AUTO_UPDATING = "auto-updating"
    BACK_UP_HOLDER_OPER_STATE_BAD_IMAGE = "bad-image"
    BACK_UP_HOLDER_OPER_STATE_DOWNGRADE_NOT_SUPPORTED = "downgrade-not-supported"
    BACK_UP_HOLDER_OPER_STATE_DOWNLOAD_ERROR = "download-error"
    BACK_UP_HOLDER_OPER_STATE_FAILED = "failed"
    BACK_UP_HOLDER_OPER_STATE_FAULTY_STATE = "faulty-state"
    BACK_UP_HOLDER_OPER_STATE_OPERATION_NOT_SUPPORTED = "operation-not-supported"
    BACK_UP_HOLDER_OPER_STATE_PENDING_NEXT_BOOT = "pending-next-boot"
    BACK_UP_HOLDER_OPER_STATE_PENDING_POWER_CYCLE = "pending-power-cycle"
    BACK_UP_HOLDER_OPER_STATE_READY = "ready"
    BACK_UP_HOLDER_OPER_STATE_REBOOTING = "rebooting"
    BACK_UP_HOLDER_OPER_STATE_REBUILDING = "rebuilding"
    BACK_UP_HOLDER_OPER_STATE_SCHEDULED = "scheduled"
    BACK_UP_HOLDER_OPER_STATE_SET_STARTUP = "set-startup"
    BACK_UP_HOLDER_OPER_STATE_THROTTLED = "throttled"
    BACK_UP_HOLDER_OPER_STATE_UPDATING = "updating"
    BACK_UP_HOLDER_OPER_STATE_UPGRADING = "upgrading"
    BACK_UP_HOLDER_OPER_STATE_VESSEL_NOT_FOUND = "vessel-not-found"
    BACK_UP_HOLDER_OPER_STATE_VESSEL_VALIDATE_ERROR = "vessel-validate-error"
    BACK_UP_HOLDER_OPER_STATE_WAITING = "waiting"
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
    SERVICE_PACK_OPER_STATE_ACTIVATING = "activating"
    SERVICE_PACK_OPER_STATE_AUTO_ACTIVATING = "auto-activating"
    SERVICE_PACK_OPER_STATE_AUTO_UPDATING = "auto-updating"
    SERVICE_PACK_OPER_STATE_BAD_IMAGE = "bad-image"
    SERVICE_PACK_OPER_STATE_DOWNGRADE_NOT_SUPPORTED = "downgrade-not-supported"
    SERVICE_PACK_OPER_STATE_DOWNLOAD_ERROR = "download-error"
    SERVICE_PACK_OPER_STATE_FAILED = "failed"
    SERVICE_PACK_OPER_STATE_FAULTY_STATE = "faulty-state"
    SERVICE_PACK_OPER_STATE_OPERATION_NOT_SUPPORTED = "operation-not-supported"
    SERVICE_PACK_OPER_STATE_PENDING_NEXT_BOOT = "pending-next-boot"
    SERVICE_PACK_OPER_STATE_PENDING_POWER_CYCLE = "pending-power-cycle"
    SERVICE_PACK_OPER_STATE_READY = "ready"
    SERVICE_PACK_OPER_STATE_REBOOTING = "rebooting"
    SERVICE_PACK_OPER_STATE_REBUILDING = "rebuilding"
    SERVICE_PACK_OPER_STATE_SCHEDULED = "scheduled"
    SERVICE_PACK_OPER_STATE_SET_STARTUP = "set-startup"
    SERVICE_PACK_OPER_STATE_THROTTLED = "throttled"
    SERVICE_PACK_OPER_STATE_UPDATING = "updating"
    SERVICE_PACK_OPER_STATE_UPGRADING = "upgrading"
    SERVICE_PACK_OPER_STATE_VESSEL_NOT_FOUND = "vessel-not-found"
    SERVICE_PACK_OPER_STATE_VESSEL_VALIDATE_ERROR = "vessel-validate-error"
    SERVICE_PACK_OPER_STATE_WAITING = "waiting"


class FirmwareStatus(ManagedObject):
    """This is FirmwareStatus class."""

    consts = FirmwareStatusConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareStatus", "firmwareStatus", "fw-status", VersionMeta.Version211a, "InputOutput", 0x1f, [], ["admin"], ['computeBlade', 'computeRackUnit', 'computeServerUnit', 'equipmentChassis', 'equipmentIOCard', 'equipmentPsu', 'networkElement', 'topSystem'], ['faultInst'], ["Get"])

    prop_meta = {
        "back_up_holder_oper_state": MoPropertyMeta("back_up_holder_oper_state", "backUpHolderOperState", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "auto-activating", "auto-updating", "bad-image", "downgrade-not-supported", "download-error", "failed", "faulty-state", "operation-not-supported", "pending-next-boot", "pending-power-cycle", "ready", "rebooting", "rebuilding", "scheduled", "set-startup", "throttled", "updating", "upgrading", "vessel-not-found", "vessel-validate-error", "waiting"], []),
        "back_up_holder_pack_version": MoPropertyMeta("back_up_holder_pack_version", "backUpHolderPackVersion", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cimc_version": MoPropertyMeta("cimc_version", "cimcVersion", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "firmware_state": MoPropertyMeta("firmware_state", "firmwareState", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|no-firmware-mismatch|cimc-firmware-mismatch|pld-firmware-mismatch),){0,3}(defaultValue|no-firmware-mismatch|cimc-firmware-mismatch|pld-firmware-mismatch){0,1}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "auto-activating", "auto-updating", "bad-image", "downgrade-not-supported", "download-error", "failed", "faulty-state", "operation-not-supported", "pending-next-boot", "pending-power-cycle", "ready", "rebooting", "rebuilding", "scheduled", "set-startup", "throttled", "updating", "upgrading", "vessel-not-found", "vessel-validate-error", "waiting"], []),
        "package_version": MoPropertyMeta("package_version", "packageVersion", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "pld_version": MoPropertyMeta("pld_version", "pldVersion", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "service_pack_oper_state": MoPropertyMeta("service_pack_oper_state", "servicePackOperState", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "auto-activating", "auto-updating", "bad-image", "downgrade-not-supported", "download-error", "failed", "faulty-state", "operation-not-supported", "pending-next-boot", "pending-power-cycle", "ready", "rebooting", "rebuilding", "scheduled", "set-startup", "throttled", "updating", "upgrading", "vessel-not-found", "vessel-validate-error", "waiting"], []),
        "service_pack_version": MoPropertyMeta("service_pack_version", "servicePackVersion", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "backUpHolderOperState": "back_up_holder_oper_state", 
        "backUpHolderPackVersion": "back_up_holder_pack_version", 
        "childAction": "child_action", 
        "cimcVersion": "cimc_version", 
        "dn": "dn", 
        "firmwareState": "firmware_state", 
        "operState": "oper_state", 
        "packageVersion": "package_version", 
        "pldVersion": "pld_version", 
        "rn": "rn", 
        "sacl": "sacl", 
        "servicePackOperState": "service_pack_oper_state", 
        "servicePackVersion": "service_pack_version", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.back_up_holder_oper_state = None
        self.back_up_holder_pack_version = None
        self.child_action = None
        self.cimc_version = None
        self.firmware_state = None
        self.oper_state = None
        self.package_version = None
        self.pld_version = None
        self.sacl = None
        self.service_pack_oper_state = None
        self.service_pack_version = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareStatus", parent_mo_or_dn, **kwargs)
