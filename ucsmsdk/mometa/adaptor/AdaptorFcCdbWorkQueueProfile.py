"""This module contains the general information for AdaptorFcCdbWorkQueueProfile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorFcCdbWorkQueueProfileConsts:
    pass


class AdaptorFcCdbWorkQueueProfile(ManagedObject):
    """This is AdaptorFcCdbWorkQueueProfile class."""

    consts = AdaptorFcCdbWorkQueueProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorFcCdbWorkQueueProfile", "adaptorFcCdbWorkQueueProfile", "fc-cdb-work-q", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["admin", "ls-config-policy", "ls-server-policy", "ls-storage"], ['adaptorHostFcIf', 'adaptorHostFcIfProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "count": MoPropertyMeta("count", "count", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1-64"]),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "ring_size": MoPropertyMeta("ring_size", "ringSize", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["64-512"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "count": "count", 
        "dn": "dn", 
        "ringSize": "ring_size", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.count = None
        self.ring_size = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorFcCdbWorkQueueProfile", parent_mo_or_dn, **kwargs)
