"""This module contains the general information for StorageScsiLunInstRef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageScsiLunInstRefConsts():
    ADMIN_STATE_OFFLINE = "offline"
    ADMIN_STATE_ONLINE = "online"
    ADMIN_STATE_UNDEPLOYED = "undeployed"
    AUTO_AQUIRED_FALSE = "false"
    AUTO_AQUIRED_NO = "no"
    AUTO_AQUIRED_TRUE = "true"
    AUTO_AQUIRED_YES = "yes"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLY_FAILED = "apply-failed"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_NOT_IN_USE = "not-in-use"
    CONFIG_STATE_ORPHANED = "orphaned"
    SNAPSHOT_ADMIN_STATE_ABORT_REPLICATION = "abort-replication"
    SNAPSHOT_ADMIN_STATE_CREATE = "create"
    SNAPSHOT_ADMIN_STATE_CREATE_LUN_REPLICA = "create-lun-replica"
    SNAPSHOT_ADMIN_STATE_REPLICATION_RESTORE = "replication-restore"
    SNAPSHOT_ADMIN_STATE_SET_REPLICATION_OFFLINE = "set-replication-offline"
    SNAPSHOT_ADMIN_STATE_SET_REPLICATION_ONLINE = "set-replication-online"
    SNAPSHOT_ADMIN_STATE_UNDEFINED = "undefined"


class StorageScsiLunInstRef(ManagedObject):
    """This is StorageScsiLunInstRef class."""

    consts = StorageScsiLunInstRefConsts()
    naming_props = set([u'lunItemName'])

    mo_meta = MoMeta("StorageScsiLunInstRef", "storageScsiLunInstRef", "lun-inst-ref-[lun_item_name]", VersionMeta.Version302c, "InputOutput", 0xfffL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], [u'lsServer'], [u'faultInst'], [None])

    prop_meta = {
        "admin_name": MoPropertyMeta("admin_name", "adminName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x2L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["offline", "online", "undeployed"], []), 
        "auto_aquired": MoPropertyMeta("auto_aquired", "autoAquired", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["false", "no", "true", "yes"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x10L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "apply-failed", "applying", "not-applied", "not-in-use", "orphaned"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "lun_dn": MoPropertyMeta("lun_dn", "lunDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40L, 0, 256, None, [], []), 
        "lun_item_dn": MoPropertyMeta("lun_item_dn", "lunItemDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "lun_item_name": MoPropertyMeta("lun_item_name", "lunItemName", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x80L, 1, 32, None, [], []), 
        "lun_mask_id": MoPropertyMeta("lun_mask_id", "lunMaskId", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-255"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x100L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "size": MoPropertyMeta("size", "size", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, [], ["1-10240"]), 
        "snapshot_admin_state": MoPropertyMeta("snapshot_admin_state", "snapshotAdminState", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, ["abort-replication", "create", "create-lun-replica", "replication-restore", "set-replication-offline", "set-replication-online", "undefined"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x800L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "volume_dn": MoPropertyMeta("volume_dn", "volumeDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
    }

    prop_map = {
        "adminName": "admin_name", 
        "adminState": "admin_state", 
        "autoAquired": "auto_aquired", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "dn": "dn", 
        "lunDn": "lun_dn", 
        "lunItemDn": "lun_item_dn", 
        "lunItemName": "lun_item_name", 
        "lunMaskId": "lun_mask_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "size": "size", 
        "snapshotAdminState": "snapshot_admin_state", 
        "status": "status", 
        "volumeDn": "volume_dn", 
    }

    def __init__(self, parent_mo_or_dn, lun_item_name, **kwargs):
        self._dirty_mask = 0
        self.lun_item_name = lun_item_name
        self.admin_name = None
        self.admin_state = None
        self.auto_aquired = None
        self.child_action = None
        self.config_state = None
        self.lun_dn = None
        self.lun_item_dn = None
        self.lun_mask_id = None
        self.sacl = None
        self.size = None
        self.snapshot_admin_state = None
        self.status = None
        self.volume_dn = None

        ManagedObject.__init__(self, "StorageScsiLunInstRef", parent_mo_or_dn, **kwargs)

