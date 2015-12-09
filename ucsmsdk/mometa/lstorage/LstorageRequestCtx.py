"""This module contains the general information for LstorageRequestCtx ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageRequestCtxConsts():
    pass


class LstorageRequestCtx(ManagedObject):
    """This is LstorageRequestCtx class."""

    consts = LstorageRequestCtxConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageRequestCtx", "lstorageRequestCtx", "", VersionMeta.Version302c, "InputOutput", 0x1fL, [], ["read-only"], [], [], [None])

    prop_meta = {
        "assigned_volume": MoPropertyMeta("assigned_volume", "assignedVolume", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cons_dn": MoPropertyMeta("cons_dn", "consDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "request_size": MoPropertyMeta("request_size", "requestSize", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "volume_pool_name": MoPropertyMeta("volume_pool_name", "volumePoolName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
    }

    prop_map = {
        "assignedVolume": "assigned_volume", 
        "childAction": "child_action", 
        "consDn": "cons_dn", 
        "dn": "dn", 
        "requestSize": "request_size", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "volumePoolName": "volume_pool_name", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.assigned_volume = None
        self.child_action = None
        self.cons_dn = None
        self.request_size = None
        self.sacl = None
        self.status = None
        self.volume_pool_name = None

        ManagedObject.__init__(self, "LstorageRequestCtx", parent_mo_or_dn, **kwargs)

