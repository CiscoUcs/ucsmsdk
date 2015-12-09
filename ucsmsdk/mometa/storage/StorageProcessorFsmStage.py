"""This module contains the general information for StorageProcessorFsmStage ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageProcessorFsmStageConsts():
    LAST_UPDATE_TIME_ = ""
    NAME_DEPLOY_SYSTEM_BEGIN = "DeploySystemBegin"
    NAME_DEPLOY_SYSTEM_CONFIG_HASTATE = "DeploySystemConfigHAState"
    NAME_DEPLOY_SYSTEM_CONFIG_NETWORK = "DeploySystemConfigNetwork"
    NAME_DEPLOY_SYSTEM_CONFIG_PLATFORM = "DeploySystemConfigPlatform"
    NAME_DEPLOY_SYSTEM_CONFIG_STORAGE_REPLICATION_SERVICE = "DeploySystemConfigStorageReplicationService"
    NAME_DEPLOY_SYSTEM_CONFIG_STORAGE_TARGET_IDENTITY = "DeploySystemConfigStorageTargetIdentity"
    NAME_DEPLOY_SYSTEM_CONNECT_SMELOCAL = "DeploySystemConnectSMELocal"
    NAME_DEPLOY_SYSTEM_CONNECT_SMEREMOTE = "DeploySystemConnectSMERemote"
    NAME_DEPLOY_SYSTEM_FAIL = "DeploySystemFail"
    NAME_DEPLOY_SYSTEM_POWER_ON = "DeploySystemPowerOn"
    NAME_DEPLOY_SYSTEM_SUCCESS = "DeploySystemSuccess"
    NAME_DISCOVER_SYSTEM_BEGIN = "DiscoverSystemBegin"
    NAME_DISCOVER_SYSTEM_CONNECT_SMELOCAL = "DiscoverSystemConnectSMELocal"
    NAME_DISCOVER_SYSTEM_CONNECT_SMEREMOTE = "DiscoverSystemConnectSMERemote"
    NAME_DISCOVER_SYSTEM_FAIL = "DiscoverSystemFail"
    NAME_DISCOVER_SYSTEM_INITIATE_POLL_BMCLOCAL = "DiscoverSystemInitiatePollBMCLocal"
    NAME_DISCOVER_SYSTEM_INITIATE_POLL_BMCREMOTE = "DiscoverSystemInitiatePollBMCRemote"
    NAME_DISCOVER_SYSTEM_SUCCESS = "DiscoverSystemSuccess"
    NAME_DISCOVER_SYSTEM_WAIT_FOR_INVENTORY = "DiscoverSystemWaitForInventory"
    NAME_DISCOVER_SYSTEM_WAIT_FOR_OSSTATUS = "DiscoverSystemWaitForOSStatus"
    NAME_DISCOVER_SYSTEM_WAIT_FOR_SMECONNECTION = "DiscoverSystemWaitForSMEConnection"
    NAME_ENTER_MAINTENANCE_BEGIN = "EnterMaintenanceBegin"
    NAME_ENTER_MAINTENANCE_DISABLE_STORAGE_TARGET = "EnterMaintenanceDisableStorageTarget"
    NAME_ENTER_MAINTENANCE_FAIL = "EnterMaintenanceFail"
    NAME_ENTER_MAINTENANCE_POWER_OFF = "EnterMaintenancePowerOff"
    NAME_ENTER_MAINTENANCE_SLOT_POWER_CYCLE = "EnterMaintenanceSlotPowerCycle"
    NAME_ENTER_MAINTENANCE_SUCCESS = "EnterMaintenanceSuccess"
    NAME_ENTER_MAINTENANCE_WAIT_FOR_SERVER_SHUTDOWN = "EnterMaintenanceWaitForServerShutdown"
    NAME_EXIT_MAINTENANCE_BEGIN = "ExitMaintenanceBegin"
    NAME_EXIT_MAINTENANCE_ENABLE_STORAGE_TARGET = "ExitMaintenanceEnableStorageTarget"
    NAME_EXIT_MAINTENANCE_FAIL = "ExitMaintenanceFail"
    NAME_EXIT_MAINTENANCE_SUCCESS = "ExitMaintenanceSuccess"
    NAME_EXIT_MAINTENANCE_WAIT_FOR_HAQUORUM = "ExitMaintenanceWaitForHAQuorum"
    NAME_EXIT_MAINTENANCE_WAIT_FOR_SMECONNECTION = "ExitMaintenanceWaitForSMEConnection"
    NAME_EXIT_MAINTENANCE_WAIT_FOR_SERVER_POWER_UP = "ExitMaintenanceWaitForServerPowerUp"
    NAME_HA_TAKE_OVER_BEGIN = "HaTakeOverBegin"
    NAME_HA_TAKE_OVER_FAIL = "HaTakeOverFail"
    NAME_HA_TAKE_OVER_PERFORM_HA_TAKE_OVER = "HaTakeOverPerformHaTakeOver"
    NAME_HA_TAKE_OVER_SUCCESS = "HaTakeOverSuccess"
    NAME_UNDEPLOY_SYSTEM_BEGIN = "UndeploySystemBegin"
    NAME_UNDEPLOY_SYSTEM_DISABLE_STORAGE_TARGET = "UndeploySystemDisableStorageTarget"
    NAME_UNDEPLOY_SYSTEM_DISASSOC_STORAGE_CONTROLLER = "UndeploySystemDisassocStorageController"
    NAME_UNDEPLOY_SYSTEM_FAIL = "UndeploySystemFail"
    NAME_UNDEPLOY_SYSTEM_POWER_OFF = "UndeploySystemPowerOff"
    NAME_UNDEPLOY_SYSTEM_SLOT_POWER_CYCLE = "UndeploySystemSlotPowerCycle"
    NAME_UNDEPLOY_SYSTEM_SUCCESS = "UndeploySystemSuccess"
    NAME_UNDEPLOY_SYSTEM_UNDEPLOY_NETWORK = "UndeploySystemUndeployNetwork"
    NAME_UNDEPLOY_SYSTEM_UNDEPLOY_PLATFORM = "UndeploySystemUndeployPlatform"
    NAME_UNDEPLOY_SYSTEM_UNDEPLOY_STORAGE = "UndeploySystemUndeployStorage"
    NAME_UNDEPLOY_SYSTEM_UNDEPLOY_TARGET_IDENTITY = "UndeploySystemUndeployTargetIdentity"
    NAME_UNDEPLOY_SYSTEM_WAIT_FOR_DISASSOC_COMPLETION = "UndeploySystemWaitForDisassocCompletion"
    NAME_UNDEPLOY_SYSTEM_WAIT_FOR_SERVER_SHUTDOWN = "UndeploySystemWaitForServerShutdown"
    NAME_UNDEPLOY_SYSTEM_WAIT_FOR_UNDEPLOY_STORAGE = "UndeploySystemWaitForUndeployStorage"
    NAME_NOP = "nop"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class StorageProcessorFsmStage(ManagedObject):
    """This is StorageProcessorFsmStage class."""

    consts = StorageProcessorFsmStageConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("StorageProcessorFsmStage", "storageProcessorFsmStage", "stage-[name]", VersionMeta.Version302c, "OutputOnly", 0xfL, [], [""], [u'storageProcessorFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, None, None, None, None, ["DeploySystemBegin", "DeploySystemConfigHAState", "DeploySystemConfigNetwork", "DeploySystemConfigPlatform", "DeploySystemConfigStorageReplicationService", "DeploySystemConfigStorageTargetIdentity", "DeploySystemConnectSMELocal", "DeploySystemConnectSMERemote", "DeploySystemFail", "DeploySystemPowerOn", "DeploySystemSuccess", "DiscoverSystemBegin", "DiscoverSystemConnectSMELocal", "DiscoverSystemConnectSMERemote", "DiscoverSystemFail", "DiscoverSystemInitiatePollBMCLocal", "DiscoverSystemInitiatePollBMCRemote", "DiscoverSystemSuccess", "DiscoverSystemWaitForInventory", "DiscoverSystemWaitForOSStatus", "DiscoverSystemWaitForSMEConnection", "EnterMaintenanceBegin", "EnterMaintenanceDisableStorageTarget", "EnterMaintenanceFail", "EnterMaintenancePowerOff", "EnterMaintenanceSlotPowerCycle", "EnterMaintenanceSuccess", "EnterMaintenanceWaitForServerShutdown", "ExitMaintenanceBegin", "ExitMaintenanceEnableStorageTarget", "ExitMaintenanceFail", "ExitMaintenanceSuccess", "ExitMaintenanceWaitForHAQuorum", "ExitMaintenanceWaitForSMEConnection", "ExitMaintenanceWaitForServerPowerUp", "HaTakeOverBegin", "HaTakeOverFail", "HaTakeOverPerformHaTakeOver", "HaTakeOverSuccess", "UndeploySystemBegin", "UndeploySystemDisableStorageTarget", "UndeploySystemDisassocStorageController", "UndeploySystemFail", "UndeploySystemPowerOff", "UndeploySystemSlotPowerCycle", "UndeploySystemSuccess", "UndeploySystemUndeployNetwork", "UndeploySystemUndeployPlatform", "UndeploySystemUndeployStorage", "UndeploySystemUndeployTargetIdentity", "UndeploySystemWaitForDisassocCompletion", "UndeploySystemWaitForServerShutdown", "UndeploySystemWaitForUndeployStorage", "nop"], []), 
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

        ManagedObject.__init__(self, "StorageProcessorFsmStage", parent_mo_or_dn, **kwargs)

