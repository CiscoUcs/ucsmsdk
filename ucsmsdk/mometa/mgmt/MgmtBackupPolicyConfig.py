"""This module contains the general information for MgmtBackupPolicyConfig ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtBackupPolicyConfigConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGER_IMMEDIATE = "trigger-immediate"
    ADMIN_STATE_TRIGGERED = "triggered"
    ADMIN_STATE_UNTRIGGERED = "untriggered"
    ADMIN_STATE_USER_ACK = "user-ack"
    ADMIN_STATE_USER_DISCARD = "user-discard"
    AUTO_DELETE_FALSE = "false"
    AUTO_DELETE_NO = "no"
    AUTO_DELETE_TRUE = "true"
    AUTO_DELETE_YES = "yes"
    BACKUP_ISSUE_NONE = "none"
    BACKUP_ISSUE_OUTDATED = "outdated"
    IGNORE_CAP_FALSE = "false"
    IGNORE_CAP_NO = "no"
    IGNORE_CAP_TRUE = "true"
    IGNORE_CAP_YES = "yes"
    INT_ID_NONE = "none"
    OPER_STATE_ACTIVE = "active"
    OPER_STATE_APPLIED = "applied"
    OPER_STATE_APPLY_PENDING = "apply-pending"
    OPER_STATE_EVALUATED = "evaluated"
    OPER_STATE_EVALUATION_PENDING = "evaluation-pending"
    OPER_STATE_EXPIRED = "expired"
    OPER_STATE_NONE = "none"
    OPER_STATE_PENDING = "pending"
    OPER_STATE_UNTRIGGERED = "untriggered"
    OPER_STATE_WAITING_FOR_DEPENDENCY = "waiting-for-dependency"
    OPER_STATE_WAITING_FOR_MAINT_WINDOW = "waiting-for-maint-window"
    OPER_STATE_WAITING_FOR_USER = "waiting-for-user"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class MgmtBackupPolicyConfig(ManagedObject):
    """This is MgmtBackupPolicyConfig class."""

    consts = MgmtBackupPolicyConfigConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtBackupPolicyConfig", "mgmtBackupPolicyConfig", "bkup-policy-cfg", VersionMeta.Version222c, "InputOutput", 0x1fff, [], ["admin"], ['topSystem'], ['faultInst', 'trigLocalSched'], ["Get"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "trigger-immediate", "triggered", "untriggered", "user-ack", "user-discard"], []),
        "auto_delete": MoPropertyMeta("auto_delete", "autoDelete", "string", VersionMeta.Version222c, MoPropertyMeta.CREATE_ONLY, 0x4, None, None, None, ["false", "no", "true", "yes"], []),
        "backup_date": MoPropertyMeta("backup_date", "backupDate", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "backup_issue": MoPropertyMeta("backup_issue", "backupIssue", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["none", "outdated"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x20, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "ignore_cap": MoPropertyMeta("ignore_cap", "ignoreCap", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_scheduler": MoPropertyMeta("oper_scheduler", "operScheduler", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "applied", "apply-pending", "evaluated", "evaluation-pending", "expired", "none", "pending", "untriggered", "waiting-for-dependency", "waiting-for-maint-window", "waiting-for-user"], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "scheduler": MoPropertyMeta("scheduler", "scheduler", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "autoDelete": "auto_delete", 
        "backupDate": "backup_date", 
        "backupIssue": "backup_issue", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "ignoreCap": "ignore_cap", 
        "intId": "int_id", 
        "name": "name", 
        "operScheduler": "oper_scheduler", 
        "operState": "oper_state", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "scheduler": "scheduler", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.auto_delete = None
        self.backup_date = None
        self.backup_issue = None
        self.child_action = None
        self.descr = None
        self.ignore_cap = None
        self.int_id = None
        self.name = None
        self.oper_scheduler = None
        self.oper_state = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.scheduler = None
        self.status = None

        ManagedObject.__init__(self, "MgmtBackupPolicyConfig", parent_mo_or_dn, **kwargs)
