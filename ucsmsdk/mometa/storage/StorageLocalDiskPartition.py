"""This module contains the general information for StorageLocalDiskPartition ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageLocalDiskPartitionConsts():
    BOOTABLE_FALSE = "false"
    BOOTABLE_TRUE = "true"
    BOOTABLE_UNKNOWN = "unknown"
    INT_ID_NONE = "none"
    ORDER_UNSPECIFIED = "unspecified"
    PARTITION_END_UNKNOWN = "unknown"
    PARTITION_START_UNKNOWN = "unknown"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SIZE_UNKNOWN = "unknown"
    TYPE_EMPTY = "empty"
    TYPE_EXT2 = "ext2"
    TYPE_EXT3 = "ext3"
    TYPE_EXTENDED = "extended"
    TYPE_FAT32 = "fat32"
    TYPE_LINUX = "linux"
    TYPE_LINUX_LVM = "linux-lvm"
    TYPE_LINUX_SWAP = "linux-swap"
    TYPE_NONE = "none"
    TYPE_NTFS = "ntfs"
    TYPE_SWAP = "swap"


class StorageLocalDiskPartition(ManagedObject):
    """This is StorageLocalDiskPartition class."""

    consts = StorageLocalDiskPartitionConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("StorageLocalDiskPartition", "storageLocalDiskPartition", "partition-[id]", VersionMeta.Version101e, "InputOutput", 0x7ffL, [], ["read-only"], [u'storageLocalDisk', u'storageLocalDiskConfigDef', u'storageLocalDiskConfigPolicy'], [], ["Get"])

    prop_meta = {
        "bootable": MoPropertyMeta("bootable", "bootable", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "true", "unknown"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x8L, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "partition_end": MoPropertyMeta("partition_end", "partitionEnd", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "partition_start": MoPropertyMeta("partition_start", "partitionStart", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "raw_type_desc": MoPropertyMeta("raw_type_desc", "rawTypeDesc", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["unknown"], ["0-4294967295"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, ["empty", "ext2", "ext3", "extended", "fat32", "linux", "linux-lvm", "linux-swap", "none", "ntfs", "swap"], ["0-4294967295"]), 
    }

    prop_map = {
        "bootable": "bootable", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "id": "id", 
        "intId": "int_id", 
        "name": "name", 
        "order": "order", 
        "partitionEnd": "partition_end", 
        "partitionStart": "partition_start", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
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
        self.descr = None
        self.int_id = None
        self.name = None
        self.order = None
        self.partition_end = None
        self.partition_start = None
        self.policy_level = None
        self.policy_owner = None
        self.raw_type_desc = None
        self.sacl = None
        self.size = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "StorageLocalDiskPartition", parent_mo_or_dn, **kwargs)

