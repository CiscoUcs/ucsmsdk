"""This module contains the general information for TrigClientToken ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class TrigClientTokenConsts:
    OPER_STATE_EXPIRED = "expired"
    OPER_STATE_VALID = "valid"


class TrigClientToken(ManagedObject):
    """This is TrigClientToken class."""

    consts = TrigClientTokenConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("TrigClientToken", "trigClientToken", "clienttoken-[id]", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["read-only"], ['trigTriggered'], [], [None])

    prop_meta = {
        "activity_ts": MoPropertyMeta("activity_ts", "activityTs", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["expired", "valid"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "activityTs": "activity_ts", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "operState": "oper_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.activity_ts = None
        self.child_action = None
        self.oper_state = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "TrigClientToken", parent_mo_or_dn, **kwargs)
