"""This module contains the general information for MacpoolFormat ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MacpoolFormatConsts:
    MASK_FF_FF_FF_FF_FF_FX = "FF-FF-FF-FF-FF-Fx"
    MASK_FF_FF_FF_FF_FF_XX = "FF-FF-FF-FF-FF-xx"
    MASK_FF_FF_FF_FF_FX_XX = "FF-FF-FF-FF-Fx-xx"
    MASK_FF_FF_FF_FF_XX_XX = "FF-FF-FF-FF-xx-xx"
    MASK_FF_FF_FF_FX_XX_XX = "FF-FF-FF-Fx-xx-xx"
    MASK_FF_FF_FF_XX_XX_XX = "FF-FF-FF-xx-xx-xx"
    MASK_FF_FF_FX_XX_XX_XX = "FF-FF-Fx-xx-xx-xx"
    MASK_FF_FF_XX_XX_XX_XX = "FF-FF-xx-xx-xx-xx"
    MASK_FF_FX_XX_XX_XX_XX = "FF-Fx-xx-xx-xx-xx"
    MASK_FF_XX_XX_XX_XX_XX = "FF-xx-xx-xx-xx-xx"
    MASK_FX_XX_XX_XX_XX_XX = "Fx-xx-xx-xx-xx-xx"


class MacpoolFormat(ManagedObject):
    """This is MacpoolFormat class."""

    consts = MacpoolFormatConsts()
    naming_props = set(['format', 'mask'])

    mo_meta = MoMeta("MacpoolFormat", "macpoolFormat", "format-[format]-[mask]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["admin", "ext-lan-config", "ext-lan-policy", "ls-network", "ls-network-policy"], ['macpoolUniverse'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "format": MoPropertyMeta("format", "format", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []),
        "mask": MoPropertyMeta("mask", "mask", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10, None, None, None, ["FF-FF-FF-FF-FF-Fx", "FF-FF-FF-FF-FF-xx", "FF-FF-FF-FF-Fx-xx", "FF-FF-FF-FF-xx-xx", "FF-FF-FF-Fx-xx-xx", "FF-FF-FF-xx-xx-xx", "FF-FF-Fx-xx-xx-xx", "FF-FF-xx-xx-xx-xx", "FF-Fx-xx-xx-xx-xx", "FF-xx-xx-xx-xx-xx", "Fx-xx-xx-xx-xx-xx"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "format": "format", 
        "mask": "mask", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, format, mask, **kwargs):
        self._dirty_mask = 0
        self.format = format
        self.mask = mask
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MacpoolFormat", parent_mo_or_dn, **kwargs)
