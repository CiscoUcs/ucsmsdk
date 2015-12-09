"""This module contains the general information for VnicConnDef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class VnicConnDefConsts():
    pass


class VnicConnDef(ManagedObject):
    """This is VnicConnDef class."""

    consts = VnicConnDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicConnDef", "vnicConnDef", "conn-def", VersionMeta.Version211a, "InputOutput", 0x7fL, [], ["admin", "ls-compute", "ls-config", "ls-server"], [u'lsServer'], [u'faultInst'], ["Add", "Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "lan_conn_policy_name": MoPropertyMeta("lan_conn_policy_name", "lanConnPolicyName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_lan_conn_policy_name": MoPropertyMeta("oper_lan_conn_policy_name", "operLanConnPolicyName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_san_conn_policy_name": MoPropertyMeta("oper_san_conn_policy_name", "operSanConnPolicyName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "san_conn_policy_name": MoPropertyMeta("san_conn_policy_name", "sanConnPolicyName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "lanConnPolicyName": "lan_conn_policy_name", 
        "operLanConnPolicyName": "oper_lan_conn_policy_name", 
        "operSanConnPolicyName": "oper_san_conn_policy_name", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sanConnPolicyName": "san_conn_policy_name", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.flt_aggr = None
        self.lan_conn_policy_name = None
        self.oper_lan_conn_policy_name = None
        self.oper_san_conn_policy_name = None
        self.prop_acl = None
        self.sacl = None
        self.san_conn_policy_name = None
        self.status = None

        ManagedObject.__init__(self, "VnicConnDef", parent_mo_or_dn, **kwargs)

