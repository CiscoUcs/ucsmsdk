"""This module contains the general information for EquipmentPfcMmuCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentPfcMmuCapConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentPfcMmuCap(ManagedObject):
    """This is EquipmentPfcMmuCap class."""

    consts = EquipmentPfcMmuCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentPfcMmuCap", "equipmentPfcMmuCap", "pfc-mmu-cap", VersionMeta.Version311e, "InputOutput", 0xff, [], [""], ['equipmentSwitchCapProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version311e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "fcoe": MoPropertyMeta("fcoe", "fcoe", "byte", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-100"]),
        "fcoe_jumbo_nodrop": MoPropertyMeta("fcoe_jumbo_nodrop", "fcoeJumboNodrop", "byte", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-100"]),
        "fcoe_normal_nodrop": MoPropertyMeta("fcoe_normal_nodrop", "fcoeNormalNodrop", "byte", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-100"]),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version311e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "jumbo_breakout_port": MoPropertyMeta("jumbo_breakout_port", "jumboBreakoutPort", "byte", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-255"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "fcoe": "fcoe", 
        "fcoeJumboNodrop": "fcoe_jumbo_nodrop", 
        "fcoeNormalNodrop": "fcoe_normal_nodrop", 
        "intId": "int_id", 
        "jumboBreakoutPort": "jumbo_breakout_port", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.fcoe = None
        self.fcoe_jumbo_nodrop = None
        self.fcoe_normal_nodrop = None
        self.int_id = None
        self.jumbo_breakout_port = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPfcMmuCap", parent_mo_or_dn, **kwargs)
