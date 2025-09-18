"""This module contains the general information for VnicIPv6Dhcp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicIPv6DhcpConsts:
    pass


class VnicIPv6Dhcp(ManagedObject):
    """This is VnicIPv6Dhcp class."""

    consts = VnicIPv6DhcpConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicIPv6Dhcp", "vnicIPv6Dhcp", "ipv6-dhcp", VersionMeta.Version601b, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server", "ls-storage"], ['adaptorVlan', 'vnicIPv6If'], [], [None])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version601b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prefix": MoPropertyMeta("prefix", "prefix", "byte", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-127"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version601b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "prefix": "prefix", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.addr = None
        self.child_action = None
        self.def_gw = None
        self.prefix = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "VnicIPv6Dhcp", parent_mo_or_dn, **kwargs)
