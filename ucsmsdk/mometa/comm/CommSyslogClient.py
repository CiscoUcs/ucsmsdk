"""This module contains the general information for CommSyslogClient ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class CommSyslogClientConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    FORWARDING_FACILITY_LOCAL0 = "local0"
    FORWARDING_FACILITY_LOCAL1 = "local1"
    FORWARDING_FACILITY_LOCAL2 = "local2"
    FORWARDING_FACILITY_LOCAL3 = "local3"
    FORWARDING_FACILITY_LOCAL4 = "local4"
    FORWARDING_FACILITY_LOCAL5 = "local5"
    FORWARDING_FACILITY_LOCAL6 = "local6"
    FORWARDING_FACILITY_LOCAL7 = "local7"
    NAME_PRIMARY = "primary"
    NAME_SECONDARY = "secondary"
    NAME_TERTIARY = "tertiary"
    SEVERITY_ALERTS = "alerts"
    SEVERITY_CRITICAL = "critical"
    SEVERITY_DEBUGGING = "debugging"
    SEVERITY_EMERGENCIES = "emergencies"
    SEVERITY_ERRORS = "errors"
    SEVERITY_INFORMATION = "information"
    SEVERITY_NOTIFICATIONS = "notifications"
    SEVERITY_WARNINGS = "warnings"


class CommSyslogClient(ManagedObject):
    """This is CommSyslogClient class."""

    consts = CommSyslogClientConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("CommSyslogClient", "commSyslogClient", "client-[name]", VersionMeta.Version101e, "InputOutput", 0x3ffL, [], ["admin", "operations"], [u'commSyslog'], [], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "forwarding_facility": MoPropertyMeta("forwarding_facility", "forwardingFacility", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"], []), 
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40L, None, None, None, ["primary", "secondary", "tertiary"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "severity": MoPropertyMeta("severity", "severity", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["alerts", "critical", "debugging", "emergencies", "errors", "information", "notifications", "warnings"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "forwardingFacility": "forwarding_facility", 
        "hostname": "hostname", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "severity": "severity", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_state = None
        self.child_action = None
        self.forwarding_facility = None
        self.hostname = None
        self.sacl = None
        self.severity = None
        self.status = None

        ManagedObject.__init__(self, "CommSyslogClient", parent_mo_or_dn, **kwargs)

