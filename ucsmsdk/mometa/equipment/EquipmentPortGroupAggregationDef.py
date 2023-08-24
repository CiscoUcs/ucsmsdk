"""This module contains the general information for EquipmentPortGroupAggregationDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentPortGroupAggregationDefConsts:
    AUTO_NEG_25G = "25g"
    AUTO_NEG_OFF = "off"
    AUTO_NEG_ON = "on"
    HW40_GPCPORT_GROUP_CAP_FALSE = "false"
    HW40_GPCPORT_GROUP_CAP_NO = "no"
    HW40_GPCPORT_GROUP_CAP_TRUE = "true"
    HW40_GPCPORT_GROUP_CAP_YES = "yes"
    HW40_GPORT_GROUP_CAP_FALSE = "false"
    HW40_GPORT_GROUP_CAP_NO = "no"
    HW40_GPORT_GROUP_CAP_TRUE = "true"
    HW40_GPORT_GROUP_CAP_YES = "yes"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    TYPE_ADAPTOR_EXT = "adaptor-ext"
    TYPE_ADAPTOR_PC = "adaptor-pc"
    TYPE_FABRIC = "fabric"
    TYPE_FABRIC_PC = "fabric-pc"
    TYPE_HOST = "host"
    TYPE_HOST_PC = "host-pc"
    TYPE_SERVER_PC = "server-pc"
    TYPE_SWITCH_ETHER = "switch-ether"
    TYPE_SWITCH_FC = "switch-fc"


class EquipmentPortGroupAggregationDef(ManagedObject):
    """This is EquipmentPortGroupAggregationDef class."""

    consts = EquipmentPortGroupAggregationDefConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("EquipmentPortGroupAggregationDef", "equipmentPortGroupAggregationDef", "port-group-aggr-def-[type]", VersionMeta.Version201m, "InputOutput", 0x3ff, [], [""], ['adaptorFruCapProvider', 'equipmentFexCapProvider', 'equipmentIOCardCapProvider', 'equipmentSwitchCapProvider', 'equipmentSwitchIOCardCapProvider'], [], ["Get"])

    prop_meta = {
        "aggregation_cap": MoPropertyMeta("aggregation_cap", "aggregationCap", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|port-channel),){0,2}(defaultValue|none|port-channel){0,1}""", [], []),
        "auto_neg": MoPropertyMeta("auto_neg", "autoNeg", "string", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["25g", "off", "on"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "hw40_gpc_port_group_cap": MoPropertyMeta("hw40_gpc_port_group_cap", "hw40GPCPortGroupCap", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "hw40_g_port_group_cap": MoPropertyMeta("hw40_g_port_group_cap", "hw40GPortGroupCap", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x200, None, None, None, ["adaptor-ext", "adaptor-pc", "fabric", "fabric-pc", "host", "host-pc", "server-pc", "switch-ether", "switch-fc"], []),
    }

    prop_map = {
        "aggregationCap": "aggregation_cap", 
        "autoNeg": "auto_neg", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "hw40GPCPortGroupCap": "hw40_gpc_port_group_cap", 
        "hw40GPortGroupCap": "hw40_g_port_group_cap", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.aggregation_cap = None
        self.auto_neg = None
        self.child_action = None
        self.descr = None
        self.hw40_gpc_port_group_cap = None
        self.hw40_g_port_group_cap = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPortGroupAggregationDef", parent_mo_or_dn, **kwargs)
