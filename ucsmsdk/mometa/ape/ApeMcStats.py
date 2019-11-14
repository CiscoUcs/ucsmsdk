"""This module contains the general information for ApeMcStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ApeMcStatsConsts:
    pass


class ApeMcStats(ManagedObject):
    """This is ApeMcStats class."""

    consts = ApeMcStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ApeMcStats", "apeMcStats", "", VersionMeta.Version312b, "InputOutput", 0x1f, [], ["read-only"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "custom_factor": MoPropertyMeta("custom_factor", "customFactor", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "custom_policy": MoPropertyMeta("custom_policy", "customPolicy", "ushort", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "default_factor": MoPropertyMeta("default_factor", "defaultFactor", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "default_policy": MoPropertyMeta("default_policy", "defaultPolicy", "ushort", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "parent_id": MoPropertyMeta("parent_id", "parentId", "ushort", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parent_name": MoPropertyMeta("parent_name", "parentName", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rand_range_end": MoPropertyMeta("rand_range_end", "randRangeEnd", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rand_range_start": MoPropertyMeta("rand_range_start", "randRangeStart", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "value": MoPropertyMeta("value", "value", "ulong", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "customFactor": "custom_factor", 
        "customPolicy": "custom_policy", 
        "defaultFactor": "default_factor", 
        "defaultPolicy": "default_policy", 
        "dn": "dn", 
        "name": "name", 
        "parentId": "parent_id", 
        "parentName": "parent_name", 
        "randRangeEnd": "rand_range_end", 
        "randRangeStart": "rand_range_start", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "value": "value", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.custom_factor = None
        self.custom_policy = None
        self.default_factor = None
        self.default_policy = None
        self.name = None
        self.parent_id = None
        self.parent_name = None
        self.rand_range_end = None
        self.rand_range_start = None
        self.sacl = None
        self.status = None
        self.value = None

        ManagedObject.__init__(self, "ApeMcStats", parent_mo_or_dn, **kwargs)
