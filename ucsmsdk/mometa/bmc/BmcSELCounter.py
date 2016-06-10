"""This module contains the general information for BmcSELCounter ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BmcSELCounterConsts:
    CONT_CLASS_ID_COMPUTE_BOARD = "compute:Board"
    CONT_CLASS_ID_MEMORY_UNIT = "memory:Unit"
    CONT_CLASS_ID_PROCESSOR_UNIT = "processor:Unit"
    CONT_CLASS_ID_UNSPECIFIED = "unspecified"
    CONT_INST_ID_UNSPECIFIED = "unspecified"
    CONT_INST_ID_PROP_ID_MEMORY_UNIT_ID = "memory:Unit:id"
    CONT_INST_ID_PROP_ID_PROCESSOR_UNIT_ID = "processor:Unit:id"
    CONT_INST_ID_PROP_ID_UNSPECIFIED = "unspecified"
    EQPT_CLASS_ID_COMPUTE_BOARD = "compute:Board"
    EQPT_CLASS_ID_MEMORY_UNIT = "memory:Unit"
    EQPT_CLASS_ID_PROCESSOR_UNIT = "processor:Unit"
    EQPT_CLASS_ID_UNSPECIFIED = "unspecified"
    EQPT_INST_ID_UNSPECIFIED = "unspecified"
    EQPT_INST_ID_PROP_ID_MEMORY_UNIT_ID = "memory:Unit:id"
    EQPT_INST_ID_PROP_ID_PROCESSOR_UNIT_ID = "processor:Unit:id"
    EQPT_INST_ID_PROP_ID_UNSPECIFIED = "unspecified"
    PC_GLOBAL_ID_NO_ERRORS = "No Errors"
    PC_LOCAL_ID_NO_ERRORS = "No Errors"
    STATS_CLASS_ID_COMPUTE_PCIE_FATAL_COMPLETION_STATS = "compute:PCIeFatalCompletionStats"
    STATS_CLASS_ID_COMPUTE_PCIE_FATAL_PROTOCOL_STATS = "compute:PCIeFatalProtocolStats"
    STATS_CLASS_ID_COMPUTE_PCIE_FATAL_RECEIVE_STATS = "compute:PCIeFatalReceiveStats"
    STATS_CLASS_ID_COMPUTE_PCIE_FATAL_STATS = "compute:PCIeFatalStats"
    STATS_CLASS_ID_MEMORY_ERROR_STATS = "memory:ErrorStats"
    STATS_CLASS_ID_PROCESSOR_ERROR_STATS = "processor:ErrorStats"
    STATS_CLASS_ID_UNSPECIFIED = "unspecified"
    STATS_PROP_ID_COMPUTE_PCIE_FATAL_COMPLETION_STATS_ABORT_ERRORS = "compute:PCIeFatalCompletionStats:AbortErrors"
    STATS_PROP_ID_COMPUTE_PCIE_FATAL_COMPLETION_STATS_TIMEOUT_ERRORS = "compute:PCIeFatalCompletionStats:TimeoutErrors"
    STATS_PROP_ID_COMPUTE_PCIE_FATAL_COMPLETION_STATS_UNEXPECTED_ERRORS = "compute:PCIeFatalCompletionStats:unexpectedErrors"
    STATS_PROP_ID_COMPUTE_PCIE_FATAL_PROTOCOL_STATS_DLLP_ERRORS = "compute:PCIeFatalProtocolStats:dllpErrors"
    STATS_PROP_ID_COMPUTE_PCIE_FATAL_PROTOCOL_STATS_FLOW_CONTROL_ERRORS = "compute:PCIeFatalProtocolStats:flowControlErrors"
    STATS_PROP_ID_COMPUTE_PCIE_FATAL_RECEIVE_STATS_BUFFER_OVERFLOW_ERRORS = "compute:PCIeFatalReceiveStats:bufferOverflowErrors"
    STATS_PROP_ID_COMPUTE_PCIE_FATAL_RECEIVE_STATS_ERR_FATAL_ERRORS = "compute:PCIeFatalReceiveStats:errFatalErrors"
    STATS_PROP_ID_COMPUTE_PCIE_FATAL_RECEIVE_STATS_ERR_NON_FATAL_ERRORS = "compute:PCIeFatalReceiveStats:errNonFatalErrors"
    STATS_PROP_ID_COMPUTE_PCIE_FATAL_RECEIVE_STATS_UNSUPPORTED_REQUEST_ERRORS = "compute:PCIeFatalReceiveStats:unsupportedRequestErrors"
    STATS_PROP_ID_COMPUTE_PCIE_FATAL_STATS_ACS_VIOLATION_ERRORS = "compute:PCIeFatalStats:acsViolationErrors"
    STATS_PROP_ID_COMPUTE_PCIE_FATAL_STATS_MALFORMED_TLPERRORS = "compute:PCIeFatalStats:malformedTLPErrors"
    STATS_PROP_ID_COMPUTE_PCIE_FATAL_STATS_POISONED_TLPERRORS = "compute:PCIeFatalStats:poisonedTLPErrors"
    STATS_PROP_ID_COMPUTE_PCIE_FATAL_STATS_SURPRISE_LINK_DOWN_ERRORS = "compute:PCIeFatalStats:surpriseLinkDownErrors"
    STATS_PROP_ID_MEMORY_ERROR_STATS_ADDRESS_PARITY_ERRORS = "memory:ErrorStats:addressParityErrors"
    STATS_PROP_ID_MEMORY_ERROR_STATS_ECC_MULTIBIT_ERRORS = "memory:ErrorStats:eccMultibitErrors"
    STATS_PROP_ID_MEMORY_ERROR_STATS_ECC_SINGLEBIT_ERRORS = "memory:ErrorStats:eccSinglebitErrors"
    STATS_PROP_ID_MEMORY_ERROR_STATS_MISMATCH_ERRORS = "memory:ErrorStats:mismatchErrors"
    STATS_PROP_ID_PROCESSOR_ERROR_STATS_MIRRORING_INTER_SOCK_ERRORS = "processor:ErrorStats:mirroringInterSockErrors"
    STATS_PROP_ID_PROCESSOR_ERROR_STATS_MIRRORING_INTRA_SOCK_ERRORS = "processor:ErrorStats:mirroringIntraSockErrors"
    STATS_PROP_ID_PROCESSOR_ERROR_STATS_SMI_LINK_CORR_ERRORS = "processor:ErrorStats:smiLinkCorrErrors"
    STATS_PROP_ID_PROCESSOR_ERROR_STATS_SMI_LINK_UNCORR_ERRORS = "processor:ErrorStats:smiLinkUncorrErrors"
    STATS_PROP_ID_PROCESSOR_ERROR_STATS_SPARING_ERRORS = "processor:ErrorStats:sparingErrors"
    STATS_PROP_ID_UNSPECIFIED = "unspecified"


class BmcSELCounter(ManagedObject):
    """This is BmcSELCounter class."""

    consts = BmcSELCounterConsts()
    naming_props = set([u'localId'])

    mo_meta = MoMeta("BmcSELCounter", "bmcSELCounter", "Counter-[local_id]", VersionMeta.Version111j, "InputOutput", 0x3f, [], ["read-only"], [u'equipmentPOSTCodeReporter'], [], ["Get"])

    prop_meta = {
        "bitmask": MoPropertyMeta("bitmask", "bitmask", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "coll_interval": MoPropertyMeta("coll_interval", "collInterval", "ushort", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "cont_class_id": MoPropertyMeta("cont_class_id", "contClassId", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["compute:Board", "memory:Unit", "processor:Unit", "unspecified"], []), 
        "cont_inst_id": MoPropertyMeta("cont_inst_id", "contInstId", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "cont_inst_id_prop_id": MoPropertyMeta("cont_inst_id_prop_id", "contInstIdPropId", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["memory:Unit:id", "processor:Unit:id", "unspecified"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "eqpt_class_id": MoPropertyMeta("eqpt_class_id", "eqptClassId", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["compute:Board", "memory:Unit", "processor:Unit", "unspecified"], []), 
        "eqpt_inst_id": MoPropertyMeta("eqpt_inst_id", "eqptInstId", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "eqpt_inst_id_prop_id": MoPropertyMeta("eqpt_inst_id_prop_id", "eqptInstIdPropId", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["memory:Unit:id", "processor:Unit:id", "unspecified"], []), 
        "global_id": MoPropertyMeta("global_id", "globalId", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "local_id": MoPropertyMeta("local_id", "localId", "uint", VersionMeta.Version111j, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "pc_global_id": MoPropertyMeta("pc_global_id", "pcGlobalId", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No Errors"], ["0-4294967295"]), 
        "pc_local_id": MoPropertyMeta("pc_local_id", "pcLocalId", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No Errors"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "stats_class_id": MoPropertyMeta("stats_class_id", "statsClassId", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["compute:PCIeFatalCompletionStats", "compute:PCIeFatalProtocolStats", "compute:PCIeFatalReceiveStats", "compute:PCIeFatalStats", "memory:ErrorStats", "processor:ErrorStats", "unspecified"], []), 
        "stats_prop_id": MoPropertyMeta("stats_prop_id", "statsPropId", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["compute:PCIeFatalCompletionStats:AbortErrors", "compute:PCIeFatalCompletionStats:TimeoutErrors", "compute:PCIeFatalCompletionStats:unexpectedErrors", "compute:PCIeFatalProtocolStats:dllpErrors", "compute:PCIeFatalProtocolStats:flowControlErrors", "compute:PCIeFatalReceiveStats:bufferOverflowErrors", "compute:PCIeFatalReceiveStats:errFatalErrors", "compute:PCIeFatalReceiveStats:errNonFatalErrors", "compute:PCIeFatalReceiveStats:unsupportedRequestErrors", "compute:PCIeFatalStats:acsViolationErrors", "compute:PCIeFatalStats:malformedTLPErrors", "compute:PCIeFatalStats:poisonedTLPErrors", "compute:PCIeFatalStats:surpriseLinkDownErrors", "memory:ErrorStats:addressParityErrors", "memory:ErrorStats:eccMultibitErrors", "memory:ErrorStats:eccSinglebitErrors", "memory:ErrorStats:mismatchErrors", "processor:ErrorStats:mirroringInterSockErrors", "processor:ErrorStats:mirroringIntraSockErrors", "processor:ErrorStats:smiLinkCorrErrors", "processor:ErrorStats:smiLinkUncorrErrors", "processor:ErrorStats:sparingErrors", "unspecified"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "threshold": MoPropertyMeta("threshold", "threshold", "ushort", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "value": MoPropertyMeta("value", "value", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "bitmask": "bitmask", 
        "childAction": "child_action", 
        "collInterval": "coll_interval", 
        "contClassId": "cont_class_id", 
        "contInstId": "cont_inst_id", 
        "contInstIdPropId": "cont_inst_id_prop_id", 
        "dn": "dn", 
        "eqptClassId": "eqpt_class_id", 
        "eqptInstId": "eqpt_inst_id", 
        "eqptInstIdPropId": "eqpt_inst_id_prop_id", 
        "globalId": "global_id", 
        "localId": "local_id", 
        "pcGlobalId": "pc_global_id", 
        "pcLocalId": "pc_local_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "statsClassId": "stats_class_id", 
        "statsPropId": "stats_prop_id", 
        "status": "status", 
        "threshold": "threshold", 
        "value": "value", 
    }

    def __init__(self, parent_mo_or_dn, local_id, **kwargs):
        self._dirty_mask = 0
        self.local_id = local_id
        self.bitmask = None
        self.child_action = None
        self.coll_interval = None
        self.cont_class_id = None
        self.cont_inst_id = None
        self.cont_inst_id_prop_id = None
        self.eqpt_class_id = None
        self.eqpt_inst_id = None
        self.eqpt_inst_id_prop_id = None
        self.global_id = None
        self.pc_global_id = None
        self.pc_local_id = None
        self.sacl = None
        self.stats_class_id = None
        self.stats_prop_id = None
        self.status = None
        self.threshold = None
        self.value = None

        ManagedObject.__init__(self, "BmcSELCounter", parent_mo_or_dn, **kwargs)
