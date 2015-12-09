"""This module contains the general information for VnicLanConnTempl ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class VnicLanConnTemplConsts():
    CDN_SOURCE_USER_DEFINED = "user-defined"
    CDN_SOURCE_VNIC_NAME = "vnic-name"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SWITCH_ID_A = "A"
    SWITCH_ID_A_B = "A-B"
    SWITCH_ID_B = "B"
    SWITCH_ID_B_A = "B-A"
    SWITCH_ID_NONE = "NONE"
    TEMPL_TYPE_INITIAL_TEMPLATE = "initial-template"
    TEMPL_TYPE_UPDATING_TEMPLATE = "updating-template"


class VnicLanConnTempl(ManagedObject):
    """This is VnicLanConnTempl class."""

    consts = VnicLanConnTemplConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("VnicLanConnTempl", "vnicLanConnTempl", "lan-conn-templ-[name]", VersionMeta.Version101e, "InputOutput", 0x7ffffL, [], ["admin", "ls-network", "ls-network-policy"], [u'orgOrg'], [u'faultInst', u'vnicDynamicConPolicyRef', u'vnicEtherIf', u'vnicFcOEIf', u'vnicUsnicConPolicyRef', u'vnicVmqConPolicyRef'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_cdn_name": MoPropertyMeta("admin_cdn_name", "adminCdnName", "string", None, MoPropertyMeta.READ_WRITE, 0x2L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "cdn_source": MoPropertyMeta("cdn_source", "cdnSource", "string", None, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["user-defined", "vnic-name"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x8L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "ident_pool_name": MoPropertyMeta("ident_pool_name", "identPoolName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "mtu": MoPropertyMeta("mtu", "mtu", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, [], ["1500-9000"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x100L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "nw_ctrl_policy_name": MoPropertyMeta("nw_ctrl_policy_name", "nwCtrlPolicyName", "string", VersionMeta.Version102d, MoPropertyMeta.READ_WRITE, 0x200L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_ident_pool_name": MoPropertyMeta("oper_ident_pool_name", "operIdentPoolName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_nw_ctrl_policy_name": MoPropertyMeta("oper_nw_ctrl_policy_name", "operNwCtrlPolicyName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_qos_policy_name": MoPropertyMeta("oper_qos_policy_name", "operQosPolicyName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_stats_policy_name": MoPropertyMeta("oper_stats_policy_name", "operStatsPolicyName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "pin_to_group_name": MoPropertyMeta("pin_to_group_name", "pinToGroupName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "qos_policy_name": MoPropertyMeta("qos_policy_name", "qosPolicyName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x2000L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "stats_policy_name": MoPropertyMeta("stats_policy_name", "statsPolicyName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10000L, None, None, None, ["A", "A-B", "B", "B-A", "NONE"], []), 
        "target": MoPropertyMeta("target", "target", "string", VersionMeta.Version101e, MoPropertyMeta.CREATE_ONLY, 0x20000L, None, None, r"""((vm|adaptor|defaultValue),){0,2}(vm|adaptor|defaultValue){0,1}""", [], []), 
        "templ_type": MoPropertyMeta("templ_type", "templType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40000L, None, None, None, ["initial-template", "updating-template"], []), 
    }

    prop_map = {
        "adminCdnName": "admin_cdn_name", 
        "cdnSource": "cdn_source", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "identPoolName": "ident_pool_name", 
        "intId": "int_id", 
        "mtu": "mtu", 
        "name": "name", 
        "nwCtrlPolicyName": "nw_ctrl_policy_name", 
        "operIdentPoolName": "oper_ident_pool_name", 
        "operNwCtrlPolicyName": "oper_nw_ctrl_policy_name", 
        "operQosPolicyName": "oper_qos_policy_name", 
        "operStatsPolicyName": "oper_stats_policy_name", 
        "pinToGroupName": "pin_to_group_name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "qosPolicyName": "qos_policy_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "statsPolicyName": "stats_policy_name", 
        "status": "status", 
        "switchId": "switch_id", 
        "target": "target", 
        "templType": "templ_type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_cdn_name = None
        self.cdn_source = None
        self.child_action = None
        self.descr = None
        self.ident_pool_name = None
        self.int_id = None
        self.mtu = None
        self.nw_ctrl_policy_name = None
        self.oper_ident_pool_name = None
        self.oper_nw_ctrl_policy_name = None
        self.oper_qos_policy_name = None
        self.oper_stats_policy_name = None
        self.pin_to_group_name = None
        self.policy_level = None
        self.policy_owner = None
        self.qos_policy_name = None
        self.sacl = None
        self.stats_policy_name = None
        self.status = None
        self.switch_id = None
        self.target = None
        self.templ_type = None

        ManagedObject.__init__(self, "VnicLanConnTempl", parent_mo_or_dn, **kwargs)

