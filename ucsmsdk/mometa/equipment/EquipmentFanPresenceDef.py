"""This module contains the general information for EquipmentFanPresenceDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentFanPresenceDefConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PRESENCE_OPTIONAL = "Optional"
    PRESENCE_REQUIRED = "Required"


class EquipmentFanPresenceDef(ManagedObject):
    """This is EquipmentFanPresenceDef class."""

    consts = EquipmentFanPresenceDefConsts()
    naming_props = set([u'fanModuleNumber'])

    mo_meta = MoMeta("EquipmentFanPresenceDef", "equipmentFanPresenceDef", "fan-presence-[fan_module_number]", None, "InputOutput", 0x1ff, [], [""], [u'equipmentRackFanModuleDef'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", None, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "fan_module_number": MoPropertyMeta("fan_module_number", "fanModuleNumber", "ushort", None, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", None, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", None, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", None, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Optional", "Required"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "fanModuleNumber": "fan_module_number", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "presence": "presence", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, fan_module_number, **kwargs):
        self._dirty_mask = 0
        self.fan_module_number = fan_module_number
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.presence = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentFanPresenceDef", parent_mo_or_dn, **kwargs)
