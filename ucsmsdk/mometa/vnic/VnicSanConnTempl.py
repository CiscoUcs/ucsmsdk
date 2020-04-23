"""This module contains the general information for VnicSanConnTempl ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicSanConnTemplConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    REDUNDANCY_PAIR_TYPE_NONE = "none"
    REDUNDANCY_PAIR_TYPE_PRIMARY = "primary"
    REDUNDANCY_PAIR_TYPE_SECONDARY = "secondary"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    TEMPL_TYPE_INITIAL_TEMPLATE = "initial-template"
    TEMPL_TYPE_UPDATING_TEMPLATE = "updating-template"


class VnicSanConnTempl(ManagedObject):
    """This is VnicSanConnTempl class."""

    consts = VnicSanConnTemplConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("VnicSanConnTempl", "vnicSanConnTempl", "san-conn-templ-[name]", VersionMeta.Version101e, "InputOutput", 0x1ffff, [], ["admin", "ls-storage", "ls-storage-policy"], ['orgOrg'], ['fabricNetGroupRef', 'fabricSanGroupRef', 'faultInst', 'vnicFcIf'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "ident_pool_name": MoPropertyMeta("ident_pool_name", "identPoolName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "max_data_field_size": MoPropertyMeta("max_data_field_size", "maxDataFieldSize", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["256-2112"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "nw_ctrl_policy_name": MoPropertyMeta("nw_ctrl_policy_name", "nwCtrlPolicyName", "string", VersionMeta.Version102d, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_ident_pool_name": MoPropertyMeta("oper_ident_pool_name", "operIdentPoolName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_peer_redundancy_templ_name": MoPropertyMeta("oper_peer_redundancy_templ_name", "operPeerRedundancyTemplName", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_qos_policy_name": MoPropertyMeta("oper_qos_policy_name", "operQosPolicyName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_stats_policy_name": MoPropertyMeta("oper_stats_policy_name", "operStatsPolicyName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "peer_redundancy_templ_name": MoPropertyMeta("peer_redundancy_templ_name", "peerRedundancyTemplName", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "pin_to_group_name": MoPropertyMeta("pin_to_group_name", "pinToGroupName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["local", "pending-policy", "policy"], []),
        "qos_policy_name": MoPropertyMeta("qos_policy_name", "qosPolicyName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "redundancy_pair_type": MoPropertyMeta("redundancy_pair_type", "redundancyPairType", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["none", "primary", "secondary"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x1000, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "stats_policy_name": MoPropertyMeta("stats_policy_name", "statsPolicyName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["A", "B", "NONE"], []),
        "target": MoPropertyMeta("target", "target", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((vm|adaptor|defaultValue),){0,2}(vm|adaptor|defaultValue){0,1}""", [], []),
        "templ_type": MoPropertyMeta("templ_type", "templType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["initial-template", "updating-template"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "identPoolName": "ident_pool_name", 
        "intId": "int_id", 
        "maxDataFieldSize": "max_data_field_size", 
        "name": "name", 
        "nwCtrlPolicyName": "nw_ctrl_policy_name", 
        "operIdentPoolName": "oper_ident_pool_name", 
        "operPeerRedundancyTemplName": "oper_peer_redundancy_templ_name", 
        "operQosPolicyName": "oper_qos_policy_name", 
        "operStatsPolicyName": "oper_stats_policy_name", 
        "peerRedundancyTemplName": "peer_redundancy_templ_name", 
        "pinToGroupName": "pin_to_group_name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "qosPolicyName": "qos_policy_name", 
        "redundancyPairType": "redundancy_pair_type", 
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
        self.child_action = None
        self.descr = None
        self.ident_pool_name = None
        self.int_id = None
        self.max_data_field_size = None
        self.nw_ctrl_policy_name = None
        self.oper_ident_pool_name = None
        self.oper_peer_redundancy_templ_name = None
        self.oper_qos_policy_name = None
        self.oper_stats_policy_name = None
        self.peer_redundancy_templ_name = None
        self.pin_to_group_name = None
        self.policy_level = None
        self.policy_owner = None
        self.qos_policy_name = None
        self.redundancy_pair_type = None
        self.sacl = None
        self.stats_policy_name = None
        self.status = None
        self.switch_id = None
        self.target = None
        self.templ_type = None

        ManagedObject.__init__(self, "VnicSanConnTempl", parent_mo_or_dn, **kwargs)
