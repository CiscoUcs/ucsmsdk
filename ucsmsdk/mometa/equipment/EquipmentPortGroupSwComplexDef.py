"""This module contains the general information for EquipmentPortGroupSwComplexDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentPortGroupSwComplexDefConsts:
    ASIC_CARMEL = "carmel"
    ASIC_GATOS = "gatos"
    ASIC_HEAVENLY = "heavenly"
    ASIC_HOMEWOOD = "homewood"
    ASIC_TRIDENT2 = "trident2"
    ASIC_UNKNOWN = "unknown"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentPortGroupSwComplexDef(ManagedObject):
    """This is EquipmentPortGroupSwComplexDef class."""

    consts = EquipmentPortGroupSwComplexDefConsts()
    naming_props = set(['asic'])

    mo_meta = MoMeta("EquipmentPortGroupSwComplexDef", "equipmentPortGroupSwComplexDef", "port-group-sw-complex-def[asic]", VersionMeta.Version201m, "InputOutput", 0x1ff, [], [""], ['equipmentSwitchCapProvider'], ['equipmentPortSwComplexRef'], ["Get"])

    prop_meta = {
        "asic": MoPropertyMeta("asic", "asic", "string", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x2, None, None, None, ["carmel", "gatos", "heavenly", "homewood", "trident2", "unknown"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "port_capacity": MoPropertyMeta("port_capacity", "portCapacity", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "sw_complex_capacity": MoPropertyMeta("sw_complex_capacity", "swComplexCapacity", "ushort", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "vif_capacity": MoPropertyMeta("vif_capacity", "vifCapacity", "ushort", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "asic": "asic", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "portCapacity": "port_capacity", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "swComplexCapacity": "sw_complex_capacity", 
        "vifCapacity": "vif_capacity", 
    }

    def __init__(self, parent_mo_or_dn, asic, **kwargs):
        self._dirty_mask = 0
        self.asic = asic
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.port_capacity = None
        self.sacl = None
        self.status = None
        self.sw_complex_capacity = None
        self.vif_capacity = None

        ManagedObject.__init__(self, "EquipmentPortGroupSwComplexDef", parent_mo_or_dn, **kwargs)
