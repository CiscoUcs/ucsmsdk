"""This module contains the general information for VnicIpV6MgmtPooledAddr ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicIpV6MgmtPooledAddrConsts:
    pass


class VnicIpV6MgmtPooledAddr(ManagedObject):
    """This is VnicIpV6MgmtPooledAddr class."""

    consts = VnicIpV6MgmtPooledAddrConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicIpV6MgmtPooledAddr", "vnicIpV6MgmtPooledAddr", "ipv6-pooled-addr", VersionMeta.Version221b, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server"], ['mgmtVnet'], ['faultInst', 'vnicIpV6History'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
        "oper_name": MoPropertyMeta("oper_name", "operName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "prefix": MoPropertyMeta("prefix", "prefix", "byte", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-127"]),
        "prim_dns": MoPropertyMeta("prim_dns", "primDns", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sec_dns": MoPropertyMeta("sec_dns", "secDns", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "name": "name", 
        "operName": "oper_name", 
        "prefix": "prefix", 
        "primDns": "prim_dns", 
        "rn": "rn", 
        "sacl": "sacl", 
        "secDns": "sec_dns", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.addr = None
        self.child_action = None
        self.def_gw = None
        self.name = None
        self.oper_name = None
        self.prefix = None
        self.prim_dns = None
        self.sacl = None
        self.sec_dns = None
        self.status = None

        ManagedObject.__init__(self, "VnicIpV6MgmtPooledAddr", parent_mo_or_dn, **kwargs)
