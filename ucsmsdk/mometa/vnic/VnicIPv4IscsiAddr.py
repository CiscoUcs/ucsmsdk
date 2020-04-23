"""This module contains the general information for VnicIPv4IscsiAddr ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicIPv4IscsiAddrConsts:
    pass


class VnicIPv4IscsiAddr(ManagedObject):
    """This is VnicIPv4IscsiAddr class."""

    consts = VnicIPv4IscsiAddrConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicIPv4IscsiAddr", "vnicIPv4IscsiAddr", "ipv4iscsi", VersionMeta.Version201m, "InputOutput", 0x3ff, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server", "ls-storage"], ['adaptorHostIscsiIf', 'adaptorVlan', 'vnicIPv4If', 'vnicIScsi'], ['vnicIPv4Dns'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x2, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "prim_dns": MoPropertyMeta("prim_dns", "primDns", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sec_dns": MoPropertyMeta("sec_dns", "secDns", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x80, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "subnet": MoPropertyMeta("subnet", "subnet", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x200, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
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
        self.prim_dns = None
        self.sacl = None
        self.sec_dns = None
        self.status = None
        self.subnet = None

        ManagedObject.__init__(self, "VnicIPv4IscsiAddr", parent_mo_or_dn, **kwargs)
