"""This module contains the general information for ComputeDataSanitize ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeDataSanitizeConsts:
    ADMIN_ACTION_FALSE = "false"
    ADMIN_ACTION_NO = "no"
    ADMIN_ACTION_TRUE = "true"
    ADMIN_ACTION_YES = "yes"
    SANITIZE_STATUS_COMPLETED = "completed"
    SANITIZE_STATUS_FAILED = "failed"
    SANITIZE_STATUS_IN_PROGRESS = "in-progress"
    SANITIZE_STATUS_NONE = "none"
    SANITIZE_STATUS_READY = "ready"
    SANITIZE_TARGET_ALL = "all"
    SANITIZE_TARGET_BOARD = "board"
    SANITIZE_TARGET_HOST = "host"
    SANITIZE_TARGET_NONE = "none"


class ComputeDataSanitize(ManagedObject):
    """This is ComputeDataSanitize class."""

    consts = ComputeDataSanitizeConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeDataSanitize", "computeDataSanitize", "data-sanitize", VersionMeta.Version434a, "InputOutput", 0x7f, [], ["admin"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], ['computeSanitizeComponent'], [None])

    prop_meta = {
        "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["false", "no", "true", "yes"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sanitize_status": MoPropertyMeta("sanitize_status", "sanitizeStatus", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["completed", "failed", "in-progress", "none", "ready"], []),
        "sanitize_target": MoPropertyMeta("sanitize_target", "sanitizeTarget", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["all", "board", "host", "none"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "adminAction": "admin_action", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sanitizeStatus": "sanitize_status", 
        "sanitizeTarget": "sanitize_target", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.child_action = None
        self.sacl = None
        self.sanitize_status = None
        self.sanitize_target = None
        self.status = None

        ManagedObject.__init__(self, "ComputeDataSanitize", parent_mo_or_dn, **kwargs)
