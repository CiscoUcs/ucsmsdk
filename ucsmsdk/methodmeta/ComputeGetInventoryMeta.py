"""This module contains the meta information of ComputeGetInventory ExternalMethod."""

from ..ucscoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ComputeGetInventory", "computeGetInventory", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_faults_only": MethodPropertyMeta("InFaultsOnly", "inFaultsOnly", "Xs:string", "Version142b", "Input", False),
    "out_blade_cap_provider_config": MethodPropertyMeta("OutBladeCapProviderConfig", "outBladeCapProviderConfig", "ConfigSet", "Version142b", "Output", True),
    "out_chassis_cap_provider_config": MethodPropertyMeta("OutChassisCapProviderConfig", "outChassisCapProviderConfig", "ConfigSet", "Version142b", "Output", True),
    "out_chassis_config": MethodPropertyMeta("OutChassisConfig", "outChassisConfig", "ConfigSet", "Version142b", "Output", True),
    "out_fi_config": MethodPropertyMeta("OutFIConfig", "outFIConfig", "ConfigSet", "Version142b", "Output", True),
    "out_faults_only": MethodPropertyMeta("OutFaultsOnly", "outFaultsOnly", "Xs:string", "Version142b", "Output", False),
    "out_fex_cap_provider_config": MethodPropertyMeta("OutFexCapProviderConfig", "outFexCapProviderConfig", "ConfigSet", "Version142b", "Output", True),
    "out_fex_config": MethodPropertyMeta("OutFexConfig", "outFexConfig", "ConfigSet", "Version142b", "Output", True),
    "out_gem_cap_provider_config": MethodPropertyMeta("OutGemCapProviderConfig", "outGemCapProviderConfig", "ConfigSet", "Version142b", "Output", True),
    "out_io_card_cap_provider_config": MethodPropertyMeta("OutIOCardCapProviderConfig", "outIOCardCapProviderConfig", "ConfigSet", "Version142b", "Output", True),
    "out_logical_config": MethodPropertyMeta("OutLogicalConfig", "outLogicalConfig", "ConfigSet", "Version142b", "Output", True),
    "out_mgmt_if_config": MethodPropertyMeta("OutMgmtIfConfig", "outMgmtIfConfig", "ConfigSet", "Version142b", "Output", True),
    "out_physical_config": MethodPropertyMeta("OutPhysicalConfig", "outPhysicalConfig", "ConfigSet", "Version142b", "Output", True),
    "out_rack_unit_cap_provider_config": MethodPropertyMeta("OutRackUnitCapProviderConfig", "outRackUnitCapProviderConfig", "ConfigSet", "Version142b", "Output", True),
    "out_switch_cap_provider_config": MethodPropertyMeta("OutSwitchCapProviderConfig", "outSwitchCapProviderConfig", "ConfigSet", "Version142b", "Output", True),
    "out_top_system_config": MethodPropertyMeta("OutTopSystemConfig", "outTopSystemConfig", "ConfigConfig", "Version142b", "Output", True),
    "out_total_faults": MethodPropertyMeta("OutTotalFaults", "outTotalFaults", "Xs:unsignedLong", "Version142b", "Output", False),
    "out_typed_fault_holder_config": MethodPropertyMeta("OutTypedFaultHolderConfig", "outTypedFaultHolderConfig", "ConfigSet", "Version142b", "Output", True),
    "out_vnic_ipv4_pooled_addr_config": MethodPropertyMeta("OutVnicIpv4PooledAddrConfig", "outVnicIpv4PooledAddrConfig", "ConfigSet", "Version142b", "Output", True),
    "out_vnic_ipv4_prof_derived_addr_config": MethodPropertyMeta("OutVnicIpv4ProfDerivedAddrConfig", "outVnicIpv4ProfDerivedAddrConfig", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inFaultsOnly": "in_faults_only",
    "outBladeCapProviderConfig": "out_blade_cap_provider_config",
    "outChassisCapProviderConfig": "out_chassis_cap_provider_config",
    "outChassisConfig": "out_chassis_config",
    "outFIConfig": "out_fi_config",
    "outFaultsOnly": "out_faults_only",
    "outFexCapProviderConfig": "out_fex_cap_provider_config",
    "outFexConfig": "out_fex_config",
    "outGemCapProviderConfig": "out_gem_cap_provider_config",
    "outIOCardCapProviderConfig": "out_io_card_cap_provider_config",
    "outLogicalConfig": "out_logical_config",
    "outMgmtIfConfig": "out_mgmt_if_config",
    "outPhysicalConfig": "out_physical_config",
    "outRackUnitCapProviderConfig": "out_rack_unit_cap_provider_config",
    "outSwitchCapProviderConfig": "out_switch_cap_provider_config",
    "outTopSystemConfig": "out_top_system_config",
    "outTotalFaults": "out_total_faults",
    "outTypedFaultHolderConfig": "out_typed_fault_holder_config",
    "outVnicIpv4PooledAddrConfig": "out_vnic_ipv4_pooled_addr_config",
    "outVnicIpv4ProfDerivedAddrConfig": "out_vnic_ipv4_prof_derived_addr_config",
}
