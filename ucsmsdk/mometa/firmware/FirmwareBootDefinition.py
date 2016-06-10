"""This module contains the general information for FirmwareBootDefinition ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareBootDefinitionConsts:
    TYPE_ADAPTOR = "adaptor"
    TYPE_BLADE_BIOS = "blade-bios"
    TYPE_BLADE_CONTROLLER = "blade-controller"
    TYPE_BOARD_CONTROLLER = "board-controller"
    TYPE_CATALOG = "catalog"
    TYPE_CHASSIS_BOARD_CONTROLLER = "chassis-board-controller"
    TYPE_CMC = "cmc"
    TYPE_DEBUG_PLUG_IN = "debug-plug-in"
    TYPE_DIAG = "diag"
    TYPE_FEX = "fex"
    TYPE_FLEXFLASH_CONTROLLER = "flexflash-controller"
    TYPE_GRAPHICS_CARD = "graphics-card"
    TYPE_HOST_HBA = "host-hba"
    TYPE_HOST_HBA_OPTIONROM = "host-hba-optionrom"
    TYPE_HOST_NIC = "host-nic"
    TYPE_HOST_NIC_OPTIONROM = "host-nic-optionrom"
    TYPE_IOCARD = "iocard"
    TYPE_LOCAL_DISK = "local-disk"
    TYPE_MGMT_EXT = "mgmt-ext"
    TYPE_PSU = "psu"
    TYPE_SAS_EXP_REG_FW = "sas-exp-reg-fw"
    TYPE_SAS_EXPANDER = "sas-expander"
    TYPE_STORAGE_CONTROLLER = "storage-controller"
    TYPE_STORAGE_CONTROLLER_ONBOARD_DEVICE = "storage-controller-onboard-device"
    TYPE_STORAGE_CONTROLLER_ONBOARD_DEVICE_CPLD = "storage-controller-onboard-device-cpld"
    TYPE_STORAGE_DEV_BRIDGE = "storage-dev-bridge"
    TYPE_STORAGE_NODE_CONTROLLER = "storage-node-controller"
    TYPE_SWITCH = "switch"
    TYPE_SWITCH_KERNEL = "switch-kernel"
    TYPE_SWITCH_SOFTWARE = "switch-software"
    TYPE_SYSTEM = "system"
    TYPE_UNSPECIFIED = "unspecified"


class FirmwareBootDefinition(ManagedObject):
    """This is FirmwareBootDefinition class."""

    consts = FirmwareBootDefinitionConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareBootDefinition", "firmwareBootDefinition", "fw-boot-def", VersionMeta.Version101e, "InputOutput", 0x1f, [], ["admin"], [u'adaptorHostEthIf', u'adaptorHostFcIf', u'biosUnit', u'capabilityCatalogue', u'capabilityMgmtExtension', u'equipmentPsu', u'graphicsCard', u'mgmtController', u'storageController', u'storageLocalDisk', u'storageOnboardDevice', u'storageSasExpander'], [u'firmwareBootUnit', u'firmwareUcscInfo'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["adaptor", "blade-bios", "blade-controller", "board-controller", "catalog", "chassis-board-controller", "cmc", "debug-plug-in", "diag", "fex", "flexflash-controller", "graphics-card", "host-hba", "host-hba-optionrom", "host-nic", "host-nic-optionrom", "iocard", "local-disk", "mgmt-ext", "psu", "sas-exp-reg-fw", "sas-expander", "storage-controller", "storage-controller-onboard-device", "storage-controller-onboard-device-cpld", "storage-dev-bridge", "storage-node-controller", "switch", "switch-kernel", "switch-software", "system", "unspecified"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "FirmwareBootDefinition", parent_mo_or_dn, **kwargs)
