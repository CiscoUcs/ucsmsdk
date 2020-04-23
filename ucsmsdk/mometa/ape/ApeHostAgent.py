"""This module contains the general information for ApeHostAgent ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ApeHostAgentConsts:
    CHASSIS_ID_N_A = "N/A"
    STATE_HALTING_HOSTOS = "HALTING_HOSTOS"
    STATE_HALTING_PNUOS = "HALTING_PNUOS"
    STATE_HOSTOS = "HOSTOS"
    STATE_PNUOS = "PNUOS"
    STATE_STARTING_HOSTOS = "STARTING_HOSTOS"
    STATE_STARTING_PNUOS = "STARTING_PNUOS"
    STATE_UNKNOWN = "UNKNOWN"


class ApeHostAgent(ManagedObject):
    """This is ApeHostAgent class."""

    consts = ApeHostAgentConsts()
    naming_props = set(['chassisId', 'slotId'])

    mo_meta = MoMeta("ApeHostAgent", "apeHostAgent", "hostagent-[chassis_id]-[slot_id]", VersionMeta.Version101e, "InputOutput", 0xff, [], ["admin"], ['apeManager'], [], [None])

    prop_meta = {
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x2, None, None, None, ["N/A"], ["0-255"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "server_id": MoPropertyMeta("server_id", "serverId", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, None, [], []),
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["HALTING_HOSTOS", "HALTING_PNUOS", "HOSTOS", "PNUOS", "STARTING_HOSTOS", "STARTING_PNUOS", "UNKNOWN"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serverId": "server_id", 
        "slotId": "slot_id", 
        "state": "state", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, chassis_id, slot_id, **kwargs):
        self._dirty_mask = 0
        self.chassis_id = chassis_id
        self.slot_id = slot_id
        self.child_action = None
        self.sacl = None
        self.server_id = None
        self.state = None
        self.status = None

        ManagedObject.__init__(self, "ApeHostAgent", parent_mo_or_dn, **kwargs)
