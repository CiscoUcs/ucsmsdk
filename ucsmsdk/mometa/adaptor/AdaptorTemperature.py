"""This module contains the general information for AdaptorTemperature ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorTemperatureConsts:
    pass


class AdaptorTemperature(ManagedObject):
    """This is AdaptorTemperature class."""

    consts = AdaptorTemperatureConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorTemperature", "adaptorTemperature", "temperature-[id]", VersionMeta.Version436a, "InputOutput", 0x3f, [], ["read-only"], ['adaptorUnit'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version436a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version436a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version436a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version436a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version436a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version436a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "string", VersionMeta.Version436a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version436a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "value": MoPropertyMeta("value", "value", "uint", VersionMeta.Version436a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "id": "id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotId": "slot_id", 
        "status": "status", 
        "value": "value", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.flt_aggr = None
        self.sacl = None
        self.slot_id = None
        self.status = None
        self.value = None

        ManagedObject.__init__(self, "AdaptorTemperature", parent_mo_or_dn, **kwargs)
