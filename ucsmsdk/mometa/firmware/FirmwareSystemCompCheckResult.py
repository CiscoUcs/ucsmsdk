"""This module contains the general information for FirmwareSystemCompCheckResult ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareSystemCompCheckResultConsts:
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


class FirmwareSystemCompCheckResult(ManagedObject):
    """This is FirmwareSystemCompCheckResult class."""

    consts = FirmwareSystemCompCheckResultConsts()
    naming_props = set(['keyDn'])

    mo_meta = MoMeta("FirmwareSystemCompCheckResult", "firmwareSystemCompCheckResult", "fw-sys-CompCheckRes-[key_dn]", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["admin"], ['firmwareSystem'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "key_descr": MoPropertyMeta("key_descr", "keyDescr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "key_dn": MoPropertyMeta("key_dn", "keyDn", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "non_comp_descr": MoPropertyMeta("non_comp_descr", "nonCompDescr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "non_comp_dns": MoPropertyMeta("non_comp_dns", "nonCompDns", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "subject": MoPropertyMeta("subject", "subject", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["adaptor", "bios", "board-controller", "cimc", "cmc", "cpld", "graphics-card", "iocard", "onboard-device", "retimer", "sas-exp-reg-fw", "sas-expander", "server", "service-profile", "storage-controller", "switch", "system", "ubm", "unknown"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "keyDescr": "key_descr", 
        "keyDn": "key_dn", 
        "nonCompDescr": "non_comp_descr", 
        "nonCompDns": "non_comp_dns", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "subject": "subject", 
    }

    def __init__(self, parent_mo_or_dn, key_dn, **kwargs):
        self._dirty_mask = 0
        self.key_dn = key_dn
        self.child_action = None
        self.key_descr = None
        self.non_comp_descr = None
        self.non_comp_dns = None
        self.sacl = None
        self.status = None
        self.subject = None

        ManagedObject.__init__(self, "FirmwareSystemCompCheckResult", parent_mo_or_dn, **kwargs)
