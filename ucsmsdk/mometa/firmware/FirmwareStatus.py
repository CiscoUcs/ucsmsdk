"""This module contains the general information for FirmwareStatus ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareStatusConsts:
    OPER_STATE_ACTIVATING = "activating"
    OPER_STATE_AUTO_ACTIVATING = "auto-activating"
    OPER_STATE_AUTO_UPDATING = "auto-updating"
    OPER_STATE_BAD_IMAGE = "bad-image"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_FAULTY_STATE = "faulty-state"
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


class FirmwareStatus(ManagedObject):
    """This is FirmwareStatus class."""

    consts = FirmwareStatusConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareStatus", "firmwareStatus", "fw-status", VersionMeta.Version211a, "InputOutput", 0x1f, [], ["admin"], [u'computeBlade', u'computeRackUnit', u'computeServerUnit', u'equipmentChassis', u'equipmentIOCard', u'equipmentPsu', u'networkElement', u'topSystem'], [u'faultInst'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cimc_version": MoPropertyMeta("cimc_version", "cimcVersion", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "firmware_state": MoPropertyMeta("firmware_state", "firmwareState", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|no-firmware-mismatch|cimc-firmware-mismatch|pld-firmware-mismatch),){0,3}(defaultValue|no-firmware-mismatch|cimc-firmware-mismatch|pld-firmware-mismatch){0,1}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "auto-activating", "auto-updating", "bad-image", "failed", "faulty-state", "pending-next-boot", "pending-power-cycle", "ready", "rebooting", "rebuilding", "scheduled", "set-startup", "throttled", "updating", "upgrading"], []), 
        "package_version": MoPropertyMeta("package_version", "packageVersion", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pld_version": MoPropertyMeta("pld_version", "pldVersion", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "cimcVersion": "cimc_version", 
        "dn": "dn", 
        "firmwareState": "firmware_state", 
        "operState": "oper_state", 
        "packageVersion": "package_version", 
        "pldVersion": "pld_version", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.cimc_version = None
        self.firmware_state = None
        self.oper_state = None
        self.package_version = None
        self.pld_version = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareStatus", parent_mo_or_dn, **kwargs)
