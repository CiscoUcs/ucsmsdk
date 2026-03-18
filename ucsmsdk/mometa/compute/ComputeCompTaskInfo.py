"""This module contains the general information for ComputeCompTaskInfo ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeCompTaskInfoConsts:
    OPERATION_CREATE = "Create"
    OPERATION_DELETE = "Delete"
    OPERATION_UPDATE = "Update"
    TASK_STATE_CANCELLED = "Cancelled"
    TASK_STATE_CANCELLING = "Cancelling"
    TASK_STATE_COMPLETED = "Completed"
    TASK_STATE_EXCEPTION = "Exception"
    TASK_STATE_INTERRUPTED = "Interrupted"
    TASK_STATE_KILLED = "Killed"
    TASK_STATE_NEW = "New"
    TASK_STATE_PENDING = "Pending"
    TASK_STATE_RUNNING = "Running"
    TASK_STATE_SERVICE = "Service"
    TASK_STATE_STARTING = "Starting"
    TASK_STATE_STOPPING = "Stopping"
    TASK_STATE_SUSPENDED = "Suspended"
    TASK_STATUS_CRITICAL = "Critical"
    TASK_STATUS_OK = "OK"
    TASK_STATUS_WARNING = "Warning"
    TYPE_VIRTUAL_DRIVE = "VirtualDrive"


class ComputeCompTaskInfo(ManagedObject):
    """This is ComputeCompTaskInfo class."""

    consts = ComputeCompTaskInfoConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ComputeCompTaskInfo", "computeCompTaskInfo", "task-[id]", VersionMeta.Version602a, "InputOutput", 0x3f, [], ["admin"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version602a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "comp_dn": MoPropertyMeta("comp_dn", "compDn", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "err_msg": MoPropertyMeta("err_msg", "errMsg", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version602a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "operation": MoPropertyMeta("operation", "operation", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Create", "Delete", "Update"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "task_state": MoPropertyMeta("task_state", "taskState", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Cancelled", "Cancelling", "Completed", "Exception", "Interrupted", "Killed", "New", "Pending", "Running", "Service", "Starting", "Stopping", "Suspended"], []),
        "task_status": MoPropertyMeta("task_status", "taskStatus", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Critical", "OK", "Warning"], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["VirtualDrive"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "compDn": "comp_dn", 
        "dn": "dn", 
        "errMsg": "err_msg", 
        "id": "id", 
        "operation": "operation", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "taskState": "task_state", 
        "taskStatus": "task_status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.comp_dn = None
        self.err_msg = None
        self.operation = None
        self.sacl = None
        self.status = None
        self.task_state = None
        self.task_status = None
        self.type = None

        ManagedObject.__init__(self, "ComputeCompTaskInfo", parent_mo_or_dn, **kwargs)
