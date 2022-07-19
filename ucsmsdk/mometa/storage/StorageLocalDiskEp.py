"""This module contains the general information for StorageLocalDiskEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageLocalDiskEpConsts:
    BOOTABLE_FALSE = "false"
    BOOTABLE_TRUE = "true"
    BOOTABLE_UNKNOWN = "unknown"
    DISK_STATE_NA = "NA"
    DISK_STATE_BAD = "bad"
    DISK_STATE_COPYBACK = "copyback"
    DISK_STATE_DEDICATED_HOT_SPARE = "dedicated-hot-spare"
    DISK_STATE_DISABLED_FOR_REMOVAL = "disabled-for-removal"
    DISK_STATE_FAILED = "failed"
    DISK_STATE_FOREIGN_CONFIGURATION = "foreign-configuration"
    DISK_STATE_GLOBAL_HOT_SPARE = "global-hot-spare"
    DISK_STATE_GOOD = "good"
    DISK_STATE_JBOD = "jbod"
    DISK_STATE_LOCKED_FOREIGN_CONFIGURATION = "locked-foreign-configuration"
    DISK_STATE_OFFLINE = "offline"
    DISK_STATE_ONLINE = "online"
    DISK_STATE_PREDICTIVE_FAILURE = "predictive-failure"
    DISK_STATE_REBUILDING = "rebuilding"
    DISK_STATE_SELF_TEST_FAILED = "self-test-failed"
    DISK_STATE_UNCONFIGURED_BAD = "unconfigured-bad"
    DISK_STATE_UNCONFIGURED_GOOD = "unconfigured-good"
    DISK_STATE_UNKNOWN = "unknown"
    DISK_STATE_ZEROING = "zeroing"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"


class StorageLocalDiskEp(ManagedObject):
    """This is StorageLocalDiskEp class."""

    consts = StorageLocalDiskEpConsts()
    naming_props = set(['encId', 'id'])

    mo_meta = MoMeta("StorageLocalDiskEp", "storageLocalDiskEp", "disk-ep-[enc_id]-id-[id]", VersionMeta.Version302c, "InputOutput", 0x7f, [], ["read-only"], ['storageController'], [], ["Get"])

    prop_meta = {
        "bootable": MoPropertyMeta("bootable", "bootable", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "true", "unknown"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "disk_dn": MoPropertyMeta("disk_dn", "diskDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "disk_state": MoPropertyMeta("disk_state", "diskState", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "bad", "copyback", "dedicated-hot-spare", "disabled-for-removal", "failed", "foreign-configuration", "global-hot-spare", "good", "jbod", "locked-foreign-configuration", "offline", "online", "predictive-failure", "rebuilding", "self-test-failed", "unconfigured-bad", "unconfigured-good", "unknown", "zeroing"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "enc_id": MoPropertyMeta("enc_id", "encId", "uint", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []),
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "bootable": "bootable", 
        "childAction": "child_action", 
        "diskDn": "disk_dn", 
        "diskState": "disk_state", 
        "dn": "dn", 
        "encId": "enc_id", 
        "id": "id", 
        "lc": "lc", 
        "model": "model", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, enc_id, id, **kwargs):
        self._dirty_mask = 0
        self.enc_id = enc_id
        self.id = id
        self.bootable = None
        self.child_action = None
        self.disk_dn = None
        self.disk_state = None
        self.lc = None
        self.model = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "StorageLocalDiskEp", parent_mo_or_dn, **kwargs)
