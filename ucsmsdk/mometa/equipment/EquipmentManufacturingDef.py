"""This module contains the general information for EquipmentManufacturingDef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentManufacturingDefConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentManufacturingDef(ManagedObject):
    """This is EquipmentManufacturingDef class."""

    consts = EquipmentManufacturingDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentManufacturingDef", "equipmentManufacturingDef", "manufacturing", VersionMeta.Version101e, "InputOutput", 0x7fL, [], [""], [u'adaptorFruCapProvider', u'diagSrvCapProvider', u'equipmentBaseBoardCapProvider', u'equipmentBladeBiosCapProvider', u'equipmentBladeCapProvider', u'equipmentCatalogCapProvider', u'equipmentChassisCapProvider', u'equipmentDbgPluginCapProvider', u'equipmentFanModuleCapProvider', u'equipmentFexCapProvider', u'equipmentGemCapProvider', u'equipmentGraphicsCardCapProvider', u'equipmentHostIfCapProvider', u'equipmentIOCardCapProvider', u'equipmentLocalDiskCapProvider', u'equipmentLocalDiskControllerCapProvider', u'equipmentMemoryUnitCapProvider', u'equipmentMgmtCapProvider', u'equipmentMgmtExtCapProvider', u'equipmentProcessorUnitCapProvider', u'equipmentPsuCapProvider', u'equipmentRackUnitCapProvider', u'equipmentSecurityUnitCapProvider', u'equipmentServerUnitCapProvider', u'equipmentStorageDevBridgeCapProvider', u'equipmentStorageSasExpanderCapProvider', u'equipmentSwitchCapProvider', u'equipmentSwitchIOCardCapProvider', u'equipmentSystemFruCapProvider', u'equipmentTpmCapProvider'], [], ["Get"])

    prop_meta = {
        "caption": MoPropertyMeta("caption", "caption", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "clei": MoPropertyMeta("clei", "clei", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "fru_major_type": MoPropertyMeta("fru_major_type", "fruMajorType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "fru_minor_type": MoPropertyMeta("fru_minor_type", "fruMinorType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oem_name": MoPropertyMeta("oem_name", "oemName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oem_part_number": MoPropertyMeta("oem_part_number", "oemPartNumber", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "part_number": MoPropertyMeta("part_number", "partNumber", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pid": MoPropertyMeta("pid", "pid", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "series": MoPropertyMeta("series", "series", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "sku": MoPropertyMeta("sku", "sku", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor_equipment_type": MoPropertyMeta("vendor_equipment_type", "vendorEquipmentType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "vid": MoPropertyMeta("vid", "vid", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "caption": "caption", 
        "childAction": "child_action", 
        "clei": "clei", 
        "descr": "descr", 
        "description": "description", 
        "dn": "dn", 
        "fruMajorType": "fru_major_type", 
        "fruMinorType": "fru_minor_type", 
        "intId": "int_id", 
        "name": "name", 
        "oemName": "oem_name", 
        "oemPartNumber": "oem_part_number", 
        "partNumber": "part_number", 
        "pid": "pid", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "series": "series", 
        "sku": "sku", 
        "status": "status", 
        "vendorEquipmentType": "vendor_equipment_type", 
        "vid": "vid", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.caption = None
        self.child_action = None
        self.clei = None
        self.descr = None
        self.description = None
        self.fru_major_type = None
        self.fru_minor_type = None
        self.int_id = None
        self.name = None
        self.oem_name = None
        self.oem_part_number = None
        self.part_number = None
        self.pid = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.series = None
        self.sku = None
        self.status = None
        self.vendor_equipment_type = None
        self.vid = None

        ManagedObject.__init__(self, "EquipmentManufacturingDef", parent_mo_or_dn, **kwargs)

