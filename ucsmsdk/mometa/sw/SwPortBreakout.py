"""This module contains the general information for SwPortBreakout ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwPortBreakoutConsts:
    BREAKOUT_TYPE_10G_4X = "10g-4x"
    BREAKOUT_TYPE_25G_4X = "25g-4x"
    BREAKOUT_TYPE_UNKNOWN = "unknown"


class SwPortBreakout(ManagedObject):
    """This is SwPortBreakout class."""

    consts = SwPortBreakoutConsts()
    naming_props = set(['slotId', 'portId'])

    mo_meta = MoMeta("SwPortBreakout", "swPortBreakout", "breakout-slot-[slot_id]-port-[port_id]", VersionMeta.Version311e, "InputOutput", 0xff, [], ["admin"], ['swExtUtility'], [], [None])

    prop_meta = {
        "breakout_type": MoPropertyMeta("breakout_type", "breakoutType", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["10g-4x", "25g-4x", "unknown"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version311e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version311e, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-108"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version311e, MoPropertyMeta.NAMING, 0x40, None, None, None, [], ["1-2"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
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

        ManagedObject.__init__(self, "SwPortBreakout", parent_mo_or_dn, **kwargs)
