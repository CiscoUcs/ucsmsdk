"""This module contains the general information for EquipmentPicture ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentPictureConsts():
    TYPE_BACK = "back"
    TYPE_BOTTOM = "bottom"
    TYPE_FRONT = "front"
    TYPE_FRONT_BOTTOM_SCALED = "front-bottom-scaled"
    TYPE_FRONT_TOP_SCALED = "front-top-scaled"
    TYPE_LEFT = "left"
    TYPE_RIGHT = "right"
    TYPE_TOP = "top"
    TYPE_TOP_SCALED = "top-scaled"
    TYPE_UNKNOWN = "unknown"


class EquipmentPicture(ManagedObject):
    """This is EquipmentPicture class."""

    consts = EquipmentPictureConsts()
    naming_props = set([u'type'])

    mo_meta = MoMeta("EquipmentPicture", "equipmentPicture", "picture-[type]", VersionMeta.Version141i, "InputOutput", 0x3fL, [], [""], [u'adaptorFruCapProvider', u'diagSrvCapProvider', u'equipmentBaseBoardCapProvider', u'equipmentBladeBiosCapProvider', u'equipmentBladeCapProvider', u'equipmentCatalogCapProvider', u'equipmentChassisCapProvider', u'equipmentDbgPluginCapProvider', u'equipmentFanModuleCapProvider', u'equipmentFexCapProvider', u'equipmentGemCapProvider', u'equipmentGraphicsCardCapProvider', u'equipmentHostIfCapProvider', u'equipmentIOCardCapProvider', u'equipmentLocalDiskCapProvider', u'equipmentLocalDiskControllerCapProvider', u'equipmentMemoryUnitCapProvider', u'equipmentMgmtCapProvider', u'equipmentMgmtExtCapProvider', u'equipmentProcessorUnitCapProvider', u'equipmentPsuCapProvider', u'equipmentRackUnitCapProvider', u'equipmentSecurityUnitCapProvider', u'equipmentServerUnitCapProvider', u'equipmentStorageDevBridgeCapProvider', u'equipmentStorageSasExpanderCapProvider', u'equipmentSwitchCapProvider', u'equipmentSwitchIOCardCapProvider', u'equipmentSystemFruCapProvider', u'equipmentTpmCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "file_name": MoPropertyMeta("file_name", "fileName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x20L, None, None, None, ["back", "bottom", "front", "front-bottom-scaled", "front-top-scaled", "left", "right", "top", "top-scaled", "unknown"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fileName": "file_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.file_name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPicture", parent_mo_or_dn, **kwargs)

