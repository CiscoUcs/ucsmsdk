"""This module contains the general information for AdaptorUplinkPortStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorUplinkPortStatsConsts:
    PORT_ID_N_A = "N/A"


class AdaptorUplinkPortStats(ManagedObject):
    """This is AdaptorUplinkPortStats class."""

    consts = AdaptorUplinkPortStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorUplinkPortStats", "adaptorUplinkPortStats", "", VersionMeta.Version251a, "InputOutput", 0x1f, [], ["read-only"], [], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "crc": MoPropertyMeta("crc", "crc", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "frame_tx": MoPropertyMeta("frame_tx", "frameTx", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "in_range": MoPropertyMeta("in_range", "inRange", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "port_id": MoPropertyMeta("port_id", "portId", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "too_long": MoPropertyMeta("too_long", "tooLong", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "too_short": MoPropertyMeta("too_short", "tooShort", "uint", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "crc": "crc", 
        "dn": "dn", 
        "frameTx": "frame_tx", 
        "inRange": "in_range", 
        "portId": "port_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "tooLong": "too_long", 
        "tooShort": "too_short", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.crc = None
        self.frame_tx = None
        self.in_range = None
        self.port_id = None
        self.sacl = None
        self.status = None
        self.too_long = None
        self.too_short = None

        ManagedObject.__init__(self, "AdaptorUplinkPortStats", parent_mo_or_dn, **kwargs)
