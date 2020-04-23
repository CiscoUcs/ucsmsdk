"""This module contains the general information for VnicIpV4PooledAddr ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicIpV4PooledAddrConsts:
    pass


class VnicIpV4PooledAddr(ManagedObject):
    """This is VnicIpV4PooledAddr class."""

    consts = VnicIpV4PooledAddrConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicIpV4PooledAddr", "vnicIpV4PooledAddr", "ipv4-pooled-addr", VersionMeta.Version101e, "InputOutput", 0xff, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server"], ['adaptorHostIscsiIf', 'adaptorVlan', 'lsServer', 'mgmtController', 'mgmtVnet', 'vnicIPv4If'], ['faultInst', 'vnicIpV4History'], ["Get"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
        "oper_name": MoPropertyMeta("oper_name", "operName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "prim_dns": MoPropertyMeta("prim_dns", "primDns", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x10, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sec_dns": MoPropertyMeta("sec_dns", "secDns", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "subnet": MoPropertyMeta("subnet", "subnet", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "name": "name", 
        "operName": "oper_name", 
        "primDns": "prim_dns", 
        "rn": "rn", 
        "sacl": "sacl", 
        "secDns": "sec_dns", 
        "status": "status", 
        "subnet": "subnet", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.addr = None
        self.child_action = None
        self.def_gw = None
        self.name = None
        self.oper_name = None
        self.prim_dns = None
        self.sacl = None
        self.sec_dns = None
        self.status = None
        self.subnet = None

        ManagedObject.__init__(self, "VnicIpV4PooledAddr", parent_mo_or_dn, **kwargs)
