"""This module contains the general information for MgmtControllerFsmTask ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtControllerFsmTaskConsts:
    COMPLETION_CANCELLED = "cancelled"
    COMPLETION_COMPLETED = "completed"
    COMPLETION_PROCESSING = "processing"
    COMPLETION_SCHEDULED = "scheduled"
    ITEM_ACTIVATE_ADAPTOR = "ActivateAdaptor"
    ITEM_ACTIVATE_BMC = "ActivateBMC"
    ITEM_ACTIVATE_CMC = "ActivateCMC"
    ITEM_ACTIVATE_IOM = "ActivateIOM"
    ITEM_ACTIVATE_LOCAL_DISK = "ActivateLocalDisk"
    ITEM_ACTIVATE_SAS_EXPANDER = "ActivateSasExpander"
    ITEM_ACTIVATE_STORAGE_SERVER_CMC = "ActivateStorageServerCMC"
    ITEM_CONFIGURE_SW_PERSONALITIES = "ConfigureSwPersonalities"
    ITEM_ENABLE_SECURE_BOOT = "EnableSecureBoot"
    ITEM_EXT_MGMT_IF_CONFIG = "ExtMgmtIfConfig"
    ITEM_EXT_MGMT_INTERFACE_CONFIG = "ExtMgmtInterfaceConfig"
    ITEM_KVM_CERT = "KvmCert"
    ITEM_LOCK_CONFIG = "LockConfig"
    ITEM_ONLINE = "Online"
    ITEM_POWER_BUDGET_RECLAIM_CONFIG = "PowerBudgetReclaimConfig"
    ITEM_POWER_CAP = "PowerCap"
    ITEM_REGISTRY_CONFIG = "RegistryConfig"
    ITEM_SYS_CONFIG = "SysConfig"
    ITEM_UPDATE_ADAPTOR = "UpdateAdaptor"
    ITEM_UPDATE_BMC = "UpdateBMC"
    ITEM_UPDATE_BOARD_CONTROLLER = "UpdateBoardController"
    ITEM_UPDATE_CMC = "UpdateCMC"
    ITEM_UPDATE_IOM = "UpdateIOM"
    ITEM_UPDATE_RAID_CONTROLLER = "UpdateRaidController"
    ITEM_UPDATE_SAS_EXPANDER = "UpdateSasExpander"
    ITEM_UPDATE_SECURE_FPGA = "UpdateSecureFPGA"
    ITEM_UPDATE_STORAGE_SERVER_CMC = "UpdateStorageServerCMC"
    ITEM_UPDATE_SWITCH = "UpdateSwitch"
    ITEM_UPDATE_UCSMANAGER = "UpdateUCSManager"
    ITEM_UPDATE_UCSMANAGER_SP = "UpdateUCSManagerSP"
    ITEM_UPGRADE_BOARD_CONTROLLER = "UpgradeBoardController"
    ITEM_NOP = "nop"


class MgmtControllerFsmTask(ManagedObject):
    """This is MgmtControllerFsmTask class."""

    consts = MgmtControllerFsmTaskConsts()
    naming_props = set(['item'])

    mo_meta = MoMeta("MgmtControllerFsmTask", "mgmtControllerFsmTask", "task-[item]", VersionMeta.Version111j, "OutputOnly", 0xf, [], [""], ['mgmtController'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "completion": MoPropertyMeta("completion", "completion", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cancelled", "completed", "processing", "scheduled"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "flags": MoPropertyMeta("flags", "flags", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""(defaultValue){0,1}""", [], []),
        "item": MoPropertyMeta("item", "item", "string", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, ["ActivateAdaptor", "ActivateBMC", "ActivateCMC", "ActivateIOM", "ActivateLocalDisk", "ActivateSasExpander", "ActivateStorageServerCMC", "ConfigureSwPersonalities", "EnableSecureBoot", "ExtMgmtIfConfig", "ExtMgmtInterfaceConfig", "KvmCert", "LockConfig", "Online", "PowerBudgetReclaimConfig", "PowerCap", "RegistryConfig", "SysConfig", "UpdateAdaptor", "UpdateBMC", "UpdateBoardController", "UpdateCMC", "UpdateIOM", "UpdateRaidController", "UpdateSasExpander", "UpdateSecureFPGA", "UpdateStorageServerCMC", "UpdateSwitch", "UpdateUCSManager", "UpdateUCSManagerSP", "UpgradeBoardController", "nop"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "seq_id": MoPropertyMeta("seq_id", "seqId", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "completion": "completion", 
        "dn": "dn", 
        "flags": "flags", 
        "item": "item", 
        "rn": "rn", 
        "sacl": "sacl", 
        "seqId": "seq_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, item, **kwargs):
        self._dirty_mask = 0
        self.item = item
        self.child_action = None
        self.completion = None
        self.flags = None
        self.sacl = None
        self.seq_id = None
        self.status = None

        ManagedObject.__init__(self, "MgmtControllerFsmTask", parent_mo_or_dn, **kwargs)
