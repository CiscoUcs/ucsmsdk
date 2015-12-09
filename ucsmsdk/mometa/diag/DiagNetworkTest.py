"""This module contains the general information for DiagNetworkTest ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class DiagNetworkTestConsts():
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    TYPE_ETH = "eth"
    TYPE_FC = "fc"


class DiagNetworkTest(ManagedObject):
    """This is DiagNetworkTest class."""

    consts = DiagNetworkTestConsts()
    naming_props = set([u'order'])

    mo_meta = MoMeta("DiagNetworkTest", "diagNetworkTest", "network-test-[order]", VersionMeta.Version131c, "InputOutput", 0x1ffL, [], ["admin", "pn-policy"], [u'diagRunPolicy'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "length": MoPropertyMeta("length", "length", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], ["1-1440"]), 
        "order": MoPropertyMeta("order", "order", "byte", VersionMeta.Version131c, MoPropertyMeta.NAMING, 0x10L, None, None, None, [], ["1-64"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["A", "B", "NONE"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["eth", "fc"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "length": "length", 
        "order": "order", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, order, **kwargs):
        self._dirty_mask = 0
        self.order = order
        self.child_action = None
        self.length = None
        self.sacl = None
        self.status = None
        self.switch_id = None
        self.type = None

        ManagedObject.__init__(self, "DiagNetworkTest", parent_mo_or_dn, **kwargs)

