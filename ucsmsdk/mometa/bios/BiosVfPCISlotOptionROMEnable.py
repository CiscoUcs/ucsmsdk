"""This module contains the general information for BiosVfPCISlotOptionROMEnable ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfPCISlotOptionROMEnableConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_PCIE_SLOT_HBAOPTION_ROM_DISABLED = "disabled"
    VP_PCIE_SLOT_HBAOPTION_ROM_ENABLED = "enabled"
    VP_PCIE_SLOT_HBAOPTION_ROM_LEGACY_ONLY = "legacy-only"
    VP_PCIE_SLOT_HBAOPTION_ROM_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE_SLOT_HBAOPTION_ROM_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PCIE_SLOT_HBAOPTION_ROM_UEFI_ONLY = "uefi-only"
    VP_PCIE_SLOT_MLOMOPTION_ROM_DISABLED = "disabled"
    VP_PCIE_SLOT_MLOMOPTION_ROM_ENABLED = "enabled"
    VP_PCIE_SLOT_MLOMOPTION_ROM_LEGACY_ONLY = "legacy-only"
    VP_PCIE_SLOT_MLOMOPTION_ROM_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE_SLOT_MLOMOPTION_ROM_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PCIE_SLOT_MLOMOPTION_ROM_UEFI_ONLY = "uefi-only"
    VP_PCIE_SLOT_N1_OPTION_ROM_DISABLED = "disabled"
    VP_PCIE_SLOT_N1_OPTION_ROM_ENABLED = "enabled"
    VP_PCIE_SLOT_N1_OPTION_ROM_LEGACY_ONLY = "legacy-only"
    VP_PCIE_SLOT_N1_OPTION_ROM_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE_SLOT_N1_OPTION_ROM_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PCIE_SLOT_N1_OPTION_ROM_UEFI_ONLY = "uefi-only"
    VP_PCIE_SLOT_N2_OPTION_ROM_DISABLED = "disabled"
    VP_PCIE_SLOT_N2_OPTION_ROM_ENABLED = "enabled"
    VP_PCIE_SLOT_N2_OPTION_ROM_LEGACY_ONLY = "legacy-only"
    VP_PCIE_SLOT_N2_OPTION_ROM_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE_SLOT_N2_OPTION_ROM_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PCIE_SLOT_N2_OPTION_ROM_UEFI_ONLY = "uefi-only"
    VP_PCIE_SLOT_SASOPTION_ROM_DISABLED = "disabled"
    VP_PCIE_SLOT_SASOPTION_ROM_ENABLED = "enabled"
    VP_PCIE_SLOT_SASOPTION_ROM_LEGACY_ONLY = "legacy-only"
    VP_PCIE_SLOT_SASOPTION_ROM_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE_SLOT_SASOPTION_ROM_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PCIE_SLOT_SASOPTION_ROM_UEFI_ONLY = "uefi-only"
    VP_SLOT10_STATE_DISABLED = "disabled"
    VP_SLOT10_STATE_ENABLED = "enabled"
    VP_SLOT10_STATE_LEGACY_ONLY = "legacy-only"
    VP_SLOT10_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT10_STATE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_SLOT10_STATE_UEFI_ONLY = "uefi-only"
    VP_SLOT1_STATE_DISABLED = "disabled"
    VP_SLOT1_STATE_ENABLED = "enabled"
    VP_SLOT1_STATE_LEGACY_ONLY = "legacy-only"
    VP_SLOT1_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT1_STATE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_SLOT1_STATE_UEFI_ONLY = "uefi-only"
    VP_SLOT2_STATE_DISABLED = "disabled"
    VP_SLOT2_STATE_ENABLED = "enabled"
    VP_SLOT2_STATE_LEGACY_ONLY = "legacy-only"
    VP_SLOT2_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT2_STATE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_SLOT2_STATE_UEFI_ONLY = "uefi-only"
    VP_SLOT3_STATE_DISABLED = "disabled"
    VP_SLOT3_STATE_ENABLED = "enabled"
    VP_SLOT3_STATE_LEGACY_ONLY = "legacy-only"
    VP_SLOT3_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT3_STATE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_SLOT3_STATE_UEFI_ONLY = "uefi-only"
    VP_SLOT4_STATE_DISABLED = "disabled"
    VP_SLOT4_STATE_ENABLED = "enabled"
    VP_SLOT4_STATE_LEGACY_ONLY = "legacy-only"
    VP_SLOT4_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT4_STATE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_SLOT4_STATE_UEFI_ONLY = "uefi-only"
    VP_SLOT5_STATE_DISABLED = "disabled"
    VP_SLOT5_STATE_ENABLED = "enabled"
    VP_SLOT5_STATE_LEGACY_ONLY = "legacy-only"
    VP_SLOT5_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT5_STATE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_SLOT5_STATE_UEFI_ONLY = "uefi-only"
    VP_SLOT6_STATE_DISABLED = "disabled"
    VP_SLOT6_STATE_ENABLED = "enabled"
    VP_SLOT6_STATE_LEGACY_ONLY = "legacy-only"
    VP_SLOT6_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT6_STATE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_SLOT6_STATE_UEFI_ONLY = "uefi-only"
    VP_SLOT7_STATE_DISABLED = "disabled"
    VP_SLOT7_STATE_ENABLED = "enabled"
    VP_SLOT7_STATE_LEGACY_ONLY = "legacy-only"
    VP_SLOT7_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT7_STATE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_SLOT7_STATE_UEFI_ONLY = "uefi-only"
    VP_SLOT8_STATE_DISABLED = "disabled"
    VP_SLOT8_STATE_ENABLED = "enabled"
    VP_SLOT8_STATE_LEGACY_ONLY = "legacy-only"
    VP_SLOT8_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT8_STATE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_SLOT8_STATE_UEFI_ONLY = "uefi-only"
    VP_SLOT9_STATE_DISABLED = "disabled"
    VP_SLOT9_STATE_ENABLED = "enabled"
    VP_SLOT9_STATE_LEGACY_ONLY = "legacy-only"
    VP_SLOT9_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT9_STATE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_SLOT9_STATE_UEFI_ONLY = "uefi-only"
    VP_SLOT_MEZZ_STATE_DISABLED = "disabled"
    VP_SLOT_MEZZ_STATE_ENABLED = "enabled"
    VP_SLOT_MEZZ_STATE_LEGACY_ONLY = "legacy-only"
    VP_SLOT_MEZZ_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_MEZZ_STATE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_SLOT_MEZZ_STATE_UEFI_ONLY = "uefi-only"


class BiosVfPCISlotOptionROMEnable(ManagedObject):
    """This is BiosVfPCISlotOptionROMEnable class."""

    consts = BiosVfPCISlotOptionROMEnableConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfPCISlotOptionROMEnable", "biosVfPCISlotOptionROMEnable", "PCI-Slot-OptionROM-Enable", VersionMeta.Version202m, "InputOutput", 0xfffff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosSettings', 'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202m, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "vp_pc_ie_slot_hba_option_rom": MoPropertyMeta("vp_pc_ie_slot_hba_option_rom", "vpPCIeSlotHBAOptionROM", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
        "vp_pc_ie_slot_mlom_option_rom": MoPropertyMeta("vp_pc_ie_slot_mlom_option_rom", "vpPCIeSlotMLOMOptionROM", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
        "vp_pc_ie_slot_n1_option_rom": MoPropertyMeta("vp_pc_ie_slot_n1_option_rom", "vpPCIeSlotN1OptionROM", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
        "vp_pc_ie_slot_n2_option_rom": MoPropertyMeta("vp_pc_ie_slot_n2_option_rom", "vpPCIeSlotN2OptionROM", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
        "vp_pc_ie_slot_sas_option_rom": MoPropertyMeta("vp_pc_ie_slot_sas_option_rom", "vpPCIeSlotSASOptionROM", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
        "vp_slot10_state": MoPropertyMeta("vp_slot10_state", "vpSlot10State", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
        "vp_slot1_state": MoPropertyMeta("vp_slot1_state", "vpSlot1State", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
        "vp_slot2_state": MoPropertyMeta("vp_slot2_state", "vpSlot2State", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
        "vp_slot3_state": MoPropertyMeta("vp_slot3_state", "vpSlot3State", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
        "vp_slot4_state": MoPropertyMeta("vp_slot4_state", "vpSlot4State", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
        "vp_slot5_state": MoPropertyMeta("vp_slot5_state", "vpSlot5State", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
        "vp_slot6_state": MoPropertyMeta("vp_slot6_state", "vpSlot6State", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
        "vp_slot7_state": MoPropertyMeta("vp_slot7_state", "vpSlot7State", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
        "vp_slot8_state": MoPropertyMeta("vp_slot8_state", "vpSlot8State", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
        "vp_slot9_state": MoPropertyMeta("vp_slot9_state", "vpSlot9State", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x80000, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
        "vp_slot_mezz_state": MoPropertyMeta("vp_slot_mezz_state", "vpSlotMezzState", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpPCIeSlotHBAOptionROM": "vp_pc_ie_slot_hba_option_rom", 
        "vpPCIeSlotMLOMOptionROM": "vp_pc_ie_slot_mlom_option_rom", 
        "vpPCIeSlotN1OptionROM": "vp_pc_ie_slot_n1_option_rom", 
        "vpPCIeSlotN2OptionROM": "vp_pc_ie_slot_n2_option_rom", 
        "vpPCIeSlotSASOptionROM": "vp_pc_ie_slot_sas_option_rom", 
        "vpSlot10State": "vp_slot10_state", 
        "vpSlot1State": "vp_slot1_state", 
        "vpSlot2State": "vp_slot2_state", 
        "vpSlot3State": "vp_slot3_state", 
        "vpSlot4State": "vp_slot4_state", 
        "vpSlot5State": "vp_slot5_state", 
        "vpSlot6State": "vp_slot6_state", 
        "vpSlot7State": "vp_slot7_state", 
        "vpSlot8State": "vp_slot8_state", 
        "vpSlot9State": "vp_slot9_state", 
        "vpSlotMezzState": "vp_slot_mezz_state", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_pc_ie_slot_hba_option_rom = None
        self.vp_pc_ie_slot_mlom_option_rom = None
        self.vp_pc_ie_slot_n1_option_rom = None
        self.vp_pc_ie_slot_n2_option_rom = None
        self.vp_pc_ie_slot_sas_option_rom = None
        self.vp_slot10_state = None
        self.vp_slot1_state = None
        self.vp_slot2_state = None
        self.vp_slot3_state = None
        self.vp_slot4_state = None
        self.vp_slot5_state = None
        self.vp_slot6_state = None
        self.vp_slot7_state = None
        self.vp_slot8_state = None
        self.vp_slot9_state = None
        self.vp_slot_mezz_state = None

        ManagedObject.__init__(self, "BiosVfPCISlotOptionROMEnable", parent_mo_or_dn, **kwargs)
