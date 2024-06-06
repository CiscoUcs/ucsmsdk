"""This module contains the general information for CallhomePolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CallhomePolicyConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    CAUSE_ADAPTOR_MISMATCH = "adaptor-mismatch"
    CAUSE_ARP_TARGETS_CONFIG_ERROR = "arp-targets-config-error"
    CAUSE_ASSOCIATION_FAILED = "association-failed"
    CAUSE_BACKPLANE_PORT_PROBLEM = "backplane-port-problem"
    CAUSE_CHASSIS_INTRUSION = "chassis-intrusion"
    CAUSE_CONFIG_MISMATCH = "config-mismatch"
    CAUSE_CONFIG_PROBLEM = "config-problem"
    CAUSE_CONFIGURATION_ERROR = "configuration-error"
    CAUSE_CONFIGURATION_FAILURE = "configuration-failure"
    CAUSE_CONFIGURATION_MISMATCH = "configuration-mismatch"
    CAUSE_CONNECTIVITY_PROBLEM = "connectivity-problem"
    CAUSE_ELECTION_FAILURE = "election-failure"
    CAUSE_EQUIPMENT_DEGRADED = "equipment-degraded"
    CAUSE_EQUIPMENT_DEPRECATED = "equipment-deprecated"
    CAUSE_EQUIPMENT_DIMM_DISABLED = "equipment-dimm-disabled"
    CAUSE_EQUIPMENT_DISABLED = "equipment-disabled"
    CAUSE_EQUIPMENT_INACCESSIBLE = "equipment-inaccessible"
    CAUSE_EQUIPMENT_INOPERABLE = "equipment-inoperable"
    CAUSE_EQUIPMENT_MISSING = "equipment-missing"
    CAUSE_EQUIPMENT_NON_OPTIMAL = "equipment-non-optimal"
    CAUSE_EQUIPMENT_OFFLINE = "equipment-offline"
    CAUSE_EQUIPMENT_PEER_DIMM_DISABLED = "equipment-peer-dimm-disabled"
    CAUSE_EQUIPMENT_PROBLEM = "equipment-problem"
    CAUSE_EQUIPMENT_REMOVED = "equipment-removed"
    CAUSE_EQUIPMENT_SELFTESTFAILED = "equipment-selftestfailed"
    CAUSE_EQUIPMENT_UNACKNOWLEDGED = "equipment-unacknowledged"
    CAUSE_EQUIPMENT_UNHEALTHY = "equipment-unhealthy"
    CAUSE_FABRIC_EVACUATED = "fabric-evacuated"
    CAUSE_FAN_REMOVAL = "fan-removal"
    CAUSE_FRU_PROBLEM = "fru-problem"
    CAUSE_HARDWARE_INVENTORY_MISMATCH = "hardware-inventory-mismatch"
    CAUSE_HARDWARE_MISMATCH = "hardware-mismatch"
    CAUSE_HEALTH_CRITICAL = "health-critical"
    CAUSE_HEALTH_LED_AMBER = "health-led-amber"
    CAUSE_HEALTH_LED_AMBER_BLINKING = "health-led-amber-blinking"
    CAUSE_HEALTH_MAJOR = "health-major"
    CAUSE_HEALTH_MINOR = "health-minor"
    CAUSE_HEALTH_WARNING = "health-warning"
    CAUSE_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    CAUSE_IMAGE_UNUSABLE = "image-unusable"
    CAUSE_INOPERABLE = "inoperable"
    CAUSE_INVENTORY_FAILED = "inventory-failed"
    CAUSE_KERNEL_MEM_CRITICAL_THRESHOLD = "kernel-mem-critical-threshold"
    CAUSE_LICENSE_GRACEPERIOD_EXPIRED = "license-graceperiod-expired"
    CAUSE_LIMIT_REACHED = "limit-reached"
    CAUSE_LINK_DOWN = "link-down"
    CAUSE_MANAGEMENT_SERVICES_FAILURE = "management-services-failure"
    CAUSE_MANAGEMENT_SERVICES_UNRESPONSIVE = "management-services-unresponsive"
    CAUSE_MEMORY_ERROR = "memory-error"
    CAUSE_MGMT_DB_CORRUPTION = "mgmt-db-corruption"
    CAUSE_MGMTIF_DOWN = "mgmtif-down"
    CAUSE_NDISC_TARGETS_CONFIG_ERROR = "ndisc-targets-config-error"
    CAUSE_NEAR_MAX_LIMIT = "near-max-limit"
    CAUSE_NOT_SUPPORTED = "not-supported"
    CAUSE_PCI_CONFIG_ISSUE = "pci-config-issue"
    CAUSE_PCI_CONFIG_MISMATCH = "pci-config-mismatch"
    CAUSE_PERSISTENT_MEMORY_DETECTION = "persistent-memory-detection"
    CAUSE_PORT_FAILED = "port-failed"
    CAUSE_POWER_PROBLEM = "power-problem"
    CAUSE_PSU_INSUFFICIENT = "psu-insufficient"
    CAUSE_PSU_MIXED_MODE = "psu-mixed-mode"
    CAUSE_THERMAL_PROBLEM = "thermal-problem"
    CAUSE_UNSPECIFIED = "unspecified"
    CAUSE_UNSUPPORTED_CONFIG = "unsupported-config"
    CAUSE_UNSUPPORTED_CONTROLLER = "unsupported-controller"
    CAUSE_UPLINK_PORT_CHANNEL_MISCONFIGURED = "uplink-port-channel-misconfigured"
    CAUSE_UPLINK_PORT_TYPE_MISCONFIGURED = "uplink-port-type-misconfigured"
    CAUSE_VERSION_INCOMPATIBLE = "version-incompatible"
    CAUSE_VIF_IDS_MISMATCH = "vif-ids-mismatch"
    CAUSE_VOLTAGE_PROBLEM = "voltage-problem"


class CallhomePolicy(ManagedObject):
    """This is CallhomePolicy class."""

    consts = CallhomePolicyConsts()
    naming_props = set(['cause'])

    mo_meta = MoMeta("CallhomePolicy", "callhomePolicy", "policy-[cause]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["admin", "fault"], ['callhomeEp'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "cause": MoPropertyMeta("cause", "cause", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x4, None, None, None, ["adaptor-mismatch", "arp-targets-config-error", "association-failed", "backplane-port-problem", "chassis-intrusion", "config-mismatch", "config-problem", "configuration-error", "configuration-failure", "configuration-mismatch", "connectivity-problem", "election-failure", "equipment-degraded", "equipment-deprecated", "equipment-dimm-disabled", "equipment-disabled", "equipment-inaccessible", "equipment-inoperable", "equipment-missing", "equipment-non-optimal", "equipment-offline", "equipment-peer-dimm-disabled", "equipment-problem", "equipment-removed", "equipment-selftestfailed", "equipment-unacknowledged", "equipment-unhealthy", "fabric-evacuated", "fan-removal", "fru-problem", "hardware-inventory-mismatch", "hardware-mismatch", "health-critical", "health-led-amber", "health-led-amber-blinking", "health-major", "health-minor", "health-warning", "identity-unestablishable", "image-unusable", "inoperable", "inventory-failed", "kernel-mem-critical-threshold", "license-graceperiod-expired", "limit-reached", "link-down", "management-services-failure", "management-services-unresponsive", "memory-error", "mgmt-db-corruption", "mgmtif-down", "ndisc-targets-config-error", "near-max-limit", "not-supported", "pci-config-issue", "pci-config-mismatch", "persistent-memory-detection", "port-failed", "power-problem", "psu-insufficient", "psu-mixed-mode", "thermal-problem", "unspecified", "unsupported-config", "unsupported-controller", "uplink-port-channel-misconfigured", "uplink-port-type-misconfigured", "version-incompatible", "vif-ids-mismatch", "voltage-problem"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x8, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "cause": "cause", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, cause, **kwargs):
        self._dirty_mask = 0
        self.cause = cause
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "CallhomePolicy", parent_mo_or_dn, **kwargs)
