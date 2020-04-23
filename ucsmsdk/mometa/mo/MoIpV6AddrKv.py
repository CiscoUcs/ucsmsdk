"""This module contains the general information for MoIpV6AddrKv ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MoIpV6AddrKvConsts:
    OWNER_INVENTORY = "inventory"
    OWNER_MGMT = "mgmt"
    TYPE_IPV4_ADDR = "ipv4-addr"
    TYPE_IPV6_ADDR = "ipv6-addr"
    TYPE_KEY_VALUE = "key-value"
    TYPE_VLAN = "vlan"
    TYPE_VNIC = "vnic"


class MoIpV6AddrKv(ManagedObject):
    """This is MoIpV6AddrKv class."""

    consts = MoIpV6AddrKvConsts()
    naming_props = set(['key'])

    mo_meta = MoMeta("MoIpV6AddrKv", "moIpV6AddrKv", "kv-[key]", VersionMeta.Version321d, "InputOutput", 0x3ff, [], ["admin", "read-only"], ['moKvCfgHolder'], ['faultInst'], ["Get", "Set"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "oper_pool_name": MoPropertyMeta("oper_pool_name", "operPoolName", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["inventory", "mgmt"], []),
        "pool_name": MoPropertyMeta("pool_name", "poolName", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "prefix": MoPropertyMeta("prefix", "prefix", "byte", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-127"]),
        "prim_dns": MoPropertyMeta("prim_dns", "primDns", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sec_dns": MoPropertyMeta("sec_dns", "secDns", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x80, 0, 256, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "target": MoPropertyMeta("target", "target", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((defaultValue|host|mgmt),){0,2}(defaultValue|host|mgmt){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ipv4-addr", "ipv6-addr", "key-value", "vlan", "vnic"], []),
        "value": MoPropertyMeta("value", "value", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "key": "key", 
        "operPoolName": "oper_pool_name", 
        "owner": "owner", 
        "poolName": "pool_name", 
        "prefix": "prefix", 
        "primDns": "prim_dns", 
        "rn": "rn", 
        "sacl": "sacl", 
        "secDns": "sec_dns", 
        "status": "status", 
        "target": "target", 
        "type": "type", 
        "value": "value", 
    }

    def __init__(self, parent_mo_or_dn, key, **kwargs):
        self._dirty_mask = 0
        self.key = key
        self.addr = None
        self.child_action = None
        self.def_gw = None
        self.oper_pool_name = None
        self.owner = None
        self.pool_name = None
        self.prefix = None
        self.prim_dns = None
        self.sacl = None
        self.sec_dns = None
        self.status = None
        self.target = None
        self.type = None
        self.value = None

        ManagedObject.__init__(self, "MoIpV6AddrKv", parent_mo_or_dn, **kwargs)
