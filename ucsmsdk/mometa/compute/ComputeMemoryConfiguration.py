"""This module contains the general information for ComputeMemoryConfiguration ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeMemoryConfigurationConsts:
    ADMIN_MEMORY_STATE_POLICY = "policy"
    ADMIN_MEMORY_STATE_RESET_IN_PROGRESS = "reset-in-progress"
    ADMIN_MEMORY_STATE_RESET_MEMORY_ERRORS = "reset-memory-errors"
    BLACK_LISTING_DISABLED = "disabled"
    BLACK_LISTING_ENABLED = "enabled"


class ComputeMemoryConfiguration(ManagedObject):
    """This is ComputeMemoryConfiguration class."""

    consts = ComputeMemoryConfigurationConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeMemoryConfiguration", "computeMemoryConfiguration", "memmory-config", VersionMeta.Version221b, "InputOutput", 0x3f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], [], ["Get", "Set"])

    prop_meta = {
        "admin_memory_state": MoPropertyMeta("admin_memory_state", "adminMemoryState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["policy", "reset-in-progress", "reset-memory-errors"], []),
        "black_listing": MoPropertyMeta("black_listing", "blackListing", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "adminMemoryState": "admin_memory_state", 
        "blackListing": "black_listing", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_memory_state = None
        self.black_listing = None
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputeMemoryConfiguration", parent_mo_or_dn, **kwargs)
