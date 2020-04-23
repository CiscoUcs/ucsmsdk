"""This module contains the general information for EquipmentHDDFaultMonDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentHDDFaultMonDefConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class EquipmentHDDFaultMonDef(ManagedObject):
    """This is EquipmentHDDFaultMonDef class."""

    consts = EquipmentHDDFaultMonDefConsts()
    naming_props = set(['ControllerFwVersion', 'HDDMonSupport'])

    mo_meta = MoMeta("EquipmentHDDFaultMonDef", "equipmentHDDFaultMonDef", "[controller_fw_version][hdd_mon_support]", VersionMeta.Version201m, "InputOutput", 0x3ff, [], [""], ['equipmentBladeCapProvider', 'equipmentServerUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "controller_fw_version": MoPropertyMeta("controller_fw_version", "ControllerFwVersion", "string", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x2, 1, 510, None, [], []),
        "controller_model": MoPropertyMeta("controller_model", "ControllerModel", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "hdd_mon_support": MoPropertyMeta("hdd_mon_support", "HDDMonSupport", "string", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x8, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "ControllerFwVersion": "controller_fw_version", 
        "ControllerModel": "controller_model", 
        "HDDMonSupport": "hdd_mon_support", 
        "childAction": "child_action", 
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

    def __init__(self, parent_mo_or_dn, controller_fw_version, hdd_mon_support, **kwargs):
        self._dirty_mask = 0
        self.controller_fw_version = controller_fw_version
        self.hdd_mon_support = hdd_mon_support
        self.controller_model = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentHDDFaultMonDef", parent_mo_or_dn, **kwargs)
