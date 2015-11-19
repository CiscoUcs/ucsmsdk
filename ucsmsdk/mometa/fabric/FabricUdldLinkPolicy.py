"""This module contains the general information for FabricUdldLinkPolicy ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FabricUdldLinkPolicyConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    INT_ID_NONE = "none"
    MODE_AGGRESSIVE = "aggressive"
    MODE_NORMAL = "normal"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PROTOCOL_CDP = "cdp"
    PROTOCOL_UDLD = "udld"
    PROTOCOL_UNKNOWN = "unknown"


class FabricUdldLinkPolicy(ManagedObject):
    """This is FabricUdldLinkPolicy class."""

    consts = FabricUdldLinkPolicyConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("FabricUdldLinkPolicy", "fabricUdldLinkPolicy", "udld-link-pol-[name]", VersionMeta.Version221b, "InputOutput", 0x1ffL, [], ["admin", "ext-lan-config", "ext-lan-policy", "read-only"], [u'fabricLanCloud'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["aggressive", "normal"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x20L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cdp", "udld", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, """((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "mode": "mode", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "protocol": "protocol", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.mode = None
        self.policy_level = None
        self.policy_owner = None
        self.protocol = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "FabricUdldLinkPolicy", parent_mo_or_dn, **kwargs)

