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

    mo_meta = MoMeta("BiosSettings", "biosSettings", "bios-settings", VersionMeta.Version131c, "InputOutput", 0x1f, [], [""], [u'biosUnit', u'computeDefaults', u'computePlatform'], [u'biosVfACPI10Support', u'biosVfASPMSupport', u'biosVfAllUSBDevices', u'biosVfAltitude', u'biosVfAssertNMIOnPERR', u'biosVfAssertNMIOnSERR', u'biosVfBootOptionRetry', u'biosVfCPUHardwarePowerManagement', u'biosVfCPUPerformance', u'biosVfCPUPowerManagement', u'biosVfConsistentDeviceNameControl', u'biosVfConsoleRedirection', u'biosVfCoreMultiProcessing', u'biosVfDDR3VoltageSelection', u'biosVfDRAMClockThrottling', u'biosVfDirectCacheAccess', u'biosVfDramRefreshRate', u'biosVfEnergyPerformanceTuning', u'biosVfEnhancedIntelSpeedStepTech', u'biosVfEnhancedPowerCappingSupport', u'biosVfExecuteDisableBit', u'biosVfFRB2Timer', u'biosVfFrequencyFloorOverride', u'biosVfFrontPanelLockout', u'biosVfIOEMezz1OptionROM', u'biosVfIOENVMe1OptionROM', u'biosVfIOENVMe2OptionROM', u'biosVfIOESlot1OptionROM', u'biosVfIOESlot2OptionROM', u'biosVfIntegratedGraphics', u'biosVfIntegratedGraphicsApertureSize', u'biosVfIntelEntrySASRAIDModule', u'biosVfIntelHyperThreadingTech', u'biosVfIntelTrustedExecutionTechnology', u'biosVfIntelTurboBoostTech', u'biosVfIntelVTForDirectedIO', u'biosVfIntelVirtualizationTechnology', u'biosVfInterleaveConfiguration', u'biosVfLocalX2Apic', u'biosVfLvDIMMSupport', u'biosVfMaxVariableMTRRSetting', u'biosVfMaximumMemoryBelow4GB', u'biosVfMemoryMappedIOAbove4GB', u'biosVfMirroringMode', u'biosVfNUMAOptimized', u'biosVfOSBootWatchdogTimer', u'biosVfOSBootWatchdogTimerPolicy', u'biosVfOSBootWatchdogTimerTimeout', u'biosVfOnboardGraphics', u'biosVfOnboardSATAController', u'biosVfOnboardStorage', u'biosVfOptionROMEnable', u'biosVfOptionROMLoad', u'biosVfOutOfBandManagement', u'biosVfPCHSATAMode', u'biosVfPCILOMPortsConfiguration', u'biosVfPCIROMCLP', u'biosVfPCISlotLinkSpeed', u'biosVfPCISlotOptionROMEnable', u'biosVfPOSTErrorPause', u'biosVfPSTATECoordination', u'biosVfPackageCStateLimit', u'biosVfProcessorC1E', u'biosVfProcessorC3Report', u'biosVfProcessorC6Report', u'biosVfProcessorC7Report', u'biosVfProcessorCMCI', u'biosVfProcessorCState', u'biosVfProcessorEnergyConfiguration', u'biosVfProcessorPrefetchConfig', u'biosVfQPILinkFrequencySelect', u'biosVfQPISnoopMode', u'biosVfQuietBoot', u'biosVfRedirectionAfterBIOSPOST', u'biosVfResumeOnACPowerLoss', u'biosVfSBMezz1OptionROM', u'biosVfSBNVMe1OptionROM', u'biosVfSIOC1OptionROM', u'biosVfSIOC2OptionROM', u'biosVfScrubPolicies', u'biosVfSelectMemoryRASConfiguration', u'biosVfSerialPortAEnable', u'biosVfSparingMode', u'biosVfSriovConfig', u'biosVfTPMPendingOperation', u'biosVfTPMSupport', u'biosVfTrustedPlatformModule', u'biosVfUCSMBootModeControl', u'biosVfUCSMBootOrderRuleControl', u'biosVfUEFIOSUseLegacyVideo', u'biosVfUSBBootConfig', u'biosVfUSBConfiguration', u'biosVfUSBFrontPanelAccessLock', u'biosVfUSBPortConfiguration', u'biosVfUSBSystemIdlePowerOptimizingSetting', u'biosVfVGAPriority', u'biosVfWorkloadConfiguration'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
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
