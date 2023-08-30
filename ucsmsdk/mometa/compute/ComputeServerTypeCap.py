"""This module contains the general information for ComputeServerTypeCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeServerTypeCapConsts:
    TYPE_APPLIANCE = "appliance"
    TYPE_GENERAL_PURPOSE = "general-purpose"
    TYPE_SHARED_IO = "shared-io"
    TYPE_X_SERIES = "x-series"


class ComputeServerTypeCap(ManagedObject):
    """This is ComputeServerTypeCap class."""

    consts = ComputeServerTypeCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeServerTypeCap", "computeServerTypeCap", "server-type", VersionMeta.Version302c, "InputOutput", 0x1f, [], ["read-only"], ['equipmentBladeCapProvider', 'equipmentRackUnitCapProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["appliance", "general-purpose", "shared-io", "x-series"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "ComputeServerTypeCap", parent_mo_or_dn, **kwargs)
