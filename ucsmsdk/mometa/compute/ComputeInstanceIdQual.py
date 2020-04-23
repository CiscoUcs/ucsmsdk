"""This module contains the general information for ComputeInstanceIdQual ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeInstanceIdQualConsts:
    pass


class ComputeInstanceIdQual(ManagedObject):
    """This is ComputeInstanceIdQual class."""

    consts = ComputeInstanceIdQualConsts()
    naming_props = set(['minId', 'maxId'])

    mo_meta = MoMeta("ComputeInstanceIdQual", "computeInstanceIdQual", "inst-from-[min_id]-to-[max_id]", VersionMeta.Version251a, "InputOutput", 0x7f, [], ["admin", "pn-policy"], ['computeSlotQual'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "max_id": MoPropertyMeta("max_id", "maxId", "uint", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-8"]),
        "min_id": MoPropertyMeta("min_id", "minId", "uint", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-8"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "maxId": "max_id", 
        "minId": "min_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, min_id, max_id, **kwargs):
        self._dirty_mask = 0
        self.min_id = min_id
        self.max_id = max_id
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputeInstanceIdQual", parent_mo_or_dn, **kwargs)
