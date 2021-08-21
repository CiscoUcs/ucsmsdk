"""This module contains the general information for BiosVProfile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVProfileConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    REBOOT_ON_UPDATE_FALSE = "false"
    REBOOT_ON_UPDATE_NO = "no"
    REBOOT_ON_UPDATE_TRUE = "true"
    REBOOT_ON_UPDATE_YES = "yes"


class BiosVProfile(ManagedObject):
    """This is BiosVProfile class."""

    consts = BiosVProfileConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("BiosVProfile", "biosVProfile", "bios-prof-[name]", VersionMeta.Version111j, "InputOutput", 0x1ff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['orgOrg'], ['biosTokenFeatureGroup', 'biosVfACPI10Support', 'biosVfASPMSupport', 'biosVfAllUSBDevices', 'biosVfAltitude', 'biosVfAssertNMIOnPERR', 'biosVfAssertNMIOnSERR', 'biosVfBMEDMAMitigation', 'biosVfBootOptionRetry', 'biosVfCPUHardwarePowerManagement', 'biosVfCPUPerformance', 'biosVfConsistentDeviceNameControl', 'biosVfConsoleRedirection', 'biosVfCoreMultiProcessing', 'biosVfDDR3VoltageSelection', 'biosVfDRAMClockThrottling', 'biosVfDirectCacheAccess', 'biosVfDramRefreshRate', 'biosVfEnergyPerformanceTuning', 'biosVfEnhancedIntelSpeedStepTech', 'biosVfEnhancedPowerCappingSupport', 'biosVfExecuteDisableBit', 'biosVfFRB2Timer', 'biosVfFrequencyFloorOverride', 'biosVfFrontPanelLockout', 'biosVfIOEMezz1OptionROM', 'biosVfIOENVMe1OptionROM', 'biosVfIOENVMe2OptionROM', 'biosVfIOESlot1OptionROM', 'biosVfIOESlot2OptionROM', 'biosVfIntegratedGraphics', 'biosVfIntegratedGraphicsApertureSize', 'biosVfIntelEntrySASRAIDModule', 'biosVfIntelHyperThreadingTech', 'biosVfIntelTrustedExecutionTechnology', 'biosVfIntelTurboBoostTech', 'biosVfIntelVTForDirectedIO', 'biosVfIntelVirtualizationTechnology', 'biosVfInterleaveConfiguration', 'biosVfLocalX2Apic', 'biosVfLvDIMMSupport', 'biosVfMaxVariableMTRRSetting', 'biosVfMaximumMemoryBelow4GB', 'biosVfMemoryMappedIOAbove4GB', 'biosVfMirroringMode', 'biosVfNUMAOptimized', 'biosVfOSBootWatchdogTimer', 'biosVfOSBootWatchdogTimerPolicy', 'biosVfOSBootWatchdogTimerTimeout', 'biosVfOnboardGraphics', 'biosVfOnboardSATAController', 'biosVfOnboardStorage', 'biosVfOptionROMEnable', 'biosVfOptionROMLoad', 'biosVfOutOfBandManagement', 'biosVfPCHSATAMode', 'biosVfPCILOMPortsConfiguration', 'biosVfPCIROMCLP', 'biosVfPCISlotLinkSpeed', 'biosVfPCISlotOptionROMEnable', 'biosVfPOSTErrorPause', 'biosVfPSTATECoordination', 'biosVfPackageCStateLimit', 'biosVfPanicAndHighWatermark', 'biosVfProcessorC1E', 'biosVfProcessorC3Report', 'biosVfProcessorC6Report', 'biosVfProcessorC7Report', 'biosVfProcessorCMCI', 'biosVfProcessorCState', 'biosVfProcessorEnergyConfiguration', 'biosVfProcessorPrefetchConfig', 'biosVfQPILinkFrequencySelect', 'biosVfQPISnoopMode', 'biosVfQuietBoot', 'biosVfRedirectionAfterBIOSPOST', 'biosVfResumeOnACPowerLoss', 'biosVfSBMezz1OptionROM', 'biosVfSBNVMe1OptionROM', 'biosVfSIOC1OptionROM', 'biosVfSIOC2OptionROM', 'biosVfScrubPolicies', 'biosVfSelectMemoryRASConfiguration', 'biosVfSerialPortAEnable', 'biosVfSparingMode', 'biosVfSriovConfig', 'biosVfTPMPendingOperation', 'biosVfTPMSupport', 'biosVfTrustedPlatformModule', 'biosVfUCSMBootModeControl', 'biosVfUCSMBootOrderRuleControl', 'biosVfUEFIOSUseLegacyVideo', 'biosVfUSBBootConfig', 'biosVfUSBConfiguration', 'biosVfUSBFrontPanelAccessLock', 'biosVfUSBPortConfiguration', 'biosVfUSBSystemIdlePowerOptimizingSetting', 'biosVfVGAPriority', 'biosVfWorkloadConfiguration'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111j, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "reboot_on_update": MoPropertyMeta("reboot_on_update", "rebootOnUpdate", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rebootOnUpdate": "reboot_on_update", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.reboot_on_update = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "BiosVProfile", parent_mo_or_dn, **kwargs)
