"""This module contains the general information for EquipmentInbandMgmtCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentInbandMgmtCapConsts:
    IS_SUPPORTED_NO = "no"
    IS_SUPPORTED_YES = "yes"


class EquipmentInbandMgmtCap(ManagedObject):
    """This is EquipmentInbandMgmtCap class."""

    consts = EquipmentInbandMgmtCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentInbandMgmtCap", "equipmentInbandMgmtCap", "ib-mgmt-cap", VersionMeta.Version221b, "InputOutput", 0x1f, [], ["read-only"], ['equipmentBladeCapProvider', 'equipmentRackUnitCapProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "is_supported": MoPropertyMeta("is_supported", "isSupported", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "min_cimc_version": MoPropertyMeta("min_cimc_version", "minCimcVersion", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "min_cmc_version": MoPropertyMeta("min_cmc_version", "minCmcVersion", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "isSupported": "is_supported", 
        "minCimcVersion": "min_cimc_version", 
        "minCmcVersion": "min_cmc_version", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.is_supported = None
        self.min_cimc_version = None
        self.min_cmc_version = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentInbandMgmtCap", parent_mo_or_dn, **kwargs)
