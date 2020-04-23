"""This module contains the general information for FabricPathConn ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricPathConnConsts:
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


class FabricPathConn(ManagedObject):
    """This is FabricPathConn class."""

    consts = FabricPathConnConsts()
    naming_props = set(['cType'])

    mo_meta = MoMeta("FabricPathConn", "fabricPathConn", "xc-[c_type]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["read-only"], ['fabricPath'], ['fabricPathEp'], ["Get"])

    prop_meta = {
        "c_type": MoPropertyMeta("c_type", "cType", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x2, None, None, None, ["mux", "mux-access", "mux-fabric", "mux-fabricpc", "mux-fabricpc-to-chpc", "mux-fabricpc-to-hostpc", "mux-fabricpc-to-hostport", "mux-fabricport-to-hostpc", "mux-hostpc-to-adaptorpc", "mux-to-appliance", "mux-to-chassis", "mux-to-host", "switch-access", "switch-fabric", "switch-fabricpc", "switch-to-host", "switch-to-mux", "switchpc-to-hostpc"], ["0-255"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "cType": "c_type", 
        "childAction": "child_action", 
        "dn": "dn", 
        "locale": "locale", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, c_type, **kwargs):
        self._dirty_mask = 0
        self.c_type = c_type
        self.child_action = None
        self.locale = None
        self.name = None
        self.sacl = None
        self.status = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "FabricPathConn", parent_mo_or_dn, **kwargs)
