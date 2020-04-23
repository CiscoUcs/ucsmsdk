"""This module contains the general information for FaultHolder ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FaultHolderConsts:
    IS_PINNING_CLEARED_FALSE = "false"
    IS_PINNING_CLEARED_NO = "no"
    IS_PINNING_CLEARED_TRUE = "true"
    IS_PINNING_CLEARED_YES = "yes"


class FaultHolder(ManagedObject):
    """This is FaultHolder class."""

    consts = FaultHolderConsts()
    naming_props = set([])

    mo_meta = MoMeta("FaultHolder", "faultHolder", "fault", VersionMeta.Version101e, "InputOutput", 0x1f, [], ["admin", "fault"], ['topRoot'], ['faultLocalTypedHolder', 'faultPolicy', 'faultSuppressPolicy', 'faultSuppressTask'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "is_pinning_cleared": MoPropertyMeta("is_pinning_cleared", "isPinningCleared", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "last_pin_time": MoPropertyMeta("last_pin_time", "lastPinTime", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "total_faults": MoPropertyMeta("total_faults", "totalFaults", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "isPinningCleared": "is_pinning_cleared", 
        "lastPinTime": "last_pin_time", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "totalFaults": "total_faults", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.is_pinning_cleared = None
        self.last_pin_time = None
        self.name = None
        self.sacl = None
        self.status = None
        self.total_faults = None

        ManagedObject.__init__(self, "FaultHolder", **kwargs)
