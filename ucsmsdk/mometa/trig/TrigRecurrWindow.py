"""This module contains the general information for TrigRecurrWindow ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class TrigRecurrWindowConsts():
    CONCUR_CAP_UNLIMITED = "unlimited"
    DAY_FRIDAY = "Friday"
    DAY_MONDAY = "Monday"
    DAY_SATURDAY = "Saturday"
    DAY_SUNDAY = "Sunday"
    DAY_THURSDAY = "Thursday"
    DAY_TUESDAY = "Tuesday"
    DAY_WEDNESDAY = "Wednesday"
    DAY_EVEN_DAY = "even-day"
    DAY_EVERY_DAY = "every-day"
    DAY_ODD_DAY = "odd-day"
    PROC_BREAK_NONE = "none"
    PROC_CAP_UNLIMITED = "unlimited"
    TIME_CAP_NONE = "none"


class TrigRecurrWindow(ManagedObject):
    """This is TrigRecurrWindow class."""

    consts = TrigRecurrWindowConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("TrigRecurrWindow", "trigRecurrWindow", "recurr-[name]", VersionMeta.Version141i, "InputOutput", 0xfffL, [], ["admin", "ls-compute", "ls-config", "ls-server"], [u'lstorageSvcSched', u'trigLocalSched', u'trigSched'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "concur_cap": MoPropertyMeta("concur_cap", "concurCap", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["unlimited"], ["0-65535"]), 
        "day": MoPropertyMeta("day", "day", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday", "even-day", "every-day", "odd-day"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "hour": MoPropertyMeta("hour", "hour", "ushort", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["0-23"]), 
        "job_count": MoPropertyMeta("job_count", "jobCount", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "minute": MoPropertyMeta("minute", "minute", "ushort", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], ["0-59"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "proc_break": MoPropertyMeta("proc_break", "procBreak", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80L, None, None, """[0-9]+:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{1,3})?""", ["none"], ["0-4294967295"]), 
        "proc_cap": MoPropertyMeta("proc_cap", "procCap", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["unlimited"], ["0-65535"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x200L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x400L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "time_cap": MoPropertyMeta("time_cap", "timeCap", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x800L, None, None, """[0-9]+:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{1,3})?""", ["none"], ["0-4294967295"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "concurCap": "concur_cap", 
        "day": "day", 
        "dn": "dn", 
        "hour": "hour", 
        "jobCount": "job_count", 
        "minute": "minute", 
        "name": "name", 
        "procBreak": "proc_break", 
        "procCap": "proc_cap", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "timeCap": "time_cap", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.concur_cap = None
        self.day = None
        self.hour = None
        self.job_count = None
        self.minute = None
        self.proc_break = None
        self.proc_cap = None
        self.sacl = None
        self.status = None
        self.time_cap = None

        ManagedObject.__init__(self, "TrigRecurrWindow", parent_mo_or_dn, **kwargs)

