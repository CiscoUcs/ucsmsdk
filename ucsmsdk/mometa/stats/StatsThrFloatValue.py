"""This module contains the general information for StatsThrFloatValue ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class StatsThrFloatValueConsts:
    DIRECTION_ABOVE_NORMAL = "aboveNormal"
    DIRECTION_BELOW_NORMAL = "belowNormal"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PROP_TYPE_FLOAT = "float"
    PROP_TYPE_UINT32 = "uint32"
    PROP_TYPE_UINT64 = "uint64"
    SEVERITY_CLEARED = "cleared"
    SEVERITY_CONDITION = "condition"
    SEVERITY_CRITICAL = "critical"
    SEVERITY_INFO = "info"
    SEVERITY_MAJOR = "major"
    SEVERITY_MINOR = "minor"
    SEVERITY_WARNING = "warning"


class StatsThrFloatValue(ManagedObject):
    """This is StatsThrFloatValue class."""

    consts = StatsThrFloatValueConsts()
    naming_props = set(['direction', 'severity'])

    mo_meta = MoMeta("StatsThrFloatValue", "statsThrFloatValue", "[direction]-[severity]", VersionMeta.Version101e, "InputOutput", 0xfff, [], ["admin", "operations"], ['statsThr32Definition', 'statsThr64Definition', 'statsThrFloatDefinition'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "deescalating": MoPropertyMeta("deescalating", "deescalating", "float", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "direction": MoPropertyMeta("direction", "direction", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10, None, None, None, ["aboveNormal", "belowNormal"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "escalating": MoPropertyMeta("escalating", "escalating", "float", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["local", "pending-policy", "policy"], []),
        "prop_type": MoPropertyMeta("prop_type", "propType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["float", "uint32", "uint64"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "severity": MoPropertyMeta("severity", "severity", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x400, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "deescalating": "deescalating", 
        "descr": "descr", 
        "direction": "direction", 
        "dn": "dn", 
        "escalating": "escalating", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "propType": "prop_type", 
        "rn": "rn", 
        "sacl": "sacl", 
        "severity": "severity", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, direction, severity, **kwargs):
        self._dirty_mask = 0
        self.direction = direction
        self.severity = severity
        self.child_action = None
        self.deescalating = None
        self.descr = None
        self.escalating = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.prop_type = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "StatsThrFloatValue", parent_mo_or_dn, **kwargs)
