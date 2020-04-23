"""This module contains the general information for FirmwareServerChassisConstraint ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareServerChassisConstraintConsts:
    pass


class FirmwareServerChassisConstraint(ManagedObject):
    """This is FirmwareServerChassisConstraint class."""

    consts = FirmwareServerChassisConstraintConsts()
    naming_props = set(['serverModel'])

    mo_meta = MoMeta("FirmwareServerChassisConstraint", "firmwareServerChassisConstraint", "server-chassis-constraint-[server_model]", VersionMeta.Version323a, "InputOutput", 0x3f, [], ["read-only"], ['firmwareConstraints'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version323a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "min_cmc_version": MoPropertyMeta("min_cmc_version", "minCmcVersion", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "server_model": MoPropertyMeta("server_model", "serverModel", "string", VersionMeta.Version323a, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
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

    def __init__(self, parent_mo_or_dn, server_model, **kwargs):
        self._dirty_mask = 0
        self.server_model = server_model
        self.child_action = None
        self.min_cmc_version = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareServerChassisConstraint", parent_mo_or_dn, **kwargs)
