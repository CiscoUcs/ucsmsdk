"""This module contains the general information for EquipmentSwitchCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentSwitchCapConsts:
    DYNAMIC_VIFS_SUPPORTED_FALSE = "false"
    DYNAMIC_VIFS_SUPPORTED_NO = "no"
    DYNAMIC_VIFS_SUPPORTED_TRUE = "true"
    DYNAMIC_VIFS_SUPPORTED_YES = "yes"
    FAN_MODULES_SUPPORTED_FALSE = "false"
    FAN_MODULES_SUPPORTED_NO = "no"
    FAN_MODULES_SUPPORTED_TRUE = "true"
    FAN_MODULES_SUPPORTED_YES = "yes"
    INT_ID_NONE = "none"
    LOCATOR_BEACON_SUPPORTED_FALSE = "false"
    LOCATOR_BEACON_SUPPORTED_NO = "no"
    LOCATOR_BEACON_SUPPORTED_TRUE = "true"
    LOCATOR_BEACON_SUPPORTED_YES = "yes"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SERENO_NETFLOW_SUPPORTED_FALSE = "false"
    SERENO_NETFLOW_SUPPORTED_NO = "no"
    SERENO_NETFLOW_SUPPORTED_TRUE = "true"
    SERENO_NETFLOW_SUPPORTED_YES = "yes"
    VP_COMPRESSION_SUPPORTED_FALSE = "false"
    VP_COMPRESSION_SUPPORTED_NO = "no"
    VP_COMPRESSION_SUPPORTED_TRUE = "true"
    VP_COMPRESSION_SUPPORTED_YES = "yes"


class EquipmentSwitchCap(ManagedObject):
    """This is EquipmentSwitchCap class."""

    consts = EquipmentSwitchCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentSwitchCap", "equipmentSwitchCap", "switch-cap", VersionMeta.Version111j, "InputOutput", 0xff, [], [""], ['equipmentSwitchCapProvider', 'equipmentSwitchIOCardCapProvider'], ['equipmentPortCap'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "dynamic_vifs_supported": MoPropertyMeta("dynamic_vifs_supported", "dynamicVifsSupported", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "fan_modules_supported": MoPropertyMeta("fan_modules_supported", "fanModulesSupported", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "locator_beacon_supported": MoPropertyMeta("locator_beacon_supported", "locatorBeaconSupported", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "max_active_span_session_count": MoPropertyMeta("max_active_span_session_count", "maxActiveSpanSessionCount", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "max_eth1g_port": MoPropertyMeta("max_eth1g_port", "maxEth1gPort", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "max_eth1g_slot": MoPropertyMeta("max_eth1g_slot", "maxEth1gSlot", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "max_eth_pc_members": MoPropertyMeta("max_eth_pc_members", "maxEthPcMembers", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "max_eth_pcs": MoPropertyMeta("max_eth_pcs", "maxEthPcs", "uint", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "max_fc_pcs": MoPropertyMeta("max_fc_pcs", "maxFcPcs", "uint", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "max_fcoe_pc_members": MoPropertyMeta("max_fcoe_pc_members", "maxFcoePcMembers", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "max_port_id": MoPropertyMeta("max_port_id", "maxPortId", "uint", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "max_slot": MoPropertyMeta("max_slot", "maxSlot", "uint", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "max_uplink_ports": MoPropertyMeta("max_uplink_ports", "maxUplinkPorts", "uint", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mgmt_daughter_card_slot_id": MoPropertyMeta("mgmt_daughter_card_slot_id", "mgmtDaughterCardSlotId", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "min_active_fan": MoPropertyMeta("min_active_fan", "minActiveFan", "ushort", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sereno_netflow_supported": MoPropertyMeta("sereno_netflow_supported", "serenoNetflowSupported", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vp_compression_supported": MoPropertyMeta("vp_compression_supported", "vpCompressionSupported", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "dynamicVifsSupported": "dynamic_vifs_supported", 
        "fanModulesSupported": "fan_modules_supported", 
        "intId": "int_id", 
        "locatorBeaconSupported": "locator_beacon_supported", 
        "maxActiveSpanSessionCount": "max_active_span_session_count", 
        "maxEth1gPort": "max_eth1g_port", 
        "maxEth1gSlot": "max_eth1g_slot", 
        "maxEthPcMembers": "max_eth_pc_members", 
        "maxEthPcs": "max_eth_pcs", 
        "maxFcPcs": "max_fc_pcs", 
        "maxFcoePcMembers": "max_fcoe_pc_members", 
        "maxPortId": "max_port_id", 
        "maxSlot": "max_slot", 
        "maxUplinkPorts": "max_uplink_ports", 
        "mgmtDaughterCardSlotId": "mgmt_daughter_card_slot_id", 
        "minActiveFan": "min_active_fan", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serenoNetflowSupported": "sereno_netflow_supported", 
        "status": "status", 
        "vpCompressionSupported": "vp_compression_supported", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.dynamic_vifs_supported = None
        self.fan_modules_supported = None
        self.int_id = None
        self.locator_beacon_supported = None
        self.max_active_span_session_count = None
        self.max_eth1g_port = None
        self.max_eth1g_slot = None
        self.max_eth_pc_members = None
        self.max_eth_pcs = None
        self.max_fc_pcs = None
        self.max_fcoe_pc_members = None
        self.max_port_id = None
        self.max_slot = None
        self.max_uplink_ports = None
        self.mgmt_daughter_card_slot_id = None
        self.min_active_fan = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.sereno_netflow_supported = None
        self.status = None
        self.vp_compression_supported = None

        ManagedObject.__init__(self, "EquipmentSwitchCap", parent_mo_or_dn, **kwargs)
