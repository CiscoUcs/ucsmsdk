"""This module contains the general information for VnicFcNode ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicFcNodeConsts:
    ADDR_POOL_DERIVED = "pool-derived"
    ADDR_VNIC_DERIVED = "vnic-derived"
    OWNER_CONN_POLICY = "conn_policy"
    OWNER_INITIATOR_POLICY = "initiator_policy"
    OWNER_LOGICAL = "logical"
    OWNER_PHYSICAL = "physical"
    OWNER_POLICY = "policy"
    OWNER_UNKNOWN = "unknown"


class VnicFcNode(ManagedObject):
    """This is VnicFcNode class."""

    consts = VnicFcNodeConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicFcNode", "vnicFcNode", "fc-node", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["admin", "ls-config", "ls-server", "ls-storage"], ['lsServer', 'vnicSanConnPolicy'], ['faultInst', 'vnicWwnnHistory'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", ["pool-derived", "vnic-derived"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "ident_pool_name": MoPropertyMeta("ident_pool_name", "identPoolName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "max_derivable_wwpn": MoPropertyMeta("max_derivable_wwpn", "maxDerivableWWPN", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "oper_ident_pool_name": MoPropertyMeta("oper_ident_pool_name", "operIdentPoolName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conn_policy", "initiator_policy", "logical", "physical", "policy", "unknown"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "identPoolName": "ident_pool_name", 
        "maxDerivableWWPN": "max_derivable_wwpn", 
        "operIdentPoolName": "oper_ident_pool_name", 
        "owner": "owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.addr = None
        self.child_action = None
        self.flt_aggr = None
        self.ident_pool_name = None
        self.max_derivable_wwpn = None
        self.oper_ident_pool_name = None
        self.owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "VnicFcNode", parent_mo_or_dn, **kwargs)
