"""This module contains the general information for EquipmentGemPortCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentGemPortCapConsts:
    INT_ID_NONE = "none"
    MAX_FC_SPEED_16GBPS = "16gbps"
    MAX_FC_SPEED_1GBPS = "1gbps"
    MAX_FC_SPEED_2GBPS = "2gbps"
    MAX_FC_SPEED_32GBPS = "32gbps"
    MAX_FC_SPEED_4GBPS = "4gbps"
    MAX_FC_SPEED_8GBPS = "8gbps"
    MAX_FC_SPEED_AUTO = "auto"
    MAX_FC_SPEED_INDETERMINATE = "indeterminate"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentGemPortCap(ManagedObject):
    """This is EquipmentGemPortCap class."""

    consts = EquipmentGemPortCapConsts()
    naming_props = set(['portNumber'])

    mo_meta = MoMeta("EquipmentGemPortCap", "equipmentGemPortCap", "gem-port-cap-[port_number]", VersionMeta.Version141i, "InputOutput", 0x1ff, [], [""], ['equipmentGemCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "max_fc_speed": MoPropertyMeta("max_fc_speed", "maxFcSpeed", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["16gbps", "1gbps", "2gbps", "32gbps", "4gbps", "8gbps", "auto", "indeterminate"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "port_number": MoPropertyMeta("port_number", "portNumber", "uint", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x40, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "maxFcSpeed": "max_fc_speed", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "portNumber": "port_number", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, port_number, **kwargs):
        self._dirty_mask = 0
        self.port_number = port_number
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.max_fc_speed = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentGemPortCap", parent_mo_or_dn, **kwargs)
