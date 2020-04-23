"""This module contains the general information for PolicyPolicyScopeFsmTask ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PolicyPolicyScopeFsmTaskConsts:
    COMPLETION_CANCELLED = "cancelled"
    COMPLETION_COMPLETED = "completed"
    COMPLETION_PROCESSING = "processing"
    COMPLETION_SCHEDULED = "scheduled"
    ITEM_RELEASE_ALL_OPERATION_FSM = "ReleaseAllOperationFsm"
    ITEM_RELEASE_ALL_POLICY_FSM = "ReleaseAllPolicyFsm"
    ITEM_RELEASE_ALL_STORAGE_FSM = "ReleaseAllStorageFsm"
    ITEM_RELEASE_MANY_OPERATION_FSM = "ReleaseManyOperationFsm"
    ITEM_RELEASE_MANY_POLICY_FSM = "ReleaseManyPolicyFsm"
    ITEM_RELEASE_MANY_STORAGE_FSM = "ReleaseManyStorageFsm"
    ITEM_RELEASE_OPERATION_FSM = "ReleaseOperationFsm"
    ITEM_RELEASE_POLICY_FSM = "ReleasePolicyFsm"
    ITEM_RELEASE_STORAGE_FSM = "ReleaseStorageFsm"
    ITEM_RESOLVE_ALL_OPERATION_FSM = "ResolveAllOperationFsm"
    ITEM_RESOLVE_ALL_POLICY_FSM = "ResolveAllPolicyFsm"
    ITEM_RESOLVE_ALL_STORAGE_FSM = "ResolveAllStorageFsm"
    ITEM_RESOLVE_MANY_OPERATION_FSM = "ResolveManyOperationFsm"
    ITEM_RESOLVE_MANY_POLICY_FSM = "ResolveManyPolicyFsm"
    ITEM_RESOLVE_MANY_STORAGE_FSM = "ResolveManyStorageFsm"
    ITEM_NOP = "nop"


class PolicyPolicyScopeFsmTask(ManagedObject):
    """This is PolicyPolicyScopeFsmTask class."""

    consts = PolicyPolicyScopeFsmTaskConsts()
    naming_props = set(['item'])

    mo_meta = MoMeta("PolicyPolicyScopeFsmTask", "policyPolicyScopeFsmTask", "task-[item]", VersionMeta.Version211a, "OutputOnly", 0xf, [], [""], ['policyPolicyScope'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "completion": MoPropertyMeta("completion", "completion", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cancelled", "completed", "processing", "scheduled"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "flags": MoPropertyMeta("flags", "flags", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""(defaultValue){0,1}""", [], []),
        "item": MoPropertyMeta("item", "item", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, None, None, None, None, ["ReleaseAllOperationFsm", "ReleaseAllPolicyFsm", "ReleaseAllStorageFsm", "ReleaseManyOperationFsm", "ReleaseManyPolicyFsm", "ReleaseManyStorageFsm", "ReleaseOperationFsm", "ReleasePolicyFsm", "ReleaseStorageFsm", "ResolveAllOperationFsm", "ResolveAllPolicyFsm", "ResolveAllStorageFsm", "ResolveManyOperationFsm", "ResolveManyPolicyFsm", "ResolveManyStorageFsm", "nop"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "seq_id": MoPropertyMeta("seq_id", "seqId", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "completion": "completion", 
        "dn": "dn", 
        "flags": "flags", 
        "item": "item", 
        "rn": "rn", 
        "sacl": "sacl", 
        "seqId": "seq_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, item, **kwargs):
        self._dirty_mask = 0
        self.item = item
        self.child_action = None
        self.completion = None
        self.flags = None
        self.sacl = None
        self.seq_id = None
        self.status = None

        ManagedObject.__init__(self, "PolicyPolicyScopeFsmTask", parent_mo_or_dn, **kwargs)
