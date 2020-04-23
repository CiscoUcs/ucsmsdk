"""This module contains the general information for StorageLocalDiskPartition ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageLocalDiskPartitionConsts:
    BOOTABLE_FALSE = "false"
    BOOTABLE_TRUE = "true"
    BOOTABLE_UNKNOWN = "unknown"
    PARTITION_END_UNKNOWN = "unknown"
    PARTITION_START_UNKNOWN = "unknown"
    SIZE_UNKNOWN = "unknown"
    TYPE_EMPTY = "empty"
    TYPE_EXTENDED = "extended"
    TYPE_LINUX = "linux"
    TYPE_LINUX_LVM = "linux-lvm"
    TYPE_LINUX_SWAP = "linux-swap"


class StorageLocalDiskPartition(ManagedObject):
    """This is StorageLocalDiskPartition class."""

    consts = StorageLocalDiskPartitionConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("StorageLocalDiskPartition", "storageLocalDiskPartition", "partition-[id]", VersionMeta.Version101e, "InputOutput", 0x3ff, [], ["read-only"], ['storageLocalDisk', 'storageLocalDiskConfigDef', 'storageLocalDiskConfigPolicy'], [], ["Get"])

    prop_meta = {
        "bootable": MoPropertyMeta("bootable", "bootable", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "true", "unknown"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "partition_end": MoPropertyMeta("partition_end", "partitionEnd", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-18446744073709551615"]),
        "partition_start": MoPropertyMeta("partition_start", "partitionStart", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-18446744073709551615"]),
        "raw_type_desc": MoPropertyMeta("raw_type_desc", "rawTypeDesc", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["unknown"], ["0-18446744073709551615"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["empty", "extended", "linux", "linux-lvm", "linux-swap"], ["0-255"]),
    }

    prop_map = {
        "bootable": "bootable", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "name": "name", 
        "partitionEnd": "partition_end", 
        "partitionStart": "partition_start", 
        "rawTypeDesc": "raw_type_desc", 
        "rn": "rn", 
        "sacl": "sacl", 
        "size": "size", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.bootable = None
        self.child_action = None
        self.name = None
        self.partition_end = None
        self.partition_start = None
        self.raw_type_desc = None
        self.sacl = None
        self.size = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "StorageLocalDiskPartition", parent_mo_or_dn, **kwargs)
