"""This module contains the general information for ComputeBladeEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeBladeEpConsts:
    ADMIN_STATE_IN_MAINTENANCE = "in-maintenance"
    ADMIN_STATE_IN_SERVICE = "in-service"
    ADMIN_STATE_OUT_OF_SERVICE = "out-of-service"
    CHASSIS_ID_N_A = "N/A"
    OPER_STATE_BIOS_PASSWORD_RESET = "bios-password-reset"
    OPER_STATE_BIOS_RESTORE = "bios-restore"
    OPER_STATE_CLEAR_TPM = "clear-tpm"
    OPER_STATE_CMOS_RESET = "cmos-reset"
    OPER_STATE_COMPUTE_FAILED = "compute-failed"
    OPER_STATE_COMPUTE_MISMATCH = "compute-mismatch"
    OPER_STATE_CONFIG = "config"
    OPER_STATE_CONFIG_FAILURE = "config-failure"
    OPER_STATE_DATA_SANITIZE = "data-sanitize"
    OPER_STATE_DATA_SANITIZE_FAILED = "data-sanitize-failed"
    OPER_STATE_DECOMISSIONING = "decomissioning"
    OPER_STATE_DEGRADED = "degraded"
    OPER_STATE_DIAGNOSTICS = "diagnostics"
    OPER_STATE_DIAGNOSTICS_FAILED = "diagnostics-failed"
    OPER_STATE_DISABLED = "disabled"
    OPER_STATE_DISCOVERY = "discovery"
    OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    OPER_STATE_INACCESSIBLE = "inaccessible"
    OPER_STATE_INDETERMINATE = "indeterminate"
    OPER_STATE_INOPERABLE = "inoperable"
    OPER_STATE_MAINTENANCE = "maintenance"
    OPER_STATE_MAINTENANCE_FAILED = "maintenance-failed"
    OPER_STATE_OK = "ok"
    OPER_STATE_PENDING_REASSOCIATION = "pending-reassociation"
    OPER_STATE_PENDING_REBOOT = "pending-reboot"
    OPER_STATE_POWER_OFF = "power-off"
    OPER_STATE_POWER_PROBLEM = "power-problem"
    OPER_STATE_REMOVED = "removed"
    OPER_STATE_RESTART = "restart"
    OPER_STATE_SVNIC_NOT_PRESENT = "svnic-not-present"
    OPER_STATE_TEST = "test"
    OPER_STATE_TEST_FAILED = "test-failed"
    OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    OPER_STATE_UNASSOCIATED = "unassociated"
    OPER_STATE_UNCONFIG = "unconfig"
    OPER_STATE_UNCONFIG_FAILED = "unconfig-failed"
    OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
    PEER_PRESENCE_EMPTY = "empty"
    PEER_PRESENCE_EQUIPPED = "equipped"
    PEER_PRESENCE_EQUIPPED_DEPRECATED = "equipped-deprecated"
    PEER_PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    PEER_PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    PEER_PRESENCE_EQUIPPED_SLAVE = "equipped-slave"
    PEER_PRESENCE_EQUIPPED_UNSUPPORTED = "equipped-unsupported"
    PEER_PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    PEER_PRESENCE_INACCESSIBLE = "inaccessible"
    PEER_PRESENCE_MISMATCH = "mismatch"
    PEER_PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    PEER_PRESENCE_MISMATCH_SLAVE = "mismatch-slave"
    PEER_PRESENCE_MISSING = "missing"
    PEER_PRESENCE_MISSING_SLAVE = "missing-slave"
    PEER_PRESENCE_UNAUTHORIZED = "unauthorized"
    PEER_PRESENCE_UNKNOWN = "unknown"
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
    PRESENCE_EQUIPPED_DEPRECATED = "equipped-deprecated"
    PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    PRESENCE_EQUIPPED_SLAVE = "equipped-slave"
    PRESENCE_EQUIPPED_UNSUPPORTED = "equipped-unsupported"
    PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    PRESENCE_INACCESSIBLE = "inaccessible"
    PRESENCE_MISMATCH = "mismatch"
    PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    PRESENCE_MISMATCH_SLAVE = "mismatch-slave"
    PRESENCE_MISSING = "missing"
    PRESENCE_MISSING_SLAVE = "missing-slave"
    PRESENCE_UNAUTHORIZED = "unauthorized"
    PRESENCE_UNKNOWN = "unknown"


class ComputeBladeEp(ManagedObject):
    """This is ComputeBladeEp class."""

    consts = ComputeBladeEpConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ComputeBladeEp", "computeBladeEp", "blade-ep-[id]", VersionMeta.Version302c, "InputOutput", 0x3f, [], ["read-only"], [], [], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["in-maintenance", "in-service", "out-of-service"], []),
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-2"]),
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["bios-password-reset", "bios-restore", "clear-tpm", "cmos-reset", "compute-failed", "compute-mismatch", "config", "config-failure", "data-sanitize", "data-sanitize-failed", "decomissioning", "degraded", "diagnostics", "diagnostics-failed", "disabled", "discovery", "discovery-failed", "inaccessible", "indeterminate", "inoperable", "maintenance", "maintenance-failed", "ok", "pending-reassociation", "pending-reboot", "power-off", "power-problem", "removed", "restart", "svnic-not-present", "test", "test-failed", "thermal-problem", "unassociated", "unconfig", "unconfig-failed", "voltage-problem"], []),
        "peer_presence": MoPropertyMeta("peer_presence", "peerPresence", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "unauthorized", "unknown"], []),
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "unauthorized", "unknown"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-8"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "id": "id", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "peerPresence": "peer_presence", 
        "presence": "presence", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotId": "slot_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_state = None
        self.chassis_id = None
        self.child_action = None
        self.ep_dn = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.peer_presence = None
        self.presence = None
        self.sacl = None
        self.slot_id = None
        self.status = None

        ManagedObject.__init__(self, "ComputeBladeEp", parent_mo_or_dn, **kwargs)
