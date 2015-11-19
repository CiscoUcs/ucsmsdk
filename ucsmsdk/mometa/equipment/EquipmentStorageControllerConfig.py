"""This module contains the general information for EquipmentStorageControllerConfig ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentStorageControllerConfigConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SUB_OEM_ID_UNDEFINED = "undefined"


class EquipmentStorageControllerConfig(ManagedObject):
    """This is EquipmentStorageControllerConfig class."""

    consts = EquipmentStorageControllerConfigConsts()
    naming_props = set([u'vendor', u'device', u'subvendor', u'subdevice'])

    mo_meta = MoMeta("EquipmentStorageControllerConfig", "equipmentStorageControllerConfig", "ven-[vendor]-dev-[device]-subven-[subvendor]-subdev-[subdevice]", VersionMeta.Version225a, "InputOutput", 0x7ffL, [], [""], [u'diagSrvCapProvider', u'equipmentBladeCapProvider', u'equipmentCatalogCapProvider', u'equipmentChassisCapProvider', u'equipmentDbgPluginCapProvider', u'equipmentMgmtCapProvider', u'equipmentMgmtExtCapProvider', u'equipmentRackUnitCapProvider', u'equipmentSwitchCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version225a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version225a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "device": MoPropertyMeta("device", "device", "uint", VersionMeta.Version225a, MoPropertyMeta.NAMING, 0x4L, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version225a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version225a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version225a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version225a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version225a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version225a, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version225a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "storage_bios_mode": MoPropertyMeta("storage_bios_mode", "storageBiosMode", "string", VersionMeta.Version225a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "storagepid": MoPropertyMeta("storagepid", "storagepid", "string", VersionMeta.Version225a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "sub_oem_id": MoPropertyMeta("sub_oem_id", "subOemId", "string", VersionMeta.Version225a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["undefined"], ["0-4294967295"]), 
        "subdevice": MoPropertyMeta("subdevice", "subdevice", "uint", VersionMeta.Version225a, MoPropertyMeta.NAMING, 0x100L, None, None, None, [], []), 
        "subvendor": MoPropertyMeta("subvendor", "subvendor", "uint", VersionMeta.Version225a, MoPropertyMeta.NAMING, 0x200L, None, None, None, [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "uint", VersionMeta.Version225a, MoPropertyMeta.NAMING, 0x400L, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "device": "device", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
        "storageBiosMode": "storage_bios_mode", 
        "storagepid": "storagepid", 
        "subOemId": "sub_oem_id", 
        "subdevice": "subdevice", 
        "subvendor": "subvendor", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, vendor, device, subvendor, subdevice, **kwargs):
        self._dirty_mask = 0
        self.vendor = vendor
        self.device = device
        self.subvendor = subvendor
        self.subdevice = subdevice
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.status = None
        self.storage_bios_mode = None
        self.storagepid = None
        self.sub_oem_id = None

        ManagedObject.__init__(self, "EquipmentStorageControllerConfig", parent_mo_or_dn, **kwargs)

