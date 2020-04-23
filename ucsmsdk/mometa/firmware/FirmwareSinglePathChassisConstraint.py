"""This module contains the general information for FirmwareSinglePathChassisConstraint ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareSinglePathChassisConstraintConsts:
    pass


class FirmwareSinglePathChassisConstraint(ManagedObject):
    """This is FirmwareSinglePathChassisConstraint class."""

    consts = FirmwareSinglePathChassisConstraintConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareSinglePathChassisConstraint", "firmwareSinglePathChassisConstraint", "single-path-chassis-constraint", VersionMeta.Version323a, "InputOutput", 0x1f, [], ["read-only"], ['firmwareConstraints'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version323a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "min_cmc_version": MoPropertyMeta("min_cmc_version", "minCmcVersion", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "server_model": MoPropertyMeta("server_model", "serverModel", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "minCmcVersion": "min_cmc_version", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serverModel": "server_model", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.min_cmc_version = None
        self.sacl = None
        self.server_model = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareSinglePathChassisConstraint", parent_mo_or_dn, **kwargs)
