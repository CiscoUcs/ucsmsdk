"""This module contains the general information for FirmwareInstallImpact ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareInstallImpactConsts:
    SUBJECT_ADAPTOR = "adaptor"
    SUBJECT_BIOS = "bios"
    SUBJECT_BOARD_CONTROLLER = "board-controller"
    SUBJECT_CIMC = "cimc"
    SUBJECT_CMC = "cmc"
    SUBJECT_CPLD = "cpld"
    SUBJECT_GRAPHICS_CARD = "graphics-card"
    SUBJECT_IOCARD = "iocard"
    SUBJECT_ONBOARD_DEVICE = "onboard-device"
    SUBJECT_RETIMER = "retimer"
    SUBJECT_SAS_EXP_REG_FW = "sas-exp-reg-fw"
    SUBJECT_SAS_EXPANDER = "sas-expander"
    SUBJECT_SERVER = "server"
    SUBJECT_SERVICE_PROFILE = "service-profile"
    SUBJECT_STORAGE_CONTROLLER = "storage-controller"
    SUBJECT_SWITCH = "switch"
    SUBJECT_SYSTEM = "system"
    SUBJECT_UBM = "ubm"
    SUBJECT_UNKNOWN = "unknown"
    TYPE_ACTIVATE = "activate"
    TYPE_NOIMPACT = "noimpact"
    TYPE_RESET = "reset"
    TYPE_UPDATE = "update"


class FirmwareInstallImpact(ManagedObject):
    """This is FirmwareInstallImpact class."""

    consts = FirmwareInstallImpactConsts()
    naming_props = set(['keyDn'])

    mo_meta = MoMeta("FirmwareInstallImpact", "firmwareInstallImpact", "fw-sys-InstallImpact-[key_dn]", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["admin", "ls-config-policy", "ls-server-policy"], [], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "key_dn": MoPropertyMeta("key_dn", "keyDn", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "maint_policy_dn": MoPropertyMeta("maint_policy_dn", "maintPolicyDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "reboot_policy": MoPropertyMeta("reboot_policy", "rebootPolicy", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "subject": MoPropertyMeta("subject", "subject", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["adaptor", "bios", "board-controller", "cimc", "cmc", "cpld", "graphics-card", "iocard", "onboard-device", "retimer", "sas-exp-reg-fw", "sas-expander", "server", "service-profile", "storage-controller", "switch", "system", "ubm", "unknown"], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activate", "noimpact", "reset", "update"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "keyDn": "key_dn", 
        "maintPolicyDn": "maint_policy_dn", 
        "rebootPolicy": "reboot_policy", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "subject": "subject", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, key_dn, **kwargs):
        self._dirty_mask = 0
        self.key_dn = key_dn
        self.child_action = None
        self.descr = None
        self.maint_policy_dn = None
        self.reboot_policy = None
        self.sacl = None
        self.status = None
        self.subject = None
        self.type = None

        ManagedObject.__init__(self, "FirmwareInstallImpact", parent_mo_or_dn, **kwargs)
