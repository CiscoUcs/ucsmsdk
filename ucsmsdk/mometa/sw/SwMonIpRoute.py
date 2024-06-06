"""This module contains the general information for SwMonIpRoute ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwMonIpRouteConsts:
    LIFE_CYCLE_DELETED = "deleted"
    LIFE_CYCLE_NEW = "new"
    LIFE_CYCLE_NORMAL = "normal"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class SwMonIpRoute(ManagedObject):
    """This is SwMonIpRoute class."""

    consts = SwMonIpRouteConsts()
    naming_props = set(['destIP', 'routeIP'])

    mo_meta = MoMeta("SwMonIpRoute", "swMonIpRoute", "dest-[dest_ip]-next-[route_ip]", VersionMeta.Version434a, "InputOutput", 0x7f, [], ["read-only"], ['swRMonSVI'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dest_ip": MoPropertyMeta("dest_ip", "destIP", "string", VersionMeta.Version434a, MoPropertyMeta.NAMING, 0x4, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "dest_netmask": MoPropertyMeta("dest_netmask", "destNetmask", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "life_cycle": MoPropertyMeta("life_cycle", "lifeCycle", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deleted", "new", "normal"], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "prefix": MoPropertyMeta("prefix", "prefix", "ushort", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "route_ip": MoPropertyMeta("route_ip", "routeIP", "string", VersionMeta.Version434a, MoPropertyMeta.NAMING, 0x20, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "destIP": "dest_ip", 
        "destNetmask": "dest_netmask", 
        "dn": "dn", 
        "lifeCycle": "life_cycle", 
        "peerDn": "peer_dn", 
        "prefix": "prefix", 
        "rn": "rn", 
        "routeIP": "route_ip", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
    }

    def __init__(self, parent_mo_or_dn, dest_ip, route_ip, **kwargs):
        self._dirty_mask = 0
        self.dest_ip = dest_ip
        self.route_ip = route_ip
        self.child_action = None
        self.dest_netmask = None
        self.life_cycle = None
        self.peer_dn = None
        self.prefix = None
        self.sacl = None
        self.status = None
        self.switch_id = None

        ManagedObject.__init__(self, "SwMonIpRoute", parent_mo_or_dn, **kwargs)
