"""This module contains the general information for VnicIPv6PooledIscsiAddr ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicIPv6PooledIscsiAddrConsts:
    pass


class VnicIPv6PooledIscsiAddr(ManagedObject):
    """This is VnicIPv6PooledIscsiAddr class."""

    consts = VnicIPv6PooledIscsiAddrConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicIPv6PooledIscsiAddr", "vnicIPv6PooledIscsiAddr", "ipv6-pooled-iscsiaddr", VersionMeta.Version601b, "InputOutput", 0xff, [], ["admin", "ls-config", "ls-network", "ls-server", "ls-storage"], ['adaptorVlan', 'vnicIPv6If'], ['faultInst', 'vnicIpV6History'], [None])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version601b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ident_pool_name": MoPropertyMeta("ident_pool_name", "identPoolName", "string", VersionMeta.Version601b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
        "oper_ident_pool_name": MoPropertyMeta("oper_ident_pool_name", "operIdentPoolName", "string", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "prefix": MoPropertyMeta("prefix", "prefix", "byte", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-127"]),
        "prim_dns": MoPropertyMeta("prim_dns", "primDns", "string", VersionMeta.Version601b, MoPropertyMeta.READ_WRITE, 0x10, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version601b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sec_dns": MoPropertyMeta("sec_dns", "secDns", "string", VersionMeta.Version601b, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version601b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "identPoolName": "ident_pool_name", 
        "operIdentPoolName": "oper_ident_pool_name", 
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
        self.ident_pool_name = None
        self.oper_ident_pool_name = None
        self.prefix = None
        self.prim_dns = None
        self.sacl = None
        self.sec_dns = None
        self.status = None

        ManagedObject.__init__(self, "VnicIPv6PooledIscsiAddr", parent_mo_or_dn, **kwargs)
