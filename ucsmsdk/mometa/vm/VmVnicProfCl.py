"""This module contains the general information for VmVnicProfCl ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VmVnicProfClConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class VmVnicProfCl(ManagedObject):
    """This is VmVnicProfCl class."""

    consts = VmVnicProfClConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("VmVnicProfCl", "vmVnicProfCl", "cl-[name]", VersionMeta.Version111j, "InputOutput", 0x7ff, [], ["admin", "ls-config", "ls-config-policy", "ls-network", "pn-policy"], ['vnicProfile'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dc_name": MoPropertyMeta("dc_name", "dcName", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%\(\)\*\+,\-\./:;\?@\[\\\]\^_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111j, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "org_path": MoPropertyMeta("org_path", "orgPath", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[ !#$%\(\)\*\+,\-\./:;\?@\[\\\]\^_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "sw_name": MoPropertyMeta("sw_name", "swName", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""[ !#$%\(\)\*\+,\-\./:;\?@\[\\\]\^_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dcName": "dc_name", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "orgPath": "org_path", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "swName": "sw_name", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.dc_name = None
        self.descr = None
        self.int_id = None
        self.org_path = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.sw_name = None

        ManagedObject.__init__(self, "VmVnicProfCl", parent_mo_or_dn, **kwargs)
