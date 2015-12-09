"""This module contains the general information for LsbootEmbeddedLocalDiskImagePath ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LsbootEmbeddedLocalDiskImagePathConsts():
    TYPE_PRIMARY = "primary"
    TYPE_SECONDARY = "secondary"


class LsbootEmbeddedLocalDiskImagePath(ManagedObject):
    """This is LsbootEmbeddedLocalDiskImagePath class."""

    consts = LsbootEmbeddedLocalDiskImagePathConsts()
    naming_props = set([u'type'])

    mo_meta = MoMeta("LsbootEmbeddedLocalDiskImagePath", "lsbootEmbeddedLocalDiskImagePath", "diskimgpath-[type]", None, "InputOutput", 0x7fL, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], [u'lsbootEmbeddedLocalDiskImage'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "slot_number": MoPropertyMeta("slot_number", "slotNumber", "ushort", None, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["1-24"]), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", None, MoPropertyMeta.NAMING, 0x40L, None, None, None, ["primary", "secondary"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotNumber": "slot_number", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.sacl = None
        self.slot_number = None
        self.status = None

        ManagedObject.__init__(self, "LsbootEmbeddedLocalDiskImagePath", parent_mo_or_dn, **kwargs)

