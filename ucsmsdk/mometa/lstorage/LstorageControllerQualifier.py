"""This module contains the general information for LstorageControllerQualifier ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LstorageControllerQualifierConsts:
    CONTROLLER_ID_ALL = "all"
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


class LstorageControllerQualifier(ManagedObject):
    """This is LstorageControllerQualifier class."""

    consts = LstorageControllerQualifierConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageControllerQualifier", "lstorageControllerQualifier", "controller-qual", VersionMeta.Version227b, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-storage", "ls-storage-policy"], ['lstorageControllerDef'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version227b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "controller_id": MoPropertyMeta("controller_id", "controllerId", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["all"], []),
        "controller_type": MoPropertyMeta("controller_type", "controllerType", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["FCH", "FLASH", "HBA", "M2", "NVME", "PCH", "PT", "SAS", "SATA", "SD", "external", "unknown"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "controllerId": "controller_id", 
        "controllerType": "controller_type", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.controller_id = None
        self.controller_type = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageControllerQualifier", parent_mo_or_dn, **kwargs)
