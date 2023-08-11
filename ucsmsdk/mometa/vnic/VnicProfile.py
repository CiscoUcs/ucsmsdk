"""This module contains the general information for VnicProfile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicProfileConsts:
    CDP_DISABLED = "disabled"
    CDP_ENABLED = "enabled"
    CONFIG_QUALIFIER_INVALID_NAME = "invalid-name"
    CONFIG_QUALIFIER_NORMAL = "normal"
    COS_ANY = "any"
    FORGE_MAC_ALLOW = "allow"
    FORGE_MAC_DENY = "deny"
    HOST_NW_IOPERF_HIGH_PERF_REQD = "high-perf-reqd"
    HOST_NW_IOPERF_NONE = "none"
    INT_ID_NONE = "none"
    MAC_REGISTER_MODE_ALL_HOST_VLANS = "all-host-vlans"
    MAC_REGISTER_MODE_ONLY_NATIVE_VLAN = "only-native-vlan"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    QOS_POLICY_ID_NONE = "none"
    TYPE_REGULAR = "regular"
    TYPE_SLA_ONLY = "sla-only"
    UPLINK_FAIL_ACTION_LINK_DOWN = "link-down"
    UPLINK_FAIL_ACTION_WARNING = "warning"


class VnicProfile(ManagedObject):
    """This is VnicProfile class."""

    consts = VnicProfileConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("VnicProfile", "vnicProfile", "vnic-[name]", VersionMeta.Version101e, "InputOutput", 0x7fff, [], ["admin", "ls-network", "ls-network-policy"], ['vnicProfileSet'], ['fabricNetGroupRef', 'fabricNetflowMonSrcEp', 'faultInst', 'swNetflowMonitorRef', 'vmVnicProfCl', 'vnicEtherIf', 'vnicOProfileAlias', 'vnicProfileAlias'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "cdp": MoPropertyMeta("cdp", "cdp", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version203a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["invalid-name", "normal"], []),
        "cos": MoPropertyMeta("cos", "cos", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["any"], ["0-6", "255-255"]),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "forge_mac": MoPropertyMeta("forge_mac", "forgeMac", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allow", "deny"], []),
        "host_nw_io_perf": MoPropertyMeta("host_nw_io_perf", "hostNwIOPerf", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["high-perf-reqd", "none"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "lldp": MoPropertyMeta("lldp", "lldp", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|transmit|receive|all),){0,4}(defaultValue|none|transmit|receive|all){0,1}""", [], []),
        "mac_register_mode": MoPropertyMeta("mac_register_mode", "macRegisterMode", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all-host-vlans", "only-native-vlan"], []),
        "max_ports": MoPropertyMeta("max_ports", "maxPorts", "ushort", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-4096"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,31}""", [], []),
        "nw_ctrl_policy_name": MoPropertyMeta("nw_ctrl_policy_name", "nwCtrlPolicyName", "string", VersionMeta.Version102d, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_nw_ctrl_policy_name": MoPropertyMeta("oper_nw_ctrl_policy_name", "operNwCtrlPolicyName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_qos_policy_name": MoPropertyMeta("oper_qos_policy_name", "operQosPolicyName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "org_dn": MoPropertyMeta("org_dn", "orgDn", "string", VersionMeta.Version422d, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "pin_to_group_name": MoPropertyMeta("pin_to_group_name", "pinToGroupName", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["local", "pending-policy", "policy"], []),
        "port_profile_uuid": MoPropertyMeta("port_profile_uuid", "portProfileUuid", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []),
        "primary_vlan_id": MoPropertyMeta("primary_vlan_id", "primaryVlanId", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4093"]),
        "qos_policy_dn": MoPropertyMeta("qos_policy_dn", "qosPolicyDn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "qos_policy_id": MoPropertyMeta("qos_policy_id", "qosPolicyId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none"], ["0-4294967295"]),
        "qos_policy_name": MoPropertyMeta("qos_policy_name", "qosPolicyName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x1000, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "sw_a_border_aggr_port": MoPropertyMeta("sw_a_border_aggr_port", "swABorderAggrPort", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sw_a_border_port": MoPropertyMeta("sw_a_border_port", "swABorderPort", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sw_a_border_slot": MoPropertyMeta("sw_a_border_slot", "swABorderSlot", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sw_b_border_aggr_port": MoPropertyMeta("sw_b_border_aggr_port", "swBBorderAggrPort", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sw_b_border_port": MoPropertyMeta("sw_b_border_port", "swBBorderPort", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sw_b_border_slot": MoPropertyMeta("sw_b_border_slot", "swBBorderSlot", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["regular", "sla-only"], []),
        "uplink_fail_action": MoPropertyMeta("uplink_fail_action", "uplinkFailAction", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["link-down", "warning"], []),
    }

    prop_map = {
        "cdp": "cdp", 
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "cos": "cos", 
        "descr": "descr", 
        "dn": "dn", 
        "forgeMac": "forge_mac", 
        "hostNwIOPerf": "host_nw_io_perf", 
        "intId": "int_id", 
        "lldp": "lldp", 
        "macRegisterMode": "mac_register_mode", 
        "maxPorts": "max_ports", 
        "name": "name", 
        "nwCtrlPolicyName": "nw_ctrl_policy_name", 
        "operNwCtrlPolicyName": "oper_nw_ctrl_policy_name", 
        "operQosPolicyName": "oper_qos_policy_name", 
        "orgDn": "org_dn", 
        "pinToGroupName": "pin_to_group_name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "portProfileUuid": "port_profile_uuid", 
        "primaryVlanId": "primary_vlan_id", 
        "qosPolicyDn": "qos_policy_dn", 
        "qosPolicyId": "qos_policy_id", 
        "qosPolicyName": "qos_policy_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "swABorderAggrPort": "sw_a_border_aggr_port", 
        "swABorderPort": "sw_a_border_port", 
        "swABorderSlot": "sw_a_border_slot", 
        "swBBorderAggrPort": "sw_b_border_aggr_port", 
        "swBBorderPort": "sw_b_border_port", 
        "swBBorderSlot": "sw_b_border_slot", 
        "type": "type", 
        "uplinkFailAction": "uplink_fail_action", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.cdp = None
        self.child_action = None
        self.config_qualifier = None
        self.cos = None
        self.descr = None
        self.forge_mac = None
        self.host_nw_io_perf = None
        self.int_id = None
        self.lldp = None
        self.mac_register_mode = None
        self.max_ports = None
        self.nw_ctrl_policy_name = None
        self.oper_nw_ctrl_policy_name = None
        self.oper_qos_policy_name = None
        self.org_dn = None
        self.pin_to_group_name = None
        self.policy_level = None
        self.policy_owner = None
        self.port_profile_uuid = None
        self.primary_vlan_id = None
        self.qos_policy_dn = None
        self.qos_policy_id = None
        self.qos_policy_name = None
        self.sacl = None
        self.status = None
        self.sw_a_border_aggr_port = None
        self.sw_a_border_port = None
        self.sw_a_border_slot = None
        self.sw_b_border_aggr_port = None
        self.sw_b_border_port = None
        self.sw_b_border_slot = None
        self.type = None
        self.uplink_fail_action = None

        ManagedObject.__init__(self, "VnicProfile", parent_mo_or_dn, **kwargs)
