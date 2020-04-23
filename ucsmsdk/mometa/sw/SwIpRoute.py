"""This module contains the general information for SwIpRoute ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwIpRouteConsts:
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class SwIpRoute(ManagedObject):
    """This is SwIpRoute class."""

    consts = SwIpRouteConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("SwIpRoute", "swIpRoute", "ip-route-[name]", VersionMeta.Version221b, "InputOutput", 0x3f, [], ["read-only"], ['swEthLanFlowMon'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "destination_ip": MoPropertyMeta("destination_ip", "destinationIp", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "destination_netmask": MoPropertyMeta("destination_netmask", "destinationNetmask", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "prefix": MoPropertyMeta("prefix", "prefix", "ushort", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "route_ip": MoPropertyMeta("route_ip", "routeIP", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "destinationIp": "destination_ip", 
        "destinationNetmask": "destination_netmask", 
        "dn": "dn", 
        "name": "name", 
        "peerDn": "peer_dn", 
        "prefix": "prefix", 
        "rn": "rn", 
        "routeIP": "route_ip", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.destination_ip = None
        self.destination_netmask = None
        self.peer_dn = None
        self.prefix = None
        self.route_ip = None
        self.sacl = None
        self.status = None
        self.switch_id = None

        ManagedObject.__init__(self, "SwIpRoute", parent_mo_or_dn, **kwargs)
