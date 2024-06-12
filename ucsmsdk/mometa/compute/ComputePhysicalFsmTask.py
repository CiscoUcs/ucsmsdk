"""This module contains the general information for ComputePhysicalFsmTask ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePhysicalFsmTaskConsts:
    COMPLETION_CANCELLED = "cancelled"
    COMPLETION_COMPLETED = "completed"
    COMPLETION_PROCESSING = "processing"
    COMPLETION_SCHEDULED = "scheduled"
    ITEM_ACTIVATE_ADAPTOR = "ActivateAdaptor"
    ITEM_ACTIVATE_BIOS = "ActivateBIOS"
    ITEM_ASSOCIATE = "Associate"
    ITEM_BIOS_PASSWORD_RESET = "BiosPasswordReset"
    ITEM_BIOS_RECOVERY = "BiosRecovery"
    ITEM_CIMC_SECURITY_CONFIG = "CimcSecurityConfig"
    ITEM_CIMC_SECURITY_UNCONFIG = "CimcSecurityUnconfig"
    ITEM_CIMC_SESSION_DELETE = "CimcSessionDelete"
    ITEM_CMOS_RESET = "CmosReset"
    ITEM_CONFIG_BOARD = "ConfigBoard"
    ITEM_CONFIG_SO_L = "ConfigSoL"
    ITEM_CONFIGURE_SERVER_PERSONALITY = "ConfigureServerPersonality"
    ITEM_DATA_SANITIZATION = "DataSanitization"
    ITEM_DECOMMISSION = "Decommission"
    ITEM_DIAG = "Diag"
    ITEM_DIAGNOSTIC_INTERRUPT = "DiagnosticInterrupt"
    ITEM_DISASSOCIATE = "Disassociate"
    ITEM_DISK_ZONING_INVENTORY = "DiskZoningInventory"
    ITEM_ENABLE_CIMC_SECURE_BOOT = "EnableCimcSecureBoot"
    ITEM_EXECUTE_ACTIONS = "ExecuteActions"
    ITEM_FLASH_CONTROLLER = "FlashController"
    ITEM_FW_UPGRADE = "FwUpgrade"
    ITEM_HARD_SHUTDOWN = "HardShutdown"
    ITEM_HARDRESET = "Hardreset"
    ITEM_NVME_SWITCH_RECOVERY = "NvmeSwitchRecovery"
    ITEM_OOB_STORAGE_ADMIN_CONFIG = "OobStorageAdminConfig"
    ITEM_POWER_CAP = "PowerCap"
    ITEM_POWERCYCLE = "Powercycle"
    ITEM_REINITIALIZE_VIRTUAL_DRIVE = "ReinitializeVirtualDrive"
    ITEM_RESET_BMC = "ResetBmc"
    ITEM_RESET_IPMI = "ResetIpmi"
    ITEM_RESET_KVM = "ResetKvm"
    ITEM_RESET_MEMORY_ERRORS = "ResetMemoryErrors"
    ITEM_SERVICE_INFRA_DEPLOY = "ServiceInfraDeploy"
    ITEM_SERVICE_INFRA_WITHDRAW = "ServiceInfraWithdraw"
    ITEM_SOFT_SHUTDOWN = "SoftShutdown"
    ITEM_SOFTRESET = "Softreset"
    ITEM_SW_CONN_UPD = "SwConnUpd"
    ITEM_TURNUP = "Turnup"
    ITEM_UNCONFIG_SO_L = "UnconfigSoL"
    ITEM_UPDATE_ADAPTOR = "UpdateAdaptor"
    ITEM_UPDATE_BIOS = "UpdateBIOS"
    ITEM_UPDATE_BOARD_CONTROLLER = "UpdateBoardController"
    ITEM_CLEAR_TPM = "clearTPM"
    ITEM_NOP = "nop"
    ITEM_UPDATE_EXT_USERS = "updateExtUsers"


class ComputePhysicalFsmTask(ManagedObject):
    """This is ComputePhysicalFsmTask class."""

    consts = ComputePhysicalFsmTaskConsts()
    naming_props = set(['item'])

    mo_meta = MoMeta("ComputePhysicalFsmTask", "computePhysicalFsmTask", "task-[item]", VersionMeta.Version141i, "OutputOnly", 0xf, [], [""], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "completion": MoPropertyMeta("completion", "completion", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cancelled", "completed", "processing", "scheduled"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "flags": MoPropertyMeta("flags", "flags", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""(defaultValue){0,1}""", [], []),
        "item": MoPropertyMeta("item", "item", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, None, None, None, None, ["ActivateAdaptor", "ActivateBIOS", "Associate", "BiosPasswordReset", "BiosRecovery", "CimcSecurityConfig", "CimcSecurityUnconfig", "CimcSessionDelete", "CmosReset", "ConfigBoard", "ConfigSoL", "ConfigureServerPersonality", "DataSanitization", "Decommission", "Diag", "DiagnosticInterrupt", "Disassociate", "DiskZoningInventory", "EnableCimcSecureBoot", "ExecuteActions", "FlashController", "FwUpgrade", "HardShutdown", "Hardreset", "NvmeSwitchRecovery", "OobStorageAdminConfig", "PowerCap", "Powercycle", "ReinitializeVirtualDrive", "ResetBmc", "ResetIpmi", "ResetKvm", "ResetMemoryErrors", "ServiceInfraDeploy", "ServiceInfraWithdraw", "SoftShutdown", "Softreset", "SwConnUpd", "Turnup", "UnconfigSoL", "UpdateAdaptor", "UpdateBIOS", "UpdateBoardController", "clearTPM", "nop", "updateExtUsers"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "seq_id": MoPropertyMeta("seq_id", "seqId", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
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

        ManagedObject.__init__(self, "ComputePhysicalFsmTask", parent_mo_or_dn, **kwargs)
