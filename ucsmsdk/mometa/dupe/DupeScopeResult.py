"""This module contains the general information for DupeScopeResult ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class DupeScopeResultConsts:
    SCOPE_STATUS_FAILURE = "failure"
    SCOPE_STATUS_SUCCESS = "success"


class DupeScopeResult(ManagedObject):
    """This is DupeScopeResult class."""

    consts = DupeScopeResultConsts()
    naming_props = set([])

    mo_meta = MoMeta("DupeScopeResult", "dupeScopeResult", "result", VersionMeta.Version302c, "InputOutput", 0x1f, [], ["admin"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "message": MoPropertyMeta("message", "message", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "scope_status": MoPropertyMeta("scope_status", "scopeStatus", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failure", "success"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "update_time": MoPropertyMeta("update_time", "updateTime", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "message": "message", 
        "rn": "rn", 
        "sacl": "sacl", 
        "scopeStatus": "scope_status", 
        "status": "status", 
        "updateTime": "update_time", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.message = None
        self.sacl = None
        self.scope_status = None
        self.status = None
        self.update_time = None

        ManagedObject.__init__(self, "DupeScopeResult", parent_mo_or_dn, **kwargs)
