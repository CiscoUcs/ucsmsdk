"""This module contains the general information for PowerGroupQual ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PowerGroupQualConsts:
    pass


class PowerGroupQual(ManagedObject):
    """This is PowerGroupQual class."""

    consts = PowerGroupQualConsts()
    naming_props = set(['groupName'])

    mo_meta = MoMeta("PowerGroupQual", "powerGroupQual", "power-group-[group_name]", VersionMeta.Version141i, "InputOutput", 0x3f, [], ["admin", "pn-policy"], ['computeQual'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "group_name": MoPropertyMeta("group_name", "groupName", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "groupName": "group_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, group_name, **kwargs):
        self._dirty_mask = 0
        self.group_name = group_name
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PowerGroupQual", parent_mo_or_dn, **kwargs)
