"""This module contains the general information for FirmwareSystemFsmStage ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareSystemFsmStageConsts:
    LAST_UPDATE_TIME_ = ""
    NAME_APPLY_CATALOG_PACK_ACTIVATE_CATALOG = "ApplyCatalogPackActivateCatalog"
    NAME_APPLY_CATALOG_PACK_BEGIN = "ApplyCatalogPackBegin"
    NAME_APPLY_CATALOG_PACK_FAIL = "ApplyCatalogPackFail"
    NAME_APPLY_CATALOG_PACK_RESOLVE_DISTRIBUTABLE = "ApplyCatalogPackResolveDistributable"
    NAME_APPLY_CATALOG_PACK_RESOLVE_DISTRIBUTABLE_NAMES = "ApplyCatalogPackResolveDistributableNames"
    NAME_APPLY_CATALOG_PACK_RESOLVE_IMAGES = "ApplyCatalogPackResolveImages"
    NAME_APPLY_CATALOG_PACK_SUCCESS = "ApplyCatalogPackSuccess"
    NAME_DEPLOY_ACTIVATE_IOM = "DeployActivateIOM"
    NAME_DEPLOY_ACTIVATE_LOCAL_FI = "DeployActivateLocalFI"
    NAME_DEPLOY_ACTIVATE_REMOTE_FI = "DeployActivateRemoteFI"
    NAME_DEPLOY_ACTIVATE_UCSM = "DeployActivateUCSM"
    NAME_DEPLOY_ACTIVATE_UCSMSERVICE_PACK = "DeployActivateUCSMServicePack"
    NAME_DEPLOY_BEGIN = "DeployBegin"
    NAME_DEPLOY_COPY_ALL_IMAGES_TO_PEER = "DeployCopyAllImagesToPeer"
    NAME_DEPLOY_DOWNLOAD_IMAGES = "DeployDownloadImages"
    NAME_DEPLOY_FAB_EVAC_OFF_REMOTE_FI = "DeployFabEvacOffRemoteFI"
    NAME_DEPLOY_FAB_EVAC_ON_REMOTE_FI = "DeployFabEvacOnRemoteFI"
    NAME_DEPLOY_FAIL = "DeployFail"
    NAME_DEPLOY_FAIL_OVER_TO_REMOTE_FI = "DeployFailOverToRemoteFI"
    NAME_DEPLOY_INTERNAL_BACKUP = "DeployInternalBackup"
    NAME_DEPLOY_POLL_ACTIVATE_OF_IOM = "DeployPollActivateOfIOM"
    NAME_DEPLOY_POLL_ACTIVATE_OF_LOCAL_FI = "DeployPollActivateOfLocalFI"
    NAME_DEPLOY_POLL_ACTIVATE_OF_REMOTE_FI = "DeployPollActivateOfRemoteFI"
    NAME_DEPLOY_POLL_ACTIVATE_OF_UCSM = "DeployPollActivateOfUCSM"
    NAME_DEPLOY_POLL_ACTIVATE_OF_UCSMSERVICE_PACK = "DeployPollActivateOfUCSMServicePack"
    NAME_DEPLOY_POLL_FAB_EVAC_OFF_REMOTE_FI = "DeployPollFabEvacOffRemoteFI"
    NAME_DEPLOY_POLL_FAB_EVAC_ON_REMOTE_FI = "DeployPollFabEvacOnRemoteFI"
    NAME_DEPLOY_POLL_FAIL_OVER_TO_REMOTE_FI = "DeployPollFailOverToRemoteFI"
    NAME_DEPLOY_POLL_INTERNAL_BACKUP = "DeployPollInternalBackup"
    NAME_DEPLOY_POLL_UPDATE_OF_IOM = "DeployPollUpdateOfIOM"
    NAME_DEPLOY_POLL_WAIT_FOR_USER_ACK = "DeployPollWaitForUserAck"
    NAME_DEPLOY_RESOLVE_DISTRIBUTABLE = "DeployResolveDistributable"
    NAME_DEPLOY_RESOLVE_DISTRIBUTABLE_NAMES = "DeployResolveDistributableNames"
    NAME_DEPLOY_RESOLVE_IMAGES = "DeployResolveImages"
    NAME_DEPLOY_SUCCESS = "DeploySuccess"
    NAME_DEPLOY_UPDATE_IOM = "DeployUpdateIOM"
    NAME_DEPLOY_WAIT_FOR_DEPLOY = "DeployWaitForDeploy"
    NAME_DEPLOY_WAIT_FOR_USER_ACK = "DeployWaitForUserAck"
    NAME_NOP = "nop"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class FirmwareSystemFsmStage(ManagedObject):
    """This is FirmwareSystemFsmStage class."""

    consts = FirmwareSystemFsmStageConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("FirmwareSystemFsmStage", "firmwareSystemFsmStage", "stage-[name]", VersionMeta.Version211a, "OutputOnly", 0xf, [], [""], [u'firmwareSystemFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, None, None, None, None, ["ApplyCatalogPackActivateCatalog", "ApplyCatalogPackBegin", "ApplyCatalogPackFail", "ApplyCatalogPackResolveDistributable", "ApplyCatalogPackResolveDistributableNames", "ApplyCatalogPackResolveImages", "ApplyCatalogPackSuccess", "DeployActivateIOM", "DeployActivateLocalFI", "DeployActivateRemoteFI", "DeployActivateUCSM", "DeployActivateUCSMServicePack", "DeployBegin", "DeployCopyAllImagesToPeer", "DeployDownloadImages", "DeployFabEvacOffRemoteFI", "DeployFabEvacOnRemoteFI", "DeployFail", "DeployFailOverToRemoteFI", "DeployInternalBackup", "DeployPollActivateOfIOM", "DeployPollActivateOfLocalFI", "DeployPollActivateOfRemoteFI", "DeployPollActivateOfUCSM", "DeployPollActivateOfUCSMServicePack", "DeployPollFabEvacOffRemoteFI", "DeployPollFabEvacOnRemoteFI", "DeployPollFailOverToRemoteFI", "DeployPollInternalBackup", "DeployPollUpdateOfIOM", "DeployPollWaitForUserAck", "DeployResolveDistributable", "DeployResolveDistributableNames", "DeployResolveImages", "DeploySuccess", "DeployUpdateIOM", "DeployWaitForDeploy", "DeployWaitForUserAck", "nop"], []), 
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "retry": MoPropertyMeta("retry", "retry", "byte", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
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

        ManagedObject.__init__(self, "FirmwareSystemFsmStage", parent_mo_or_dn, **kwargs)
