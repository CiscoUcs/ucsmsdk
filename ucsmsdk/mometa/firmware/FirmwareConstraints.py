"""This module contains the general information for FirmwareConstraints ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareConstraintsConsts:
    pass


class FirmwareConstraints(ManagedObject):
    """This is FirmwareConstraints class."""

    consts = FirmwareConstraintsConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareConstraints", "firmwareConstraints", "fw-constraints", VersionMeta.Version223a, "InputOutput", 0x1f, [], [""], ['diagSrvCapProvider', 'equipmentBladeCapProvider', 'equipmentCatalogCapProvider', 'equipmentChassisCapProvider', 'equipmentDbgPluginCapProvider', 'equipmentIOExpanderCapProvider', 'equipmentMgmtCapProvider', 'equipmentMgmtExtCapProvider', 'equipmentRackEnclosureCapProvider', 'equipmentRackUnitCapProvider', 'equipmentServerUnitCapProvider', 'equipmentSiocCapProvider', 'equipmentStorageEncCapProvider', 'equipmentSwitchCapProvider'], ['firmwareConnectionManagementChassisConstraint', 'firmwareDriveSecurityConstraint', 'firmwareDualVicChassisConstraint', 'firmwareDualVicServerConstraint', 'firmwarePCHStorageConfigConstraint', 'firmwarePcieNodeConstraint', 'firmwareProcessorTypeConstraint', 'firmwareRackPowerCapConstraint', 'firmwareSecondControllerChassisConstraint', 'firmwareSecondControllerServerConstraint', 'firmwareServerChassisConstraint', 'firmwareServerTypeConstraint', 'firmwareSinglePathChassisConstraint', 'firmwareTPMConstraint', 'firmwareVicSlotConstraint', 'firmwareVnicCdnConstraint', 'firmwareWaterbaySiocServerConstraint'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareConstraints", parent_mo_or_dn, **kwargs)
