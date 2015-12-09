"""This module contains the general information for LstorageReplicationSources ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageReplicationSourcesConsts():
    ACCESS_TYPE_ALLOW_ALL = "ALLOW_ALL"
    ACCESS_TYPE_ALLOW_NONE = "ALLOW_NONE"
    ACCESS_TYPE_ALLOW_ONLY = "ALLOW_ONLY"


class LstorageReplicationSources(ManagedObject):
    """This is LstorageReplicationSources class."""

    consts = LstorageReplicationSourcesConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageReplicationSources", "lstorageReplicationSources", "repl-sources", VersionMeta.Version302c, "InputOutput", 0x3fL, [], ["admin", "ls-storage", "ls-storage-policy"], [u'lstorageLunReplicationService'], [u'lstorageReplicationSourceEp'], [None])

    prop_meta = {
        "access_type": MoPropertyMeta("access_type", "accessType", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["ALLOW_ALL", "ALLOW_NONE", "ALLOW_ONLY"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "accessType": "access_type", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.access_type = None
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageReplicationSources", parent_mo_or_dn, **kwargs)

