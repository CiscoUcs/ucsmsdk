"""This module contains the general information for LstorageInvictaReplicationExt ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageInvictaReplicationExtConsts():
    pass


class LstorageInvictaReplicationExt(ManagedObject):
    """This is LstorageInvictaReplicationExt class."""

    consts = LstorageInvictaReplicationExtConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageInvictaReplicationExt", "lstorageInvictaReplicationExt", "extension-invicta", VersionMeta.Version302c, "InputOutput", 0x3fL, [], ["admin", "ls-storage", "ls-storage-policy"], [u'lstorageLunReplicationPolicy', u'storageReplicationProfile'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "max_rate": MoPropertyMeta("max_rate", "maxRate", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "maxRate": "max_rate", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.max_rate = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageInvictaReplicationExt", parent_mo_or_dn, **kwargs)

