"""This module contains the general information for StorageLunResourceSelectionLog ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageLunResourceSelectionLogConsts:
    DECISION_TYPE_AFFINITY = "affinity"
    DECISION_TYPE_DEDICATED_HOT_SPARE = "dedicated-hot-spare"
    DECISION_TYPE_GLOBAL_HOT_SPARE = "global-hot-spare"
    DECISION_TYPE_NORMAL_DISK = "normal-disk"
    DECISION_TYPE_SELECT_LUN = "select-lun"
    DECISION_TYPE_SHARE_DISK_GROUP = "share-disk-group"
    DECISION_TYPE_UNSPECIFIED = "unspecified"
    DECISION_TYPE_USE_REMAINING_DISK = "use-remaining-disk"
    DECISION_TYPE_USE_REMAINING_SPACE = "use-remaining-space"
    DECISION_TYPE_VERIFY_CONTROLLER_CONFIG = "verify-controller-config"
    DECISION_TYPE_VERIFY_DISK_CONFIG = "verify-disk-config"
    DECISION_TYPE_VERIFY_DISKGROUP_CONFIG = "verify-diskgroup-config"
    DECISION_TYPE_VERIFY_LUN_CONFIG = "verify-lun-config"
    DECISION_TYPE_VERIFY_RAID_CONFIG = "verify-raid-config"
    DECISION_TYPE_VERIFY_RESOURCES = "verify-resources"
    DECISION_TYPE_VERIFY_STRIP_SIZE_CONFIG = "verify-strip-size-config"
    DECISION_TYPE_VERIFY_VIRTUAL_DRIVE_CONFIG = "verify-virtual-drive-config"
    RESULT_DATA_LOSS = "data-loss"
    RESULT_FAILED = "failed"
    RESULT_SUCCEEDED = "succeeded"
    RESULT_UNSPECIFIED = "unspecified"


class StorageLunResourceSelectionLog(ManagedObject):
    """This is StorageLunResourceSelectionLog class."""

    consts = StorageLunResourceSelectionLogConsts()
    naming_props = set(['order'])

    mo_meta = MoMeta("StorageLunResourceSelectionLog", "storageLunResourceSelectionLog", "selection-log-[order]", VersionMeta.Version224b, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], ['storageVirtualDriveRef'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "decision_type": MoPropertyMeta("decision_type", "decisionType", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["affinity", "dedicated-hot-spare", "global-hot-spare", "normal-disk", "select-lun", "share-disk-group", "unspecified", "use-remaining-disk", "use-remaining-space", "verify-controller-config", "verify-disk-config", "verify-diskgroup-config", "verify-lun-config", "verify-raid-config", "verify-resources", "verify-strip-size-config", "verify-virtual-drive-config"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version224b, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "result": MoPropertyMeta("result", "result", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["data-loss", "failed", "succeeded", "unspecified"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "time_stamp": MoPropertyMeta("time_stamp", "timeStamp", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "decisionType": "decision_type", 
        "descr": "descr", 
        "dn": "dn", 
        "order": "order", 
        "result": "result", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "timeStamp": "time_stamp", 
    }

    def __init__(self, parent_mo_or_dn, order, **kwargs):
        self._dirty_mask = 0
        self.order = order
        self.child_action = None
        self.decision_type = None
        self.descr = None
        self.result = None
        self.sacl = None
        self.status = None
        self.time_stamp = None

        ManagedObject.__init__(self, "StorageLunResourceSelectionLog", parent_mo_or_dn, **kwargs)
