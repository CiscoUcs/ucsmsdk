"""This module contains the general information for NwctrlDefinition ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class NwctrlDefinitionConsts:
    CDP_DISABLED = "disabled"
    CDP_ENABLED = "enabled"
    INT_ID_NONE = "none"
    LLDP_RECEIVE_DISABLED = "disabled"
    LLDP_RECEIVE_ENABLED = "enabled"
    LLDP_TRANSMIT_DISABLED = "disabled"
    LLDP_TRANSMIT_ENABLED = "enabled"
    MAC_REGISTER_MODE_ALL_HOST_VLANS = "all-host-vlans"
    MAC_REGISTER_MODE_ONLY_NATIVE_VLAN = "only-native-vlan"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    UPLINK_FAIL_ACTION_LINK_DOWN = "link-down"
    UPLINK_FAIL_ACTION_WARNING = "warning"


class NwctrlDefinition(ManagedObject):
    """This is NwctrlDefinition class."""

    consts = NwctrlDefinitionConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("NwctrlDefinition", "nwctrlDefinition", "nwctrl-[name]", VersionMeta.Version102d, "InputOutput", 0x1fff, [], ["admin", "ls-network", "ls-network-policy"], ['fabricEthEstcCloud', 'orgOrg', 'policySystemEp'], ['dpsecMac'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "cdp": MoPropertyMeta("cdp", "cdp", "string", VersionMeta.Version102d, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version102d, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version102d, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version102d, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version102d, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "lldp_init": MoPropertyMeta("lldp_init", "lldpInit", "byte", VersionMeta.Version411a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "lldp_receive": MoPropertyMeta("lldp_receive", "lldpReceive", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["disabled", "enabled"], []),
        "lldp_transmit": MoPropertyMeta("lldp_transmit", "lldpTransmit", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["disabled", "enabled"], []),
        "mac_register_mode": MoPropertyMeta("mac_register_mode", "macRegisterMode", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["all-host-vlans", "only-native-vlan"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version102d, MoPropertyMeta.NAMING, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["local", "pending-policy", "policy"], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version102d, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version102d, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "uplink_fail_action": MoPropertyMeta("uplink_fail_action", "uplinkFailAction", "string", VersionMeta.Version102d, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["link-down", "warning"], []),
    }

    prop_map = {
        "cdp": "cdp", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "lldpInit": "lldp_init", 
        "lldpReceive": "lldp_receive", 
        "lldpTransmit": "lldp_transmit", 
        "macRegisterMode": "mac_register_mode", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "uplinkFailAction": "uplink_fail_action", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.cdp = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.lldp_init = None
        self.lldp_receive = None
        self.lldp_transmit = None
        self.mac_register_mode = None
        self.policy_level = None
        self.policy_owner = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.uplink_fail_action = None

        ManagedObject.__init__(self, "NwctrlDefinition", parent_mo_or_dn, **kwargs)
