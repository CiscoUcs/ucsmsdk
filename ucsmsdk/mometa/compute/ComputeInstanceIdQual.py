"""This module contains the general information for ComputeInstanceIdQual ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ComputeInstanceIdQualConsts():
    pass


class ComputeInstanceIdQual(ManagedObject):
    """This is ComputeInstanceIdQual class."""

    consts = ComputeInstanceIdQualConsts()
    naming_props = set([u'minId', u'maxId'])

    mo_meta = MoMeta("ComputeInstanceIdQual", "computeInstanceIdQual", "inst-from-[min_id]-to-[max_id]", VersionMeta.Version251a, "InputOutput", 0x3fL, [], ["admin", "pn-policy"], [u'computeSlotQual'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "max_id": MoPropertyMeta("max_id", "maxId", "uint", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x4L, None, None, None, [], ["1-8"]), 
        "min_id": MoPropertyMeta("min_id", "minId", "uint", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x8L, None, None, None, [], ["1-8"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "maxId": "max_id", 
        "minId": "min_id", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, min_id, max_id, **kwargs):
        self._dirty_mask = 0
        self.min_id = min_id
        self.max_id = max_id
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "ComputeInstanceIdQual", parent_mo_or_dn, **kwargs)

