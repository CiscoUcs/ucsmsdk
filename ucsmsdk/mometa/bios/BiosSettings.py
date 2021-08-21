"""This module contains the general information for BiosSettings ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosSettingsConsts:
    pass


class BiosSettings(ManagedObject):
    """This is BiosSettings class."""

    consts = BiosSettingsConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosSettings", "biosSettings", "bios-settings", VersionMeta.Version131c, "InputOutput", 0x1f, [], [""], ['biosUnit', 'capabilityCatalogue', 'computeDefaults', 'computePlatform'], ['biosTokenFeatureGroup', 'biosTokenParam', 'biosVfACPI10Support', 'biosVfASPMSupport', 'biosVfAllUSBDevices', 'biosVfAltitude', 'biosVfAssertNMIOnPERR', 'biosVfAssertNMIOnSERR', 'biosVfBMEDMAMitigation', 'biosVfBootOptionRetry', 'biosVfCPUHardwarePowerManagement', 'biosVfCPUPerformance', 'biosVfConsistentDeviceNameControl', 'biosVfConsoleRedirection', 'biosVfCoreMultiProcessing', 'biosVfDDR3VoltageSelection', 'biosVfDRAMClockThrottling', 'biosVfDirectCacheAccess', 'biosVfDramRefreshRate', 'biosVfEnergyPerformanceTuning', 'biosVfEnhancedIntelSpeedStepTech', 'biosVfEnhancedPowerCappingSupport', 'biosVfExecuteDisableBit', 'biosVfFRB2Timer', 'biosVfFrequencyFloorOverride', 'biosVfFrontPanelLockout', 'biosVfIOEMezz1OptionROM', 'biosVfIOENVMe1OptionROM', 'biosVfIOENVMe2OptionROM', 'biosVfIOESlot1OptionROM', 'biosVfIOESlot2OptionROM', 'biosVfIntegratedGraphics', 'biosVfIntegratedGraphicsApertureSize', 'biosVfIntelEntrySASRAIDModule', 'biosVfIntelHyperThreadingTech', 'biosVfIntelTrustedExecutionTechnology', 'biosVfIntelTurboBoostTech', 'biosVfIntelVTForDirectedIO', 'biosVfIntelVirtualizationTechnology', 'biosVfInterleaveConfiguration', 'biosVfLocalX2Apic', 'biosVfLvDIMMSupport', 'biosVfMaxVariableMTRRSetting', 'biosVfMaximumMemoryBelow4GB', 'biosVfMemoryMappedIOAbove4GB', 'biosVfMirroringMode', 'biosVfNUMAOptimized', 'biosVfOSBootWatchdogTimer', 'biosVfOSBootWatchdogTimerPolicy', 'biosVfOSBootWatchdogTimerTimeout', 'biosVfOnboardGraphics', 'biosVfOnboardSATAController', 'biosVfOnboardStorage', 'biosVfOptionROMEnable', 'biosVfOptionROMLoad', 'biosVfOutOfBandManagement', 'biosVfPCHSATAMode', 'biosVfPCILOMPortsConfiguration', 'biosVfPCIROMCLP', 'biosVfPCISlotLinkSpeed', 'biosVfPCISlotOptionROMEnable', 'biosVfPOSTErrorPause', 'biosVfPSTATECoordination', 'biosVfPackageCStateLimit', 'biosVfPanicAndHighWatermark', 'biosVfProcessorC1E', 'biosVfProcessorC3Report', 'biosVfProcessorC6Report', 'biosVfProcessorC7Report', 'biosVfProcessorCMCI', 'biosVfProcessorCState', 'biosVfProcessorEnergyConfiguration', 'biosVfProcessorPrefetchConfig', 'biosVfQPILinkFrequencySelect', 'biosVfQPISnoopMode', 'biosVfQuietBoot', 'biosVfRedirectionAfterBIOSPOST', 'biosVfResumeOnACPowerLoss', 'biosVfSBMezz1OptionROM', 'biosVfSBNVMe1OptionROM', 'biosVfSIOC1OptionROM', 'biosVfSIOC2OptionROM', 'biosVfScrubPolicies', 'biosVfSelectMemoryRASConfiguration', 'biosVfSerialPortAEnable', 'biosVfSparingMode', 'biosVfSriovConfig', 'biosVfTPMPendingOperation', 'biosVfTPMSupport', 'biosVfTrustedPlatformModule', 'biosVfUCSMBootModeControl', 'biosVfUCSMBootOrderRuleControl', 'biosVfUEFIOSUseLegacyVideo', 'biosVfUSBBootConfig', 'biosVfUSBConfiguration', 'biosVfUSBFrontPanelAccessLock', 'biosVfUSBPortConfiguration', 'biosVfUSBSystemIdlePowerOptimizingSetting', 'biosVfVGAPriority', 'biosVfWorkloadConfiguration'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "BiosSettings", parent_mo_or_dn, **kwargs)
