"""This module contains the general information for EpqosEgress ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EpqosEgressConsts:
    HOST_CONTROL_FULL = "full"
    HOST_CONTROL_FULL_WITH_EXCEPTION = "full-with-exception"
    HOST_CONTROL_NONE = "none"
    OPER_PRIO_BEST_EFFORT = "best-effort"
    OPER_PRIO_BRONZE = "bronze"
    OPER_PRIO_FC = "fc"
    OPER_PRIO_GOLD = "gold"
    OPER_PRIO_PLATINUM = "platinum"
    OPER_PRIO_SILVER = "silver"
    PRIO_BEST_EFFORT = "best-effort"
    PRIO_BRONZE = "bronze"
    PRIO_FC = "fc"
    PRIO_GOLD = "gold"
    PRIO_PLATINUM = "platinum"
    PRIO_SILVER = "silver"
    RATE_LINE_RATE = "line-rate"


class EpqosEgress(ManagedObject):
    """This is EpqosEgress class."""

    consts = EpqosEgressConsts()
    naming_props = set([])

    mo_meta = MoMeta("EpqosEgress", "epqosEgress", "egress", VersionMeta.Version101e, "InputOutput", 0x3ff, [], ["admin", "ls-network", "ls-network-policy", "ls-qos-policy", "read-only"], ['epqosDefinition'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "burst": MoPropertyMeta("burst", "burst", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-65535"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "host_control": MoPropertyMeta("host_control", "hostControl", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["full", "full-with-exception", "none"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_prio": MoPropertyMeta("oper_prio", "operPrio", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["best-effort", "bronze", "fc", "gold", "platinum", "silver"], []),
        "prio": MoPropertyMeta("prio", "prio", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["best-effort", "bronze", "fc", "gold", "platinum", "silver"], []),
        "rate": MoPropertyMeta("rate", "rate", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["line-rate"], ["8-100000000"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "burst": "burst", 
        "childAction": "child_action", 
        "dn": "dn", 
        "hostControl": "host_control", 
        "name": "name", 
        "operPrio": "oper_prio", 
        "prio": "prio", 
        "rate": "rate", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.burst = None
        self.child_action = None
        self.host_control = None
        self.name = None
        self.oper_prio = None
        self.prio = None
        self.rate = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EpqosEgress", parent_mo_or_dn, **kwargs)
