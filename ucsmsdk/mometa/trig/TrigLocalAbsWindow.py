"""This module contains the general information for TrigLocalAbsWindow ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class TrigLocalAbsWindowConsts():
    CONCUR_CAP_UNLIMITED = "unlimited"
    EXPIRED_FALSE = "false"
    EXPIRED_NO = "no"
    EXPIRED_TRUE = "true"
    EXPIRED_YES = "yes"
    PROC_BREAK_NONE = "none"
    PROC_CAP_UNLIMITED = "unlimited"
    TIME_CAP_NONE = "none"
    TIME_CAPPED_FALSE = "false"
    TIME_CAPPED_NO = "no"
    TIME_CAPPED_TRUE = "true"
    TIME_CAPPED_YES = "yes"


class TrigLocalAbsWindow(ManagedObject):
    """This is TrigLocalAbsWindow class."""

    consts = TrigLocalAbsWindowConsts()
    naming_props = set([])

    mo_meta = MoMeta("TrigLocalAbsWindow", "trigLocalAbsWindow", "local-abs-default", VersionMeta.Version211a, "InputOutput", 0x3ffL, [], ["admin"], [u'lstorageSvcSched', u'trigLocalSched', u'trigSched'], [], ["Add", "Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "concur_cap": MoPropertyMeta("concur_cap", "concurCap", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["unlimited"], ["0-65535"]), 
        "date": MoPropertyMeta("date", "date", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "expired": MoPropertyMeta("expired", "expired", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "job_count": MoPropertyMeta("job_count", "jobCount", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "proc_break": MoPropertyMeta("proc_break", "procBreak", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""[0-9]+:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{1,3})?""", ["none"], ["0-4294967295"]), 
        "proc_cap": MoPropertyMeta("proc_cap", "procCap", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["unlimited"], ["0-65535"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "time_cap": MoPropertyMeta("time_cap", "timeCap", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200L, None, None, r"""[0-9]+:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{1,3})?""", ["none"], ["0-4294967295"]), 
        "time_capped": MoPropertyMeta("time_capped", "timeCapped", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "concurCap": "concur_cap", 
        "date": "date", 
        "dn": "dn", 
        "expired": "expired", 
        "jobCount": "job_count", 
        "name": "name", 
        "procBreak": "proc_break", 
        "procCap": "proc_cap", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "timeCap": "time_cap", 
        "timeCapped": "time_capped", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.concur_cap = None
        self.date = None
        self.expired = None
        self.job_count = None
        self.name = None
        self.proc_break = None
        self.proc_cap = None
        self.sacl = None
        self.status = None
        self.time_cap = None
        self.time_capped = None

        ManagedObject.__init__(self, "TrigLocalAbsWindow", parent_mo_or_dn, **kwargs)

