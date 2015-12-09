"""This module contains the general information for LstorageRecurrWindow ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageRecurrWindowConsts():
    CONCUR_CAP_UNLIMITED = "unlimited"
    DAY_FRIDAY = "Friday"
    DAY_MONDAY = "Monday"
    DAY_SATURDAY = "Saturday"
    DAY_SUNDAY = "Sunday"
    DAY_THURSDAY = "Thursday"
    DAY_TUESDAY = "Tuesday"
    DAY_WEDNESDAY = "Wednesday"
    DAY_EVERY_DAY = "every-day"
    DAY_EVERY_HOUR = "every-hour"
    DAY_EVERY_MONTH = "every-month"
    PROC_BREAK_NONE = "none"
    PROC_CAP_UNLIMITED = "unlimited"
    TIME_CAP_NONE = "none"


class LstorageRecurrWindow(ManagedObject):
    """This is LstorageRecurrWindow class."""

    consts = LstorageRecurrWindowConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("LstorageRecurrWindow", "lstorageRecurrWindow", "recurr-window-[name]", VersionMeta.Version302c, "InputOutput", 0x3fffL, [], ["admin", "ls-compute", "ls-config", "ls-server"], [u'lstorageSvcSched', u'trigLocalSched', u'trigSched'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "concur_cap": MoPropertyMeta("concur_cap", "concurCap", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["unlimited"], ["0-65535"]), 
        "day": MoPropertyMeta("day", "day", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday", "every-day", "every-hour", "every-month"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "dom": MoPropertyMeta("dom", "dom", "byte", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], ["1-31"]), 
        "hour": MoPropertyMeta("hour", "hour", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], ["0-23"]), 
        "job_count": MoPropertyMeta("job_count", "jobCount", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "minute": MoPropertyMeta("minute", "minute", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, [], ["0-59"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x100L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "proc_break": MoPropertyMeta("proc_break", "procBreak", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x200L, None, None, r"""[0-9]+:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{1,3})?""", ["none"], ["0-4294967295"]), 
        "proc_cap": MoPropertyMeta("proc_cap", "procCap", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, ["unlimited"], ["0-65535"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x800L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "time_cap": MoPropertyMeta("time_cap", "timeCap", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, r"""[0-9]+:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{1,3})?""", ["none"], ["0-4294967295"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "concurCap": "concur_cap", 
        "day": "day", 
        "dn": "dn", 
        "dom": "dom", 
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
        self.dom = None
        self.hour = None
        self.job_count = None
        self.minute = None
        self.proc_break = None
        self.proc_cap = None
        self.sacl = None
        self.status = None
        self.time_cap = None

        ManagedObject.__init__(self, "LstorageRecurrWindow", parent_mo_or_dn, **kwargs)

