"""This module contains the general information for ApePaloVnicStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ApePaloVnicStatsConsts:
    pass


class ApePaloVnicStats(ManagedObject):
    """This is ApePaloVnicStats class."""

    consts = ApePaloVnicStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ApePaloVnicStats", "apePaloVnicStats", "palostats", VersionMeta.Version211a, "InputOutput", 0x1fff, [], ["read-only"], ['apeMenloVnic', 'apePaloVnic'], [], [None])

    prop_meta = {
        "bytes_eg": MoPropertyMeta("bytes_eg", "bytes_eg", "ulong", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []),
        "bytes_in": MoPropertyMeta("bytes_in", "bytes_in", "ulong", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x8, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "dropped_pkts_eg": MoPropertyMeta("dropped_pkts_eg", "dropped_pkts_eg", "ulong", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
        "dropped_pkts_in": MoPropertyMeta("dropped_pkts_in", "dropped_pkts_in", "ulong", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []),
        "errors_eg": MoPropertyMeta("errors_eg", "errors_eg", "ulong", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
        "errors_in": MoPropertyMeta("errors_in", "errors_in", "ulong", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], []),
        "pkts_eg": MoPropertyMeta("pkts_eg", "pkts_eg", "ulong", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], []),
        "pkts_in": MoPropertyMeta("pkts_in", "pkts_in", "ulong", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x800, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "bytes_eg": "bytes_eg", 
        "bytes_in": "bytes_in", 
        "childAction": "child_action", 
        "dn": "dn", 
        "dropped_pkts_eg": "dropped_pkts_eg", 
        "dropped_pkts_in": "dropped_pkts_in", 
        "errors_eg": "errors_eg", 
        "errors_in": "errors_in", 
        "pkts_eg": "pkts_eg", 
        "pkts_in": "pkts_in", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.bytes_eg = None
        self.bytes_in = None
        self.child_action = None
        self.dropped_pkts_eg = None
        self.dropped_pkts_in = None
        self.errors_eg = None
        self.errors_in = None
        self.pkts_eg = None
        self.pkts_in = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ApePaloVnicStats", parent_mo_or_dn, **kwargs)
