"""This module contains the general information for EquipmentPortSwComplexRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentPortSwComplexRefConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentPortSwComplexRef(ManagedObject):
    """This is EquipmentPortSwComplexRef class."""

    consts = EquipmentPortSwComplexRefConsts()
    naming_props = set(['swComplexId'])

    mo_meta = MoMeta("EquipmentPortSwComplexRef", "equipmentPortSwComplexRef", "port-sw-complex-ref-[sw_complex_id]", VersionMeta.Version201m, "InputOutput", 0x1ff, [], [""], ['equipmentPortGroupSwComplexDef'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "max_port_id": MoPropertyMeta("max_port_id", "maxPortId", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "min_port_id": MoPropertyMeta("min_port_id", "minPortId", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "sw_complex_id": MoPropertyMeta("sw_complex_id", "swComplexId", "ushort", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x100, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "maxPortId": "max_port_id", 
        "minPortId": "min_port_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotId": "slot_id", 
        "status": "status", 
        "swComplexId": "sw_complex_id", 
    }

    def __init__(self, parent_mo_or_dn, sw_complex_id, **kwargs):
        self._dirty_mask = 0
        self.sw_complex_id = sw_complex_id
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.max_port_id = None
        self.min_port_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.slot_id = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPortSwComplexRef", parent_mo_or_dn, **kwargs)
