"""This module contains the general information for ComputePowerSavePolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePowerSavePolicyConsts:
    EXTENDED_MODE_DISABLE = "Disable"
    EXTENDED_MODE_ENABLE = "Enable"
    INT_ID_NONE = "none"
    MODE_DISABLE = "Disable"
    MODE_ENABLE = "Enable"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    REDUNDANCY_GRID = "grid"
    REDUNDANCY_N_1 = "n+1"
    REDUNDANCY_N_2 = "n+2"
    REDUNDANCY_NON_REDUNDANT = "non-redundant"


class ComputePowerSavePolicy(ManagedObject):
    """This is ComputePowerSavePolicy class."""

    consts = ComputePowerSavePolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputePowerSavePolicy", "computePowerSavePolicy", "power-save-policy", VersionMeta.Version413a, "InputOutput", 0x3ff, [], ["admin", "pn-equipment", "pn-policy"], ['orgOrg'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "extended_mode": MoPropertyMeta("extended_mode", "extendedMode", "string", VersionMeta.Version432b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disable", "Enable"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disable", "Enable"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "redundancy": MoPropertyMeta("redundancy", "redundancy", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["grid", "n+1", "n+2", "non-redundant"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "extendedMode": "extended_mode", 
        "intId": "int_id", 
        "mode": "mode", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "redundancy": "redundancy", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.extended_mode = None
        self.int_id = None
        self.mode = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.redundancy = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputePowerSavePolicy", parent_mo_or_dn, **kwargs)
