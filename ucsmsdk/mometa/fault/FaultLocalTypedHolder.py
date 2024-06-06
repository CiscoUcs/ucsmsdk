"""This module contains the general information for FaultLocalTypedHolder ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FaultLocalTypedHolderConsts:
    TYPE_ANY = "any"
    TYPE_CHASSIS_PROFILE = "chassis-profile"
    TYPE_CONFIGURATION = "configuration"
    TYPE_CONNECTIVITY = "connectivity"
    TYPE_ENVIRONMENTAL = "environmental"
    TYPE_EQUIPMENT = "equipment"
    TYPE_FORWARD = "forward"
    TYPE_FSM = "fsm"
    TYPE_GENERIC = "generic"
    TYPE_INVENTORY = "inventory"
    TYPE_MANAGEMENT = "management"
    TYPE_NETWORK = "network"
    TYPE_OPERATIONAL = "operational"
    TYPE_POWER = "power"
    TYPE_SECURITY = "security"
    TYPE_SERVER = "server"
    TYPE_SYSDEBUG = "sysdebug"
    TYPE_UNMANAGEABLE_HARDWARE = "unmanageable-hardware"


class FaultLocalTypedHolder(ManagedObject):
    """This is FaultLocalTypedHolder class."""

    consts = FaultLocalTypedHolderConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("FaultLocalTypedHolder", "faultLocalTypedHolder", "type-[type]", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["admin", "fault"], ['faultHolder'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "total_faults": MoPropertyMeta("total_faults", "totalFaults", "ulong", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x20, None, None, None, ["any", "chassis-profile", "configuration", "connectivity", "environmental", "equipment", "forward", "fsm", "generic", "inventory", "management", "network", "operational", "power", "security", "server", "sysdebug", "unmanageable-hardware"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "totalFaults": "total_faults", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.name = None
        self.sacl = None
        self.status = None
        self.total_faults = None

        ManagedObject.__init__(self, "FaultLocalTypedHolder", parent_mo_or_dn, **kwargs)
