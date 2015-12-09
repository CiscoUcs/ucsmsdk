"""This module contains the general information for OsControllerFsmStage ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class OsControllerFsmStageConsts():
    LAST_UPDATE_TIME_ = ""
    NAME_DEPLOY_OSBEGIN = "DeployOSBegin"
    NAME_DEPLOY_OSCOPY_REMOTE = "DeployOSCopyRemote"
    NAME_DEPLOY_OSDELETE_CURL_DOWNLOADED_IMAGES = "DeployOSDeleteCurlDownloadedImages"
    NAME_DEPLOY_OSDOWNLOAD_IMAGES = "DeployOSDownloadImages"
    NAME_DEPLOY_OSFAIL = "DeployOSFail"
    NAME_DEPLOY_OSHOST_BIOS_POST_COMPLETION = "DeployOSHostBiosPostCompletion"
    NAME_DEPLOY_OSHOST_BMC_PRE_CONFIG_LOCAL = "DeployOSHostBmcPreConfigLocal"
    NAME_DEPLOY_OSHOST_BMC_PRE_CONFIG_PEER = "DeployOSHostBmcPreConfigPeer"
    NAME_DEPLOY_OSHOST_BOOT = "DeployOSHostBoot"
    NAME_DEPLOY_OSHOST_BOOT_FOR_UPGRADE = "DeployOSHostBootForUpgrade"
    NAME_DEPLOY_OSHOST_BOOT_WAIT = "DeployOSHostBootWait"
    NAME_DEPLOY_OSHOST_CLEAR_OS_INSTALL_STATUS = "DeployOSHostClearOsInstallStatus"
    NAME_DEPLOY_OSHOST_POST_FIRST_BOOT = "DeployOSHostPostFirstBoot"
    NAME_DEPLOY_OSHOST_POST_INSTALL = "DeployOSHostPostInstall"
    NAME_DEPLOY_OSHOST_POST_UPGRADE = "DeployOSHostPostUpgrade"
    NAME_DEPLOY_OSHOST_PRE_FIRST_BOOT = "DeployOSHostPreFirstBoot"
    NAME_DEPLOY_OSHOST_PRE_INSTALL = "DeployOSHostPreInstall"
    NAME_DEPLOY_OSHOST_READ_SMBIOS = "DeployOSHostReadSmbios"
    NAME_DEPLOY_OSHOST_SERIAL_DEBUG_CONNECT = "DeployOSHostSerialDebugConnect"
    NAME_DEPLOY_OSHOST_SERIAL_DEBUG_DISCONNECT = "DeployOSHostSerialDebugDisconnect"
    NAME_DEPLOY_OSHOST_SETUP_VMEDIA_LOCAL = "DeployOSHostSetupVmediaLocal"
    NAME_DEPLOY_OSHOST_SETUP_VMEDIA_PEER = "DeployOSHostSetupVmediaPeer"
    NAME_DEPLOY_OSHOST_SOL_REDIRECT_DISABLE = "DeployOSHostSolRedirectDisable"
    NAME_DEPLOY_OSHOST_SOL_REDIRECT_ENABLE = "DeployOSHostSolRedirectEnable"
    NAME_DEPLOY_OSHOST_TEARDOWN_VMEDIA_LOCAL = "DeployOSHostTeardownVmediaLocal"
    NAME_DEPLOY_OSHOST_TEARDOWN_VMEDIA_PEER = "DeployOSHostTeardownVmediaPeer"
    NAME_DEPLOY_OSSUCCESS = "DeployOSSuccess"
    NAME_DEPLOY_OSWAIT_FOR_SMECONNECTION = "DeployOSWaitForSMEConnection"
    NAME_NOP = "nop"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class OsControllerFsmStage(ManagedObject):
    """This is OsControllerFsmStage class."""

    consts = OsControllerFsmStageConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("OsControllerFsmStage", "osControllerFsmStage", "stage-[name]", VersionMeta.Version302c, "OutputOnly", 0xfL, [], [""], [u'osControllerFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, None, None, None, None, ["DeployOSBegin", "DeployOSCopyRemote", "DeployOSDeleteCurlDownloadedImages", "DeployOSDownloadImages", "DeployOSFail", "DeployOSHostBiosPostCompletion", "DeployOSHostBmcPreConfigLocal", "DeployOSHostBmcPreConfigPeer", "DeployOSHostBoot", "DeployOSHostBootForUpgrade", "DeployOSHostBootWait", "DeployOSHostClearOsInstallStatus", "DeployOSHostPostFirstBoot", "DeployOSHostPostInstall", "DeployOSHostPostUpgrade", "DeployOSHostPreFirstBoot", "DeployOSHostPreInstall", "DeployOSHostReadSmbios", "DeployOSHostSerialDebugConnect", "DeployOSHostSerialDebugDisconnect", "DeployOSHostSetupVmediaLocal", "DeployOSHostSetupVmediaPeer", "DeployOSHostSolRedirectDisable", "DeployOSHostSolRedirectEnable", "DeployOSHostTeardownVmediaLocal", "DeployOSHostTeardownVmediaPeer", "DeployOSSuccess", "DeployOSWaitForSMEConnection", "nop"], []), 
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "retry": MoPropertyMeta("retry", "retry", "byte", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "stage_status": MoPropertyMeta("stage_status", "stageStatus", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
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

        ManagedObject.__init__(self, "OsControllerFsmStage", parent_mo_or_dn, **kwargs)

