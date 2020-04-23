"""This module contains the general information for MgmtIfFsmStage ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtIfFsmStageConsts:
    LAST_UPDATE_TIME_ = ""
    NAME_DISABLE_VIP_BEGIN = "DisableVipBegin"
    NAME_DISABLE_VIP_FAIL = "DisableVipFail"
    NAME_DISABLE_VIP_PEER = "DisableVipPeer"
    NAME_DISABLE_VIP_SUCCESS = "DisableVipSuccess"
    NAME_ENABLE_HABEGIN = "EnableHABegin"
    NAME_ENABLE_HAFAIL = "EnableHAFail"
    NAME_ENABLE_HALOCAL = "EnableHALocal"
    NAME_ENABLE_HASUCCESS = "EnableHASuccess"
    NAME_ENABLE_VIP_BEGIN = "EnableVipBegin"
    NAME_ENABLE_VIP_FAIL = "EnableVipFail"
    NAME_ENABLE_VIP_LOCAL = "EnableVipLocal"
    NAME_ENABLE_VIP_SUCCESS = "EnableVipSuccess"
    NAME_FA_CONN_BEGIN = "FaConnBegin"
    NAME_FA_CONN_CONFIGURE_VIF_NS = "FaConnConfigureVifNs"
    NAME_FA_CONN_DISCOVER_CHASSIS = "FaConnDiscoverChassis"
    NAME_FA_CONN_DISCOVER_SAS_EXPANDER = "FaConnDiscoverSasExpander"
    NAME_FA_CONN_FAIL = "FaConnFail"
    NAME_FA_CONN_OOB_STORAGE_INVENTORY = "FaConnOobStorageInventory"
    NAME_FA_CONN_SHARED_IOMODULE_INVENTORY = "FaConnSharedIOModuleInventory"
    NAME_FA_CONN_SUCCESS = "FaConnSuccess"
    NAME_FA_PRESENCE_BEGIN = "FaPresenceBegin"
    NAME_FA_PRESENCE_CHECK_LICENSE = "FaPresenceCheckLicense"
    NAME_FA_PRESENCE_FAIL = "FaPresenceFail"
    NAME_FA_PRESENCE_IDENTIFY = "FaPresenceIdentify"
    NAME_FA_PRESENCE_SUCCESS = "FaPresenceSuccess"
    NAME_SW_MGMT_INBAND_IF_CONFIG_BEGIN = "SwMgmtInbandIfConfigBegin"
    NAME_SW_MGMT_INBAND_IF_CONFIG_FAIL = "SwMgmtInbandIfConfigFail"
    NAME_SW_MGMT_INBAND_IF_CONFIG_SUCCESS = "SwMgmtInbandIfConfigSuccess"
    NAME_SW_MGMT_INBAND_IF_CONFIG_SWITCH = "SwMgmtInbandIfConfigSwitch"
    NAME_SW_MGMT_OOB_IF_CONFIG_BEGIN = "SwMgmtOobIfConfigBegin"
    NAME_SW_MGMT_OOB_IF_CONFIG_FAIL = "SwMgmtOobIfConfigFail"
    NAME_SW_MGMT_OOB_IF_CONFIG_SUCCESS = "SwMgmtOobIfConfigSuccess"
    NAME_SW_MGMT_OOB_IF_CONFIG_SWITCH = "SwMgmtOobIfConfigSwitch"
    NAME_VIRTUAL_IF_CONFIG_BEGIN = "VirtualIfConfigBegin"
    NAME_VIRTUAL_IF_CONFIG_FAIL = "VirtualIfConfigFail"
    NAME_VIRTUAL_IF_CONFIG_LOCAL = "VirtualIfConfigLocal"
    NAME_VIRTUAL_IF_CONFIG_REMOTE = "VirtualIfConfigRemote"
    NAME_VIRTUAL_IF_CONFIG_SUCCESS = "VirtualIfConfigSuccess"
    NAME_NOP = "nop"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class MgmtIfFsmStage(ManagedObject):
    """This is MgmtIfFsmStage class."""

    consts = MgmtIfFsmStageConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("MgmtIfFsmStage", "mgmtIfFsmStage", "stage-[name]", VersionMeta.Version211a, "OutputOnly", 0xf, [], [""], ['mgmtIfFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, None, None, None, None, ["DisableVipBegin", "DisableVipFail", "DisableVipPeer", "DisableVipSuccess", "EnableHABegin", "EnableHAFail", "EnableHALocal", "EnableHASuccess", "EnableVipBegin", "EnableVipFail", "EnableVipLocal", "EnableVipSuccess", "FaConnBegin", "FaConnConfigureVifNs", "FaConnDiscoverChassis", "FaConnDiscoverSasExpander", "FaConnFail", "FaConnOobStorageInventory", "FaConnSharedIOModuleInventory", "FaConnSuccess", "FaPresenceBegin", "FaPresenceCheckLicense", "FaPresenceFail", "FaPresenceIdentify", "FaPresenceSuccess", "SwMgmtInbandIfConfigBegin", "SwMgmtInbandIfConfigFail", "SwMgmtInbandIfConfigSuccess", "SwMgmtInbandIfConfigSwitch", "SwMgmtOobIfConfigBegin", "SwMgmtOobIfConfigFail", "SwMgmtOobIfConfigSuccess", "SwMgmtOobIfConfigSwitch", "VirtualIfConfigBegin", "VirtualIfConfigFail", "VirtualIfConfigLocal", "VirtualIfConfigRemote", "VirtualIfConfigSuccess", "nop"], []),
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

        ManagedObject.__init__(self, "MgmtIfFsmStage", parent_mo_or_dn, **kwargs)
