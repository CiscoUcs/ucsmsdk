"""This module contains the general information for EquipmentPciDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentPciDefConsts:
    DEVICE_TYPE_BROADCOM57712_NIC = "Broadcom57712Nic"
    DEVICE_TYPE_BROADCOM_NIC = "BroadcomNic"
    DEVICE_TYPE_EMULEX_FC = "EmulexFC"
    DEVICE_TYPE_EMULEX_NIC = "EmulexNic"
    DEVICE_TYPE_FUSION_HBA = "FusionHba"
    DEVICE_TYPE_GPU_AMD = "GpuAmd"
    DEVICE_TYPE_GPU_AMD_MI = "GpuAmdMi"
    DEVICE_TYPE_GPU_INTEL = "GpuIntel"
    DEVICE_TYPE_GPU_NVIDIA = "GpuNvidia"
    DEVICE_TYPE_INTEL_ICH10_RHBA = "IntelICH10RHba"
    DEVICE_TYPE_INTEL_NIC = "IntelNic"
    DEVICE_TYPE_LSIMEGA_RAID3008 = "LSIMegaRaid3008"
    DEVICE_TYPE_LAGUNA_BEACH = "LagunaBeach"
    DEVICE_TYPE_LAGUNA_BEACH_PLUS = "LagunaBeachPlus"
    DEVICE_TYPE_LAGUNA_ROCK = "LagunaRock"
    DEVICE_TYPE_LAGUNA_ROCK_PLUS = "LagunaRockPlus"
    DEVICE_TYPE_LEWISBURG_PSATA = "LewisburgPSata"
    DEVICE_TYPE_LEWISBURG_PSATA_AHCI = "LewisburgPSataAhci"
    DEVICE_TYPE_LEWISBURG_SSATA_SW_RAID = "LewisburgSSataSwRaid"
    DEVICE_TYPE_LODI_HBA = "LodiHba"
    DEVICE_TYPE_LSI1064_EHBA = "Lsi1064EHba"
    DEVICE_TYPE_LSI1068_EHBA = "Lsi1068EHba"
    DEVICE_TYPE_LSI_EXTERNAL_MEGA_RAID_HBA = "LsiExternalMegaRaidHba"
    DEVICE_TYPE_LSI_MEGA_RAID_HBA = "LsiMegaRaidHba"
    DEVICE_TYPE_LSI_WALNUT_CREEK_HBA = "LsiWalnutCreekHba"
    DEVICE_TYPE_M2_HW_RAID_MARVELL_HBA = "M2HwRaidMarvellHba"
    DEVICE_TYPE_MAX_COUNT = "MaxCount"
    DEVICE_TYPE_MELLANOX_NIC = "MellanoxNic"
    DEVICE_TYPE_MENLO_EMULEX_HBA = "MenloEmulexHba"
    DEVICE_TYPE_MENLO_QLOGIC_FC_HBA = "MenloQlogicFcHba"
    DEVICE_TYPE_MEZZ_DUBLIN_QLOGIC_FC_HBA = "MezzDublinQlogicFcHba"
    DEVICE_TYPE_MEZZ_SCHULZ_QLOGIC_FC_HBA = "MezzSchulzQlogicFcHba"
    DEVICE_TYPE_MEZZ_TIGER_SHARK_HBA = "MezzTigerSharkHba"
    DEVICE_TYPE_MIAMI_BEACH = "MiamiBeach"
    DEVICE_TYPE_MIAMI_ROCK = "MiamiRock"
    DEVICE_TYPE_NVME_HBA = "NvmeHba"
    DEVICE_TYPE_NVME_INTEL_HBA = "NvmeIntelHba"
    DEVICE_TYPE_NVME_MEZZ = "NvmeMezz"
    DEVICE_TYPE_NVME_WD_HBA = "NvmeWdHba"
    DEVICE_TYPE_PCI_DUBLIN_QLOGIC_FC_HBA = "PciDublinQlogicFcHba"
    DEVICE_TYPE_PCI_EVEREST_NIC = "PciEverestNic"
    DEVICE_TYPE_PCI_INTEL_E810_NIC = "PciIntelE810Nic"
    DEVICE_TYPE_PCI_INTEL_X520_NIC = "PciIntelX520Nic"
    DEVICE_TYPE_PCI_INTEL_X550_NIC = "PciIntelX550Nic"
    DEVICE_TYPE_PCI_INTEL_X710_NIC = "PciIntelX710Nic"
    DEVICE_TYPE_PCI_MPCISCO_NIC = "PciMPCiscoNic"
    DEVICE_TYPE_PCI_NIANTIC_NIC = "PciNianticNic"
    DEVICE_TYPE_PCI_PLX_SWITCH = "PciPlxSwitch"
    DEVICE_TYPE_PCI_QLOGIC8362_FC_HBA = "PciQlogic8362FcHba"
    DEVICE_TYPE_PCI_QLOGIC_BIG_BEAR = "PciQlogicBigBear"
    DEVICE_TYPE_PCI_SCHULZ_QLOGIC_FC_HBA = "PciSchulzQlogicFcHba"
    DEVICE_TYPE_PCI_TIGER_SHARK_HBA = "PciTigerSharkHba"
    DEVICE_TYPE_PISMO_BEACH = "PismoBeach"
    DEVICE_TYPE_PISMO_ROCK = "PismoRock"
    DEVICE_TYPE_QLOGIC_FC = "QlogicFC"
    DEVICE_TYPE_QLOGIC_NIC = "QlogicNic"
    DEVICE_TYPE_SATA_HBA = "SataHba"
    DEVICE_TYPE_TALLADEGA = "Talladega"
    DEVICE_TYPE_UNKNOWN = "Unknown"
    DEVICE_TYPE_WELLSBURG_HBA = "WellsburgHba"
    DEVICE_TYPE_ZUMA_BEACH = "ZumaBeach"
    DEVICE_TYPE_ZUMA_ROCK = "ZumaRock"
    INT_ID_NONE = "none"
    MODEL_CHECK_FALSE = "false"
    MODEL_CHECK_NO = "no"
    MODEL_CHECK_TRUE = "true"
    MODEL_CHECK_YES = "yes"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentPciDef(ManagedObject):
    """This is EquipmentPciDef class."""

    consts = EquipmentPciDefConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("EquipmentPciDef", "equipmentPciDef", "pci-[name]", VersionMeta.Version141i, "InputOutput", 0xff, [], [""], ['adaptorFruCapProvider', 'adaptorUnit', 'equipmentCoprocessorUnitCapProvider', 'equipmentGraphicsCardCapProvider', 'equipmentLocalDiskControllerCapProvider', 'equipmentPciSwitchCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "device": MoPropertyMeta("device", "device", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "device_type": MoPropertyMeta("device_type", "deviceType", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Broadcom57712Nic", "BroadcomNic", "EmulexFC", "EmulexNic", "FusionHba", "GpuAmd", "GpuAmdMi", "GpuIntel", "GpuNvidia", "IntelICH10RHba", "IntelNic", "LSIMegaRaid3008", "LagunaBeach", "LagunaBeachPlus", "LagunaRock", "LagunaRockPlus", "LewisburgPSata", "LewisburgPSataAhci", "LewisburgSSataSwRaid", "LodiHba", "Lsi1064EHba", "Lsi1068EHba", "LsiExternalMegaRaidHba", "LsiMegaRaidHba", "LsiWalnutCreekHba", "M2HwRaidMarvellHba", "MaxCount", "MellanoxNic", "MenloEmulexHba", "MenloQlogicFcHba", "MezzDublinQlogicFcHba", "MezzSchulzQlogicFcHba", "MezzTigerSharkHba", "MiamiBeach", "MiamiRock", "NvmeHba", "NvmeIntelHba", "NvmeMezz", "NvmeWdHba", "PciDublinQlogicFcHba", "PciEverestNic", "PciIntelE810Nic", "PciIntelX520Nic", "PciIntelX550Nic", "PciIntelX710Nic", "PciMPCiscoNic", "PciNianticNic", "PciPlxSwitch", "PciQlogic8362FcHba", "PciQlogicBigBear", "PciSchulzQlogicFcHba", "PciTigerSharkHba", "PismoBeach", "PismoRock", "QlogicFC", "QlogicNic", "SataHba", "Talladega", "Unknown", "WellsburgHba", "ZumaBeach", "ZumaRock"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "model_check": MoPropertyMeta("model_check", "modelCheck", "string", VersionMeta.Version422d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x10, 1, 512, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "subdevice": MoPropertyMeta("subdevice", "subdevice", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "subvendor": MoPropertyMeta("subvendor", "subvendor", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "device": "device", 
        "deviceType": "device_type", 
        "dn": "dn", 
        "intId": "int_id", 
        "modelCheck": "model_check", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "subdevice": "subdevice", 
        "subvendor": "subvendor", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.device = None
        self.device_type = None
        self.int_id = None
        self.model_check = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.subdevice = None
        self.subvendor = None
        self.vendor = None

        ManagedObject.__init__(self, "EquipmentPciDef", parent_mo_or_dn, **kwargs)
