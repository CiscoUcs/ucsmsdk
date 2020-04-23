"""This module contains the general information for ExtvmmVMNetworkDefinition ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ExtvmmVMNetworkDefinitionConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    REF_OPER_STATE_INVALID_REFERENCE = "invalid-reference"
    REF_OPER_STATE_UP = "up"


class ExtvmmVMNetworkDefinition(ManagedObject):
    """This is ExtvmmVMNetworkDefinition class."""

    consts = ExtvmmVMNetworkDefinitionConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("ExtvmmVMNetworkDefinition", "extvmmVMNetworkDefinition", "vm-network-def-[name]", VersionMeta.Version221b, "InputOutput", 0x7ff, [], ["admin", "ls-network", "ls-network-policy"], ['extvmmFabricNetworkDefinition'], ['faultInst', 'vnicEtherIf'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "ext_ip_pool_name": MoPropertyMeta("ext_ip_pool_name", "extIpPoolName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "guid": MoPropertyMeta("guid", "guid", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "ip_pool_guid": MoPropertyMeta("ip_pool_guid", "ipPoolGuid", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []),
        "max_ports": MoPropertyMeta("max_ports", "maxPorts", "ushort", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-4096"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "oper_ext_ip_pool_name": MoPropertyMeta("oper_ext_ip_pool_name", "operExtIpPoolName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["local", "pending-policy", "policy"], []),
        "primary_vlan_id": MoPropertyMeta("primary_vlan_id", "primaryVlanId", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4093"]),
        "ref_oper_state": MoPropertyMeta("ref_oper_state", "refOperState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["invalid-reference", "up"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vlan_name": MoPropertyMeta("vlan_name", "vlanName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "extIpPoolName": "ext_ip_pool_name", 
        "guid": "guid", 
        "intId": "int_id", 
        "ipPoolGuid": "ip_pool_guid", 
        "maxPorts": "max_ports", 
        "name": "name", 
        "operExtIpPoolName": "oper_ext_ip_pool_name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "primaryVlanId": "primary_vlan_id", 
        "refOperState": "ref_oper_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vlanName": "vlan_name", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.ext_ip_pool_name = None
        self.guid = None
        self.int_id = None
        self.ip_pool_guid = None
        self.max_ports = None
        self.oper_ext_ip_pool_name = None
        self.policy_level = None
        self.policy_owner = None
        self.primary_vlan_id = None
        self.ref_oper_state = None
        self.sacl = None
        self.status = None
        self.vlan_name = None

        ManagedObject.__init__(self, "ExtvmmVMNetworkDefinition", parent_mo_or_dn, **kwargs)
