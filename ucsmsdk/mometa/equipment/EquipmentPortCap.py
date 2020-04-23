"""This module contains the general information for EquipmentPortCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentPortCapConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PORT_ATTRIBUTE_NONE = "None"
    PORT_ATTRIBUTE_SCALABILITY = "Scalability"


class EquipmentPortCap(ManagedObject):
    """This is EquipmentPortCap class."""

    consts = EquipmentPortCapConsts()
    naming_props = set(['startPortId', 'endPortId'])

    mo_meta = MoMeta("EquipmentPortCap", "equipmentPortCap", "port-cap-start-[start_port_id]-end-[end_port_id]", VersionMeta.Version302c, "InputOutput", 0x3ff, [], [""], ['equipmentSwitchCap', 'equipmentSwitchIOCardCapProvider'], [], [None])

    prop_meta = {
        "breakout_port_speed_gb": MoPropertyMeta("breakout_port_speed_gb", "breakoutPortSpeedGb", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "count_breakout_ports": MoPropertyMeta("count_breakout_ports", "countBreakoutPorts", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "end_port_id": MoPropertyMeta("end_port_id", "endPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "port_attribute": MoPropertyMeta("port_attribute", "portAttribute", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["None", "Scalability"], []),
        "port_speed_gb": MoPropertyMeta("port_speed_gb", "portSpeedGb", "ushort", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "start_port_id": MoPropertyMeta("start_port_id", "startPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x100, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "breakoutPortSpeedGb": "breakout_port_speed_gb", 
        "childAction": "child_action", 
        "countBreakoutPorts": "count_breakout_ports", 
        "descr": "descr", 
        "dn": "dn", 
        "endPortId": "end_port_id", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "portAttribute": "port_attribute", 
        "portSpeedGb": "port_speed_gb", 
        "rn": "rn", 
        "sacl": "sacl", 
        "startPortId": "start_port_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, start_port_id, end_port_id, **kwargs):
        self._dirty_mask = 0
        self.start_port_id = start_port_id
        self.end_port_id = end_port_id
        self.breakout_port_speed_gb = None
        self.child_action = None
        self.count_breakout_ports = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.port_attribute = None
        self.port_speed_gb = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPortCap", parent_mo_or_dn, **kwargs)
