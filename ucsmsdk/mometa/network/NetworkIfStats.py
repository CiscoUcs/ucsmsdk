"""This module contains the general information for NetworkIfStats ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class NetworkIfStatsConsts():
    TYPE_BROADCAST = "broadcast"
    TYPE_GENERIC = "generic"
    TYPE_MULTICAST = "multicast"
    TYPE_TOTAL = "total"
    TYPE_UNICAST = "unicast"
    UNITS_OCTETS = "octets"
    UNITS_PACKETS = "packets"
    UNITS_RAW = "raw"


class NetworkIfStats(ManagedObject):
    """This is NetworkIfStats class."""

    consts = NetworkIfStatsConsts()
    naming_props = set([u'type', u'units'])

    mo_meta = MoMeta("NetworkIfStats", "networkIfStats", "if-stat-[type]-[units]", VersionMeta.Version101e, "InputOutput", 0x7fL, [], ["read-only"], [u'adaptorHostEthIf', u'adaptorHostFcIf', u'adaptorHostIscsiIf', u'adaptorHostScsiIf', u'adaptorHostServiceEthIf', u'etherPIo', u'fcPIo'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "r_in": MoPropertyMeta("r_in", "in", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "out": MoPropertyMeta("out", "out", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rin": MoPropertyMeta("rin", "rin", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20L, None, None, None, ["broadcast", "generic", "multicast", "total", "unicast"], []), 
        "units": MoPropertyMeta("units", "units", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40L, None, None, None, ["octets", "packets", "raw"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "in": "r_in", 
        "out": "out", 
        "rin": "rin", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
        "units": "units", 
    }

    def __init__(self, parent_mo_or_dn, type, units, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.units = units
        self.child_action = None
        self.r_in = None
        self.out = None
        self.rin = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "NetworkIfStats", parent_mo_or_dn, **kwargs)

