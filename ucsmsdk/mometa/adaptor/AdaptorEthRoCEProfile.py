"""This module contains the general information for AdaptorEthRoCEProfile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorEthRoCEProfileConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    COS_ANY = "any"
    COS_BEST_EFFORT = "best-effort"
    COS_BRONZE = "bronze"
    COS_GOLD = "gold"
    COS_PLATINUM = "platinum"
    COS_SILVER = "silver"
    PRIO_BEST_EFFORT = "best-effort"
    PRIO_BRONZE = "bronze"
    PRIO_FC = "fc"
    PRIO_GOLD = "gold"
    PRIO_PLATINUM = "platinum"
    PRIO_SILVER = "silver"
    V1_DISABLED = "disabled"
    V1_ENABLED = "enabled"
    V2_DISABLED = "disabled"
    V2_ENABLED = "enabled"


class AdaptorEthRoCEProfile(ManagedObject):
    """This is AdaptorEthRoCEProfile class."""

    consts = AdaptorEthRoCEProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorEthRoCEProfile", "adaptorEthRoCEProfile", "eth-roce", VersionMeta.Version223a, "InputOutput", 0x1fff, [], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"], ['adaptorHostEthIf', 'adaptorHostEthIfProfile', 'adaptorVmmqConnDef'], [], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cos": MoPropertyMeta("cos", "cos", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["any", "best-effort", "bronze", "gold", "platinum", "silver"], ["0-6", "255-255"]),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "memory_regions": MoPropertyMeta("memory_regions", "memoryRegions", "uint", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-524288"]),
        "prio": MoPropertyMeta("prio", "prio", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["best-effort", "bronze", "fc", "gold", "platinum", "silver"], []),
        "queue_pairs": MoPropertyMeta("queue_pairs", "queuePairs", "uint", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["1-8192"]),
        "resource_groups": MoPropertyMeta("resource_groups", "resourceGroups", "uint", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["1-128"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "v1": MoPropertyMeta("v1", "v1", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["disabled", "enabled"], []),
        "v2": MoPropertyMeta("v2", "v2", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["disabled", "enabled"], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "cos": "cos", 
        "dn": "dn", 
        "memoryRegions": "memory_regions", 
        "prio": "prio", 
        "queuePairs": "queue_pairs", 
        "resourceGroups": "resource_groups", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "v1": "v1", 
        "v2": "v2", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.cos = None
        self.memory_regions = None
        self.prio = None
        self.queue_pairs = None
        self.resource_groups = None
        self.sacl = None
        self.status = None
        self.v1 = None
        self.v2 = None

        ManagedObject.__init__(self, "AdaptorEthRoCEProfile", parent_mo_or_dn, **kwargs)
