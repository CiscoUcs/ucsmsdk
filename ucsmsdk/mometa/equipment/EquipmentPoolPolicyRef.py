"""This module contains the general information for EquipmentPoolPolicyRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentPoolPolicyRefConsts:
    pass


class EquipmentPoolPolicyRef(ManagedObject):
    """This is EquipmentPoolPolicyRef class."""

    consts = EquipmentPoolPolicyRefConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EquipmentPoolPolicyRef", "equipmentPoolPolicyRef", "chassis-poolref-[id]", VersionMeta.Version312b, "InputOutput", 0x3f, [], ["read-only"], ['equipmentPoolable'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "policy_dn": MoPropertyMeta("policy_dn", "policyDn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "policyDn": "policy_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.policy_dn = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPoolPolicyRef", parent_mo_or_dn, **kwargs)
