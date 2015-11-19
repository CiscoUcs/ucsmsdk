"""This module contains the general information for CommSyslogMonitor ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class CommSyslogMonitorConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    SEVERITY_ALERTS = "alerts"
    SEVERITY_CRITICAL = "critical"
    SEVERITY_DEBUGGING = "debugging"
    SEVERITY_EMERGENCIES = "emergencies"
    SEVERITY_ERRORS = "errors"
    SEVERITY_INFORMATION = "information"
    SEVERITY_NOTIFICATIONS = "notifications"
    SEVERITY_WARNINGS = "warnings"


class CommSyslogMonitor(ManagedObject):
    """This is CommSyslogMonitor class."""

    consts = CommSyslogMonitorConsts()
    naming_props = set([])

    mo_meta = MoMeta("CommSyslogMonitor", "commSyslogMonitor", "monitor", VersionMeta.Version101e, "InputOutput", 0xffL, [], ["admin", "operations"], [u'commSyslog'], [], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "severity": MoPropertyMeta("severity", "severity", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["alerts", "critical", "debugging", "emergencies", "errors", "information", "notifications", "warnings"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "severity": "severity", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.name = None
        self.sacl = None
        self.severity = None
        self.status = None

        ManagedObject.__init__(self, "CommSyslogMonitor", parent_mo_or_dn, **kwargs)

