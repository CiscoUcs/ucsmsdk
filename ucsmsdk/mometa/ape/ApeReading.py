"""This module contains the general information for ApeReading ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ApeReadingConsts():
    pass


class ApeReading(ManagedObject):
    """This is ApeReading class."""

    consts = ApeReadingConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("ApeReading", "apeReading", "reading-[id]", VersionMeta.Version101e, "InputOutput", 0x7fL, [], ["read-only"], [u'apeMcTable'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x4L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "state": MoPropertyMeta("state", "state", "ushort", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "value": MoPropertyMeta("value", "value", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "state": "state", 
        "status": "status", 
        "value": "value", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.sacl = None
        self.state = None
        self.status = None
        self.value = None

        ManagedObject.__init__(self, "ApeReading", parent_mo_or_dn, **kwargs)

