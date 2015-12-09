"""This module contains the general information for FabricSanMonCloud ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FabricSanMonCloudConsts():
    MODE_END_HOST = "end-host"
    MODE_SWITCH = "switch"


class FabricSanMonCloud(ManagedObject):
    """This is FabricSanMonCloud class."""

    consts = FabricSanMonCloudConsts()
    naming_props = set([])

    mo_meta = MoMeta("FabricSanMonCloud", "fabricSanMonCloud", "sanmon", VersionMeta.Version141i, "InputOutput", 0x1fL, [], ["admin", "ext-san-config", "ext-san-policy"], [u'fabricEp'], [u'fabricFcMonSan', u'statsThresholdPolicy'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["end-host", "switch"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "mode": "mode", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.mode = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FabricSanMonCloud", parent_mo_or_dn, **kwargs)

