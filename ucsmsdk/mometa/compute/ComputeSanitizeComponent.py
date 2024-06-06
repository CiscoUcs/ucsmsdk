"""This module contains the general information for ComputeSanitizeComponent ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeSanitizeComponentConsts:
    SANITIZE_STATUS_COMPLETED = "completed"
    SANITIZE_STATUS_FAILED = "failed"
    SANITIZE_STATUS_IN_PROGRESS = "in-progress"
    SANITIZE_STATUS_NONE = "none"
    SANITIZE_STATUS_READY = "ready"
    TYPE_BOARD = "board"
    TYPE_HOST = "host"
    TYPE_NETWORK_ADAPTER = "networkAdapter"
    TYPE_STORAGE = "storage"


class ComputeSanitizeComponent(ManagedObject):
    """This is ComputeSanitizeComponent class."""

    consts = ComputeSanitizeComponentConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("ComputeSanitizeComponent", "computeSanitizeComponent", "comp-[type]", VersionMeta.Version434a, "InputOutput", 0x3f, [], ["admin"], ['computeDataSanitize'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "completion": MoPropertyMeta("completion", "completion", "uint", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "end_time": MoPropertyMeta("end_time", "endTime", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "failed_comps": MoPropertyMeta("failed_comps", "failedComps", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sanitize_status": MoPropertyMeta("sanitize_status", "sanitizeStatus", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["completed", "failed", "in-progress", "none", "ready"], []),
        "sanitized_comps": MoPropertyMeta("sanitized_comps", "sanitizedComps", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "start_time": MoPropertyMeta("start_time", "startTime", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version434a, MoPropertyMeta.NAMING, 0x20, None, None, None, ["board", "host", "networkAdapter", "storage"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "completion": "completion", 
        "dn": "dn", 
        "endTime": "end_time", 
        "failedComps": "failed_comps", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sanitizeStatus": "sanitize_status", 
        "sanitizedComps": "sanitized_comps", 
        "startTime": "start_time", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.completion = None
        self.end_time = None
        self.failed_comps = None
        self.sacl = None
        self.sanitize_status = None
        self.sanitized_comps = None
        self.start_time = None
        self.status = None

        ManagedObject.__init__(self, "ComputeSanitizeComponent", parent_mo_or_dn, **kwargs)
