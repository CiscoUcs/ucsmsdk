"""This module contains the general information for EquipmentDriveSecCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentDriveSecCapConsts:
    IS_HX_SEC_CAP_NO = "no"
    IS_HX_SEC_CAP_YES = "yes"
    IS_SUPPORTED_NO = "no"
    IS_SUPPORTED_YES = "yes"


class EquipmentDriveSecCap(ManagedObject):
    """This is EquipmentDriveSecCap class."""

    consts = EquipmentDriveSecCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentDriveSecCap", "equipmentDriveSecCap", "drive-sec-cap", VersionMeta.Version321d, "InputOutput", 0x1f, [], ["read-only"], ['equipmentBladeCapProvider', 'equipmentLocalDiskCapProvider', 'equipmentLocalDiskControllerCapProvider', 'equipmentRackUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "is_hx_sec_cap": MoPropertyMeta("is_hx_sec_cap", "isHxSecCap", "string", VersionMeta.Version422d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "is_supported": MoPropertyMeta("is_supported", "isSupported", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "min_version": MoPropertyMeta("min_version", "minVersion", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "isHxSecCap": "is_hx_sec_cap", 
        "isSupported": "is_supported", 
        "minVersion": "min_version", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.is_hx_sec_cap = None
        self.is_supported = None
        self.min_version = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentDriveSecCap", parent_mo_or_dn, **kwargs)
