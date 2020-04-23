"""This module contains the general information for VnicDynamicProviderEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicDynamicProviderEpConsts:
    CHASSIS_ID_N_A = "N/A"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class VnicDynamicProviderEp(ManagedObject):
    """This is VnicDynamicProviderEp class."""

    consts = VnicDynamicProviderEpConsts()
    naming_props = set(['switchId', 'chassisId', 'slotId', 'portId'])

    mo_meta = MoMeta("VnicDynamicProviderEp", "vnicDynamicProviderEp", "ep-[switch_id]-[chassis_id]:[slot_id]:[port_id]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["read-only"], ['vnicDynamicProvider'], [], ["Get"])

    prop_meta = {
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x2, None, None, None, ["N/A"], ["0-255"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x100, None, None, None, ["A", "B", "NONE"], []),
    }

    prop_map = {
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "portId": "port_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotId": "slot_id", 
        "status": "status", 
        "switchId": "switch_id", 
    }

    def __init__(self, parent_mo_or_dn, switch_id, chassis_id, slot_id, port_id, **kwargs):
        self._dirty_mask = 0
        self.switch_id = switch_id
        self.chassis_id = chassis_id
        self.slot_id = slot_id
        self.port_id = port_id
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "VnicDynamicProviderEp", parent_mo_or_dn, **kwargs)
