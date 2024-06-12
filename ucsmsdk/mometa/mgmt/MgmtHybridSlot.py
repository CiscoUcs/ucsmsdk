"""This module contains the general information for MgmtHybridSlot ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtHybridSlotConsts:
    CURRENT_MODE_CONTROLLER_ATTACHED = "controller-attached"
    CURRENT_MODE_CPU_DIRECT_ATTACHED = "cpu-direct-attached"
    CURRENT_MODE_UNKNOWN = "unknown"
    DRIVE_TYPE_SAS = "SAS"
    DRIVE_TYPE_SATA = "SATA"
    DRIVE_TYPE_U2_NVME = "U2-NVME"
    DRIVE_TYPE_U3_NVME = "U3-NVME"
    DRIVE_TYPE_BAY_EMPTY = "bay-empty"
    PREFERRED_MODE_CONTROLLER_ATTACHED = "controller-attached"
    PREFERRED_MODE_CPU_DIRECT_ATTACHED = "cpu-direct-attached"
    PREFERRED_MODE_UNKNOWN = "unknown"
    REQUESTED_MODE_CONTROLLER_ATTACHED = "controller-attached"
    REQUESTED_MODE_CPU_DIRECT_ATTACHED = "cpu-direct-attached"
    REQUESTED_MODE_UNKNOWN = "unknown"


class MgmtHybridSlot(ManagedObject):
    """This is MgmtHybridSlot class."""

    consts = MgmtHybridSlotConsts()
    naming_props = set(['hybridSlotId'])

    mo_meta = MoMeta("MgmtHybridSlot", "mgmtHybridSlot", "hybridslot-[hybrid_slot_id]", VersionMeta.Version434a, "InputOutput", 0x3f, [], ["read-only"], ['mgmtController'], ['faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "current_mode": MoPropertyMeta("current_mode", "currentMode", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["controller-attached", "cpu-direct-attached", "unknown"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "drive_type": MoPropertyMeta("drive_type", "driveType", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["SAS", "SATA", "U2-NVME", "U3-NVME", "bay-empty"], []),
        "hybrid_slot_id": MoPropertyMeta("hybrid_slot_id", "hybridSlotId", "uint", VersionMeta.Version434a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "preferred_mode": MoPropertyMeta("preferred_mode", "preferredMode", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["controller-attached", "cpu-direct-attached", "unknown"], []),
        "requested_mode": MoPropertyMeta("requested_mode", "requestedMode", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["controller-attached", "cpu-direct-attached", "unknown"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "currentMode": "current_mode", 
        "dn": "dn", 
        "driveType": "drive_type", 
        "hybridSlotId": "hybrid_slot_id", 
        "preferredMode": "preferred_mode", 
        "requestedMode": "requested_mode", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, hybrid_slot_id, **kwargs):
        self._dirty_mask = 0
        self.hybrid_slot_id = hybrid_slot_id
        self.child_action = None
        self.current_mode = None
        self.drive_type = None
        self.preferred_mode = None
        self.requested_mode = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtHybridSlot", parent_mo_or_dn, **kwargs)
