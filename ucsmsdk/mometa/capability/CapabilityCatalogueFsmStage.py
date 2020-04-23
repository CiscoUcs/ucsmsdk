"""This module contains the general information for CapabilityCatalogueFsmStage ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CapabilityCatalogueFsmStageConsts:
    LAST_UPDATE_TIME_ = ""
    NAME_ACTIVATE_CATALOG_APPLY_CATALOG = "ActivateCatalogApplyCatalog"
    NAME_ACTIVATE_CATALOG_BEGIN = "ActivateCatalogBegin"
    NAME_ACTIVATE_CATALOG_COPY_CAT_FROM_REP = "ActivateCatalogCopyCatFromRep"
    NAME_ACTIVATE_CATALOG_COPY_EXTERNAL_REP_TO_REMOTE = "ActivateCatalogCopyExternalRepToRemote"
    NAME_ACTIVATE_CATALOG_COPY_REMOTE = "ActivateCatalogCopyRemote"
    NAME_ACTIVATE_CATALOG_EVALUATE_STATUS = "ActivateCatalogEvaluateStatus"
    NAME_ACTIVATE_CATALOG_FAIL = "ActivateCatalogFail"
    NAME_ACTIVATE_CATALOG_RESCAN_IMAGES = "ActivateCatalogRescanImages"
    NAME_ACTIVATE_CATALOG_SUCCESS = "ActivateCatalogSuccess"
    NAME_ACTIVATE_CATALOG_UNPACK_LOCAL = "ActivateCatalogUnpackLocal"
    NAME_DEPLOY_CATALOGUE_BEGIN = "DeployCatalogueBegin"
    NAME_DEPLOY_CATALOGUE_FAIL = "DeployCatalogueFail"
    NAME_DEPLOY_CATALOGUE_FINALIZE = "DeployCatalogueFinalize"
    NAME_DEPLOY_CATALOGUE_SUCCESS = "DeployCatalogueSuccess"
    NAME_DEPLOY_CATALOGUE_SYNC_BLADE_AGLOCAL = "DeployCatalogueSyncBladeAGLocal"
    NAME_DEPLOY_CATALOGUE_SYNC_BLADE_AGREMOTE = "DeployCatalogueSyncBladeAGRemote"
    NAME_DEPLOY_CATALOGUE_SYNC_HOSTAGENT_AGLOCAL = "DeployCatalogueSyncHostagentAGLocal"
    NAME_DEPLOY_CATALOGUE_SYNC_HOSTAGENT_AGREMOTE = "DeployCatalogueSyncHostagentAGRemote"
    NAME_DEPLOY_CATALOGUE_SYNC_NIC_AGLOCAL = "DeployCatalogueSyncNicAGLocal"
    NAME_DEPLOY_CATALOGUE_SYNC_NIC_AGREMOTE = "DeployCatalogueSyncNicAGRemote"
    NAME_DEPLOY_CATALOGUE_SYNC_PORT_AGLOCAL = "DeployCatalogueSyncPortAGLocal"
    NAME_DEPLOY_CATALOGUE_SYNC_PORT_AGREMOTE = "DeployCatalogueSyncPortAGRemote"
    NAME_NOP = "nop"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class CapabilityCatalogueFsmStage(ManagedObject):
    """This is CapabilityCatalogueFsmStage class."""

    consts = CapabilityCatalogueFsmStageConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("CapabilityCatalogueFsmStage", "capabilityCatalogueFsmStage", "stage-[name]", VersionMeta.Version211a, "OutputOnly", 0xf, [], [""], ['capabilityCatalogueFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, None, None, None, None, ["ActivateCatalogApplyCatalog", "ActivateCatalogBegin", "ActivateCatalogCopyCatFromRep", "ActivateCatalogCopyExternalRepToRemote", "ActivateCatalogCopyRemote", "ActivateCatalogEvaluateStatus", "ActivateCatalogFail", "ActivateCatalogRescanImages", "ActivateCatalogSuccess", "ActivateCatalogUnpackLocal", "DeployCatalogueBegin", "DeployCatalogueFail", "DeployCatalogueFinalize", "DeployCatalogueSuccess", "DeployCatalogueSyncBladeAGLocal", "DeployCatalogueSyncBladeAGRemote", "DeployCatalogueSyncHostagentAGLocal", "DeployCatalogueSyncHostagentAGRemote", "DeployCatalogueSyncNicAGLocal", "DeployCatalogueSyncNicAGRemote", "DeployCatalogueSyncPortAGLocal", "DeployCatalogueSyncPortAGRemote", "nop"], []),
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

        ManagedObject.__init__(self, "CapabilityCatalogueFsmStage", parent_mo_or_dn, **kwargs)
