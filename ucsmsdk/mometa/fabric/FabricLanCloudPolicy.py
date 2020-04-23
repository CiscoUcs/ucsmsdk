"""This module contains the general information for FabricLanCloudPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricLanCloudPolicyConsts:
    INT_ID_NONE = "none"
    MAC_AGING_MODE_DEFAULT = "mode-default"
    MAC_AGING_NEVER = "never"
    MODE_END_HOST = "end-host"
    MODE_SWITCH = "switch"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    VLAN_COMPRESSION_DISABLED = "disabled"
    VLAN_COMPRESSION_ENABLED = "enabled"


class FabricLanCloudPolicy(ManagedObject):
    """This is FabricLanCloudPolicy class."""

    consts = FabricLanCloudPolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("FabricLanCloudPolicy", "fabricLanCloudPolicy", "lan-policy", VersionMeta.Version227b, "InputOutput", 0x7ff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['orgOrg'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version227b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version227b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "mac_aging": MoPropertyMeta("mac_aging", "macAging", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[0-9]{1,7}|(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", ["mode-default", "never"], ["0-4294967295"]),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["end-host", "switch"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vlan_compression": MoPropertyMeta("vlan_compression", "vlanCompression", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["disabled", "enabled"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "macAging": "mac_aging", 
        "mode": "mode", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vlanCompression": "vlan_compression", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.mac_aging = None
        self.mode = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.vlan_compression = None

        ManagedObject.__init__(self, "FabricLanCloudPolicy", parent_mo_or_dn, **kwargs)
