"""This module contains the general information for MoKvInvHolder ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MoKvInvHolderConsts:
    LAST_UPDATE_NEVER = "never"


class MoKvInvHolder(ManagedObject):
    """This is MoKvInvHolder class."""

    consts = MoKvInvHolderConsts()
    naming_props = set(['endpoint'])

    mo_meta = MoMeta("MoKvInvHolder", "moKvInvHolder", "inv-kv-[endpoint]", VersionMeta.Version321d, "InputOutput", 0x3f, [], ["read-only"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], ['moInvKv'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "endpoint": MoPropertyMeta("endpoint", "endpoint", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x8, 1, 32, None, [], []),
        "last_update": MoPropertyMeta("last_update", "lastUpdate", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "endpoint": "endpoint", 
        "lastUpdate": "last_update", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, endpoint, **kwargs):
        self._dirty_mask = 0
        self.endpoint = endpoint
        self.child_action = None
        self.last_update = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MoKvInvHolder", parent_mo_or_dn, **kwargs)
