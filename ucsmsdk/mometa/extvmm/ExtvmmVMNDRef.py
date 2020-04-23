"""This module contains the general information for ExtvmmVMNDRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ExtvmmVMNDRefConsts:
    CONFIG_QUALIFIER_DUPLICATE_VMND_REFERENCE = "duplicate-vmnd-reference"
    CONFIG_QUALIFIER_NORMAL = "normal"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class ExtvmmVMNDRef(ManagedObject):
    """This is ExtvmmVMNDRef class."""

    consts = ExtvmmVMNDRefConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("ExtvmmVMNDRef", "extvmmVMNDRef", "vm-network-def-ref[name]", VersionMeta.Version221b, "InputOutput", 0x7ff, [], ["admin", "ls-network", "ls-network-policy"], ['extvmmVMNetwork'], ['faultInst'], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["duplicate-vmnd-reference", "normal"], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "fn_def_name": MoPropertyMeta("fn_def_name", "fnDefName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "fn_name": MoPropertyMeta("fn_name", "fnName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "oper_vm_network_def_name": MoPropertyMeta("oper_vm_network_def_name", "operVmNetworkDefName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vm_network_def_name": MoPropertyMeta("vm_network_def_name", "vmNetworkDefName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "descr": "descr", 
        "dn": "dn", 
        "fnDefName": "fn_def_name", 
        "fnName": "fn_name", 
        "intId": "int_id", 
        "name": "name", 
        "operVmNetworkDefName": "oper_vm_network_def_name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vmNetworkDefName": "vm_network_def_name", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.config_qualifier = None
        self.descr = None
        self.fn_def_name = None
        self.fn_name = None
        self.int_id = None
        self.oper_vm_network_def_name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.vm_network_def_name = None

        ManagedObject.__init__(self, "ExtvmmVMNDRef", parent_mo_or_dn, **kwargs)
