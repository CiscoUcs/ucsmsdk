"""This module contains the general information for EquipmentSwitchCap ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentSwitchCapConsts():
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


class EquipmentSwitchCap(ManagedObject):
    """This is EquipmentSwitchCap class."""

    consts = EquipmentSwitchCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentSwitchCap", "equipmentSwitchCap", "switch-cap", VersionMeta.Version111j, "InputOutput", 0x7fL, [], [""], [u'equipmentSwitchCapProvider', u'equipmentSwitchIOCardCapProvider'], [u'equipmentPortCap'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "fan_modules_supported": MoPropertyMeta("fan_modules_supported", "fanModulesSupported", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "locator_beacon_supported": MoPropertyMeta("locator_beacon_supported", "locatorBeaconSupported", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "max_active_span_session_count": MoPropertyMeta("max_active_span_session_count", "maxActiveSpanSessionCount", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "max_eth1g_port": MoPropertyMeta("max_eth1g_port", "maxEth1gPort", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "max_eth1g_slot": MoPropertyMeta("max_eth1g_slot", "maxEth1gSlot", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "max_eth_pc_members": MoPropertyMeta("max_eth_pc_members", "maxEthPcMembers", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "max_eth_pcs": MoPropertyMeta("max_eth_pcs", "maxEthPcs", "uint", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "max_fcoe_pc_members": MoPropertyMeta("max_fcoe_pc_members", "maxFcoePcMembers", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "max_uplink_ports": MoPropertyMeta("max_uplink_ports", "maxUplinkPorts", "uint", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mgmt_daughter_card_slot_id": MoPropertyMeta("mgmt_daughter_card_slot_id", "mgmtDaughterCardSlotId", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "sereno_netflow_supported": MoPropertyMeta("sereno_netflow_supported", "serenoNetflowSupported", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "fanModulesSupported": "fan_modules_supported", 
        "intId": "int_id", 
        "locatorBeaconSupported": "locator_beacon_supported", 
        "maxActiveSpanSessionCount": "max_active_span_session_count", 
        "maxEth1gPort": "max_eth1g_port", 
        "maxEth1gSlot": "max_eth1g_slot", 
        "maxEthPcMembers": "max_eth_pc_members", 
        "maxEthPcs": "max_eth_pcs", 
        "maxFcoePcMembers": "max_fcoe_pc_members", 
        "maxUplinkPorts": "max_uplink_ports", 
        "mgmtDaughterCardSlotId": "mgmt_daughter_card_slot_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serenoNetflowSupported": "sereno_netflow_supported", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.fan_modules_supported = None
        self.int_id = None
        self.locator_beacon_supported = None
        self.max_active_span_session_count = None
        self.max_eth1g_port = None
        self.max_eth1g_slot = None
        self.max_eth_pc_members = None
        self.max_eth_pcs = None
        self.max_fcoe_pc_members = None
        self.max_uplink_ports = None
        self.mgmt_daughter_card_slot_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.sereno_netflow_supported = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentSwitchCap", parent_mo_or_dn, **kwargs)

