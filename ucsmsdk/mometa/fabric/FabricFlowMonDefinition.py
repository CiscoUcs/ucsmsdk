"""This module contains the general information for FabricFlowMonDefinition ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricFlowMonDefinitionConsts:
    INT_ID_NONE = "none"
    KEY_TYPE_IPV4KEYS = "ipv4keys"
    KEY_TYPE_IPV6KEYS = "ipv6keys"
    KEY_TYPE_L2KEYS = "l2keys"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    RECORD_TYPE_SYSTEM_DEFINED = "system-defined"
    RECORD_TYPE_USER_DEFINED = "user-defined"


class FabricFlowMonDefinition(ManagedObject):
    """This is FabricFlowMonDefinition class."""

    consts = FabricFlowMonDefinitionConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricFlowMonDefinition", "fabricFlowMonDefinition", "flow-record-[name]", VersionMeta.Version221b, "InputOutput", 0x1fff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricEthLanFlowMonitoring'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "ipv4keys": MoPropertyMeta("ipv4keys", "ipv4keys", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((defaultValue|none|src-port|ipv4-src-address|ipv4-dest-address|dest-port|ip-protocol|ip-tos),){0,7}(defaultValue|none|src-port|ipv4-src-address|ipv4-dest-address|dest-port|ip-protocol|ip-tos){0,1}""", [], []),
        "ipv6keys": MoPropertyMeta("ipv6keys", "ipv6keys", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((defaultValue|none|src-port|ipv6-src-address|ipv6-dest-address|dest-port|ip-protocol),){0,6}(defaultValue|none|src-port|ipv6-src-address|ipv6-dest-address|dest-port|ip-protocol){0,1}""", [], []),
        "key_type": MoPropertyMeta("key_type", "keyType", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["ipv4keys", "ipv6keys", "l2keys"], []),
        "l2keys": MoPropertyMeta("l2keys", "l2keys", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((defaultValue|none|ethertype|dest-mac-address|src-mac-address),){0,4}(defaultValue|none|ethertype|dest-mac-address|src-mac-address){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "nonkeys": MoPropertyMeta("nonkeys", "nonkeys", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((defaultValue|none|counter-packets-long|counter-bytes-long|sys-uptime-first|sys-uptime-last),){0,5}(defaultValue|none|counter-packets-long|counter-bytes-long|sys-uptime-first|sys-uptime-last){0,1}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["local", "pending-policy", "policy"], []),
        "record_type": MoPropertyMeta("record_type", "recordType", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["system-defined", "user-defined"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x800, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "ipv4keys": "ipv4keys", 
        "ipv6keys": "ipv6keys", 
        "keyType": "key_type", 
        "l2keys": "l2keys", 
        "name": "name", 
        "nonkeys": "nonkeys", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "recordType": "record_type", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.ipv4keys = None
        self.ipv6keys = None
        self.key_type = None
        self.l2keys = None
        self.nonkeys = None
        self.policy_level = None
        self.policy_owner = None
        self.record_type = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FabricFlowMonDefinition", parent_mo_or_dn, **kwargs)
