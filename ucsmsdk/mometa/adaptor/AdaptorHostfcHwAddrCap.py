"""This module contains the general information for AdaptorHostfcHwAddrCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorHostfcHwAddrCapConsts:
    pass


class AdaptorHostfcHwAddrCap(ManagedObject):
    """This is AdaptorHostfcHwAddrCap class."""

    consts = AdaptorHostfcHwAddrCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorHostfcHwAddrCap", "adaptorHostfcHwAddrCap", "hwaddr-hostfc", VersionMeta.Version141i, "InputOutput", 0x7ff, [], ["read-only"], ['adaptorFruCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "mac_offset1": MoPropertyMeta("mac_offset1", "macOffset1", "byte", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
        "mac_offset2": MoPropertyMeta("mac_offset2", "macOffset2", "byte", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "wwn_reverse_mask_a": MoPropertyMeta("wwn_reverse_mask_a", "wwnReverseMaskA", "ulong", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
        "wwn_reverse_mask_b": MoPropertyMeta("wwn_reverse_mask_b", "wwnReverseMaskB", "ulong", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], []),
        "wwnn_reverse_mask_a": MoPropertyMeta("wwnn_reverse_mask_a", "wwnnReverseMaskA", "ulong", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], []),
        "wwnn_reverse_mask_b": MoPropertyMeta("wwnn_reverse_mask_b", "wwnnReverseMaskB", "ulong", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "macOffset1": "mac_offset1", 
        "macOffset2": "mac_offset2", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "wwnReverseMaskA": "wwn_reverse_mask_a", 
        "wwnReverseMaskB": "wwn_reverse_mask_b", 
        "wwnnReverseMaskA": "wwnn_reverse_mask_a", 
        "wwnnReverseMaskB": "wwnn_reverse_mask_b", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.mac_offset1 = None
        self.mac_offset2 = None
        self.sacl = None
        self.status = None
        self.wwn_reverse_mask_a = None
        self.wwn_reverse_mask_b = None
        self.wwnn_reverse_mask_a = None
        self.wwnn_reverse_mask_b = None

        ManagedObject.__init__(self, "AdaptorHostfcHwAddrCap", parent_mo_or_dn, **kwargs)
