"""This module contains the general information for VnicIPv4StaticRoute ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicIPv4StaticRouteConsts:
    pass


class VnicIPv4StaticRoute(ManagedObject):
    """This is VnicIPv4StaticRoute class."""

    consts = VnicIPv4StaticRouteConsts()
    naming_props = set(['addr'])

    mo_meta = MoMeta("VnicIPv4StaticRoute", "vnicIPv4StaticRoute", "ipv4-route-[addr]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server"], ['adaptorHostIscsiIf', 'adaptorVlan', 'vnicIPv4If'], [], ["Get"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x2, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "gw_addr": MoPropertyMeta("gw_addr", "gwAddr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "gw_subnet": MoPropertyMeta("gw_subnet", "gwSubnet", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "subnet": MoPropertyMeta("subnet", "subnet", "string", VersionMeta.Version101e, MoPropertyMeta.CREATE_ONLY, 0x100, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "gwAddr": "gw_addr", 
        "gwSubnet": "gw_subnet", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "subnet": "subnet", 
    }

    def __init__(self, parent_mo_or_dn, addr, **kwargs):
        self._dirty_mask = 0
        self.addr = addr
        self.child_action = None
        self.def_gw = None
        self.gw_addr = None
        self.gw_subnet = None
        self.sacl = None
        self.status = None
        self.subnet = None

        ManagedObject.__init__(self, "VnicIPv4StaticRoute", parent_mo_or_dn, **kwargs)
