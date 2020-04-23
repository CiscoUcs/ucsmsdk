"""This module contains the general information for AdaptorDiagCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorDiagCapConsts:
    ENABLE_LLDP_TRANSMIT_FALSE = "false"
    ENABLE_LLDP_TRANSMIT_NO = "no"
    ENABLE_LLDP_TRANSMIT_TRUE = "true"
    ENABLE_LLDP_TRANSMIT_YES = "yes"


class AdaptorDiagCap(ManagedObject):
    """This is AdaptorDiagCap class."""

    consts = AdaptorDiagCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorDiagCap", "adaptorDiagCap", "diag", VersionMeta.Version131c, "InputOutput", 0x3f, [], ["read-only"], ['adaptorFruCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "enable_lldp_transmit": MoPropertyMeta("enable_lldp_transmit", "enableLldpTransmit", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "enableLldpTransmit": "enable_lldp_transmit", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.enable_lldp_transmit = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorDiagCap", parent_mo_or_dn, **kwargs)
