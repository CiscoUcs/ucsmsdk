"""This module contains the general information for SysdebugLogExportStatus ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SysdebugLogExportStatusConsts:
    EXPORT_STATUS_FAILURE = "failure"
    EXPORT_STATUS_SUCCESS = "success"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class SysdebugLogExportStatus(ManagedObject):
    """This is SysdebugLogExportStatus class."""

    consts = SysdebugLogExportStatusConsts()
    naming_props = set(['switchId'])

    mo_meta = MoMeta("SysdebugLogExportStatus", "sysdebugLogExportStatus", "log-export-status-[switch_id]", VersionMeta.Version222c, "InputOutput", 0x3f, [], ["read-only"], ['sysdebugLogExportPolicy'], ['faultInst'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "export_failure_reason": MoPropertyMeta("export_failure_reason", "exportFailureReason", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "export_status": MoPropertyMeta("export_status", "exportStatus", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failure", "success"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version222c, MoPropertyMeta.NAMING, 0x20, None, None, None, ["A", "B", "NONE"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "exportFailureReason": "export_failure_reason", 
        "exportStatus": "export_status", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
    }

    def __init__(self, parent_mo_or_dn, switch_id, **kwargs):
        self._dirty_mask = 0
        self.switch_id = switch_id
        self.child_action = None
        self.export_failure_reason = None
        self.export_status = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "SysdebugLogExportStatus", parent_mo_or_dn, **kwargs)
