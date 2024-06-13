"""This module contains the general information for EquipmentFirmwareUpdateRestriction ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentFirmwareUpdateRestrictionConsts:
    pass


class EquipmentFirmwareUpdateRestriction(ManagedObject):
    """This is EquipmentFirmwareUpdateRestriction class."""

    consts = EquipmentFirmwareUpdateRestrictionConsts()
    naming_props = set(['restrictionId'])

    mo_meta = MoMeta("EquipmentFirmwareUpdateRestriction", "equipmentFirmwareUpdateRestriction", "firmwareUpdateRestriction-[restriction_id]", VersionMeta.Version434a, "InputOutput", 0x7f, [], [""], ['adaptorFruCapProvider', 'diagSrvCapProvider', 'equipmentBaseBoardCapProvider', 'equipmentBladeBiosCapProvider', 'equipmentBladeCapProvider', 'equipmentCatalogCapProvider', 'equipmentChassisCapProvider', 'equipmentCoprocessorUnitCapProvider', 'equipmentCpldCapProvider', 'equipmentCrossFabricModuleCapProvider', 'equipmentDbgPluginCapProvider', 'equipmentFanModuleCapProvider', 'equipmentFexCapProvider', 'equipmentGemCapProvider', 'equipmentGraphicsCardCapProvider', 'equipmentHostIfCapProvider', 'equipmentIOCardCapProvider', 'equipmentIOExpanderCapProvider', 'equipmentIntelAmcCapProvider', 'equipmentLocalDiskCapProvider', 'equipmentLocalDiskControllerCapProvider', 'equipmentMemoryUnitCapProvider', 'equipmentMgmtCapProvider', 'equipmentMgmtExtCapProvider', 'equipmentMiniStorageCapProvider', 'equipmentPciSwitchCapProvider', 'equipmentPcieConnectorCapProvider', 'equipmentPcieNodeCapProvider', 'equipmentPersistentMemoryUnitCapProvider', 'equipmentProcessorUnitCapProvider', 'equipmentPsuCapProvider', 'equipmentRackEnclosureCapProvider', 'equipmentRackUnitCapProvider', 'equipmentRetimerCapProvider', 'equipmentSecurityUnitCapProvider', 'equipmentServerUnitCapProvider', 'equipmentSiocCapProvider', 'equipmentStorageEncCapProvider', 'equipmentStorageNvmeSwitchCapProvider', 'equipmentStorageSasExpanderCapProvider', 'equipmentSwitchCapProvider', 'equipmentSwitchIOCardCapProvider', 'equipmentTpmCapProvider', 'equipmentUbmCapProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "fw_restriction_versions": MoPropertyMeta("fw_restriction_versions", "fwRestrictionVersions", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], []),
        "restriction_id": MoPropertyMeta("restriction_id", "restrictionId", "ushort", VersionMeta.Version434a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fwRestrictionVersions": "fw_restriction_versions", 
        "restrictionId": "restriction_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, restriction_id, **kwargs):
        self._dirty_mask = 0
        self.restriction_id = restriction_id
        self.child_action = None
        self.fw_restriction_versions = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentFirmwareUpdateRestriction", parent_mo_or_dn, **kwargs)
