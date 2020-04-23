"""This module contains the general information for EquipmentBladeAggregationCapRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentBladeAggregationCapRefConsts:
    IS_SUPPORTED_FALSE = "false"
    IS_SUPPORTED_NO = "no"
    IS_SUPPORTED_TRUE = "true"
    IS_SUPPORTED_YES = "yes"


class EquipmentBladeAggregationCapRef(ManagedObject):
    """This is EquipmentBladeAggregationCapRef class."""

    consts = EquipmentBladeAggregationCapRefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentBladeAggregationCapRef", "equipmentBladeAggregationCapRef", "blade-aggr", VersionMeta.Version222c, "InputOutput", 0x1f, [], [""], ['equipmentBladeCapProvider'], ['equipmentPhysDevicesPerBoard'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "is_supported": MoPropertyMeta("is_supported", "isSupported", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "isSupported": "is_supported", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.is_supported = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentBladeAggregationCapRef", parent_mo_or_dn, **kwargs)
