"""This module contains the general information for EquipmentBladeConnDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentBladeConnDefConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentBladeConnDef(ManagedObject):
    """This is EquipmentBladeConnDef class."""

    consts = EquipmentBladeConnDefConsts()
    naming_props = set(['adaptorType', 'adaptorFamily', 'adaptorSlotNumber'])

    mo_meta = MoMeta("EquipmentBladeConnDef", "equipmentBladeConnDef", "adaptor-type-[adaptor_type]-family-[adaptor_family]-slot-[adaptor_slot_number]", VersionMeta.Version202m, "InputOutput", 0x7ff, [], [""], ['equipmentBladeCapProvider', 'equipmentServerUnitCapProvider'], ['equipmentBladeIOMConnDef', 'equipmentBladeSwitchConnDef'], ["Get"])

    prop_meta = {
        "adaptor_family": MoPropertyMeta("adaptor_family", "adaptorFamily", "string", VersionMeta.Version202m, MoPropertyMeta.NAMING, 0x2, 1, 510, None, [], []),
        "adaptor_slot_number": MoPropertyMeta("adaptor_slot_number", "adaptorSlotNumber", "ushort", VersionMeta.Version203a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []),
        "adaptor_slot_span": MoPropertyMeta("adaptor_slot_span", "adaptorSlotSpan", "ushort", VersionMeta.Version203a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
        "adaptor_type": MoPropertyMeta("adaptor_type", "adaptorType", "string", VersionMeta.Version202m, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202m, MoPropertyMeta.INTERNAL, 0x10, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version202m, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "parent_adaptor_slot_num": MoPropertyMeta("parent_adaptor_slot_num", "parentAdaptorSlotNum", "ushort", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_port_mux_offset": MoPropertyMeta("switch_port_mux_offset", "switchPortMuxOffset", "ushort", VersionMeta.Version203a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
    }

    prop_map = {
        "adaptorFamily": "adaptor_family", 
        "adaptorSlotNumber": "adaptor_slot_number", 
        "adaptorSlotSpan": "adaptor_slot_span", 
        "adaptorType": "adaptor_type", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "parentAdaptorSlotNum": "parent_adaptor_slot_num", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchPortMuxOffset": "switch_port_mux_offset", 
    }

    def __init__(self, parent_mo_or_dn, adaptor_type, adaptor_family, adaptor_slot_number, **kwargs):
        self._dirty_mask = 0
        self.adaptor_type = adaptor_type
        self.adaptor_family = adaptor_family
        self.adaptor_slot_number = adaptor_slot_number
        self.adaptor_slot_span = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.parent_adaptor_slot_num = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.switch_port_mux_offset = None

        ManagedObject.__init__(self, "EquipmentBladeConnDef", parent_mo_or_dn, **kwargs)
