"""This module contains the general information for LstorageArray ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageArrayConsts():
    ASSIGN_STATE_ASSIGNED = "assigned"
    ASSIGN_STATE_FAILED = "failed"
    ASSIGN_STATE_UNASSIGNED = "unassigned"
    ASSOC_STATE_ASSOCIATED = "associated"
    ASSOC_STATE_ASSOCIATING = "associating"
    ASSOC_STATE_DISASSOCIATING = "disassociating"
    ASSOC_STATE_FAILED = "failed"
    ASSOC_STATE_UNASSOCIATED = "unassociated"
    INT_ID_NONE = "none"
    OPER_STATE_BIOS_RESTORE = "bios-restore"
    OPER_STATE_CMOS_RESET = "cmos-reset"
    OPER_STATE_COMPUTE_FAILED = "compute-failed"
    OPER_STATE_COMPUTE_MISMATCH = "compute-mismatch"
    OPER_STATE_CONFIG = "config"
    OPER_STATE_CONFIG_FAILURE = "config-failure"
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
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    RESOLVE_REMOTE_NO = "no"
    RESOLVE_REMOTE_YES = "yes"
    TYPE_INITIAL_TEMPLATE = "initial-template"
    TYPE_INSTANCE = "instance"
    TYPE_UPDATING_TEMPLATE = "updating-template"


class LstorageArray(ManagedObject):
    """This is LstorageArray class."""

    consts = LstorageArrayConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("LstorageArray", "lstorageArray", "storage-array-[name]", VersionMeta.Version302c, "InputOutput", 0xffffL, [], ["admin", "ls-storage"], [u'orgOrg'], [u'faultInst', u'faultSuppressTask', u'lstorageArrayBinding', u'lstorageExtension', u'lstorageLunReplicationService', u'lstorageProcessor', u'lstorageProcessorBinding', u'lstorageTargetIdentity', u'vnicStorageEthLif'], [None])

    prop_meta = {
        "assign_state": MoPropertyMeta("assign_state", "assignState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["assigned", "failed", "unassigned"], []), 
        "assoc_state": MoPropertyMeta("assoc_state", "assocState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["associated", "associating", "disassociating", "failed", "unassociated"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x4L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "host_fw_policy_name": MoPropertyMeta("host_fw_policy_name", "hostFwPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "id": MoPropertyMeta("id", "id", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "maint_policy_name": MoPropertyMeta("maint_policy_name", "maintPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x40L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []), 
        "oper_host_fw_policy_name": MoPropertyMeta("oper_host_fw_policy_name", "operHostFwPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_maint_policy_name": MoPropertyMeta("oper_maint_policy_name", "operMaintPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_src_templ_name": MoPropertyMeta("oper_src_templ_name", "operSrcTemplName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["bios-restore", "cmos-reset", "compute-failed", "compute-mismatch", "config", "config-failure", "decomissioning", "degraded", "diagnostics", "diagnostics-failed", "disabled", "discovery", "discovery-failed", "inaccessible", "indeterminate", "inoperable", "maintenance", "maintenance-failed", "ok", "pending-reassociation", "pending-reboot", "power-off", "power-problem", "removed", "restart", "svnic-not-present", "test", "test-failed", "thermal-problem", "unassociated", "unconfig", "unconfig-failed", "voltage-problem"], []), 
        "oper_stats_policy_name": MoPropertyMeta("oper_stats_policy_name", "operStatsPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_storage_fw_policy_name": MoPropertyMeta("oper_storage_fw_policy_name", "operStorageFwPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "pn_dn": MoPropertyMeta("pn_dn", "pnDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "processor_count": MoPropertyMeta("processor_count", "processorCount", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "resolve_remote": MoPropertyMeta("resolve_remote", "resolveRemote", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["no", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x200L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "src_templ_name": MoPropertyMeta("src_templ_name", "srcTemplName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, [], []), 
        "stats_policy_name": MoPropertyMeta("stats_policy_name", "statsPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x800L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "storage_fw_policy_name": MoPropertyMeta("storage_fw_policy_name", "storageFwPolicyName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version302c, MoPropertyMeta.CREATE_ONLY, 0x4000L, None, None, None, ["initial-template", "instance", "updating-template"], []), 
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8000L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []), 
    }

    prop_map = {
        "assignState": "assign_state", 
        "assocState": "assoc_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "hostFwPolicyName": "host_fw_policy_name", 
        "id": "id", 
        "intId": "int_id", 
        "maintPolicyName": "maint_policy_name", 
        "name": "name", 
        "operHostFwPolicyName": "oper_host_fw_policy_name", 
        "operMaintPolicyName": "oper_maint_policy_name", 
        "operSrcTemplName": "oper_src_templ_name", 
        "operState": "oper_state", 
        "operStatsPolicyName": "oper_stats_policy_name", 
        "operStorageFwPolicyName": "oper_storage_fw_policy_name", 
        "peerDn": "peer_dn", 
        "pnDn": "pn_dn", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "processorCount": "processor_count", 
        "propAcl": "prop_acl", 
        "resolveRemote": "resolve_remote", 
        "rn": "rn", 
        "sacl": "sacl", 
        "srcTemplName": "src_templ_name", 
        "statsPolicyName": "stats_policy_name", 
        "status": "status", 
        "storageFwPolicyName": "storage_fw_policy_name", 
        "type": "type", 
        "usrLbl": "usr_lbl", 
        "uuid": "uuid", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.assign_state = None
        self.assoc_state = None
        self.child_action = None
        self.descr = None
        self.flt_aggr = None
        self.host_fw_policy_name = None
        self.id = None
        self.int_id = None
        self.maint_policy_name = None
        self.oper_host_fw_policy_name = None
        self.oper_maint_policy_name = None
        self.oper_src_templ_name = None
        self.oper_state = None
        self.oper_stats_policy_name = None
        self.oper_storage_fw_policy_name = None
        self.peer_dn = None
        self.pn_dn = None
        self.policy_level = None
        self.policy_owner = None
        self.processor_count = None
        self.prop_acl = None
        self.resolve_remote = None
        self.sacl = None
        self.src_templ_name = None
        self.stats_policy_name = None
        self.status = None
        self.storage_fw_policy_name = None
        self.type = None
        self.usr_lbl = None
        self.uuid = None

        ManagedObject.__init__(self, "LstorageArray", parent_mo_or_dn, **kwargs)

