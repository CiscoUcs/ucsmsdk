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
    naming_props = set([u'name'])

    mo_meta = MoMeta("BiosVProfile", "biosVProfile", "bios-prof-[name]", VersionMeta.Version111j, "InputOutput", 0x1ff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'orgOrg'], [u'biosVfACPI10Support', u'biosVfASPMSupport', u'biosVfAllUSBDevices', u'biosVfAltitude', u'biosVfAssertNMIOnPERR', u'biosVfAssertNMIOnSERR', u'biosVfBootOptionRetry', u'biosVfCPUHardwarePowerManagement', u'biosVfCPUPerformance', u'biosVfCPUPowerManagement', u'biosVfConsistentDeviceNameControl', u'biosVfConsoleRedirection', u'biosVfCoreMultiProcessing', u'biosVfDDR3VoltageSelection', u'biosVfDRAMClockThrottling', u'biosVfDirectCacheAccess', u'biosVfDramRefreshRate', u'biosVfEnergyPerformanceTuning', u'biosVfEnhancedIntelSpeedStepTech', u'biosVfEnhancedPowerCappingSupport', u'biosVfExecuteDisableBit', u'biosVfFRB2Timer', u'biosVfFrequencyFloorOverride', u'biosVfFrontPanelLockout', u'biosVfIOEMezz1OptionROM', u'biosVfIOENVMe1OptionROM', u'biosVfIOENVMe2OptionROM', u'biosVfIOESlot1OptionROM', u'biosVfIOESlot2OptionROM', u'biosVfIntegratedGraphics', u'biosVfIntegratedGraphicsApertureSize', u'biosVfIntelEntrySASRAIDModule', u'biosVfIntelHyperThreadingTech', u'biosVfIntelTrustedExecutionTechnology', u'biosVfIntelTurboBoostTech', u'biosVfIntelVTForDirectedIO', u'biosVfIntelVirtualizationTechnology', u'biosVfInterleaveConfiguration', u'biosVfLocalX2Apic', u'biosVfLvDIMMSupport', u'biosVfMaxVariableMTRRSetting', u'biosVfMaximumMemoryBelow4GB', u'biosVfMemoryMappedIOAbove4GB', u'biosVfMirroringMode', u'biosVfNUMAOptimized', u'biosVfOSBootWatchdogTimer', u'biosVfOSBootWatchdogTimerPolicy', u'biosVfOSBootWatchdogTimerTimeout', u'biosVfOnboardGraphics', u'biosVfOnboardSATAController', u'biosVfOnboardStorage', u'biosVfOptionROMEnable', u'biosVfOptionROMLoad', u'biosVfOutOfBandManagement', u'biosVfPCHSATAMode', u'biosVfPCILOMPortsConfiguration', u'biosVfPCIROMCLP', u'biosVfPCISlotLinkSpeed', u'biosVfPCISlotOptionROMEnable', u'biosVfPOSTErrorPause', u'biosVfPSTATECoordination', u'biosVfPackageCStateLimit', u'biosVfProcessorC1E', u'biosVfProcessorC3Report', u'biosVfProcessorC6Report', u'biosVfProcessorC7Report', u'biosVfProcessorCMCI', u'biosVfProcessorCState', u'biosVfProcessorEnergyConfiguration', u'biosVfProcessorPrefetchConfig', u'biosVfQPILinkFrequencySelect', u'biosVfQPISnoopMode', u'biosVfQuietBoot', u'biosVfRedirectionAfterBIOSPOST', u'biosVfResumeOnACPowerLoss', u'biosVfSBMezz1OptionROM', u'biosVfSBNVMe1OptionROM', u'biosVfSIOC1OptionROM', u'biosVfSIOC2OptionROM', u'biosVfScrubPolicies', u'biosVfSelectMemoryRASConfiguration', u'biosVfSerialPortAEnable', u'biosVfSparingMode', u'biosVfSriovConfig', u'biosVfTPMPendingOperation', u'biosVfTPMSupport', u'biosVfTrustedPlatformModule', u'biosVfUCSMBootModeControl', u'biosVfUCSMBootOrderRuleControl', u'biosVfUEFIOSUseLegacyVideo', u'biosVfUSBBootConfig', u'biosVfUSBConfiguration', u'biosVfUSBFrontPanelAccessLock', u'biosVfUSBPortConfiguration', u'biosVfUSBSystemIdlePowerOptimizingSetting', u'biosVfVGAPriority', u'biosVfWorkloadConfiguration'], ["Add", "Get", "Remove", "Set"])

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
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
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
