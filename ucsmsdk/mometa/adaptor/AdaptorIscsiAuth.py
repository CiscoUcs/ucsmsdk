"""This module contains the general information for AdaptorIscsiAuth ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorIscsiAuthConsts:
    pass


class AdaptorIscsiAuth(ManagedObject):
    """This is AdaptorIscsiAuth class."""

    consts = AdaptorIscsiAuthConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorIscsiAuth", "adaptorIscsiAuth", "iscsi-auth", VersionMeta.Version201m, "InputOutput", 0x1f, [], ["read-only"], [], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "user_id": MoPropertyMeta("user_id", "userId", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "password": "password", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "userId": "user_id", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.password = None
        self.sacl = None
        self.status = None
        self.user_id = None

        ManagedObject.__init__(self, "AdaptorIscsiAuth", parent_mo_or_dn, **kwargs)
