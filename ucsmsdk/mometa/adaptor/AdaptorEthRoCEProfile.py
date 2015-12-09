"""This module contains the general information for AdaptorEthRoCEProfile ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class AdaptorEthRoCEProfileConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"


class AdaptorEthRoCEProfile(ManagedObject):
    """This is AdaptorEthRoCEProfile class."""

    consts = AdaptorEthRoCEProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorEthRoCEProfile", "adaptorEthRoCEProfile", "eth-roce", VersionMeta.Version223a, "InputOutput", 0x1ffL, [], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"], [u'adaptorHostEthIf', u'adaptorHostEthIfProfile'], [], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "memory_regions": MoPropertyMeta("memory_regions", "memoryRegions", "uint", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["1-524288"]), 
        "queue_pairs": MoPropertyMeta("queue_pairs", "queuePairs", "uint", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], ["1-8192"]), 
        "resource_groups": MoPropertyMeta("resource_groups", "resourceGroups", "uint", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], ["1-128", "1-512"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x100L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "memoryRegions": "memory_regions", 
        "queuePairs": "queue_pairs", 
        "resourceGroups": "resource_groups", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.memory_regions = None
        self.queue_pairs = None
        self.resource_groups = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorEthRoCEProfile", parent_mo_or_dn, **kwargs)

