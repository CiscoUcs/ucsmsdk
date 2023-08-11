"""This module contains the general information for ComputeRebootLog ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeRebootLogConsts:
    PWR_CHANGE_SRC_HOST_PWR_TRANSITION = "HOST_PWR_TRANSITION"
    PWR_CHANGE_SRC_NONE = "NONE"
    PWR_CHANGE_SRC_SOFTWARE = "SOFTWARE"
    PWR_CHANGE_SRC_UCS_ACTIVATE_ADAPTOR_FW = "UCS_ACTIVATE_ADAPTOR_FW"
    PWR_CHANGE_SRC_UCS_ACTIVATE_BIOS_FW = "UCS_ACTIVATE_BIOS_FW"
    PWR_CHANGE_SRC_UCS_ASSOCIATE = "UCS_ASSOCIATE"
    PWR_CHANGE_SRC_UCS_BIOS_PASSWORD_RESET = "UCS_BIOS_PASSWORD_RESET"
    PWR_CHANGE_SRC_UCS_BIOS_RECOVERY = "UCS_BIOS_RECOVERY"
    PWR_CHANGE_SRC_UCS_BLADE_SHUTDOWN = "UCS_BLADE_SHUTDOWN"
    PWR_CHANGE_SRC_UCS_CLEAR_TPM = "UCS_CLEAR_TPM"
    PWR_CHANGE_SRC_UCS_CMOS_RESET = "UCS_CMOS_RESET"
    PWR_CHANGE_SRC_UCS_DIAG = "UCS_DIAG"
    PWR_CHANGE_SRC_UCS_DIAGNOSTIC_INTERRUPT = "UCS_DIAGNOSTIC_INTERRUPT"
    PWR_CHANGE_SRC_UCS_DISASSOCIATE = "UCS_DISASSOCIATE"
    PWR_CHANGE_SRC_UCS_DISK_ZONING_INVENTORY = "UCS_DISK_ZONING_INVENTORY"
    PWR_CHANGE_SRC_UCS_FW_UPGRADE = "UCS_FW_UPGRADE"
    PWR_CHANGE_SRC_UCS_HARDRESET = "UCS_HARDRESET"
    PWR_CHANGE_SRC_UCS_HARD_SHUTDOWN = "UCS_HARD_SHUTDOWN"
    PWR_CHANGE_SRC_UCS_OOB_ADMIN_CONFIG = "UCS_OOB_ADMIN_CONFIG"
    PWR_CHANGE_SRC_UCS_POWERCYCLE = "UCS_POWERCYCLE"
    PWR_CHANGE_SRC_UCS_RACKUNIT_DISCOVER = "UCS_RACKUNIT_DISCOVER"
    PWR_CHANGE_SRC_UCS_RACK_UNIT_ADAPTER_RESET = "UCS_RACK_UNIT_ADAPTER_RESET"
    PWR_CHANGE_SRC_UCS_SERVERUNIT_DISCOVER = "UCS_SERVERUNIT_DISCOVER"
    PWR_CHANGE_SRC_UCS_SERVER_DISCOVER = "UCS_SERVER_DISCOVER"
    PWR_CHANGE_SRC_UCS_SOFTRESET = "UCS_SOFTRESET"
    PWR_CHANGE_SRC_UCS_SOFT_SHUTDOWN = "UCS_SOFT_SHUTDOWN"
    PWR_CHANGE_SRC_UCS_TURNUP = "UCS_TURNUP"
    PWR_CHANGE_SRC_UCS_UPDATE_ADAPTOR_FW = "UCS_UPDATE_ADAPTOR_FW"
    PWR_CHANGE_SRC_UCS_UPDATE_BOARDCTRL_FW = "UCS_UPDATE_BOARDCTRL_FW"
    PWR_CHANGE_SRC_UNKNOWN = "UNKNOWN"
    PWR_CHANGE_SRC_USER_FRONT_PANEL = "USER_FRONT_PANEL"
    TIME_STAMP_ = ""


class ComputeRebootLog(ManagedObject):
    """This is ComputeRebootLog class."""

    consts = ComputeRebootLogConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ComputeRebootLog", "computeRebootLog", "reboot-log-[id]", VersionMeta.Version321d, "InputOutput", 0x3f, [], ["read-only"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "count": MoPropertyMeta("count", "count", "uint", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "pwr_change_src": MoPropertyMeta("pwr_change_src", "pwrChangeSrc", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["HOST_PWR_TRANSITION", "NONE", "SOFTWARE", "UCS_ACTIVATE_ADAPTOR_FW", "UCS_ACTIVATE_BIOS_FW", "UCS_ASSOCIATE", "UCS_BIOS_PASSWORD_RESET", "UCS_BIOS_RECOVERY", "UCS_BLADE_SHUTDOWN", "UCS_CLEAR_TPM", "UCS_CMOS_RESET", "UCS_DIAG", "UCS_DIAGNOSTIC_INTERRUPT", "UCS_DISASSOCIATE", "UCS_DISK_ZONING_INVENTORY", "UCS_FW_UPGRADE", "UCS_HARDRESET", "UCS_HARD_SHUTDOWN", "UCS_OOB_ADMIN_CONFIG", "UCS_POWERCYCLE", "UCS_RACKUNIT_DISCOVER", "UCS_RACK_UNIT_ADAPTER_RESET", "UCS_SERVERUNIT_DISCOVER", "UCS_SERVER_DISCOVER", "UCS_SOFTRESET", "UCS_SOFT_SHUTDOWN", "UCS_TURNUP", "UCS_UPDATE_ADAPTOR_FW", "UCS_UPDATE_BOARDCTRL_FW", "UNKNOWN", "USER_FRONT_PANEL"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "time_stamp": MoPropertyMeta("time_stamp", "timeStamp", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "count": "count", 
        "dn": "dn", 
        "id": "id", 
        "pwrChangeSrc": "pwr_change_src", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "timeStamp": "time_stamp", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.count = None
        self.pwr_change_src = None
        self.sacl = None
        self.status = None
        self.time_stamp = None

        ManagedObject.__init__(self, "ComputeRebootLog", parent_mo_or_dn, **kwargs)
