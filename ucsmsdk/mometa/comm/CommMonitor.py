"""This module contains the general information for CommMonitor ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CommMonitorConsts:
    ALL_DISABLED = "disabled"
    ALL_ENABLED = "enabled"
    AUTHLOG_FILES_DISABLED = "disabled"
    AUTHLOG_FILES_ENABLED = "enabled"
    CRON_FILES_DISABLED = "disabled"
    CRON_FILES_ENABLED = "enabled"
    DNS_CLIENT_FILES_DISABLED = "disabled"
    DNS_CLIENT_FILES_ENABLED = "enabled"
    KERNEL_MODULE_MGMT_DISABLED = "disabled"
    KERNEL_MODULE_MGMT_ENABLED = "enabled"
    LXC_CONTAINERS_DISABLED = "disabled"
    LXC_CONTAINERS_ENABLED = "enabled"
    PROCESS_AUDIT_DISABLED = "disabled"
    PROCESS_AUDIT_ENABLED = "enabled"
    SYSTEM_LOG_FILES_DISABLED = "disabled"
    SYSTEM_LOG_FILES_ENABLED = "enabled"
    SYSTEM_LOGIN_REBOOT_DISABLED = "disabled"
    SYSTEM_LOGIN_REBOOT_ENABLED = "enabled"
    SYSTEM_SOFTWARE_DISABLED = "disabled"
    SYSTEM_SOFTWARE_ENABLED = "enabled"
    SYSTEM_TIME_CHANGE_DISABLED = "disabled"
    SYSTEM_TIME_CHANGE_ENABLED = "enabled"
    USER_GROUP_CONFIG_FILES_DISABLED = "disabled"
    USER_GROUP_CONFIG_FILES_ENABLED = "enabled"
    USER_PRIVILEGE_MGMT_DISABLED = "disabled"
    USER_PRIVILEGE_MGMT_ENABLED = "enabled"


class CommMonitor(ManagedObject):
    """This is CommMonitor class."""

    consts = CommMonitorConsts()
    naming_props = set([])

    mo_meta = MoMeta("CommMonitor", "commMonitor", "monitor", VersionMeta.Version602a, "InputOutput", 0x3ffff, [], ["admin", "operations"], ['commFabricInterconnectAuditLogs'], [], [None])

    prop_meta = {
        "all": MoPropertyMeta("all", "all", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "authlog_files": MoPropertyMeta("authlog_files", "authlogFiles", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version602a, MoPropertyMeta.INTERNAL, 0x8, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cron_files": MoPropertyMeta("cron_files", "cronFiles", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "dns_client_files": MoPropertyMeta("dns_client_files", "dnsClientFiles", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["disabled", "enabled"], []),
        "kernel_module_mgmt": MoPropertyMeta("kernel_module_mgmt", "kernelModuleMgmt", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["disabled", "enabled"], []),
        "lxc_containers": MoPropertyMeta("lxc_containers", "lxcContainers", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["disabled", "enabled"], []),
        "process_audit": MoPropertyMeta("process_audit", "processAudit", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["disabled", "enabled"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version602a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "system_log_files": MoPropertyMeta("system_log_files", "systemLogFiles", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["disabled", "enabled"], []),
        "system_login_reboot": MoPropertyMeta("system_login_reboot", "systemLoginReboot", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["disabled", "enabled"], []),
        "system_software": MoPropertyMeta("system_software", "systemSoftware", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["disabled", "enabled"], []),
        "system_time_change": MoPropertyMeta("system_time_change", "systemTimeChange", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["disabled", "enabled"], []),
        "user_group_config_files": MoPropertyMeta("user_group_config_files", "userGroupConfigFiles", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["disabled", "enabled"], []),
        "user_privilege_mgmt": MoPropertyMeta("user_privilege_mgmt", "userPrivilegeMgmt", "string", VersionMeta.Version602a, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, ["disabled", "enabled"], []),
    }

    prop_map = {
        "all": "all", 
        "authlogFiles": "authlog_files", 
        "childAction": "child_action", 
        "cronFiles": "cron_files", 
        "dn": "dn", 
        "dnsClientFiles": "dns_client_files", 
        "kernelModuleMgmt": "kernel_module_mgmt", 
        "lxcContainers": "lxc_containers", 
        "processAudit": "process_audit", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "systemLogFiles": "system_log_files", 
        "systemLoginReboot": "system_login_reboot", 
        "systemSoftware": "system_software", 
        "systemTimeChange": "system_time_change", 
        "userGroupConfigFiles": "user_group_config_files", 
        "userPrivilegeMgmt": "user_privilege_mgmt", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.all = None
        self.authlog_files = None
        self.child_action = None
        self.cron_files = None
        self.dns_client_files = None
        self.kernel_module_mgmt = None
        self.lxc_containers = None
        self.process_audit = None
        self.sacl = None
        self.status = None
        self.system_log_files = None
        self.system_login_reboot = None
        self.system_software = None
        self.system_time_change = None
        self.user_group_config_files = None
        self.user_privilege_mgmt = None

        ManagedObject.__init__(self, "CommMonitor", parent_mo_or_dn, **kwargs)
