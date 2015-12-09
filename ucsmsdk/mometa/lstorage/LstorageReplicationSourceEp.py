"""This module contains the general information for LstorageReplicationSourceEp ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageReplicationSourceEpConsts():
    pass


class LstorageReplicationSourceEp(ManagedObject):
    """This is LstorageReplicationSourceEp class."""

    consts = LstorageReplicationSourceEpConsts()
    naming_props = set([u'serialNumber'])

    mo_meta = MoMeta("LstorageReplicationSourceEp", "lstorageReplicationSourceEp", "repl-source-ep[serial_number]", VersionMeta.Version302c, "InputOutput", 0x3fL, [], ["admin", "ls-storage", "ls-storage-policy"], [u'lstorageReplicationSources'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "serial_number": MoPropertyMeta("serial_number", "serialNumber", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x10L, 1, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serialNumber": "serial_number", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, serial_number, **kwargs):
        self._dirty_mask = 0
        self.serial_number = serial_number
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageReplicationSourceEp", parent_mo_or_dn, **kwargs)

