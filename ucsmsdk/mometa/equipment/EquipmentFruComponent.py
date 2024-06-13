"""This module contains the general information for EquipmentFruComponent ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentFruComponentConsts:
    TYPE_CPLD = "CPLD"
    TYPE_INTEL_AMC = "INTEL-AMC"
    TYPE_RETIMER = "RETIMER"
    TYPE_UBM = "UBM"
    TYPE_UNKNOWN = "unknown"


class EquipmentFruComponent(ManagedObject):
    """This is EquipmentFruComponent class."""

    consts = EquipmentFruComponentConsts()
    naming_props = set(['type', 'id'])

    mo_meta = MoMeta("EquipmentFruComponent", "equipmentFruComponent", "frucomp-[type]-[id]", VersionMeta.Version432b, "InputOutput", 0x7f, [], ["read-only"], ['adaptorUnit', 'computeRackUnit', 'equipmentPcieConnectorUnit', 'equipmentPcieNode', 'graphicsCard', 'storageController'], ['mgmtController'], [None])

    prop_meta = {
        "asset_tag": MoPropertyMeta("asset_tag", "assetTag", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []),
        "backup_version": MoPropertyMeta("backup_version", "backupVersion", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version432b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version432b, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-5"]),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "part_number": MoPropertyMeta("part_number", "partNumber", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "pid": MoPropertyMeta("pid", "pid", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "startup_version": MoPropertyMeta("startup_version", "startupVersion", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version432b, MoPropertyMeta.NAMING, 0x40, None, None, None, ["CPLD", "INTEL-AMC", "RETIMER", "UBM", "unknown"], []),
        "type_string": MoPropertyMeta("type_string", "typeString", "string", VersionMeta.Version433a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "update_status": MoPropertyMeta("update_status", "updateStatus", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "vid": MoPropertyMeta("vid", "vid", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "assetTag": "asset_tag", 
        "backupVersion": "backup_version", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "model": "model", 
        "partNumber": "part_number", 
        "pid": "pid", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "startupVersion": "startup_version", 
        "status": "status", 
        "type": "type", 
        "typeString": "type_string", 
        "updateStatus": "update_status", 
        "vendor": "vendor", 
        "vid": "vid", 
    }

    def __init__(self, parent_mo_or_dn, type, id, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.id = id
        self.asset_tag = None
        self.backup_version = None
        self.child_action = None
        self.model = None
        self.part_number = None
        self.pid = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.startup_version = None
        self.status = None
        self.type_string = None
        self.update_status = None
        self.vendor = None
        self.vid = None

        ManagedObject.__init__(self, "EquipmentFruComponent", parent_mo_or_dn, **kwargs)
