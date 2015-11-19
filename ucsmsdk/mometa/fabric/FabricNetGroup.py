"""This module contains the general information for FabricNetGroup ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FabricNetGroupConsts():
    ASSIGNMENT_ORDER_DEFAULT = "default"
    ASSIGNMENT_ORDER_SEQUENTIAL = "sequential"
    INT_ID_NONE = "none"
    OWNER_MANAGEMENT = "management"
    OWNER_POLICY = "policy"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_DUAL = "dual"


class FabricNetGroup(ManagedObject):
    """This is FabricNetGroup class."""

    consts = FabricNetGroupConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("FabricNetGroup", "fabricNetGroup", "net-group-[name]", VersionMeta.Version211a, "InputOutput", 0x1ffL, [], ["admin", "ext-lan-config", "ext-lan-policy"], [u'fabricEthLan', u'fabricLanCloud'], [u'fabricEthVlanPc', u'fabricEthVlanPortEp', u'fabricPooledVlan'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "assignment_order": MoPropertyMeta("assignment_order", "assignmentOrder", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["default", "sequential"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{1,32}""", [], []), 
        "native_net": MoPropertyMeta("native_net", "nativeNet", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10L, 0, 510, None, [], []), 
        "native_net_dn": MoPropertyMeta("native_net_dn", "nativeNetDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["management", "policy"], []), 
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "size": MoPropertyMeta("size", "size", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "dual"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100L, None, None, """((defaultValue|mgmt|vlan-compression|vlan-uncompressed),){0,3}(defaultValue|mgmt|vlan-compression|vlan-uncompressed){0,1}""", [], []), 
    }

    prop_map = {
        "assigned": "assigned", 
        "assignmentOrder": "assignment_order", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "id": "id", 
        "intId": "int_id", 
        "name": "name", 
        "nativeNet": "native_net", 
        "nativeNetDn": "native_net_dn", 
        "owner": "owner", 
        "peerDn": "peer_dn", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "size": "size", 
        "status": "status", 
        "switchId": "switch_id", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.assigned = None
        self.assignment_order = None
        self.child_action = None
        self.descr = None
        self.id = None
        self.int_id = None
        self.native_net = None
        self.native_net_dn = None
        self.owner = None
        self.peer_dn = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.size = None
        self.status = None
        self.switch_id = None
        self.type = None

        ManagedObject.__init__(self, "FabricNetGroup", parent_mo_or_dn, **kwargs)

