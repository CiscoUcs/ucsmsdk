"""This module contains the general information for LstorageCtrlService ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageCtrlServiceConsts():
    ADMIN_STATE_IN_MAINTENANCE = "in-maintenance"
    ADMIN_STATE_IN_SERVICE = "in-service"
    FAIL_OVER_STATE_TRIGGER = "trigger"
    FAIL_OVER_STATE_TRIGGERED = "triggered"
    OPER_MAINT_STATE_ENTERING_MAINTENANCE = "entering-maintenance"
    OPER_MAINT_STATE_EXITING_MAINTENANCE = "exiting-maintenance"
    OPER_MAINT_STATE_IN_MAINTENANCE = "in-maintenance"
    OPER_MAINT_STATE_IN_SERVICE = "in-service"
    OPER_MAINT_STATE_NOT_APPLICABLE = "not-applicable"
    OPER_MAINT_STATE_UNKNOWN = "unknown"


class LstorageCtrlService(ManagedObject):
    """This is LstorageCtrlService class."""

    consts = LstorageCtrlServiceConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageCtrlService", "lstorageCtrlService", "services", VersionMeta.Version302c, "InputOutput", 0x7fL, [], ["admin", "ls-storage", "pn-equipment", "pn-maintenance", "pn-policy"], [u'lstorageProcessor'], [], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["in-maintenance", "in-service"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "fail_over_state": MoPropertyMeta("fail_over_state", "failOverState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["trigger", "triggered"], []), 
        "oper_maint_state": MoPropertyMeta("oper_maint_state", "operMaintState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["entering-maintenance", "exiting-maintenance", "in-maintenance", "in-service", "not-applicable", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "failOverState": "fail_over_state", 
        "operMaintState": "oper_maint_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.fail_over_state = None
        self.oper_maint_state = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageCtrlService", parent_mo_or_dn, **kwargs)

