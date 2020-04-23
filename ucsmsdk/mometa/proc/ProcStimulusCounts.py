"""This module contains the general information for ProcStimulusCounts ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ProcStimulusCountsConsts:
    ADMIN_STATE_CLEAR_STATS = "clear-stats"
    ADMIN_STATE_LOG_STATS = "log-stats"
    ADMIN_STATE_ON = "on"


class ProcStimulusCounts(ManagedObject):
    """This is ProcStimulusCounts class."""

    consts = ProcStimulusCountsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcStimulusCounts", "procStimulusCounts", "stim", VersionMeta.Version101e, "InputOutput", 0x3f, [], ["admin", "read-only"], ['procManager', 'procSvc'], [], ["Get"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["clear-stats", "log-stats", "on"], []),
        "bulked": MoPropertyMeta("bulked", "bulked", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "failed": MoPropertyMeta("failed", "failed", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "retried": MoPropertyMeta("retried", "retried", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "singleton": MoPropertyMeta("singleton", "singleton", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "successfull": MoPropertyMeta("successfull", "successfull", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total": MoPropertyMeta("total", "total", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "bulked": "bulked", 
        "childAction": "child_action", 
        "dn": "dn", 
        "failed": "failed", 
        "retried": "retried", 
        "rn": "rn", 
        "sacl": "sacl", 
        "singleton": "singleton", 
        "status": "status", 
        "successfull": "successfull", 
        "total": "total", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.bulked = None
        self.child_action = None
        self.failed = None
        self.retried = None
        self.sacl = None
        self.singleton = None
        self.status = None
        self.successfull = None
        self.total = None

        ManagedObject.__init__(self, "ProcStimulusCounts", parent_mo_or_dn, **kwargs)
