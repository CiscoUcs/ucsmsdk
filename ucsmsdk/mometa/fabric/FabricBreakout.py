"""This module contains the general information for FabricBreakout ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FabricBreakoutConsts():
    BREAKOUT_TYPE_10G_4X = "10g-4x"
    BREAKOUT_TYPE_UNKNOWN = "unknown"


class FabricBreakout(ManagedObject):
    """This is FabricBreakout class."""

    consts = FabricBreakoutConsts()
    naming_props = set([u'slotId', u'portId'])

    mo_meta = MoMeta("FabricBreakout", "fabricBreakout", "breakout-slot-[slot_id]-port-[port_id]", None, "InputOutput", 0xffL, [], ["admin", "ext-lan-config", "ext-lan-policy", "ext-san-config", "ext-san-policy"], [u'fabricCablingSw'], [], [None])

    prop_meta = {
        "breakout_type": MoPropertyMeta("breakout_type", "breakoutType", "string", None, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["10g-4x", "unknown"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "port_id": MoPropertyMeta("port_id", "portId", "uint", None, MoPropertyMeta.NAMING, 0x10L, None, None, None, [], ["1-48"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", None, MoPropertyMeta.NAMING, 0x40L, None, None, None, [], ["1-2"]), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "breakoutType": "breakout_type", 
        "childAction": "child_action", 
        "dn": "dn", 
        "portId": "port_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotId": "slot_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, slot_id, port_id, **kwargs):
        self._dirty_mask = 0
        self.slot_id = slot_id
        self.port_id = port_id
        self.breakout_type = None
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FabricBreakout", parent_mo_or_dn, **kwargs)

