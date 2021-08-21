"""This module contains the general information for StorageEnclosureCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StorageEnclosureCapConsts:
    REMOVABLE_FALSE = "false"
    REMOVABLE_NO = "no"
    REMOVABLE_TRUE = "true"
    REMOVABLE_YES = "yes"
    TYPE_DEDICATED_REAR_SSD_ENCLOSURE = "dedicated-rear-ssd-enclosure"
    TYPE_HDD_EXPANSION_TRAY = "hdd-expansion-tray"
    TYPE_HDD_MOTHER_BOARD = "hdd-mother-board"
    TYPE_IOE_NVME_ENCLOSURE = "ioe-nvme-enclosure"
    TYPE_SB_NVME_ENCLOSURE = "sb-nvme-enclosure"
    TYPE_SERVER_FRONT_LOAD = "server-front-load"
    TYPE_SERVER_MID = "server-mid"
    TYPE_SERVER_NVME = "server-nvme"
    TYPE_SERVER_PCH = "server-pch"
    TYPE_SERVER_REAR = "server-rear"
    TYPE_SIOC_NVME_ENCLOSURE = "sioc-nvme-enclosure"
    TYPE_UNKNOWN = "unknown"


class StorageEnclosureCap(ManagedObject):
    """This is StorageEnclosureCap class."""

    consts = StorageEnclosureCapConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("StorageEnclosureCap", "storageEnclosureCap", "physical-holder-[type]", VersionMeta.Version312b, "InputOutput", 0x3f, [], [""], ['equipmentBladeCapProvider', 'equipmentChassisCapProvider', 'equipmentRackUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "disk_base_id": MoPropertyMeta("disk_base_id", "diskBaseId", "uint", VersionMeta.Version323a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "disk_variant": MoPropertyMeta("disk_variant", "diskVariant", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "num_slots": MoPropertyMeta("num_slots", "numSlots", "ushort", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "removable": MoPropertyMeta("removable", "removable", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x20, None, None, None, ["dedicated-rear-ssd-enclosure", "hdd-expansion-tray", "hdd-mother-board", "ioe-nvme-enclosure", "sb-nvme-enclosure", "server-front-load", "server-mid", "server-nvme", "server-pch", "server-rear", "sioc-nvme-enclosure", "unknown"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "diskBaseId": "disk_base_id", 
        "diskVariant": "disk_variant", 
        "dn": "dn", 
        "id": "id", 
        "numSlots": "num_slots", 
        "removable": "removable", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.descr = None
        self.disk_base_id = None
        self.disk_variant = None
        self.id = None
        self.num_slots = None
        self.removable = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "StorageEnclosureCap", parent_mo_or_dn, **kwargs)
