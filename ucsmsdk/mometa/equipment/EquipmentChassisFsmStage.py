"""This module contains the general information for EquipmentChassisFsmStage ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentChassisFsmStageConsts:
    LAST_UPDATE_TIME_ = ""
    NAME_ASSOCIATE_ACTIVATE_ADAPTOR = "AssociateActivateAdaptor"
    NAME_ASSOCIATE_ACTIVATE_BRD_CTLR = "AssociateActivateBrdCtlr"
    NAME_ASSOCIATE_ACTIVATE_CMC = "AssociateActivateCmc"
    NAME_ASSOCIATE_ACTIVATE_LOCAL_DISK = "AssociateActivateLocalDisk"
    NAME_ASSOCIATE_ACTIVATE_SAS_EXPANDER = "AssociateActivateSasExpander"
    NAME_ASSOCIATE_ACTIVATE_STORAGE_CTLR = "AssociateActivateStorageCtlr"
    NAME_ASSOCIATE_BEGIN = "AssociateBegin"
    NAME_ASSOCIATE_COPY_REMOTE = "AssociateCopyRemote"
    NAME_ASSOCIATE_DELETE_CURL_DOWNLOADED_IMAGES = "AssociateDeleteCurlDownloadedImages"
    NAME_ASSOCIATE_DELETE_IMAGES_REMOTE = "AssociateDeleteImagesRemote"
    NAME_ASSOCIATE_DISK_ZONING_CONFIG = "AssociateDiskZoningConfig"
    NAME_ASSOCIATE_DOWNLOAD_IMAGES = "AssociateDownloadImages"
    NAME_ASSOCIATE_FAIL = "AssociateFail"
    NAME_ASSOCIATE_POLL_ADAPTOR_ACTIVATION = "AssociatePollAdaptorActivation"
    NAME_ASSOCIATE_POLL_BRD_CTLR_ACTIVATION = "AssociatePollBrdCtlrActivation"
    NAME_ASSOCIATE_POLL_CMC_ACTIVATION = "AssociatePollCmcActivation"
    NAME_ASSOCIATE_POLL_POST_DISK_ZONE_STORAGE_INV_CIMC = "AssociatePollPostDiskZoneStorageInvCIMC"
    NAME_ASSOCIATE_POLL_SAS_EXPANDER_ACTIVATE = "AssociatePollSasExpanderActivate"
    NAME_ASSOCIATE_POLL_STORAGE_CTLR_ACTIVATION = "AssociatePollStorageCtlrActivation"
    NAME_ASSOCIATE_POLL_UPDATE_CMC = "AssociatePollUpdateCmc"
    NAME_ASSOCIATE_POLL_UPDATE_CRUZ = "AssociatePollUpdateCruz"
    NAME_ASSOCIATE_POLL_UPDATE_SAS_EXPANDER = "AssociatePollUpdateSasExpander"
    NAME_ASSOCIATE_POST_DISK_ZONE_STORAGE_INV_CIMC = "AssociatePostDiskZoneStorageInvCIMC"
    NAME_ASSOCIATE_POST_DISK_ZONE_STORAGE_INV_CMC = "AssociatePostDiskZoneStorageInvCMC"
    NAME_ASSOCIATE_POWER_OFF_SERVERS = "AssociatePowerOffServers"
    NAME_ASSOCIATE_POWER_ON_SERVERS = "AssociatePowerOnServers"
    NAME_ASSOCIATE_SUCCESS = "AssociateSuccess"
    NAME_ASSOCIATE_UNLOCK_FIRMWARE_IMAGE = "AssociateUnlockFirmwareImage"
    NAME_ASSOCIATE_UPDATE_CMC = "AssociateUpdateCmc"
    NAME_ASSOCIATE_UPDATE_CRUZ = "AssociateUpdateCruz"
    NAME_ASSOCIATE_UPDATE_SAS_EXPANDER = "AssociateUpdateSasExpander"
    NAME_ASSOCIATE_WAIT_BEFORE_INSTALLATION = "AssociateWaitBeforeInstallation"
    NAME_ASSOCIATE_WAIT_FOR_POWER_OFF = "AssociateWaitForPowerOff"
    NAME_CHASSIS_UPGRADE_ACTIVATE_ADAPTOR = "ChassisUpgradeActivateAdaptor"
    NAME_CHASSIS_UPGRADE_ACTIVATE_BRD_CTLR = "ChassisUpgradeActivateBrdCtlr"
    NAME_CHASSIS_UPGRADE_ACTIVATE_CMC = "ChassisUpgradeActivateCmc"
    NAME_CHASSIS_UPGRADE_ACTIVATE_LOCAL_DISK = "ChassisUpgradeActivateLocalDisk"
    NAME_CHASSIS_UPGRADE_ACTIVATE_SAS_EXPANDER = "ChassisUpgradeActivateSasExpander"
    NAME_CHASSIS_UPGRADE_ACTIVATE_STORAGE_CTLR = "ChassisUpgradeActivateStorageCtlr"
    NAME_CHASSIS_UPGRADE_BEGIN = "ChassisUpgradeBegin"
    NAME_CHASSIS_UPGRADE_FAIL = "ChassisUpgradeFail"
    NAME_CHASSIS_UPGRADE_POLL_ADAPTOR_ACTIVATION = "ChassisUpgradePollAdaptorActivation"
    NAME_CHASSIS_UPGRADE_POLL_BRD_CTLR_ACTIVATION = "ChassisUpgradePollBrdCtlrActivation"
    NAME_CHASSIS_UPGRADE_POLL_CMC_ACTIVATION = "ChassisUpgradePollCmcActivation"
    NAME_CHASSIS_UPGRADE_POLL_LOCAL_DISK_ACTIVATE = "ChassisUpgradePollLocalDiskActivate"
    NAME_CHASSIS_UPGRADE_POLL_SAS_EXPANDER_ACTIVATE = "ChassisUpgradePollSasExpanderActivate"
    NAME_CHASSIS_UPGRADE_POLL_STORAGE_CTLR_ACTIVATION = "ChassisUpgradePollStorageCtlrActivation"
    NAME_CHASSIS_UPGRADE_POLL_UPDATE_STATUS = "ChassisUpgradePollUpdateStatus"
    NAME_CHASSIS_UPGRADE_POWER_OFF_SERVERS = "ChassisUpgradePowerOffServers"
    NAME_CHASSIS_UPGRADE_POWER_ON_SERVERS = "ChassisUpgradePowerOnServers"
    NAME_CHASSIS_UPGRADE_RESET_SAS_EXPANDER = "ChassisUpgradeResetSasExpander"
    NAME_CHASSIS_UPGRADE_SUCCESS = "ChassisUpgradeSuccess"
    NAME_CHASSIS_UPGRADE_UPDATE_REQUEST = "ChassisUpgradeUpdateRequest"
    NAME_CHASSIS_UPGRADE_WAIT_FOR_POWER_OFF = "ChassisUpgradeWaitForPowerOff"
    NAME_DISASSOCIATE_BEGIN = "DisassociateBegin"
    NAME_DISASSOCIATE_COMPLETE = "DisassociateComplete"
    NAME_DISASSOCIATE_FAIL = "DisassociateFail"
    NAME_DISASSOCIATE_SUCCESS = "DisassociateSuccess"
    NAME_DYNAMIC_REALLOCATION_BEGIN = "DynamicReallocationBegin"
    NAME_DYNAMIC_REALLOCATION_CONFIG = "DynamicReallocationConfig"
    NAME_DYNAMIC_REALLOCATION_FAIL = "DynamicReallocationFail"
    NAME_DYNAMIC_REALLOCATION_SUCCESS = "DynamicReallocationSuccess"
    NAME_OOB_STORAGE_ADMIN_CFG_BEGIN = "OobStorageAdminCfgBegin"
    NAME_OOB_STORAGE_ADMIN_CFG_FAIL = "OobStorageAdminCfgFail"
    NAME_OOB_STORAGE_ADMIN_CFG_OOB_STORAGE_CONFIG = "OobStorageAdminCfgOobStorageConfig"
    NAME_OOB_STORAGE_ADMIN_CFG_OOB_STORAGE_INVENTORY = "OobStorageAdminCfgOobStorageInventory"
    NAME_OOB_STORAGE_ADMIN_CFG_SUCCESS = "OobStorageAdminCfgSuccess"
    NAME_POWER_CAP_BEGIN = "PowerCapBegin"
    NAME_POWER_CAP_CONFIG = "PowerCapConfig"
    NAME_POWER_CAP_FAIL = "PowerCapFail"
    NAME_POWER_CAP_SUCCESS = "PowerCapSuccess"
    NAME_PSU_POLICY_CONFIG_BEGIN = "PsuPolicyConfigBegin"
    NAME_PSU_POLICY_CONFIG_EXECUTE = "PsuPolicyConfigExecute"
    NAME_PSU_POLICY_CONFIG_FAIL = "PsuPolicyConfigFail"
    NAME_PSU_POLICY_CONFIG_SUCCESS = "PsuPolicyConfigSuccess"
    NAME_REMOVE_CHASSIS_BEGIN = "RemoveChassisBegin"
    NAME_REMOVE_CHASSIS_CLEANUP_VNICS_LOCAL = "RemoveChassisCleanupVnicsLocal"
    NAME_REMOVE_CHASSIS_CLEANUP_VNICS_PEER = "RemoveChassisCleanupVnicsPeer"
    NAME_REMOVE_CHASSIS_DECOMISSION = "RemoveChassisDecomission"
    NAME_REMOVE_CHASSIS_DISABLE_END_POINT = "RemoveChassisDisableEndPoint"
    NAME_REMOVE_CHASSIS_FAIL = "RemoveChassisFail"
    NAME_REMOVE_CHASSIS_SUCCESS = "RemoveChassisSuccess"
    NAME_REMOVE_CHASSIS_UN_IDENTIFY_LOCAL = "RemoveChassisUnIdentifyLocal"
    NAME_REMOVE_CHASSIS_UN_IDENTIFY_PEER = "RemoveChassisUnIdentifyPeer"
    NAME_REMOVE_CHASSIS_WAIT = "RemoveChassisWait"
    NAME_NOP = "nop"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class EquipmentChassisFsmStage(ManagedObject):
    """This is EquipmentChassisFsmStage class."""

    consts = EquipmentChassisFsmStageConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("EquipmentChassisFsmStage", "equipmentChassisFsmStage", "stage-[name]", VersionMeta.Version211a, "OutputOnly", 0xf, [], [""], [u'equipmentChassisFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, None, None, None, None, ["AssociateActivateAdaptor", "AssociateActivateBrdCtlr", "AssociateActivateCmc", "AssociateActivateLocalDisk", "AssociateActivateSasExpander", "AssociateActivateStorageCtlr", "AssociateBegin", "AssociateCopyRemote", "AssociateDeleteCurlDownloadedImages", "AssociateDeleteImagesRemote", "AssociateDiskZoningConfig", "AssociateDownloadImages", "AssociateFail", "AssociatePollAdaptorActivation", "AssociatePollBrdCtlrActivation", "AssociatePollCmcActivation", "AssociatePollPostDiskZoneStorageInvCIMC", "AssociatePollSasExpanderActivate", "AssociatePollStorageCtlrActivation", "AssociatePollUpdateCmc", "AssociatePollUpdateCruz", "AssociatePollUpdateSasExpander", "AssociatePostDiskZoneStorageInvCIMC", "AssociatePostDiskZoneStorageInvCMC", "AssociatePowerOffServers", "AssociatePowerOnServers", "AssociateSuccess", "AssociateUnlockFirmwareImage", "AssociateUpdateCmc", "AssociateUpdateCruz", "AssociateUpdateSasExpander", "AssociateWaitBeforeInstallation", "AssociateWaitForPowerOff", "ChassisUpgradeActivateAdaptor", "ChassisUpgradeActivateBrdCtlr", "ChassisUpgradeActivateCmc", "ChassisUpgradeActivateLocalDisk", "ChassisUpgradeActivateSasExpander", "ChassisUpgradeActivateStorageCtlr", "ChassisUpgradeBegin", "ChassisUpgradeFail", "ChassisUpgradePollAdaptorActivation", "ChassisUpgradePollBrdCtlrActivation", "ChassisUpgradePollCmcActivation", "ChassisUpgradePollLocalDiskActivate", "ChassisUpgradePollSasExpanderActivate", "ChassisUpgradePollStorageCtlrActivation", "ChassisUpgradePollUpdateStatus", "ChassisUpgradePowerOffServers", "ChassisUpgradePowerOnServers", "ChassisUpgradeResetSasExpander", "ChassisUpgradeSuccess", "ChassisUpgradeUpdateRequest", "ChassisUpgradeWaitForPowerOff", "DisassociateBegin", "DisassociateComplete", "DisassociateFail", "DisassociateSuccess", "DynamicReallocationBegin", "DynamicReallocationConfig", "DynamicReallocationFail", "DynamicReallocationSuccess", "OobStorageAdminCfgBegin", "OobStorageAdminCfgFail", "OobStorageAdminCfgOobStorageConfig", "OobStorageAdminCfgOobStorageInventory", "OobStorageAdminCfgSuccess", "PowerCapBegin", "PowerCapConfig", "PowerCapFail", "PowerCapSuccess", "PsuPolicyConfigBegin", "PsuPolicyConfigExecute", "PsuPolicyConfigFail", "PsuPolicyConfigSuccess", "RemoveChassisBegin", "RemoveChassisCleanupVnicsLocal", "RemoveChassisCleanupVnicsPeer", "RemoveChassisDecomission", "RemoveChassisDisableEndPoint", "RemoveChassisFail", "RemoveChassisSuccess", "RemoveChassisUnIdentifyLocal", "RemoveChassisUnIdentifyPeer", "RemoveChassisWait", "nop"], []), 
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "retry": MoPropertyMeta("retry", "retry", "byte", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "stage_status": MoPropertyMeta("stage_status", "stageStatus", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "lastUpdateTime": "last_update_time", 
        "name": "name", 
        "order": "order", 
        "retry": "retry", 
        "rn": "rn", 
        "sacl": "sacl", 
        "stageStatus": "stage_status", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.last_update_time = None
        self.order = None
        self.retry = None
        self.sacl = None
        self.stage_status = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentChassisFsmStage", parent_mo_or_dn, **kwargs)
