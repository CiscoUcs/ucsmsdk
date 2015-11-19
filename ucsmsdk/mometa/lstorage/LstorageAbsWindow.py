"""This module contains the general information for LstorageAbsWindow ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageAbsWindowConsts():
    EXPIRED_FALSE = "false"
    EXPIRED_NO = "no"
    EXPIRED_TRUE = "true"
    EXPIRED_YES = "yes"


class LstorageAbsWindow(ManagedObject):
    """This is LstorageAbsWindow class."""

    consts = LstorageAbsWindowConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("LstorageAbsWindow", "lstorageAbsWindow", "abs-window[name]", VersionMeta.Version302a, "InputOutput", 0x3fL, [], ["admin", "ls-storage", "ls-storage-policy"], [u'lstorageSvcSched'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "date": MoPropertyMeta("date", "date", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "expired": MoPropertyMeta("expired", "expired", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "job_count": MoPropertyMeta("job_count", "jobCount", "uint", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302a, MoPropertyMeta.NAMING, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "date": "date", 
        "dn": "dn", 
        "expired": "expired", 
        "jobCount": "job_count", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.date = None
        self.expired = None
        self.job_count = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageAbsWindow", parent_mo_or_dn, **kwargs)

