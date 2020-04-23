"""This module contains the general information for MorefProp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MorefPropConsts:
    ADMIN_STATE_APPLIED = "applied"
    ADMIN_STATE_DELETED = "deleted"
    ADMIN_STATE_UNAPPLIED = "unapplied"


class MorefProp(ManagedObject):
    """This is MorefProp class."""

    consts = MorefPropConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("MorefProp", "morefProp", "[name]", VersionMeta.Version227b, "InputOutput", 0xff, [], ["admin"], ['morefFruRef', 'morefRef'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["applied", "deleted", "unapplied"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version227b, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version227b, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "value": MoPropertyMeta("value", "value", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, None, [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "value": "value", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_state = None
        self.child_action = None
        self.sacl = None
        self.status = None
        self.value = None

        ManagedObject.__init__(self, "MorefProp", parent_mo_or_dn, **kwargs)
