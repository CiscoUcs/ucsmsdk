"""This module contains the general information for MemoryQual ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class MemoryQualConsts():
    CLOCK_UNSPECIFIED = "unspecified"
    LATENCY_UNSPECIFIED = "unspecified"
    MAX_CAP_UNSPECIFIED = "unspecified"
    MIN_CAP_UNSPECIFIED = "unspecified"
    SPEED_UNSPECIFIED = "unspecified"
    UNITS_UNSPECIFIED = "unspecified"
    WIDTH_UNSPECIFIED = "unspecified"


class MemoryQual(ManagedObject):
    """This is MemoryQual class."""

    consts = MemoryQualConsts()
    naming_props = set([])

    mo_meta = MoMeta("MemoryQual", "memoryQual", "memory", VersionMeta.Version101e, "InputOutput", 0xfffL, [], ["admin", "pn-policy"], [u'computeQual'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "clock": MoPropertyMeta("clock", "clock", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "latency": MoPropertyMeta("latency", "latency", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "max_cap": MoPropertyMeta("max_cap", "maxCap", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "min_cap": MoPropertyMeta("min_cap", "minCap", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "speed": MoPropertyMeta("speed", "speed", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "units": MoPropertyMeta("units", "units", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "width": MoPropertyMeta("width", "width", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, ["unspecified"], ["0-4294967295"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "clock": "clock", 
        "dn": "dn", 
        "latency": "latency", 
        "maxCap": "max_cap", 
        "minCap": "min_cap", 
        "rn": "rn", 
        "sacl": "sacl", 
        "speed": "speed", 
        "status": "status", 
        "units": "units", 
        "width": "width", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.clock = None
        self.latency = None
        self.max_cap = None
        self.min_cap = None
        self.sacl = None
        self.speed = None
        self.status = None
        self.units = None
        self.width = None

        ManagedObject.__init__(self, "MemoryQual", parent_mo_or_dn, **kwargs)

