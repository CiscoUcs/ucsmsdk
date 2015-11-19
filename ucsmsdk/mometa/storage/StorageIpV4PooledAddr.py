"""This module contains the general information for StorageIpV4PooledAddr ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageIpV4PooledAddrConsts():
    pass


class StorageIpV4PooledAddr(ManagedObject):
    """This is StorageIpV4PooledAddr class."""

    consts = StorageIpV4PooledAddrConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageIpV4PooledAddr", "storageIpV4PooledAddr", "storage-ipv4-pooled-addr", VersionMeta.Version302a, "InputOutput", 0xffL, [], ["admin", "ls-storage"], [u'adaptorHostIscsiIf', u'adaptorVlan', u'lsServer', u'lstorageProcessor', u'mgmtVnet', u'vnicIPv4If'], [u'faultInst', u'vnicIpV4History'], [None])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302a, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "ident_pool_name": MoPropertyMeta("ident_pool_name", "identPoolName", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], []), 
        "oper_ident_pool_name": MoPropertyMeta("oper_ident_pool_name", "operIdentPoolName", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "prim_dns": MoPropertyMeta("prim_dns", "primDns", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x10L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "sec_dns": MoPropertyMeta("sec_dns", "secDns", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x40L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "subnet": MoPropertyMeta("subnet", "subnet", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "identPoolName": "ident_pool_name", 
        "operIdentPoolName": "oper_ident_pool_name", 
        "primDns": "prim_dns", 
        "propAcl": "prop_acl", 
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
        self.ident_pool_name = None
        self.oper_ident_pool_name = None
        self.prim_dns = None
        self.prop_acl = None
        self.sacl = None
        self.sec_dns = None
        self.status = None
        self.subnet = None

        ManagedObject.__init__(self, "StorageIpV4PooledAddr", parent_mo_or_dn, **kwargs)

