"""This module contains the general information for SwVlanPortNsOverride ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwVlanPortNsOverrideConsts:
    pass


class SwVlanPortNsOverride(ManagedObject):
    """This is SwVlanPortNsOverride class."""

    consts = SwVlanPortNsOverrideConsts()
    naming_props = set([])

    mo_meta = MoMeta("SwVlanPortNsOverride", "swVlanPortNsOverride", "vlan-port-override", VersionMeta.Version142b, "InputOutput", 0x3f, [], ["admin"], ['topSysDefaults'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version142b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version142b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "limit": MoPropertyMeta("limit", "limit", "uint", VersionMeta.Version142b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version142b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version142b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "limit": "limit", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.limit = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "SwVlanPortNsOverride", parent_mo_or_dn, **kwargs)
