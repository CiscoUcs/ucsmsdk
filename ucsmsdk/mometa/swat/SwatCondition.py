"""This module contains the general information for SwatCondition ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwatConditionConsts:
    OPERATION_EQ = "EQ"
    OPERATION_GE = "GE"
    OPERATION_GT = "GT"
    OPERATION_LE = "LE"
    OPERATION_LT = "LT"
    OPERATION_NE = "NE"


class SwatCondition(ManagedObject):
    """This is SwatCondition class."""

    consts = SwatConditionConsts()
    naming_props = set(['varName', 'operation', 'varValue'])

    mo_meta = MoMeta("SwatCondition", "swatCondition", "cond-[var_name]-[operation]-[var_value]", VersionMeta.Version101e, "InputOutput", 0xff, [], ["admin"], ['swatAction', 'swatTrigger'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "operation": MoPropertyMeta("operation", "operation", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, None, None, None, ["EQ", "GE", "GT", "LE", "LT", "NE"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "var_name": MoPropertyMeta("var_name", "varName", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "var_value": MoPropertyMeta("var_value", "varValue", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "operation": "operation", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "varName": "var_name", 
        "varValue": "var_value", 
    }

    def __init__(self, parent_mo_or_dn, var_name, operation, var_value, **kwargs):
        self._dirty_mask = 0
        self.var_name = var_name
        self.operation = operation
        self.var_value = var_value
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "SwatCondition", parent_mo_or_dn, **kwargs)
