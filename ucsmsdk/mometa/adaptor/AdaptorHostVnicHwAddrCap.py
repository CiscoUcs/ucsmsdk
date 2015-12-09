"""This module contains the general information for AdaptorHostVnicHwAddrCap ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class AdaptorHostVnicHwAddrCapConsts():
    pass


class AdaptorHostVnicHwAddrCap(ManagedObject):
    """This is AdaptorHostVnicHwAddrCap class."""

    consts = AdaptorHostVnicHwAddrCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorHostVnicHwAddrCap", "adaptorHostVnicHwAddrCap", "hwaddr-hostvnic", VersionMeta.Version302c, "InputOutput", 0x1ffL, [], ["read-only"], [u'adaptorFruCapProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "mac_offset1": MoPropertyMeta("mac_offset1", "macOffset1", "byte", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], []), 
        "mac_offset2": MoPropertyMeta("mac_offset2", "macOffset2", "byte", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], []), 
        "mac_offset_vnic_from": MoPropertyMeta("mac_offset_vnic_from", "macOffsetVnicFrom", "byte", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], []), 
        "mac_offset_vnic_to": MoPropertyMeta("mac_offset_vnic_to", "macOffsetVnicTo", "byte", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x100L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "macOffset1": "mac_offset1", 
        "macOffset2": "mac_offset2", 
        "macOffsetVnicFrom": "mac_offset_vnic_from", 
        "macOffsetVnicTo": "mac_offset_vnic_to", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.mac_offset1 = None
        self.mac_offset2 = None
        self.mac_offset_vnic_from = None
        self.mac_offset_vnic_to = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorHostVnicHwAddrCap", parent_mo_or_dn, **kwargs)

