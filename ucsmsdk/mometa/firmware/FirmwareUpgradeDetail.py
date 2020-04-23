"""This module contains the general information for FirmwareUpgradeDetail ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareUpgradeDetailConsts:
    CATEGORY_CATALOG = "catalog"
    CATEGORY_CONFIG = "config"
    CATEGORY_DATA_LOAD = "data-load"
    CATEGORY_FAULTS = "faults"
    CATEGORY_OTHER = "other"
    CATEGORY_SERVER_REBOOT = "server-reboot"
    SEVERITY_ERROR = "error"
    SEVERITY_FATAL = "fatal"
    SEVERITY_INFO = "info"
    SEVERITY_UNKNOWN = "unknown"
    SEVERITY_WARN = "warn"


class FirmwareUpgradeDetail(ManagedObject):
    """This is FirmwareUpgradeDetail class."""

    consts = FirmwareUpgradeDetailConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("FirmwareUpgradeDetail", "firmwareUpgradeDetail", "id-[id]", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["admin"], ['firmwareUpgradeInfo'], [], ["Get"])

    prop_meta = {
        "category": MoPropertyMeta("category", "category", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["catalog", "config", "data-load", "faults", "other", "server-reboot"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "severity": MoPropertyMeta("severity", "severity", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["error", "fatal", "info", "unknown", "warn"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "category": "category", 
        "childAction": "child_action", 
        "description": "description", 
        "dn": "dn", 
        "id": "id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "severity": "severity", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.category = None
        self.child_action = None
        self.description = None
        self.sacl = None
        self.severity = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareUpgradeDetail", parent_mo_or_dn, **kwargs)
