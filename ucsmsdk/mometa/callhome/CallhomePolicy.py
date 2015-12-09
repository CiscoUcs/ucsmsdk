"""This module contains the general information for CallhomePolicy ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class CallhomePolicyConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    CAUSE_ADAPTOR_MISMATCH = "adaptor-mismatch"
    CAUSE_ADMIN_STATE_OFFLINE = "admin-state-offline"
    CAUSE_ARP_TARGETS_CONFIG_ERROR = "arp-targets-config-error"
    CAUSE_ASSOCIATION_FAILED = "association-failed"
    CAUSE_CAPACITY_PROBLEM = "capacity-problem"
    CAUSE_CIMC_BACKUP_TRIGGER_NOT_ENABLED = "cimc-backup-trigger-not-enabled"
    CAUSE_CIMC_HEARTBEAT_TIMED_OUT = "cimc-heartbeat-timed-out"
    CAUSE_CONFIGURATION_FAILURE = "configuration-failure"
    CAUSE_CONFIGURATION_MISMATCH = "configuration-mismatch"
    CAUSE_CONNECTIVITY_PROBLEM = "connectivity-problem"
    CAUSE_ELECTION_FAILURE = "election-failure"
    CAUSE_EQUIPMENT_DEGRADED = "equipment-degraded"
    CAUSE_EQUIPMENT_DEPRECATED = "equipment-deprecated"
    CAUSE_EQUIPMENT_DISABLED = "equipment-disabled"
    CAUSE_EQUIPMENT_INACCESSIBLE = "equipment-inaccessible"
    CAUSE_EQUIPMENT_INOPERABLE = "equipment-inoperable"
    CAUSE_EQUIPMENT_MISSING = "equipment-missing"
    CAUSE_EQUIPMENT_OFFLINE = "equipment-offline"
    CAUSE_EQUIPMENT_PROBLEM = "equipment-problem"
    CAUSE_EQUIPMENT_REMOVED = "equipment-removed"
    CAUSE_FAN_REMOVAL = "fan-removal"
    CAUSE_FRU_PROBLEM = "fru-problem"
    CAUSE_HEALTH_CRITICAL = "health-critical"
    CAUSE_HEALTH_LED_AMBER = "health-led-amber"
    CAUSE_HEALTH_LED_AMBER_BLINKING = "health-led-amber-blinking"
    CAUSE_HEALTH_MAJOR = "health-major"
    CAUSE_HEALTH_PROBLEM = "health-problem"
    CAUSE_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    CAUSE_INVALID_CONTROLLER_PROFILE_COUNT = "invalid-controller-profile-count"
    CAUSE_INVENTORY_FAILED = "inventory-failed"
    CAUSE_KERNEL_MEM_CRITICAL_THRESHOLD = "kernel-mem-critical-threshold"
    CAUSE_LICENSE_GRACEPERIOD_EXPIRED = "license-graceperiod-expired"
    CAUSE_LIMIT_REACHED = "limit-reached"
    CAUSE_LINK_DOWN = "link-down"
    CAUSE_MANAGEMENT_SERVICES_FAILURE = "management-services-failure"
    CAUSE_MANAGEMENT_SERVICES_UNRESPONSIVE = "management-services-unresponsive"
    CAUSE_MEMORY_ERROR = "memory-error"
    CAUSE_MGMTIF_DOWN = "mgmtif-down"
    CAUSE_NDISC_TARGETS_CONFIG_ERROR = "ndisc-targets-config-error"
    CAUSE_NEAR_MAX_LIMIT = "near-max-limit"
    CAUSE_NO_VOLUME_SPACE = "no-volume-space"
    CAUSE_NOT_SUPPORTED = "not-supported"
    CAUSE_PORT_FAILED = "port-failed"
    CAUSE_POWER_PROBLEM = "power-problem"
    CAUSE_PSU_INSUFFICIENT = "psu-insufficient"
    CAUSE_PSU_MIXED_MODE = "psu-mixed-mode"
    CAUSE_RAIDGROUP_BAD = "raidgroup-bad"
    CAUSE_RAIDGROUP_DEGRADED = "raidgroup-degraded"
    CAUSE_RAIDGROUP_OFFLINE = "raidgroup-offline"
    CAUSE_RAIDGROUP_REBUILDING = "raidgroup-rebuilding"
    CAUSE_SMALL_VOLUME_SPACE = "small-volume-space"
    CAUSE_THERMAL_PROBLEM = "thermal-problem"
    CAUSE_UNSPECIFIED = "unspecified"
    CAUSE_VERSION_INCOMPATIBLE = "version-incompatible"
    CAUSE_VIF_IDS_MISMATCH = "vif-ids-mismatch"
    CAUSE_VOLTAGE_PROBLEM = "voltage-problem"


class CallhomePolicy(ManagedObject):
    """This is CallhomePolicy class."""

    consts = CallhomePolicyConsts()
    naming_props = set([u'cause'])

    mo_meta = MoMeta("CallhomePolicy", "callhomePolicy", "policy-[cause]", VersionMeta.Version101e, "InputOutput", 0x1ffL, [], ["admin", "fault"], [u'callhomeEp'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["disabled", "enabled"], []), 
        "cause": MoPropertyMeta("cause", "cause", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x4L, None, None, None, ["adaptor-mismatch", "admin-state-offline", "arp-targets-config-error", "association-failed", "capacity-problem", "cimc-backup-trigger-not-enabled", "cimc-heartbeat-timed-out", "configuration-failure", "configuration-mismatch", "connectivity-problem", "election-failure", "equipment-degraded", "equipment-deprecated", "equipment-disabled", "equipment-inaccessible", "equipment-inoperable", "equipment-missing", "equipment-offline", "equipment-problem", "equipment-removed", "fan-removal", "fru-problem", "health-critical", "health-led-amber", "health-led-amber-blinking", "health-major", "health-problem", "identity-unestablishable", "invalid-controller-profile-count", "inventory-failed", "kernel-mem-critical-threshold", "license-graceperiod-expired", "limit-reached", "link-down", "management-services-failure", "management-services-unresponsive", "memory-error", "mgmtif-down", "ndisc-targets-config-error", "near-max-limit", "no-volume-space", "not-supported", "port-failed", "power-problem", "psu-insufficient", "psu-mixed-mode", "raidgroup-bad", "raidgroup-degraded", "raidgroup-offline", "raidgroup-rebuilding", "small-volume-space", "thermal-problem", "unspecified", "version-incompatible", "vif-ids-mismatch", "voltage-problem"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x8L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
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

