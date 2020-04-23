"""This module contains the general information for FabricLocale ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricLocaleConsts:
    C_TYPE_MUX = "mux"
    C_TYPE_MUX_ACCESS = "mux-access"
    C_TYPE_MUX_FABRIC = "mux-fabric"
    C_TYPE_MUX_FABRICPC = "mux-fabricpc"
    C_TYPE_MUX_FABRICPC_TO_CHPC = "mux-fabricpc-to-chpc"
    C_TYPE_MUX_FABRICPC_TO_HOSTPC = "mux-fabricpc-to-hostpc"
    C_TYPE_MUX_FABRICPC_TO_HOSTPORT = "mux-fabricpc-to-hostport"
    C_TYPE_MUX_FABRICPORT_TO_HOSTPC = "mux-fabricport-to-hostpc"
    C_TYPE_MUX_HOSTPC_TO_ADAPTORPC = "mux-hostpc-to-adaptorpc"
    C_TYPE_MUX_TO_APPLIANCE = "mux-to-appliance"
    C_TYPE_MUX_TO_CHASSIS = "mux-to-chassis"
    C_TYPE_MUX_TO_HOST = "mux-to-host"
    C_TYPE_SWITCH_ACCESS = "switch-access"
    C_TYPE_SWITCH_FABRIC = "switch-fabric"
    C_TYPE_SWITCH_FABRICPC = "switch-fabricpc"
    C_TYPE_SWITCH_TO_HOST = "switch-to-host"
    C_TYPE_SWITCH_TO_MUX = "switch-to-mux"
    C_TYPE_SWITCHPC_TO_HOSTPC = "switchpc-to-hostpc"
    CHASSIS_ID_N_A = "N/A"
    EVAC_STATE_DRAIN = "drain"
    EVAC_STATE_FILL = "fill"
    EVAC_STATE_UNKNOWN = "unknown"
    SIDE_LEFT = "left"
    SIDE_RIGHT = "right"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class FabricLocale(ManagedObject):
    """This is FabricLocale class."""

    consts = FabricLocaleConsts()
    naming_props = set(['switchId'])

    mo_meta = MoMeta("FabricLocale", "fabricLocale", "fabric-[switch_id]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["read-only"], ['computeBlade', 'computeRackUnit', 'computeServerUnit', 'equipmentChassis', 'equipmentFex', 'mgmtController'], ['adaptorExtEthIfPc', 'dcxVc', 'fabricPath'], ["Get"])

    prop_meta = {
        "c_type": MoPropertyMeta("c_type", "cType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["mux", "mux-access", "mux-fabric", "mux-fabricpc", "mux-fabricpc-to-chpc", "mux-fabricpc-to-hostpc", "mux-fabricpc-to-hostport", "mux-fabricport-to-hostpc", "mux-hostpc-to-adaptorpc", "mux-to-appliance", "mux-to-chassis", "mux-to-host", "switch-access", "switch-fabric", "switch-fabricpc", "switch-to-host", "switch-to-mux", "switchpc-to-hostpc"], ["0-255"]),
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "evac_state": MoPropertyMeta("evac_state", "evacState", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["drain", "fill", "unknown"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "side": MoPropertyMeta("side", "side", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["left", "right"], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, None, ["A", "B", "NONE"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "cType": "c_type", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "evacState": "evac_state", 
        "locale": "locale", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "side": "side", 
        "slotId": "slot_id", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, switch_id, **kwargs):
        self._dirty_mask = 0
        self.switch_id = switch_id
        self.c_type = None
        self.chassis_id = None
        self.child_action = None
        self.evac_state = None
        self.locale = None
        self.name = None
        self.sacl = None
        self.side = None
        self.slot_id = None
        self.status = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "FabricLocale", parent_mo_or_dn, **kwargs)
