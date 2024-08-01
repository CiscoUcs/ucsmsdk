"""This module contains the general information for EquipmentPortGroupDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentPortGroupDefConsts:
    BREAKOUT_FALSE = "false"
    BREAKOUT_NO = "no"
    BREAKOUT_TRUE = "true"
    BREAKOUT_YES = "yes"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    TYPE_ADAPTOR_EXT = "adaptor-ext"
    TYPE_ADAPTOR_PC = "adaptor-pc"
    TYPE_FABRIC = "fabric"
    TYPE_FABRIC_PC = "fabric-pc"
    TYPE_HOST = "host"
    TYPE_HOST_PC = "host-pc"
    TYPE_SERVER_PC = "server-pc"
    TYPE_SWITCH_ETHER = "switch-ether"
    TYPE_SWITCH_FC = "switch-fc"


class EquipmentPortGroupDef(ManagedObject):
    """This is EquipmentPortGroupDef class."""

    consts = EquipmentPortGroupDefConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("EquipmentPortGroupDef", "equipmentPortGroupDef", "port-group-def[type]", VersionMeta.Version141i, "InputOutput", 0x1ff, [], [""], ['adaptorFruCapProvider', 'equipmentFexCapProvider', 'equipmentIOCardCapProvider', 'equipmentSwitchIOCardCapProvider'], [], ["Get"])

    prop_meta = {
        "breakout": MoPropertyMeta("breakout", "breakout", "string", VersionMeta.Version434b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "number_of_ports": MoPropertyMeta("number_of_ports", "numberOfPorts", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "start_port_id": MoPropertyMeta("start_port_id", "startPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x100, None, None, None, ["adaptor-ext", "adaptor-pc", "fabric", "fabric-pc", "host", "host-pc", "server-pc", "switch-ether", "switch-fc"], []),
    }

    prop_map = {
        "breakout": "breakout", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "numberOfPorts": "number_of_ports", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "startPortId": "start_port_id", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.breakout = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.number_of_ports = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.start_port_id = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPortGroupDef", parent_mo_or_dn, **kwargs)
