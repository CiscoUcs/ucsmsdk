"""This module contains the general information for StatsThresholdClass ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StatsThresholdClassConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    STATS_CLASS_ID_ADAPTOR_ETH_PORT_BY_SIZE_LARGE_STATS = "adaptorEthPortBySizeLargeStats"
    STATS_CLASS_ID_ADAPTOR_ETH_PORT_BY_SIZE_SMALL_STATS = "adaptorEthPortBySizeSmallStats"
    STATS_CLASS_ID_ADAPTOR_ETH_PORT_ERR_STATS = "adaptorEthPortErrStats"
    STATS_CLASS_ID_ADAPTOR_ETH_PORT_MCAST_STATS = "adaptorEthPortMcastStats"
    STATS_CLASS_ID_ADAPTOR_ETH_PORT_OUTSIZED_STATS = "adaptorEthPortOutsizedStats"
    STATS_CLASS_ID_ADAPTOR_ETH_PORT_PFC_STATS = "adaptorEthPortPfcStats"
    STATS_CLASS_ID_ADAPTOR_ETH_PORT_STATS = "adaptorEthPortStats"
    STATS_CLASS_ID_ADAPTOR_ETHER_IF_STATS = "adaptorEtherIfStats"
    STATS_CLASS_ID_ADAPTOR_FC_IF_EVENT_STATS = "adaptorFcIfEventStats"
    STATS_CLASS_ID_ADAPTOR_FC_IF_FC4_STATS = "adaptorFcIfFC4Stats"
    STATS_CLASS_ID_ADAPTOR_FC_IF_FRAME_STATS = "adaptorFcIfFrameStats"
    STATS_CLASS_ID_ADAPTOR_FC_PORT_STATS = "adaptorFcPortStats"
    STATS_CLASS_ID_ADAPTOR_MENLO_BASE_ERROR_STATS = "adaptorMenloBaseErrorStats"
    STATS_CLASS_ID_ADAPTOR_MENLO_DCE_PORT_STATS = "adaptorMenloDcePortStats"
    STATS_CLASS_ID_ADAPTOR_MENLO_ETH_ERROR_STATS = "adaptorMenloEthErrorStats"
    STATS_CLASS_ID_ADAPTOR_MENLO_ETH_STATS = "adaptorMenloEthStats"
    STATS_CLASS_ID_ADAPTOR_MENLO_FC_ERROR_STATS = "adaptorMenloFcErrorStats"
    STATS_CLASS_ID_ADAPTOR_MENLO_FC_STATS = "adaptorMenloFcStats"
    STATS_CLASS_ID_ADAPTOR_MENLO_HOST_PORT_STATS = "adaptorMenloHostPortStats"
    STATS_CLASS_ID_ADAPTOR_MENLO_MCPU_ERROR_STATS = "adaptorMenloMcpuErrorStats"
    STATS_CLASS_ID_ADAPTOR_MENLO_MCPU_STATS = "adaptorMenloMcpuStats"
    STATS_CLASS_ID_ADAPTOR_MENLO_NET_EG_STATS = "adaptorMenloNetEgStats"
    STATS_CLASS_ID_ADAPTOR_MENLO_NET_IN_STATS = "adaptorMenloNetInStats"
    STATS_CLASS_ID_ADAPTOR_MENLO_QERROR_STATS = "adaptorMenloQErrorStats"
    STATS_CLASS_ID_ADAPTOR_MENLO_QSTATS = "adaptorMenloQStats"
    STATS_CLASS_ID_ADAPTOR_VNIC_STATS = "adaptorVnicStats"
    STATS_CLASS_ID_COMPUTE_IOHUB_ENV_STATS = "computeIOHubEnvStats"
    STATS_CLASS_ID_COMPUTE_MB_POWER_STATS = "computeMbPowerStats"
    STATS_CLASS_ID_COMPUTE_MB_TEMP_STATS = "computeMbTempStats"
    STATS_CLASS_ID_COMPUTE_PCIE_FATAL_COMPLETION_STATS = "computePCIeFatalCompletionStats"
    STATS_CLASS_ID_COMPUTE_PCIE_FATAL_PROTOCOL_STATS = "computePCIeFatalProtocolStats"
    STATS_CLASS_ID_COMPUTE_PCIE_FATAL_RECEIVE_STATS = "computePCIeFatalReceiveStats"
    STATS_CLASS_ID_COMPUTE_PCIE_FATAL_STATS = "computePCIeFatalStats"
    STATS_CLASS_ID_COMPUTE_RACK_UNIT_MB_TEMP_STATS = "computeRackUnitMbTempStats"
    STATS_CLASS_ID_EQUIPMENT_CHASSIS_STATS = "equipmentChassisStats"
    STATS_CLASS_ID_EQUIPMENT_CROSS_FABRIC_MODULE_FAN_STATS = "equipmentCrossFabricModuleFanStats"
    STATS_CLASS_ID_EQUIPMENT_CROSS_FABRIC_MODULE_STATS = "equipmentCrossFabricModuleStats"
    STATS_CLASS_ID_EQUIPMENT_FAN_MODULE_STATS = "equipmentFanModuleStats"
    STATS_CLASS_ID_EQUIPMENT_FAN_STATS = "equipmentFanStats"
    STATS_CLASS_ID_EQUIPMENT_FEX_ENV_STATS = "equipmentFexEnvStats"
    STATS_CLASS_ID_EQUIPMENT_FEX_POWER_SUMMARY = "equipmentFexPowerSummary"
    STATS_CLASS_ID_EQUIPMENT_FEX_PSU_INPUT_STATS = "equipmentFexPsuInputStats"
    STATS_CLASS_ID_EQUIPMENT_FEX_SYSTEM_STATS = "equipmentFexSystemStats"
    STATS_CLASS_ID_EQUIPMENT_IOCARD_FAN_MODULE_STATS = "equipmentIOCardFanModuleStats"
    STATS_CLASS_ID_EQUIPMENT_IOCARD_FAN_STATS = "equipmentIOCardFanStats"
    STATS_CLASS_ID_EQUIPMENT_IOCARD_STATS = "equipmentIOCardStats"
    STATS_CLASS_ID_EQUIPMENT_NETWORK_ELEMENT_FAN_STATS = "equipmentNetworkElementFanStats"
    STATS_CLASS_ID_EQUIPMENT_PSU_INPUT_STATS = "equipmentPsuInputStats"
    STATS_CLASS_ID_EQUIPMENT_PSU_OUTPUT_STATS = "equipmentPsuOutputStats"
    STATS_CLASS_ID_EQUIPMENT_PSU_STATS = "equipmentPsuStats"
    STATS_CLASS_ID_EQUIPMENT_RACK_UNIT_FAN_STATS = "equipmentRackUnitFanStats"
    STATS_CLASS_ID_EQUIPMENT_RACK_UNIT_PSU_STATS = "equipmentRackUnitPsuStats"
    STATS_CLASS_ID_EQUIPMENT_SIOC_TEMP_STATS = "equipmentSiocTempStats"
    STATS_CLASS_ID_ETHER_ERR_STATS = "etherErrStats"
    STATS_CLASS_ID_ETHER_FCOE_INTERFACE_STATS = "etherFcoeInterfaceStats"
    STATS_CLASS_ID_ETHER_LOSS_STATS = "etherLossStats"
    STATS_CLASS_ID_ETHER_MAC_SEC_RX_STATS = "etherMacSecRxStats"
    STATS_CLASS_ID_ETHER_MAC_SEC_TX_STATS = "etherMacSecTxStats"
    STATS_CLASS_ID_ETHER_NI_ERR_STATS = "etherNiErrStats"
    STATS_CLASS_ID_ETHER_PAUSE_STATS = "etherPauseStats"
    STATS_CLASS_ID_ETHER_RX_STATS = "etherRxStats"
    STATS_CLASS_ID_ETHER_TX_STATS = "etherTxStats"
    STATS_CLASS_ID_FC_ERR_STATS = "fcErrStats"
    STATS_CLASS_ID_FC_STATS = "fcStats"
    STATS_CLASS_ID_MEMORY_ARRAY_ENV_STATS = "memoryArrayEnvStats"
    STATS_CLASS_ID_MEMORY_BUFFER_UNIT_ENV_STATS = "memoryBufferUnitEnvStats"
    STATS_CLASS_ID_MEMORY_ERROR_STATS = "memoryErrorStats"
    STATS_CLASS_ID_MEMORY_RUNTIME = "memoryRuntime"
    STATS_CLASS_ID_MEMORY_UNIT_ENV_STATS = "memoryUnitEnvStats"
    STATS_CLASS_ID_POWER_GROUP_STATS = "powerGroupStats"
    STATS_CLASS_ID_PROCESSOR_CACHE_MEM_STATS = "processorCacheMemStats"
    STATS_CLASS_ID_PROCESSOR_ENV_STATS = "processorEnvStats"
    STATS_CLASS_ID_PROCESSOR_ERROR_STATS = "processorErrorStats"
    STATS_CLASS_ID_PROCESSOR_EXEC_STATS = "processorExecStats"
    STATS_CLASS_ID_PROCESSOR_IOSTATS = "processorIOStats"
    STATS_CLASS_ID_PROCESSOR_MISC_STATS = "processorMiscStats"
    STATS_CLASS_ID_PROCESSOR_PCIBUS_STATS = "processorPCIBusStats"
    STATS_CLASS_ID_PROCESSOR_PMUSTATS = "processorPMUStats"
    STATS_CLASS_ID_PROCESSOR_RUNTIME = "processorRuntime"
    STATS_CLASS_ID_PROCESSOR_SECURITY_STATS = "processorSecurityStats"
    STATS_CLASS_ID_STORAGE_DISK_ENV_STATS = "storageDiskEnvStats"
    STATS_CLASS_ID_STORAGE_HDD_MOTHER_BOARD_TEMP_STATS = "storageHddMotherBoardTempStats"
    STATS_CLASS_ID_STORAGE_NVME_STATS = "storageNvmeStats"
    STATS_CLASS_ID_STORAGE_SSD_HEALTH_STATS = "storageSsdHealthStats"
    STATS_CLASS_ID_SW_CARD_ENV_STATS = "swCardEnvStats"
    STATS_CLASS_ID_SW_ENV_STATS = "swEnvStats"
    STATS_CLASS_ID_SW_SYSTEM_STATS = "swSystemStats"
    STATS_CLASS_ID_UNSPECIFIED = "unspecified"


class StatsThresholdClass(ManagedObject):
    """This is StatsThresholdClass class."""

    consts = StatsThresholdClassConsts()
    naming_props = set(['statsClassId'])

    mo_meta = MoMeta("StatsThresholdClass", "statsThresholdClass", "[stats_class_id]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["admin", "operations"], ['statsThresholdPolicy'], ['statsThr32Definition', 'statsThr64Definition', 'statsThrFloatDefinition'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "stats_class_id": MoPropertyMeta("stats_class_id", "statsClassId", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x80, None, None, None, ["adaptorEthPortBySizeLargeStats", "adaptorEthPortBySizeSmallStats", "adaptorEthPortErrStats", "adaptorEthPortMcastStats", "adaptorEthPortOutsizedStats", "adaptorEthPortPfcStats", "adaptorEthPortStats", "adaptorEtherIfStats", "adaptorFcIfEventStats", "adaptorFcIfFC4Stats", "adaptorFcIfFrameStats", "adaptorFcPortStats", "adaptorMenloBaseErrorStats", "adaptorMenloDcePortStats", "adaptorMenloEthErrorStats", "adaptorMenloEthStats", "adaptorMenloFcErrorStats", "adaptorMenloFcStats", "adaptorMenloHostPortStats", "adaptorMenloMcpuErrorStats", "adaptorMenloMcpuStats", "adaptorMenloNetEgStats", "adaptorMenloNetInStats", "adaptorMenloQErrorStats", "adaptorMenloQStats", "adaptorVnicStats", "computeIOHubEnvStats", "computeMbPowerStats", "computeMbTempStats", "computePCIeFatalCompletionStats", "computePCIeFatalProtocolStats", "computePCIeFatalReceiveStats", "computePCIeFatalStats", "computeRackUnitMbTempStats", "equipmentChassisStats", "equipmentCrossFabricModuleFanStats", "equipmentCrossFabricModuleStats", "equipmentFanModuleStats", "equipmentFanStats", "equipmentFexEnvStats", "equipmentFexPowerSummary", "equipmentFexPsuInputStats", "equipmentFexSystemStats", "equipmentIOCardFanModuleStats", "equipmentIOCardFanStats", "equipmentIOCardStats", "equipmentNetworkElementFanStats", "equipmentPsuInputStats", "equipmentPsuOutputStats", "equipmentPsuStats", "equipmentRackUnitFanStats", "equipmentRackUnitPsuStats", "equipmentSiocTempStats", "etherErrStats", "etherFcoeInterfaceStats", "etherLossStats", "etherMacSecRxStats", "etherMacSecTxStats", "etherNiErrStats", "etherPauseStats", "etherRxStats", "etherTxStats", "fcErrStats", "fcStats", "memoryArrayEnvStats", "memoryBufferUnitEnvStats", "memoryErrorStats", "memoryRuntime", "memoryUnitEnvStats", "powerGroupStats", "processorCacheMemStats", "processorEnvStats", "processorErrorStats", "processorExecStats", "processorIOStats", "processorMiscStats", "processorPCIBusStats", "processorPMUStats", "processorRuntime", "processorSecurityStats", "storageDiskEnvStats", "storageHddMotherBoardTempStats", "storageNvmeStats", "storageSsdHealthStats", "swCardEnvStats", "swEnvStats", "swSystemStats", "unspecified"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "statsClassId": "stats_class_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, stats_class_id, **kwargs):
        self._dirty_mask = 0
        self.stats_class_id = stats_class_id
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "StatsThresholdClass", parent_mo_or_dn, **kwargs)
