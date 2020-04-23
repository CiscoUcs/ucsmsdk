"""This module contains the general information for VnicFcGroupTempl ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicFcGroupTemplConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    REDUNDANCY_PAIR_TYPE_NONE = "none"
    REDUNDANCY_PAIR_TYPE_PRIMARY = "primary"
    REDUNDANCY_PAIR_TYPE_SECONDARY = "secondary"
    TEMPL_TYPE_INITIAL_TEMPLATE = "initial-template"
    TEMPL_TYPE_UPDATING_TEMPLATE = "updating-template"


class VnicFcGroupTempl(ManagedObject):
    """This is VnicFcGroupTempl class."""

    consts = VnicFcGroupTemplConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("VnicFcGroupTempl", "vnicFcGroupTempl", "fc-group-templ-[name]", VersionMeta.Version211a, "InputOutput", 0xfff, [], ["admin", "ls-config", "ls-server", "ls-storage", "ls-storage-policy"], ['orgOrg'], ['faultInst'], [None])

    prop_meta = {
        "adaptor_profile_name": MoPropertyMeta("adaptor_profile_name", "adaptorProfileName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "ident_pool_name": MoPropertyMeta("ident_pool_name", "identPoolName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "max_data_field_size": MoPropertyMeta("max_data_field_size", "maxDataFieldSize", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["256-2112"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "nw_templ_name": MoPropertyMeta("nw_templ_name", "nwTemplName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_stats_policy_name": MoPropertyMeta("oper_stats_policy_name", "operStatsPolicyName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_storage_conn_policy_name": MoPropertyMeta("oper_storage_conn_policy_name", "operStorageConnPolicyName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "qos_policy_name": MoPropertyMeta("qos_policy_name", "qosPolicyName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "redundancy_pair_type": MoPropertyMeta("redundancy_pair_type", "redundancyPairType", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["none", "primary", "secondary"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "stats_policy_name": MoPropertyMeta("stats_policy_name", "statsPolicyName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "storage_conn_policy_name": MoPropertyMeta("storage_conn_policy_name", "storageConnPolicyName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "templ_type": MoPropertyMeta("templ_type", "templType", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["initial-template", "updating-template"], []),
    }

    prop_map = {
        "adaptorProfileName": "adaptor_profile_name", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "identPoolName": "ident_pool_name", 
        "intId": "int_id", 
        "maxDataFieldSize": "max_data_field_size", 
        "name": "name", 
        "nwTemplName": "nw_templ_name", 
        "operStatsPolicyName": "oper_stats_policy_name", 
        "operStorageConnPolicyName": "oper_storage_conn_policy_name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "qosPolicyName": "qos_policy_name", 
        "redundancyPairType": "redundancy_pair_type", 
        "rn": "rn", 
        "sacl": "sacl", 
        "statsPolicyName": "stats_policy_name", 
        "status": "status", 
        "storageConnPolicyName": "storage_conn_policy_name", 
        "templType": "templ_type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.adaptor_profile_name = None
        self.child_action = None
        self.descr = None
        self.ident_pool_name = None
        self.int_id = None
        self.max_data_field_size = None
        self.nw_templ_name = None
        self.oper_stats_policy_name = None
        self.oper_storage_conn_policy_name = None
        self.policy_level = None
        self.policy_owner = None
        self.qos_policy_name = None
        self.redundancy_pair_type = None
        self.sacl = None
        self.stats_policy_name = None
        self.status = None
        self.storage_conn_policy_name = None
        self.templ_type = None

        ManagedObject.__init__(self, "VnicFcGroupTempl", parent_mo_or_dn, **kwargs)
