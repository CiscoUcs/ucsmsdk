"""This module contains the general information for FabricSanPinTarget ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FabricSanPinTargetConsts():
    FABRIC_ID_A = "A"
    FABRIC_ID_B = "B"
    FABRIC_ID_NONE = "NONE"
    FABRIC_ID_DUAL = "dual"
    TARGET_STATUS_INVALID = "invalid"
    TARGET_STATUS_VALID = "valid"


class FabricSanPinTarget(ManagedObject):
    """This is FabricSanPinTarget class."""

    consts = FabricSanPinTargetConsts()
    naming_props = set([u'fabricId'])

    mo_meta = MoMeta("FabricSanPinTarget", "fabricSanPinTarget", "target-[fabric_id]", VersionMeta.Version101e, "InputOutput", 0x3fL, [], ["admin", "ext-san-config", "ext-san-policy"], [u'fabricSanPinGroup'], [u'faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, 0, 256, None, [], []), 
        "fabric_id": MoPropertyMeta("fabric_id", "fabricId", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8L, None, None, None, ["A", "B", "NONE", "dual"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "target_status": MoPropertyMeta("target_status", "targetStatus", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["invalid", "valid"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "fabricId": "fabric_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "targetStatus": "target_status", 
    }

    def __init__(self, parent_mo_or_dn, fabric_id, **kwargs):
        self._dirty_mask = 0
        self.fabric_id = fabric_id
        self.child_action = None
        self.ep_dn = None
        self.sacl = None
        self.status = None
        self.target_status = None

        ManagedObject.__init__(self, "FabricSanPinTarget", parent_mo_or_dn, **kwargs)

