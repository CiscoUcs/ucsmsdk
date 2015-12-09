"""This module contains the general information for ComputeRackQual ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ComputeRackQualConsts():
    pass


class ComputeRackQual(ManagedObject):
    """This is ComputeRackQual class."""

    consts = ComputeRackQualConsts()
    naming_props = set([u'minId', u'maxId'])

    mo_meta = MoMeta("ComputeRackQual", "computeRackQual", "rack-from-[min_id]-to-[max_id]", VersionMeta.Version141i, "InputOutput", 0x7fL, [], ["admin", "pn-policy"], [u'computeQual'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "max_id": MoPropertyMeta("max_id", "maxId", "uint", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8L, None, None, None, [], ["1-255"]), 
        "min_id": MoPropertyMeta("min_id", "minId", "uint", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x10L, None, None, None, [], ["1-255"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
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

        ManagedObject.__init__(self, "ComputeRackQual", parent_mo_or_dn, **kwargs)

