"""This module contains the general information for IppoolPool ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class IppoolPoolConsts:
    ASSIGNMENT_ORDER_DEFAULT = "default"
    ASSIGNMENT_ORDER_SEQUENTIAL = "sequential"
    EXT_MANAGED_EXTERNAL = "external"
    EXT_MANAGED_INTERNAL = "internal"
    INT_ID_NONE = "none"
    IS_NET_BIOSENABLED_DISABLED = "disabled"
    IS_NET_BIOSENABLED_ENABLED = "enabled"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SUPPORTS_DHCP_DISABLED = "disabled"
    SUPPORTS_DHCP_ENABLED = "enabled"


class IppoolPool(ManagedObject):
    """This is IppoolPool class."""

    consts = IppoolPoolConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("IppoolPool", "ippoolPool", "ip-pool-[name]", VersionMeta.Version101e, "InputOutput", 0x1fff, [], ["admin", "ls-network-policy"], ['extvmmNetworkSets', 'orgOrg'], ['faultInst', 'ipDnsSuffix', 'ipIPv4WinsServer', 'ippoolBlock', 'ippoolIpV6Block', 'ippoolIpV6Pooled', 'ippoolPooled'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "assignment_order": MoPropertyMeta("assignment_order", "assignmentOrder", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["default", "sequential"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "ext_managed": MoPropertyMeta("ext_managed", "extManaged", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["external", "internal"], []),
        "guid": MoPropertyMeta("guid", "guid", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "is_net_bios_enabled": MoPropertyMeta("is_net_bios_enabled", "isNetBIOSEnabled", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["disabled", "enabled"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["local", "pending-policy", "policy"], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "size": MoPropertyMeta("size", "size", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supports_dhcp": MoPropertyMeta("supports_dhcp", "supportsDHCP", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["disabled", "enabled"], []),
        "v4_assigned": MoPropertyMeta("v4_assigned", "v4Assigned", "uint", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "v4_size": MoPropertyMeta("v4_size", "v4Size", "uint", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "v6_assigned": MoPropertyMeta("v6_assigned", "v6Assigned", "uint", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "v6_size": MoPropertyMeta("v6_size", "v6Size", "uint", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "assigned": "assigned", 
        "assignmentOrder": "assignment_order", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "extManaged": "ext_managed", 
        "guid": "guid", 
        "intId": "int_id", 
        "isNetBIOSEnabled": "is_net_bios_enabled", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "size": "size", 
        "status": "status", 
        "supportsDHCP": "supports_dhcp", 
        "v4Assigned": "v4_assigned", 
        "v4Size": "v4_size", 
        "v6Assigned": "v6_assigned", 
        "v6Size": "v6_size", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.assigned = None
        self.assignment_order = None
        self.child_action = None
        self.descr = None
        self.ext_managed = None
        self.guid = None
        self.int_id = None
        self.is_net_bios_enabled = None
        self.policy_level = None
        self.policy_owner = None
        self.prop_acl = None
        self.sacl = None
        self.size = None
        self.status = None
        self.supports_dhcp = None
        self.v4_assigned = None
        self.v4_size = None
        self.v6_assigned = None
        self.v6_size = None

        ManagedObject.__init__(self, "IppoolPool", parent_mo_or_dn, **kwargs)
