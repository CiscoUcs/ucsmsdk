"""This module contains the general information for LstorageControllerRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LstorageControllerRefConsts:
    CONTROLLER_TYPE_FCH = "FCH"
    CONTROLLER_TYPE_FLASH = "FLASH"
    CONTROLLER_TYPE_HBA = "HBA"
    CONTROLLER_TYPE_M2 = "M2"
    CONTROLLER_TYPE_NVME = "NVME"
    CONTROLLER_TYPE_PCH = "PCH"
    CONTROLLER_TYPE_PT = "PT"
    CONTROLLER_TYPE_SAS = "SAS"
    CONTROLLER_TYPE_SATA = "SATA"
    CONTROLLER_TYPE_SD = "SD"
    CONTROLLER_TYPE_EXTERNAL = "external"
    CONTROLLER_TYPE_UNKNOWN = "unknown"


class LstorageControllerRef(ManagedObject):
    """This is LstorageControllerRef class."""

    consts = LstorageControllerRefConsts()
    naming_props = set(['serverId', 'controllerType', 'controllerId'])

    mo_meta = MoMeta("LstorageControllerRef", "lstorageControllerRef", "server-[server_id]-controller-[controller_type]-[controller_id]", VersionMeta.Version312b, "InputOutput", 0xff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['lstorageDiskSlot'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "controller_id": MoPropertyMeta("controller_id", "controllerId", "uint", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x4, None, None, None, [], ["1-2"]),
        "controller_type": MoPropertyMeta("controller_type", "controllerType", "string", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x8, None, None, None, ["FCH", "FLASH", "HBA", "M2", "NVME", "PCH", "PT", "SAS", "SATA", "SD", "external", "unknown"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "server_id": MoPropertyMeta("server_id", "serverId", "uint", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x40, None, None, None, [], ["1-2"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "controllerId": "controller_id", 
        "controllerType": "controller_type", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serverId": "server_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, server_id, controller_type, controller_id, **kwargs):
        self._dirty_mask = 0
        self.server_id = server_id
        self.controller_type = controller_type
        self.controller_id = controller_id
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageControllerRef", parent_mo_or_dn, **kwargs)
