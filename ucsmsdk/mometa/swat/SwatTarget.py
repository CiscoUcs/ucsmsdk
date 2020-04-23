"""This module contains the general information for SwatTarget ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwatTargetConsts:
    pass


class SwatTarget(ManagedObject):
    """This is SwatTarget class."""

    consts = SwatTargetConsts()
    naming_props = set(['varName', 'varValue'])

    mo_meta = MoMeta("SwatTarget", "swatTarget", "target-[var_name]-[var_value]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["admin"], ['swatAction'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "var_name": MoPropertyMeta("var_name", "varName", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "var_value": MoPropertyMeta("var_value", "varValue", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "varName": "var_name", 
        "varValue": "var_value", 
    }

    def __init__(self, parent_mo_or_dn, var_name, var_value, **kwargs):
        self._dirty_mask = 0
        self.var_name = var_name
        self.var_value = var_value
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "SwatTarget", parent_mo_or_dn, **kwargs)
