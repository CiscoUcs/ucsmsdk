"""This module contains the general information for EquipmentPOSTCode ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentPOSTCodeConsts:
    GLOBAL_ID_NO_ERRORS = "No Errors"
    LOCAL_ID_NO_ERRORS = "No Errors"
    RECOVERABLE_NON_RECOVERABLE = "non-recoverable"
    RECOVERABLE_RECOVERABLE = "recoverable"
    RECOVERABLE_UNKNOWN = "unknown"
    SEVERITY_CLEARED = "cleared"
    SEVERITY_CONDITION = "condition"
    SEVERITY_CRITICAL = "critical"
    SEVERITY_INFO = "info"
    SEVERITY_MAJOR = "major"
    SEVERITY_MINOR = "minor"
    SEVERITY_WARNING = "warning"


class EquipmentPOSTCode(ManagedObject):
    """This is EquipmentPOSTCode class."""

    consts = EquipmentPOSTCodeConsts()
    naming_props = set(['localId'])

    mo_meta = MoMeta("EquipmentPOSTCode", "equipmentPOSTCode", "code-[local_id]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["read-only"], ['equipmentPOSTCodeReporter', 'equipmentPOSTCodeTemplate'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "code": MoPropertyMeta("code", "code", "string", VersionMeta.Version101e, MoPropertyMeta.CREATE_ONLY, 0x4, 0, 510, None, [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,384}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "global_id": MoPropertyMeta("global_id", "globalId", "string", VersionMeta.Version101e, MoPropertyMeta.CREATE_ONLY, 0x10, None, None, None, ["No Errors"], ["0-4294967295"]),
        "local_id": MoPropertyMeta("local_id", "localId", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, None, None, None, ["No Errors"], ["0-4294967295"]),
        "method": MoPropertyMeta("method", "method", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""((POST|defaultValue|config-check|diag-check|sel-check),){0,4}(POST|defaultValue|config-check|diag-check|sel-check){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "recoverable": MoPropertyMeta("recoverable", "recoverable", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["non-recoverable", "recoverable", "unknown"], []),
        "recovery_action": MoPropertyMeta("recovery_action", "recoveryAction", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,384}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "severity": MoPropertyMeta("severity", "severity", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "code": "code", 
        "descr": "descr", 
        "dn": "dn", 
        "globalId": "global_id", 
        "localId": "local_id", 
        "method": "method", 
        "name": "name", 
        "recoverable": "recoverable", 
        "recoveryAction": "recovery_action", 
        "rn": "rn", 
        "sacl": "sacl", 
        "severity": "severity", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, local_id, **kwargs):
        self._dirty_mask = 0
        self.local_id = local_id
        self.child_action = None
        self.code = None
        self.descr = None
        self.global_id = None
        self.method = None
        self.name = None
        self.recoverable = None
        self.recovery_action = None
        self.sacl = None
        self.severity = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPOSTCode", parent_mo_or_dn, **kwargs)
