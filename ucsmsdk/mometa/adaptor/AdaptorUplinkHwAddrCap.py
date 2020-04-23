"""This module contains the general information for AdaptorUplinkHwAddrCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorUplinkHwAddrCapConsts:
    pass


class AdaptorUplinkHwAddrCap(ManagedObject):
    """This is AdaptorUplinkHwAddrCap class."""

    consts = AdaptorUplinkHwAddrCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorUplinkHwAddrCap", "adaptorUplinkHwAddrCap", "hwaddr-uplink", VersionMeta.Version141i, "InputOutput", 0x1ffff, [], ["read-only"], ['adaptorFruCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "lldp_mac_offset1": MoPropertyMeta("lldp_mac_offset1", "lldpMacOffset1", "byte", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
        "lldp_mac_offset2": MoPropertyMeta("lldp_mac_offset2", "lldpMacOffset2", "byte", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "mac_offset1": MoPropertyMeta("mac_offset1", "macOffset1", "byte", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
        "mac_offset2": MoPropertyMeta("mac_offset2", "macOffset2", "byte", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []),
        "mac_offset_sub00": MoPropertyMeta("mac_offset_sub00", "macOffsetSub00", "byte", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
        "mac_offset_sub01": MoPropertyMeta("mac_offset_sub01", "macOffsetSub01", "byte", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], []),
        "mac_offset_sub02": MoPropertyMeta("mac_offset_sub02", "macOffsetSub02", "byte", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], []),
        "mac_offset_sub03": MoPropertyMeta("mac_offset_sub03", "macOffsetSub03", "byte", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], []),
        "mac_offset_sub10": MoPropertyMeta("mac_offset_sub10", "macOffsetSub10", "byte", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, [], []),
        "mac_offset_sub11": MoPropertyMeta("mac_offset_sub11", "macOffsetSub11", "byte", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], []),
        "mac_offset_sub12": MoPropertyMeta("mac_offset_sub12", "macOffsetSub12", "byte", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, [], []),
        "mac_offset_sub13": MoPropertyMeta("mac_offset_sub13", "macOffsetSub13", "byte", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8000, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "lldpMacOffset1": "lldp_mac_offset1", 
        "lldpMacOffset2": "lldp_mac_offset2", 
        "macOffset1": "mac_offset1", 
        "macOffset2": "mac_offset2", 
        "macOffsetSub00": "mac_offset_sub00", 
        "macOffsetSub01": "mac_offset_sub01", 
        "macOffsetSub02": "mac_offset_sub02", 
        "macOffsetSub03": "mac_offset_sub03", 
        "macOffsetSub10": "mac_offset_sub10", 
        "macOffsetSub11": "mac_offset_sub11", 
        "macOffsetSub12": "mac_offset_sub12", 
        "macOffsetSub13": "mac_offset_sub13", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.lldp_mac_offset1 = None
        self.lldp_mac_offset2 = None
        self.mac_offset1 = None
        self.mac_offset2 = None
        self.mac_offset_sub00 = None
        self.mac_offset_sub01 = None
        self.mac_offset_sub02 = None
        self.mac_offset_sub03 = None
        self.mac_offset_sub10 = None
        self.mac_offset_sub11 = None
        self.mac_offset_sub12 = None
        self.mac_offset_sub13 = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorUplinkHwAddrCap", parent_mo_or_dn, **kwargs)
