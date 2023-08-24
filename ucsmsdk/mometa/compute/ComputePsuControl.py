"""This module contains the general information for ComputePsuControl ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePsuControlConsts:
    CLUSTER_STATE_N_A = "N/A"
    CLUSTER_STATE_NOT_CLUSTERED = "not-clustered"
    CLUSTER_STATE_SLOT_1_MASTER = "slot-1-master"
    CLUSTER_STATE_SLOT_2_MASTER = "slot-2-master"
    CLUSTER_STATE_UNKNOWN = "unknown"
    EXTENDED_MODE_DISABLE = "Disable"
    EXTENDED_MODE_ENABLE = "Enable"
    INPUT_POWER_STATE_LOWER_CRITICAL = "lower-critical"
    INPUT_POWER_STATE_LOWER_NON_CRITICAL = "lower-non-critical"
    INPUT_POWER_STATE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    INPUT_POWER_STATE_NOT_SUPPORTED = "not-supported"
    INPUT_POWER_STATE_OK = "ok"
    INPUT_POWER_STATE_UNKNOWN = "unknown"
    INPUT_POWER_STATE_UPPER_CRITICAL = "upper-critical"
    INPUT_POWER_STATE_UPPER_NON_CRITICAL = "upper-non-critical"
    INPUT_POWER_STATE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    INT_ID_NONE = "none"
    MODE_DISABLE = "Disable"
    MODE_ENABLE = "Enable"
    OPER_STATE_DEGRADED = "degraded"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_OK = "ok"
    OPER_STATE_UNKNOWN = "unknown"
    OUTPUT_POWER_STATE_LOWER_CRITICAL = "lower-critical"
    OUTPUT_POWER_STATE_LOWER_NON_CRITICAL = "lower-non-critical"
    OUTPUT_POWER_STATE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    OUTPUT_POWER_STATE_NOT_SUPPORTED = "not-supported"
    OUTPUT_POWER_STATE_OK = "ok"
    OUTPUT_POWER_STATE_UNKNOWN = "unknown"
    OUTPUT_POWER_STATE_UPPER_CRITICAL = "upper-critical"
    OUTPUT_POWER_STATE_UPPER_NON_CRITICAL = "upper-non-critical"
    OUTPUT_POWER_STATE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    REDUNDANCY_GRID = "grid"
    REDUNDANCY_N_1 = "n+1"
    REDUNDANCY_N_2 = "n+2"
    REDUNDANCY_NON_REDUNDANT = "non-redundant"
    REDUNDANCY_UNKNOWN = "unknown"


class ComputePsuControl(ManagedObject):
    """This is ComputePsuControl class."""

    consts = ComputePsuControlConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputePsuControl", "computePsuControl", "psu-contr", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["read-only"], ['equipmentChassis'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cluster_state": MoPropertyMeta("cluster_state", "clusterState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A", "not-clustered", "slot-1-master", "slot-2-master", "unknown"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "extended_mode": MoPropertyMeta("extended_mode", "extendedMode", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disable", "Enable"], []),
        "input_power_state": MoPropertyMeta("input_power_state", "inputPowerState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disable", "Enable"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_qualifier": MoPropertyMeta("oper_qualifier", "operQualifier", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|ok|redundancy-lost|redundancy-degraded|non-redundant-sufficient-resources|non-redundant-insufficient-resources),){0,5}(defaultValue|ok|redundancy-lost|redundancy-degraded|non-redundant-sufficient-resources|non-redundant-insufficient-resources){0,1}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "failed", "ok", "unknown"], []),
        "output_power_state": MoPropertyMeta("output_power_state", "outputPowerState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["local", "pending-policy", "policy"], []),
        "redundancy": MoPropertyMeta("redundancy", "redundancy", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["grid", "n+1", "n+2", "non-redundant", "unknown"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "clusterState": "cluster_state", 
        "descr": "descr", 
        "dn": "dn", 
        "extendedMode": "extended_mode", 
        "inputPowerState": "input_power_state", 
        "intId": "int_id", 
        "mode": "mode", 
        "name": "name", 
        "operQualifier": "oper_qualifier", 
        "operState": "oper_state", 
        "outputPowerState": "output_power_state", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "redundancy": "redundancy", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.cluster_state = None
        self.descr = None
        self.extended_mode = None
        self.input_power_state = None
        self.int_id = None
        self.mode = None
        self.name = None
        self.oper_qualifier = None
        self.oper_state = None
        self.output_power_state = None
        self.policy_level = None
        self.policy_owner = None
        self.redundancy = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputePsuControl", parent_mo_or_dn, **kwargs)
