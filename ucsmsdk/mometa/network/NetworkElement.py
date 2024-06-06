"""This module contains the general information for NetworkElement ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class NetworkElementConsts:
    ADMIN_EVAC_STATE_DRAIN = "drain"
    ADMIN_EVAC_STATE_FILL = "fill"
    ADMIN_EVAC_STATE_UNKNOWN = "unknown"
    ADMIN_INBAND_IF_STATE_DISABLE = "disable"
    ADMIN_INBAND_IF_STATE_ENABLE = "enable"
    FORCE_EVAC_FALSE = "false"
    FORCE_EVAC_NO = "no"
    FORCE_EVAC_TRUE = "true"
    FORCE_EVAC_YES = "yes"
    ID_A = "A"
    ID_B = "B"
    ID_NONE = "NONE"
    OPER_EVAC_STATE_DRAIN = "drain"
    OPER_EVAC_STATE_FILL = "fill"
    OPER_EVAC_STATE_UNKNOWN = "unknown"
    OPERABILITY_DEPRECATED = "deprecated"
    OPERABILITY_INOPERABLE = "inoperable"
    OPERABILITY_OPERABLE = "operable"
    OPERABILITY_REMOVED = "removed"
    OPERABILITY_UNKNOWN = "unknown"
    SHUTDOWN_FAN_REMOVEAL_FALSE = "false"
    SHUTDOWN_FAN_REMOVEAL_NO = "no"
    SHUTDOWN_FAN_REMOVEAL_TRUE = "true"
    SHUTDOWN_FAN_REMOVEAL_YES = "yes"
    THERMAL_LOWER_CRITICAL = "lower-critical"
    THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    THERMAL_NOT_SUPPORTED = "not-supported"
    THERMAL_OK = "ok"
    THERMAL_UNKNOWN = "unknown"
    THERMAL_UPPER_CRITICAL = "upper-critical"
    THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"


class NetworkElement(ManagedObject):
    """This is NetworkElement class."""

    consts = NetworkElementConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("NetworkElement", "networkElement", "switch-[id]", VersionMeta.Version101e, "InputOutput", 0x7ff, [], ["admin", "ext-lan-config"], ['topSystem'], ['equipmentFan', 'equipmentFanModule', 'equipmentLocatorLed', 'equipmentPsu', 'equipmentSwitchCard', 'extmgmtIf', 'faultInst', 'fcpoolOuis', 'firmwareSecureFPGA', 'firmwareStatus', 'mgmtController', 'mgmtDbState', 'mgmtHealthStatus', 'mgmtIPv6IfConfig', 'networkLanNeighbors', 'networkLimit', 'networkLldpNeighbors', 'networkOperLevel', 'networkSanNeighbors', 'nfsMountInst', 'powerBudget', 'storageItem', 'swAccessDomain', 'swCardEnvStats', 'swEnvStats', 'swEthLanBorder', 'swEthLanFlowMon', 'swEthLanMon', 'swExtUtility', 'swFabricZoneNs', 'swFcSanBorder', 'swFcSanMon', 'swPhys', 'swPortDiscover', 'swRMonEp', 'swSystemStats', 'swUtilityDomain', 'swVlanPortNs'], ["Get", "Set"])

    prop_meta = {
        "admin_evac_state": MoPropertyMeta("admin_evac_state", "adminEvacState", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["drain", "fill", "unknown"], []),
        "admin_inband_if_state": MoPropertyMeta("admin_inband_if_state", "adminInbandIfState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disable", "enable"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "diff_memory": MoPropertyMeta("diff_memory", "diffMemory", "uint", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "expected_memory": MoPropertyMeta("expected_memory", "expectedMemory", "uint", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "force_evac": MoPropertyMeta("force_evac", "forceEvac", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, None, None, None, ["A", "B", "NONE"], []),
        "inband_if_gw": MoPropertyMeta("inband_if_gw", "inbandIfGw", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "inband_if_ip": MoPropertyMeta("inband_if_ip", "inbandIfIp", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "inband_if_mask": MoPropertyMeta("inband_if_mask", "inbandIfMask", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "inband_if_vnet": MoPropertyMeta("inband_if_vnet", "inbandIfVnet", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4090"]),
        "inventory_status": MoPropertyMeta("inventory_status", "inventoryStatus", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|up|remote-eth-port-inventory|fc-pc-inventory|fc-port-inventory|switch-fru|vlan-comp-grp-inventory|switch-inventory|vlan-port-count|mgmt-port-inventory|macsec-state-inventory|card-inventory|xcvr-inventory|eth-pc-inventory|eth-port-inventory),){0,14}(defaultValue|up|remote-eth-port-inventory|fc-pc-inventory|fc-port-inventory|switch-fru|vlan-comp-grp-inventory|switch-inventory|vlan-port-count|mgmt-port-inventory|macsec-state-inventory|card-inventory|xcvr-inventory|eth-pc-inventory|eth-port-inventory){0,1}""", [], []),
        "licensing_msg": MoPropertyMeta("licensing_msg", "licensingMsg", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "min_active_fan": MoPropertyMeta("min_active_fan", "minActiveFan", "ushort", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "oob_if_gw": MoPropertyMeta("oob_if_gw", "oobIfGw", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "oob_if_ip": MoPropertyMeta("oob_if_ip", "oobIfIp", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "oob_if_mac": MoPropertyMeta("oob_if_mac", "oobIfMac", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "oob_if_mask": MoPropertyMeta("oob_if_mask", "oobIfMask", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "oper_evac_state": MoPropertyMeta("oper_evac_state", "operEvacState", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["drain", "fill", "unknown"], []),
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deprecated", "inoperable", "operable", "removed", "unknown"], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "shutdown_fan_removeal": MoPropertyMeta("shutdown_fan_removeal", "shutdownFanRemoveal", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "total_memory": MoPropertyMeta("total_memory", "totalMemory", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "adminEvacState": "admin_evac_state", 
        "adminInbandIfState": "admin_inband_if_state", 
        "childAction": "child_action", 
        "diffMemory": "diff_memory", 
        "dn": "dn", 
        "expectedMemory": "expected_memory", 
        "fltAggr": "flt_aggr", 
        "forceEvac": "force_evac", 
        "id": "id", 
        "inbandIfGw": "inband_if_gw", 
        "inbandIfIp": "inband_if_ip", 
        "inbandIfMask": "inband_if_mask", 
        "inbandIfVnet": "inband_if_vnet", 
        "inventoryStatus": "inventory_status", 
        "licensingMsg": "licensing_msg", 
        "minActiveFan": "min_active_fan", 
        "model": "model", 
        "oobIfGw": "oob_if_gw", 
        "oobIfIp": "oob_if_ip", 
        "oobIfMac": "oob_if_mac", 
        "oobIfMask": "oob_if_mask", 
        "operEvacState": "oper_evac_state", 
        "operability": "operability", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "shutdownFanRemoveal": "shutdown_fan_removeal", 
        "status": "status", 
        "thermal": "thermal", 
        "totalMemory": "total_memory", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_evac_state = None
        self.admin_inband_if_state = None
        self.child_action = None
        self.diff_memory = None
        self.expected_memory = None
        self.flt_aggr = None
        self.force_evac = None
        self.inband_if_gw = None
        self.inband_if_ip = None
        self.inband_if_mask = None
        self.inband_if_vnet = None
        self.inventory_status = None
        self.licensing_msg = None
        self.min_active_fan = None
        self.model = None
        self.oob_if_gw = None
        self.oob_if_ip = None
        self.oob_if_mac = None
        self.oob_if_mask = None
        self.oper_evac_state = None
        self.operability = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.shutdown_fan_removeal = None
        self.status = None
        self.thermal = None
        self.total_memory = None
        self.vendor = None

        ManagedObject.__init__(self, "NetworkElement", parent_mo_or_dn, **kwargs)
