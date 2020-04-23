"""This module contains the general information for VnicIScsiNode ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicIScsiNodeConsts:
    OWNER_CONN_POLICY = "conn_policy"
    OWNER_INITIATOR_POLICY = "initiator_policy"
    OWNER_LOGICAL = "logical"
    OWNER_PHYSICAL = "physical"
    OWNER_POLICY = "policy"
    OWNER_UNKNOWN = "unknown"


class VnicIScsiNode(ManagedObject):
    """This is VnicIScsiNode class."""

    consts = VnicIScsiNodeConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicIScsiNode", "vnicIScsiNode", "iscsi-node", VersionMeta.Version201m, "InputOutput", 0xff, [], ["admin", "ls-config", "ls-network", "ls-server"], ['lsServer', 'vnicLanConnPolicy'], ['faultInst', 'vnicIqnHistory'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "init_name_suffix": MoPropertyMeta("init_name_suffix", "initNameSuffix", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "initiator_name": MoPropertyMeta("initiator_name", "initiatorName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[0-9a-zA-Z\.:-]{0,223}""", [], []),
        "initiator_policy_name": MoPropertyMeta("initiator_policy_name", "initiatorPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "iqn_ident_pool_name": MoPropertyMeta("iqn_ident_pool_name", "iqnIdentPoolName", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
        "oper_initiator_policy_name": MoPropertyMeta("oper_initiator_policy_name", "operInitiatorPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_iqn_ident_pool_name": MoPropertyMeta("oper_iqn_ident_pool_name", "operIqnIdentPoolName", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conn_policy", "initiator_policy", "logical", "physical", "policy", "unknown"], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "initNameSuffix": "init_name_suffix", 
        "initiatorName": "initiator_name", 
        "initiatorPolicyName": "initiator_policy_name", 
        "iqnIdentPoolName": "iqn_ident_pool_name", 
        "operInitiatorPolicyName": "oper_initiator_policy_name", 
        "operIqnIdentPoolName": "oper_iqn_ident_pool_name", 
        "owner": "owner", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.flt_aggr = None
        self.init_name_suffix = None
        self.initiator_name = None
        self.initiator_policy_name = None
        self.iqn_ident_pool_name = None
        self.oper_initiator_policy_name = None
        self.oper_iqn_ident_pool_name = None
        self.owner = None
        self.prop_acl = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "VnicIScsiNode", parent_mo_or_dn, **kwargs)
