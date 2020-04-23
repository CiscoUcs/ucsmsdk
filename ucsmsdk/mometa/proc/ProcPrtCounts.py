"""This module contains the general information for ProcPrtCounts ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ProcPrtCountsConsts:
    pass


class ProcPrtCounts(ManagedObject):
    """This is ProcPrtCounts class."""

    consts = ProcPrtCountsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcPrtCounts", "procPrtCounts", "prt", VersionMeta.Version101e, "InputOutput", 0x1f, [], ["read-only"], ['procManager'], [], ["Get"])

    prop_meta = {
        "cachenospc": MoPropertyMeta("cachenospc", "cachenospc", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dbtxs": MoPropertyMeta("dbtxs", "dbtxs", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "largetxs": MoPropertyMeta("largetxs", "largetxs", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "persist_time": MoPropertyMeta("persist_time", "persistTime", "ulong", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "total": MoPropertyMeta("total", "total", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "cachenospc": "cachenospc", 
        "childAction": "child_action", 
        "dbtxs": "dbtxs", 
        "dn": "dn", 
        "largetxs": "largetxs", 
        "persistTime": "persist_time", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "total": "total", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.cachenospc = None
        self.child_action = None
        self.dbtxs = None
        self.largetxs = None
        self.persist_time = None
        self.sacl = None
        self.status = None
        self.total = None

        ManagedObject.__init__(self, "ProcPrtCounts", parent_mo_or_dn, **kwargs)
