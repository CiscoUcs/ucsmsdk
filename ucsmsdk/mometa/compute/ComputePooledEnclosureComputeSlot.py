"""This module contains the general information for ComputePooledEnclosureComputeSlot ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePooledEnclosureComputeSlotConsts:
    ASSIGNED_FALSE = "false"
    ASSIGNED_NO = "no"
    ASSIGNED_TRUE = "true"
    ASSIGNED_YES = "yes"
    CHASSIS_ID_N_A = "N/A"
    OWNER_MANAGEMENT = "management"
    OWNER_POLICY = "policy"


class ComputePooledEnclosureComputeSlot(ManagedObject):
    """This is ComputePooledEnclosureComputeSlot class."""

    consts = ComputePooledEnclosureComputeSlotConsts()
    naming_props = set(['chassisId', 'slotId', 'serverInstanceId'])

    mo_meta = MoMeta("ComputePooledEnclosureComputeSlot", "computePooledEnclosureComputeSlot", "server-[chassis_id]-[slot_id]-[server_instance_id]", VersionMeta.Version251a, "InputOutput", 0xff, [], ["admin", "pn-policy"], ['computePool'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x2, None, None, None, ["N/A"], ["1-255"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["management", "policy"], []),
        "poolable_dn": MoPropertyMeta("poolable_dn", "poolableDn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "prev_assigned_to_dn": MoPropertyMeta("prev_assigned_to_dn", "prevAssignedToDn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "server_instance_id": MoPropertyMeta("server_instance_id", "serverInstanceId", "uint", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], ["1-8"]),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x40, None, None, None, [], ["1-8"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "assigned": "assigned", 
        "assignedToDn": "assigned_to_dn", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "owner": "owner", 
        "poolableDn": "poolable_dn", 
        "prevAssignedToDn": "prev_assigned_to_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serverInstanceId": "server_instance_id", 
        "slotId": "slot_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, chassis_id, slot_id, server_instance_id, **kwargs):
        self._dirty_mask = 0
        self.chassis_id = chassis_id
        self.slot_id = slot_id
        self.server_instance_id = server_instance_id
        self.assigned = None
        self.assigned_to_dn = None
        self.child_action = None
        self.owner = None
        self.poolable_dn = None
        self.prev_assigned_to_dn = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputePooledEnclosureComputeSlot", parent_mo_or_dn, **kwargs)
