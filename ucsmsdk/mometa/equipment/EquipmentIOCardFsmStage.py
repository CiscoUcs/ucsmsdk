"""This module contains the general information for EquipmentIOCardFsmStage ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentIOCardFsmStageConsts:
    LAST_UPDATE_TIME_ = ""
    NAME_EVACUATE_BEGIN = "EvacuateBegin"
    NAME_EVACUATE_EXECUTE = "EvacuateExecute"
    NAME_EVACUATE_FAIL = "EvacuateFail"
    NAME_EVACUATE_SUCCESS = "EvacuateSuccess"
    NAME_FE_CONN_BEGIN = "FeConnBegin"
    NAME_FE_CONN_CONFIGURE_END_POINT = "FeConnConfigureEndPoint"
    NAME_FE_CONN_CONFIGURE_SW_MGMT_END_POINT = "FeConnConfigureSwMgmtEndPoint"
    NAME_FE_CONN_CONFIGURE_VIF_NS = "FeConnConfigureVifNs"
    NAME_FE_CONN_DISCOVER_CHASSIS = "FeConnDiscoverChassis"
    NAME_FE_CONN_ENABLE_CHASSIS = "FeConnEnableChassis"
    NAME_FE_CONN_FAIL = "FeConnFail"
    NAME_FE_CONN_SUCCESS = "FeConnSuccess"
    NAME_FE_PRESENCE_BEGIN = "FePresenceBegin"
    NAME_FE_PRESENCE_CHECK_LICENSE = "FePresenceCheckLicense"
    NAME_FE_PRESENCE_CONFIG_CHASSIS_ID = "FePresenceConfigChassisId"
    NAME_FE_PRESENCE_FAIL = "FePresenceFail"
    NAME_FE_PRESENCE_IDENTIFY = "FePresenceIdentify"
    NAME_FE_PRESENCE_SUCCESS = "FePresenceSuccess"
    NAME_RESET_CMC_BEGIN = "ResetCmcBegin"
    NAME_RESET_CMC_EXECUTE = "ResetCmcExecute"
    NAME_RESET_CMC_FAIL = "ResetCmcFail"
    NAME_RESET_CMC_SUCCESS = "ResetCmcSuccess"
    NAME_RESET_EVACUATE_BEGIN = "ResetEvacuateBegin"
    NAME_RESET_EVACUATE_EXECUTE = "ResetEvacuateExecute"
    NAME_RESET_EVACUATE_FAIL = "ResetEvacuateFail"
    NAME_RESET_EVACUATE_SUCCESS = "ResetEvacuateSuccess"
    NAME_RESET_IOM_BEGIN = "ResetIomBegin"
    NAME_RESET_IOM_EXECUTE = "ResetIomExecute"
    NAME_RESET_IOM_FAIL = "ResetIomFail"
    NAME_RESET_IOM_SUCCESS = "ResetIomSuccess"
    NAME_RESET_PEER_CMC_BEGIN = "ResetPeerCmcBegin"
    NAME_RESET_PEER_CMC_EXECUTE = "ResetPeerCmcExecute"
    NAME_RESET_PEER_CMC_FAIL = "ResetPeerCmcFail"
    NAME_RESET_PEER_CMC_SUCCESS = "ResetPeerCmcSuccess"
    NAME_MUX_OFFLINE_BEGIN = "muxOfflineBegin"
    NAME_MUX_OFFLINE_CLEANUP_ENTRIES = "muxOfflineCleanupEntries"
    NAME_MUX_OFFLINE_FAIL = "muxOfflineFail"
    NAME_MUX_OFFLINE_SUCCESS = "muxOfflineSuccess"
    NAME_NOP = "nop"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class EquipmentIOCardFsmStage(ManagedObject):
    """This is EquipmentIOCardFsmStage class."""

    consts = EquipmentIOCardFsmStageConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("EquipmentIOCardFsmStage", "equipmentIOCardFsmStage", "stage-[name]", VersionMeta.Version211a, "OutputOnly", 0xf, [], [""], ['equipmentIOCardFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, None, None, None, None, ["EvacuateBegin", "EvacuateExecute", "EvacuateFail", "EvacuateSuccess", "FeConnBegin", "FeConnConfigureEndPoint", "FeConnConfigureSwMgmtEndPoint", "FeConnConfigureVifNs", "FeConnDiscoverChassis", "FeConnEnableChassis", "FeConnFail", "FeConnSuccess", "FePresenceBegin", "FePresenceCheckLicense", "FePresenceConfigChassisId", "FePresenceFail", "FePresenceIdentify", "FePresenceSuccess", "ResetCmcBegin", "ResetCmcExecute", "ResetCmcFail", "ResetCmcSuccess", "ResetEvacuateBegin", "ResetEvacuateExecute", "ResetEvacuateFail", "ResetEvacuateSuccess", "ResetIomBegin", "ResetIomExecute", "ResetIomFail", "ResetIomSuccess", "ResetPeerCmcBegin", "ResetPeerCmcExecute", "ResetPeerCmcFail", "ResetPeerCmcSuccess", "muxOfflineBegin", "muxOfflineCleanupEntries", "muxOfflineFail", "muxOfflineSuccess", "nop"], []),
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

        ManagedObject.__init__(self, "EquipmentIOCardFsmStage", parent_mo_or_dn, **kwargs)
