"""This module contains the general information for LstorageControllerQualifier ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageControllerQualifierConsts():
    CONTROLLER_ID_ALL = "all"
    CONTROLLER_TYPE_FLASH = "FLASH"
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

    mo_meta = MoMeta("LstorageControllerQualifier", "lstorageControllerQualifier", "controller-qual", None, "InputOutput", 0x7fL, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-storage", "ls-storage-policy"], [u'lstorageControllerDef'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "controller_id": MoPropertyMeta("controller_id", "controllerId", "string", None, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["all"], []), 
        "controller_type": MoPropertyMeta("controller_type", "controllerType", "string", None, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["FLASH", "NVME", "PCH", "PT", "SAS", "SATA", "SD", "external", "unknown"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
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

