"""This module contains the general information for StorageQual ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageQualConsts():
    BLOCK_SIZE_UNKNOWN = "unknown"
    DISK_TYPE_HDD = "HDD"
    DISK_TYPE_SSD = "SSD"
    DISK_TYPE_UNSPECIFIED = "unspecified"
    DISKLESS_NO = "no"
    DISKLESS_UNSPECIFIED = "unspecified"
    DISKLESS_YES = "yes"
    MAX_CAP_UNKNOWN = "unknown"
    MIN_CAP_UNKNOWN = "unknown"
    NUMBER_OF_BLOCKS_UNKNOWN = "unknown"
    NUMBER_OF_FLEX_FLASH_CARDS_UNKNOWN = "unknown"
    PER_DISK_CAP_UNKNOWN = "unknown"
    UNITS_UNSPECIFIED = "unspecified"


class StorageQual(ManagedObject):
    """This is StorageQual class."""

    consts = StorageQualConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageQual", "storageQual", "local-storage", VersionMeta.Version101e, "InputOutput", 0x3fffL, [], ["admin", "pn-policy"], [u'computeQual'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "block_size": MoPropertyMeta("block_size", "blockSize", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["unknown"], ["0-4294967295"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "disk_type": MoPropertyMeta("disk_type", "diskType", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["HDD", "SSD", "unspecified"], []), 
        "diskless": MoPropertyMeta("diskless", "diskless", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["no", "unspecified", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "max_cap": MoPropertyMeta("max_cap", "maxCap", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["unknown"], ["0-4294967295"]), 
        "min_cap": MoPropertyMeta("min_cap", "minCap", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["unknown"], ["0-4294967295"]), 
        "number_of_blocks": MoPropertyMeta("number_of_blocks", "numberOfBlocks", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["unknown"], ["0-4294967295"]), 
        "number_of_flex_flash_cards": MoPropertyMeta("number_of_flex_flash_cards", "numberOfFlexFlashCards", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["unknown"], ["0-4294967295"]), 
        "per_disk_cap": MoPropertyMeta("per_disk_cap", "perDiskCap", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, ["unknown"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x800L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "units": MoPropertyMeta("units", "units", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, ["unspecified"], ["0-4294967295"]), 
    }

    prop_map = {
        "blockSize": "block_size", 
        "childAction": "child_action", 
        "diskType": "disk_type", 
        "diskless": "diskless", 
        "dn": "dn", 
        "maxCap": "max_cap", 
        "minCap": "min_cap", 
        "numberOfBlocks": "number_of_blocks", 
        "numberOfFlexFlashCards": "number_of_flex_flash_cards", 
        "perDiskCap": "per_disk_cap", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "units": "units", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.block_size = None
        self.child_action = None
        self.disk_type = None
        self.diskless = None
        self.max_cap = None
        self.min_cap = None
        self.number_of_blocks = None
        self.number_of_flex_flash_cards = None
        self.per_disk_cap = None
        self.sacl = None
        self.status = None
        self.units = None

        ManagedObject.__init__(self, "StorageQual", parent_mo_or_dn, **kwargs)

