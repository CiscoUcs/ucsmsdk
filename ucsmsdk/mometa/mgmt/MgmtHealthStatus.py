"""This module contains the general information for MgmtHealthStatus ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtHealthStatusConsts:
    HEALTH_SEVERITY_CLEARED = "cleared"
    HEALTH_SEVERITY_CONDITION = "condition"
    HEALTH_SEVERITY_CRITICAL = "critical"
    HEALTH_SEVERITY_INFO = "info"
    HEALTH_SEVERITY_MAJOR = "major"
    HEALTH_SEVERITY_MINOR = "minor"
    HEALTH_SEVERITY_WARNING = "warning"


class MgmtHealthStatus(ManagedObject):
    """This is MgmtHealthStatus class."""

    consts = MgmtHealthStatusConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtHealthStatus", "mgmtHealthStatus", "health", VersionMeta.Version311e, "InputOutput", 0x1f, [], ["read-only"], ['mgmtController', 'networkElement'], ['faultInst', 'mgmtHealthAttr'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version311e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "health_qualifier": MoPropertyMeta("health_qualifier", "healthQualifier", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "health_severity": MoPropertyMeta("health_severity", "healthSeverity", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "healthQualifier": "health_qualifier", 
        "healthSeverity": "health_severity", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.health_qualifier = None
        self.health_severity = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtHealthStatus", parent_mo_or_dn, **kwargs)
