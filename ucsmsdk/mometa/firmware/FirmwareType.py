"""This module contains the general information for FirmwareType ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareTypeConsts:
    EP_ADAPTOR = "adaptor"
    EP_BLADE_BIOS = "blade-bios"
    EP_BLADE_CONTROLLER = "blade-controller"
    EP_BOARD_CONTROLLER = "board-controller"
    EP_CATALOG = "catalog"
    EP_CHASSIS_BOARD_CONTROLLER = "chassis-board-controller"
    EP_CMC = "cmc"
    EP_DEBUG_PLUG_IN = "debug-plug-in"
    EP_DIAG = "diag"
    EP_FEX = "fex"
    EP_FLEXFLASH_CONTROLLER = "flexflash-controller"
    EP_GRAPHICS_CARD = "graphics-card"
    EP_HOST_HBA = "host-hba"
    EP_HOST_HBA_OPTIONROM = "host-hba-optionrom"
    EP_HOST_NIC = "host-nic"
    EP_HOST_NIC_OPTIONROM = "host-nic-optionrom"
    EP_IOCARD = "iocard"
    EP_LOCAL_DISK = "local-disk"
    EP_MGMT_EXT = "mgmt-ext"
    EP_PSU = "psu"
    EP_SAS_EXP_REG_FW = "sas-exp-reg-fw"
    EP_SAS_EXPANDER = "sas-expander"
    EP_STORAGE_CONTROLLER = "storage-controller"
    EP_STORAGE_CONTROLLER_ONBOARD_DEVICE = "storage-controller-onboard-device"
    EP_STORAGE_CONTROLLER_ONBOARD_DEVICE_CPLD = "storage-controller-onboard-device-cpld"
    EP_STORAGE_DEV_BRIDGE = "storage-dev-bridge"
    EP_STORAGE_NODE_CONTROLLER = "storage-node-controller"
    EP_SWITCH = "switch"
    EP_SWITCH_KERNEL = "switch-kernel"
    EP_SWITCH_SOFTWARE = "switch-software"
    EP_SYSTEM = "system"
    EP_UNSPECIFIED = "unspecified"
    FW_FPGA_REVISION_SUPPORTED_FALSE = "false"
    FW_FPGA_REVISION_SUPPORTED_NO = "no"
    FW_FPGA_REVISION_SUPPORTED_TRUE = "true"
    FW_FPGA_REVISION_SUPPORTED_YES = "yes"


class FirmwareType(ManagedObject):
    """This is FirmwareType class."""

    consts = FirmwareTypeConsts()
    naming_props = set([u'invTag'])

    mo_meta = MoMeta("FirmwareType", "firmwareType", "fw-type-[inv_tag]", VersionMeta.Version101e, "InputOutput", 0x7f, [], [""], [u'adaptorFruCapProvider', u'diagSrvCapProvider', u'equipmentBaseBoardCapProvider', u'equipmentBladeBiosCapProvider', u'equipmentBladeCapProvider', u'equipmentCatalogCapProvider', u'equipmentChassisCapProvider', u'equipmentDbgPluginCapProvider', u'equipmentFanModuleCapProvider', u'equipmentFexCapProvider', u'equipmentGemCapProvider', u'equipmentGraphicsCardCapProvider', u'equipmentHostIfCapProvider', u'equipmentIOCardCapProvider', u'equipmentIOExpanderCapProvider', u'equipmentLocalDiskCapProvider', u'equipmentLocalDiskControllerCapProvider', u'equipmentMemoryUnitCapProvider', u'equipmentMgmtCapProvider', u'equipmentMgmtExtCapProvider', u'equipmentOnboardDeviceDef', u'equipmentProcessorUnitCapProvider', u'equipmentPsuCapProvider', u'equipmentRackUnitCapProvider', u'equipmentSecurityUnitCapProvider', u'equipmentServerUnitCapProvider', u'equipmentStorageEncCapProvider', u'equipmentStorageSasExpanderCapProvider', u'equipmentSwitchCapProvider', u'equipmentSwitchIOCardCapProvider', u'equipmentTpmCapProvider'], [u'firmwareDependency'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "ep": MoPropertyMeta("ep", "ep", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["adaptor", "blade-bios", "blade-controller", "board-controller", "catalog", "chassis-board-controller", "cmc", "debug-plug-in", "diag", "fex", "flexflash-controller", "graphics-card", "host-hba", "host-hba-optionrom", "host-nic", "host-nic-optionrom", "iocard", "local-disk", "mgmt-ext", "psu", "sas-exp-reg-fw", "sas-expander", "storage-controller", "storage-controller-onboard-device", "storage-controller-onboard-device-cpld", "storage-dev-bridge", "storage-node-controller", "switch", "switch-kernel", "switch-software", "system", "unspecified"], []), 
        "fw_fpga_revision_supported": MoPropertyMeta("fw_fpga_revision_supported", "fwFpgaRevisionSupported", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "inv_tag": MoPropertyMeta("inv_tag", "invTag", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []), 
        "max_ver": MoPropertyMeta("max_ver", "maxVer", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "min_ver": MoPropertyMeta("min_ver", "minVer", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ep": "ep", 
        "fwFpgaRevisionSupported": "fw_fpga_revision_supported", 
        "invTag": "inv_tag", 
        "maxVer": "max_ver", 
        "minVer": "min_ver", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, inv_tag, **kwargs):
        self._dirty_mask = 0
        self.inv_tag = inv_tag
        self.child_action = None
        self.ep = None
        self.fw_fpga_revision_supported = None
        self.max_ver = None
        self.min_ver = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareType", parent_mo_or_dn, **kwargs)
