"""This module contains the general information for NetworkIfStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class NetworkIfStatsConsts:
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
    naming_props = set(['type', 'units'])

    mo_meta = MoMeta("NetworkIfStats", "networkIfStats", "if-stat-[type]-[units]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["read-only"], ['adaptorHostEthIf', 'adaptorHostFcIf', 'adaptorHostIscsiIf', 'adaptorHostScsiIf', 'adaptorHostServiceEthIf', 'etherPIo', 'fcPIo'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "out": MoPropertyMeta("out", "out", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rin": MoPropertyMeta("rin", "rin", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, None, None, None, ["broadcast", "generic", "multicast", "total", "unicast"], []),
        "units": MoPropertyMeta("units", "units", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, None, ["octets", "packets", "raw"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
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
        self.out = None
        self.rin = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "NetworkIfStats", parent_mo_or_dn, **kwargs)
