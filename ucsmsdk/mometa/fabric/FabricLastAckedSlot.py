"""This module contains the general information for FabricLastAckedSlot ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricLastAckedSlotConsts:
    BOARD_AGGREGATION_ROLE_MULTI_MASTER = "multi-master"
    BOARD_AGGREGATION_ROLE_MULTI_SLAVE = "multi-slave"
    BOARD_AGGREGATION_ROLE_NONE = "none"
    BOARD_AGGREGATION_ROLE_SINGLE = "single"
    CHASSIS_ID_N_A = "N/A"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class FabricLastAckedSlot(ManagedObject):
    """This is FabricLastAckedSlot class."""

    consts = FabricLastAckedSlotConsts()
    naming_props = set([])

    mo_meta = MoMeta("FabricLastAckedSlot", "fabricLastAckedSlot", "last-acked-slot", VersionMeta.Version101e, "InputOutput", 0x1f, [], ["read-only"], ['fabricCartridgePhEp', 'fabricComputePhEp'], [], ["Get"])

    prop_meta = {
        "board_aggregation_role": MoPropertyMeta("board_aggregation_role", "boardAggregationRole", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["multi-master", "multi-slave", "none", "single"], []),
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "instance_id": MoPropertyMeta("instance_id", "instanceId", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "server_instance_id": MoPropertyMeta("server_instance_id", "serverInstanceId", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
    }

    prop_map = {
        "boardAggregationRole": "board_aggregation_role", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "instanceId": "instance_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serverInstanceId": "server_instance_id", 
        "slotId": "slot_id", 
        "status": "status", 
        "switchId": "switch_id", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.board_aggregation_role = None
        self.chassis_id = None
        self.child_action = None
        self.instance_id = None
        self.sacl = None
        self.server_instance_id = None
        self.slot_id = None
        self.status = None
        self.switch_id = None

        ManagedObject.__init__(self, "FabricLastAckedSlot", parent_mo_or_dn, **kwargs)
