"""This module contains the general information for EquipmentStorageProcessorCap ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentStorageProcessorCapConsts():
    VIRTUALIZED_CESUPPORTED_FALSE = "false"
    VIRTUALIZED_CESUPPORTED_NO = "no"
    VIRTUALIZED_CESUPPORTED_TRUE = "true"
    VIRTUALIZED_CESUPPORTED_YES = "yes"


class EquipmentStorageProcessorCap(ManagedObject):
    """This is EquipmentStorageProcessorCap class."""

    consts = EquipmentStorageProcessorCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentStorageProcessorCap", "equipmentStorageProcessorCap", "storage-proc-cap", VersionMeta.Version302c, "InputOutput", 0x1fL, [], ["read-only"], [u'equipmentBladeCapProvider', u'equipmentRackUnitCapProvider'], [u'equipmentImpliedStorageEnclosureDef', u'equipmentStorageProviderDriverLibrary'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "virtualized_ce_supported": MoPropertyMeta("virtualized_ce_supported", "virtualizedCESupported", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "virtualizedCESupported": "virtualized_ce_supported", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.sacl = None
        self.status = None
        self.virtualized_ce_supported = None

        ManagedObject.__init__(self, "EquipmentStorageProcessorCap", parent_mo_or_dn, **kwargs)

