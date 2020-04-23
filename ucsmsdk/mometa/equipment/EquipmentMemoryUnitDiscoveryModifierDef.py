"""This module contains the general information for EquipmentMemoryUnitDiscoveryModifierDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentMemoryUnitDiscoveryModifierDefConsts:
    ACTION_SET_REV = "setRev"
    ACTION_SET_REV_STRICT = "setRevStrict"
    ACTION_SET_REV_TO_ONE = "setRevToOne"
    ACTION_UNKNOWN = "unknown"
    CONSTRAINT_TYPE_KIT = "kit"
    CONSTRAINT_TYPE_UNKNOWN = "unknown"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentMemoryUnitDiscoveryModifierDef(ManagedObject):
    """This is EquipmentMemoryUnitDiscoveryModifierDef class."""

    consts = EquipmentMemoryUnitDiscoveryModifierDefConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("EquipmentMemoryUnitDiscoveryModifierDef", "equipmentMemoryUnitDiscoveryModifierDef", "discmod-[name]", VersionMeta.Version102d, "InputOutput", 0xff, [], [""], ['equipmentMemoryUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "action": MoPropertyMeta("action", "action", "string", VersionMeta.Version102d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["setRev", "setRevStrict", "setRevToOne", "unknown"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version102d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "constraint_type": MoPropertyMeta("constraint_type", "constraintType", "string", VersionMeta.Version102d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["kit", "unknown"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version102d, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version102d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version102d, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version102d, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version102d, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version102d, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "action": "action", 
        "childAction": "child_action", 
        "constraintType": "constraint_type", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.action = None
        self.child_action = None
        self.constraint_type = None
        self.descr = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentMemoryUnitDiscoveryModifierDef", parent_mo_or_dn, **kwargs)
