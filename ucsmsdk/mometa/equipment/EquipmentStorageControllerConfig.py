"""This module contains the general information for EquipmentStorageControllerConfig ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentStorageControllerConfigConsts:
    INT_ID_NONE = "none"
    PNUOS_SUPPORTED_FALSE = "false"
    PNUOS_SUPPORTED_NO = "no"
    PNUOS_SUPPORTED_TRUE = "true"
    PNUOS_SUPPORTED_YES = "yes"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SUB_OEM_ID_UNDEFINED = "undefined"


class EquipmentStorageControllerConfig(ManagedObject):
    """This is EquipmentStorageControllerConfig class."""

    consts = EquipmentStorageControllerConfigConsts()
    naming_props = set(['vendor', 'device', 'subvendor', 'subdevice'])

    mo_meta = MoMeta("EquipmentStorageControllerConfig", "equipmentStorageControllerConfig", "ven-[vendor]-dev-[device]-subven-[subvendor]-subdev-[subdevice]", VersionMeta.Version225a, "InputOutput", 0xfff, [], [""], ['diagSrvCapProvider', 'equipmentBladeCapProvider', 'equipmentCatalogCapProvider', 'equipmentChassisCapProvider', 'equipmentDbgPluginCapProvider', 'equipmentIOExpanderCapProvider', 'equipmentMgmtCapProvider', 'equipmentMgmtExtCapProvider', 'equipmentRackEnclosureCapProvider', 'equipmentRackUnitCapProvider', 'equipmentServerUnitCapProvider', 'equipmentSiocCapProvider', 'equipmentStorageEncCapProvider', 'equipmentSwitchCapProvider'], ['equipmentPciSlotSubOEMIdEntry'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version225a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version225a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "device": MoPropertyMeta("device", "device", "uint", VersionMeta.Version225a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version225a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version225a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "min_version": MoPropertyMeta("min_version", "minVersion", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version225a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "pnuos_supported": MoPropertyMeta("pnuos_supported", "pnuosSupported", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version225a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version225a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version225a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version225a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "storage_bios_mode": MoPropertyMeta("storage_bios_mode", "storageBiosMode", "string", VersionMeta.Version225a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "storagepid": MoPropertyMeta("storagepid", "storagepid", "string", VersionMeta.Version225a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "sub_oem_id": MoPropertyMeta("sub_oem_id", "subOemId", "string", VersionMeta.Version225a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["undefined"], ["0-65535"]),
        "subdevice": MoPropertyMeta("subdevice", "subdevice", "uint", VersionMeta.Version225a, MoPropertyMeta.NAMING, 0x200, None, None, None, [], []),
        "subvendor": MoPropertyMeta("subvendor", "subvendor", "uint", VersionMeta.Version225a, MoPropertyMeta.NAMING, 0x400, None, None, None, [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "uint", VersionMeta.Version225a, MoPropertyMeta.NAMING, 0x800, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "device": "device", 
        "dn": "dn", 
        "intId": "int_id", 
        "minVersion": "min_version", 
        "name": "name", 
        "pnuosSupported": "pnuos_supported", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
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
        self.min_version = None
        self.name = None
        self.pnuos_supported = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.storage_bios_mode = None
        self.storagepid = None
        self.sub_oem_id = None

        ManagedObject.__init__(self, "EquipmentStorageControllerConfig", parent_mo_or_dn, **kwargs)
