"""This module contains the general information for CommSyslogSource ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class CommSyslogSourceConsts():
    AUDITS_DISABLED = "disabled"
    AUDITS_ENABLED = "enabled"
    EVENTS_DISABLED = "disabled"
    EVENTS_ENABLED = "enabled"
    FAULTS_DISABLED = "disabled"
    FAULTS_ENABLED = "enabled"


class CommSyslogSource(ManagedObject):
    """This is CommSyslogSource class."""

    consts = CommSyslogSourceConsts()
    naming_props = set([])

    mo_meta = MoMeta("CommSyslogSource", "commSyslogSource", "source", VersionMeta.Version141i, "InputOutput", 0x3ffL, [], ["admin", "operations"], [u'commSyslog'], [], ["Get", "Set"])

    prop_meta = {
        "audits": MoPropertyMeta("audits", "audits", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "events": MoPropertyMeta("events", "events", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["disabled", "enabled"], []), 
        "faults": MoPropertyMeta("faults", "faults", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["disabled", "enabled"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x100L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x200L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "audits": "audits", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "events": "events", 
        "faults": "faults", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.audits = None
        self.child_action = None
        self.descr = None
        self.events = None
        self.faults = None
        self.name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "CommSyslogSource", parent_mo_or_dn, **kwargs)

