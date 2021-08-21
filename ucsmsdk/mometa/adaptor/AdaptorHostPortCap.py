"""This module contains the general information for AdaptorHostPortCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorHostPortCapConsts:
    HOST_PORT_ID_ANY = "any"
    HOST_PORT_ID_HOSTPORT1 = "hostport1"
    HOST_PORT_ID_HOSTPORT2 = "hostport2"


class AdaptorHostPortCap(ManagedObject):
    """This is AdaptorHostPortCap class."""

    consts = AdaptorHostPortCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorHostPortCap", "adaptorHostPortCap", "max-host-port", VersionMeta.Version223a, "InputOutput", 0x7f, [], ["read-only"], ['adaptorFruCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "host_port_id": MoPropertyMeta("host_port_id", "hostPortId", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["any", "hostport1", "hostport2"], ["0-255"]),
        "max_ports": MoPropertyMeta("max_ports", "maxPorts", "ushort", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "hostPortId": "host_port_id", 
        "maxPorts": "max_ports", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.host_port_id = None
        self.max_ports = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorHostPortCap", parent_mo_or_dn, **kwargs)
