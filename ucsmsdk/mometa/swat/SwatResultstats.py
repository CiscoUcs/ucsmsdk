"""This module contains the general information for SwatResultstats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwatResultstatsConsts:
    pass


class SwatResultstats(ManagedObject):
    """This is SwatResultstats class."""

    consts = SwatResultstatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("SwatResultstats", "swatResultstats", "", VersionMeta.Version101e, "InputOutput", 0x3ff, [], ["admin"], [], [], ["Get"])

    prop_meta = {
        "activity_name": MoPropertyMeta("activity_name", "activityName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "false_hits": MoPropertyMeta("false_hits", "falseHits", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "label": MoPropertyMeta("label", "label", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "total_passes": MoPropertyMeta("total_passes", "totalPasses", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], []),
        "true_hits": MoPropertyMeta("true_hits", "trueHits", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], []),
    }

    prop_map = {
        "activityName": "activity_name", 
        "childAction": "child_action", 
        "dn": "dn", 
        "falseHits": "false_hits", 
        "label": "label", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "totalPasses": "total_passes", 
        "trueHits": "true_hits", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.activity_name = None
        self.child_action = None
        self.false_hits = None
        self.label = None
        self.sacl = None
        self.status = None
        self.total_passes = None
        self.true_hits = None

        ManagedObject.__init__(self, "SwatResultstats", parent_mo_or_dn, **kwargs)
