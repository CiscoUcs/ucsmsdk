"""This module contains the general information for LsmaintMaintPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LsmaintMaintPolicyConsts:
    DATA_DISR_IMMEDIATE = "immediate"
    DATA_DISR_USER_ACK = "user-ack"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SOFT_SHUTDOWN_TIMER_150_SECS = "150-secs"
    SOFT_SHUTDOWN_TIMER_300_SECS = "300-secs"
    SOFT_SHUTDOWN_TIMER_600_SECS = "600-secs"
    SOFT_SHUTDOWN_TIMER_NEVER = "never"
    UPTIME_DISR_IMMEDIATE = "immediate"
    UPTIME_DISR_TIMER_AUTOMATIC = "timer-automatic"
    UPTIME_DISR_USER_ACK = "user-ack"


class LsmaintMaintPolicy(ManagedObject):
    """This is LsmaintMaintPolicy class."""

    consts = LsmaintMaintPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("LsmaintMaintPolicy", "lsmaintMaintPolicy", "maint-[name]", VersionMeta.Version141i, "InputOutput", 0x1fff, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy"], ['orgOrg'], ['faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "data_disr": MoPropertyMeta("data_disr", "dataDisr", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["immediate", "user-ack"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "oper_sched_name": MoPropertyMeta("oper_sched_name", "operSchedName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sched_name": MoPropertyMeta("sched_name", "schedName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "soft_shutdown_timer": MoPropertyMeta("soft_shutdown_timer", "softShutdownTimer", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", ["150-secs", "300-secs", "600-secs", "never"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "trigger_config": MoPropertyMeta("trigger_config", "triggerConfig", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((defaultValue|none|on-next-boot),){0,2}(defaultValue|none|on-next-boot){0,1}""", [], []),
        "uptime_disr": MoPropertyMeta("uptime_disr", "uptimeDisr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["immediate", "timer-automatic", "user-ack"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dataDisr": "data_disr", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "operSchedName": "oper_sched_name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "schedName": "sched_name", 
        "softShutdownTimer": "soft_shutdown_timer", 
        "status": "status", 
        "triggerConfig": "trigger_config", 
        "uptimeDisr": "uptime_disr", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.data_disr = None
        self.descr = None
        self.int_id = None
        self.oper_sched_name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.sched_name = None
        self.soft_shutdown_timer = None
        self.status = None
        self.trigger_config = None
        self.uptime_disr = None

        ManagedObject.__init__(self, "LsmaintMaintPolicy", parent_mo_or_dn, **kwargs)
