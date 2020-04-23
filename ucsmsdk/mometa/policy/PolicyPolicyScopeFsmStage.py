"""This module contains the general information for PolicyPolicyScopeFsmStage ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PolicyPolicyScopeFsmStageConsts:
    LAST_UPDATE_TIME_ = ""
    NAME_RELEASE_ALL_OPERATION_FSM_BEGIN = "ReleaseAllOperationFsmBegin"
    NAME_RELEASE_ALL_OPERATION_FSM_FAIL = "ReleaseAllOperationFsmFail"
    NAME_RELEASE_ALL_OPERATION_FSM_RELEASE_ALL = "ReleaseAllOperationFsmReleaseAll"
    NAME_RELEASE_ALL_OPERATION_FSM_SUCCESS = "ReleaseAllOperationFsmSuccess"
    NAME_RELEASE_ALL_POLICY_FSM_BEGIN = "ReleaseAllPolicyFsmBegin"
    NAME_RELEASE_ALL_POLICY_FSM_FAIL = "ReleaseAllPolicyFsmFail"
    NAME_RELEASE_ALL_POLICY_FSM_RELEASE_ALL = "ReleaseAllPolicyFsmReleaseAll"
    NAME_RELEASE_ALL_POLICY_FSM_SUCCESS = "ReleaseAllPolicyFsmSuccess"
    NAME_RELEASE_ALL_STORAGE_FSM_BEGIN = "ReleaseAllStorageFsmBegin"
    NAME_RELEASE_ALL_STORAGE_FSM_FAIL = "ReleaseAllStorageFsmFail"
    NAME_RELEASE_ALL_STORAGE_FSM_RELEASE_ALL = "ReleaseAllStorageFsmReleaseAll"
    NAME_RELEASE_ALL_STORAGE_FSM_SUCCESS = "ReleaseAllStorageFsmSuccess"
    NAME_RELEASE_MANY_OPERATION_FSM_BEGIN = "ReleaseManyOperationFsmBegin"
    NAME_RELEASE_MANY_OPERATION_FSM_FAIL = "ReleaseManyOperationFsmFail"
    NAME_RELEASE_MANY_OPERATION_FSM_RELEASE_MANY = "ReleaseManyOperationFsmReleaseMany"
    NAME_RELEASE_MANY_OPERATION_FSM_SUCCESS = "ReleaseManyOperationFsmSuccess"
    NAME_RELEASE_MANY_POLICY_FSM_BEGIN = "ReleaseManyPolicyFsmBegin"
    NAME_RELEASE_MANY_POLICY_FSM_FAIL = "ReleaseManyPolicyFsmFail"
    NAME_RELEASE_MANY_POLICY_FSM_RELEASE_MANY = "ReleaseManyPolicyFsmReleaseMany"
    NAME_RELEASE_MANY_POLICY_FSM_SUCCESS = "ReleaseManyPolicyFsmSuccess"
    NAME_RELEASE_MANY_STORAGE_FSM_BEGIN = "ReleaseManyStorageFsmBegin"
    NAME_RELEASE_MANY_STORAGE_FSM_FAIL = "ReleaseManyStorageFsmFail"
    NAME_RELEASE_MANY_STORAGE_FSM_RELEASE_MANY = "ReleaseManyStorageFsmReleaseMany"
    NAME_RELEASE_MANY_STORAGE_FSM_SUCCESS = "ReleaseManyStorageFsmSuccess"
    NAME_RELEASE_OPERATION_FSM_BEGIN = "ReleaseOperationFsmBegin"
    NAME_RELEASE_OPERATION_FSM_FAIL = "ReleaseOperationFsmFail"
    NAME_RELEASE_OPERATION_FSM_RELEASE = "ReleaseOperationFsmRelease"
    NAME_RELEASE_OPERATION_FSM_SUCCESS = "ReleaseOperationFsmSuccess"
    NAME_RELEASE_POLICY_FSM_BEGIN = "ReleasePolicyFsmBegin"
    NAME_RELEASE_POLICY_FSM_FAIL = "ReleasePolicyFsmFail"
    NAME_RELEASE_POLICY_FSM_RELEASE = "ReleasePolicyFsmRelease"
    NAME_RELEASE_POLICY_FSM_SUCCESS = "ReleasePolicyFsmSuccess"
    NAME_RELEASE_STORAGE_FSM_BEGIN = "ReleaseStorageFsmBegin"
    NAME_RELEASE_STORAGE_FSM_FAIL = "ReleaseStorageFsmFail"
    NAME_RELEASE_STORAGE_FSM_RELEASE = "ReleaseStorageFsmRelease"
    NAME_RELEASE_STORAGE_FSM_SUCCESS = "ReleaseStorageFsmSuccess"
    NAME_RESOLVE_ALL_OPERATION_FSM_BEGIN = "ResolveAllOperationFsmBegin"
    NAME_RESOLVE_ALL_OPERATION_FSM_FAIL = "ResolveAllOperationFsmFail"
    NAME_RESOLVE_ALL_OPERATION_FSM_RESOLVE_ALL = "ResolveAllOperationFsmResolveAll"
    NAME_RESOLVE_ALL_OPERATION_FSM_SUCCESS = "ResolveAllOperationFsmSuccess"
    NAME_RESOLVE_ALL_POLICY_FSM_BEGIN = "ResolveAllPolicyFsmBegin"
    NAME_RESOLVE_ALL_POLICY_FSM_FAIL = "ResolveAllPolicyFsmFail"
    NAME_RESOLVE_ALL_POLICY_FSM_RESOLVE_ALL = "ResolveAllPolicyFsmResolveAll"
    NAME_RESOLVE_ALL_POLICY_FSM_SUCCESS = "ResolveAllPolicyFsmSuccess"
    NAME_RESOLVE_ALL_STORAGE_FSM_BEGIN = "ResolveAllStorageFsmBegin"
    NAME_RESOLVE_ALL_STORAGE_FSM_FAIL = "ResolveAllStorageFsmFail"
    NAME_RESOLVE_ALL_STORAGE_FSM_RESOLVE_ALL = "ResolveAllStorageFsmResolveAll"
    NAME_RESOLVE_ALL_STORAGE_FSM_SUCCESS = "ResolveAllStorageFsmSuccess"
    NAME_RESOLVE_MANY_OPERATION_FSM_BEGIN = "ResolveManyOperationFsmBegin"
    NAME_RESOLVE_MANY_OPERATION_FSM_FAIL = "ResolveManyOperationFsmFail"
    NAME_RESOLVE_MANY_OPERATION_FSM_RESOLVE_MANY = "ResolveManyOperationFsmResolveMany"
    NAME_RESOLVE_MANY_OPERATION_FSM_SUCCESS = "ResolveManyOperationFsmSuccess"
    NAME_RESOLVE_MANY_POLICY_FSM_BEGIN = "ResolveManyPolicyFsmBegin"
    NAME_RESOLVE_MANY_POLICY_FSM_FAIL = "ResolveManyPolicyFsmFail"
    NAME_RESOLVE_MANY_POLICY_FSM_RESOLVE_MANY = "ResolveManyPolicyFsmResolveMany"
    NAME_RESOLVE_MANY_POLICY_FSM_SUCCESS = "ResolveManyPolicyFsmSuccess"
    NAME_RESOLVE_MANY_STORAGE_FSM_BEGIN = "ResolveManyStorageFsmBegin"
    NAME_RESOLVE_MANY_STORAGE_FSM_FAIL = "ResolveManyStorageFsmFail"
    NAME_RESOLVE_MANY_STORAGE_FSM_RESOLVE_MANY = "ResolveManyStorageFsmResolveMany"
    NAME_RESOLVE_MANY_STORAGE_FSM_SUCCESS = "ResolveManyStorageFsmSuccess"
    NAME_NOP = "nop"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class PolicyPolicyScopeFsmStage(ManagedObject):
    """This is PolicyPolicyScopeFsmStage class."""

    consts = PolicyPolicyScopeFsmStageConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("PolicyPolicyScopeFsmStage", "policyPolicyScopeFsmStage", "stage-[name]", VersionMeta.Version211a, "OutputOnly", 0xf, [], [""], ['policyPolicyScopeFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, None, None, None, None, ["ReleaseAllOperationFsmBegin", "ReleaseAllOperationFsmFail", "ReleaseAllOperationFsmReleaseAll", "ReleaseAllOperationFsmSuccess", "ReleaseAllPolicyFsmBegin", "ReleaseAllPolicyFsmFail", "ReleaseAllPolicyFsmReleaseAll", "ReleaseAllPolicyFsmSuccess", "ReleaseAllStorageFsmBegin", "ReleaseAllStorageFsmFail", "ReleaseAllStorageFsmReleaseAll", "ReleaseAllStorageFsmSuccess", "ReleaseManyOperationFsmBegin", "ReleaseManyOperationFsmFail", "ReleaseManyOperationFsmReleaseMany", "ReleaseManyOperationFsmSuccess", "ReleaseManyPolicyFsmBegin", "ReleaseManyPolicyFsmFail", "ReleaseManyPolicyFsmReleaseMany", "ReleaseManyPolicyFsmSuccess", "ReleaseManyStorageFsmBegin", "ReleaseManyStorageFsmFail", "ReleaseManyStorageFsmReleaseMany", "ReleaseManyStorageFsmSuccess", "ReleaseOperationFsmBegin", "ReleaseOperationFsmFail", "ReleaseOperationFsmRelease", "ReleaseOperationFsmSuccess", "ReleasePolicyFsmBegin", "ReleasePolicyFsmFail", "ReleasePolicyFsmRelease", "ReleasePolicyFsmSuccess", "ReleaseStorageFsmBegin", "ReleaseStorageFsmFail", "ReleaseStorageFsmRelease", "ReleaseStorageFsmSuccess", "ResolveAllOperationFsmBegin", "ResolveAllOperationFsmFail", "ResolveAllOperationFsmResolveAll", "ResolveAllOperationFsmSuccess", "ResolveAllPolicyFsmBegin", "ResolveAllPolicyFsmFail", "ResolveAllPolicyFsmResolveAll", "ResolveAllPolicyFsmSuccess", "ResolveAllStorageFsmBegin", "ResolveAllStorageFsmFail", "ResolveAllStorageFsmResolveAll", "ResolveAllStorageFsmSuccess", "ResolveManyOperationFsmBegin", "ResolveManyOperationFsmFail", "ResolveManyOperationFsmResolveMany", "ResolveManyOperationFsmSuccess", "ResolveManyPolicyFsmBegin", "ResolveManyPolicyFsmFail", "ResolveManyPolicyFsmResolveMany", "ResolveManyPolicyFsmSuccess", "ResolveManyStorageFsmBegin", "ResolveManyStorageFsmFail", "ResolveManyStorageFsmResolveMany", "ResolveManyStorageFsmSuccess", "nop"], []),
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "retry": MoPropertyMeta("retry", "retry", "byte", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "stage_status": MoPropertyMeta("stage_status", "stageStatus", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "lastUpdateTime": "last_update_time", 
        "name": "name", 
        "order": "order", 
        "retry": "retry", 
        "rn": "rn", 
        "sacl": "sacl", 
        "stageStatus": "stage_status", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.last_update_time = None
        self.order = None
        self.retry = None
        self.sacl = None
        self.stage_status = None
        self.status = None

        ManagedObject.__init__(self, "PolicyPolicyScopeFsmStage", parent_mo_or_dn, **kwargs)
