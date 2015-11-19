"""This module contains the general information for ComputeBladeDiscPolicy ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ComputeBladeDiscPolicyConsts():
    ACTION_DIAG = "diag"
    ACTION_IMMEDIATE = "immediate"
    ACTION_USER_ACKNOWLEDGED = "user-acknowledged"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class ComputeBladeDiscPolicy(ManagedObject):
    """This is ComputeBladeDiscPolicy class."""

    consts = ComputeBladeDiscPolicyConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("ComputeBladeDiscPolicy", "computeBladeDiscPolicy", "blade-discovery[name]", VersionMeta.Version101e, "InputOutput", 0x3ffL, [], ["admin", "pn-policy", "read-only"], [u'orgOrg'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "action": MoPropertyMeta("action", "action", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["diag", "immediate", "user-acknowledged"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "qualifier": MoPropertyMeta("qualifier", "qualifier", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "scrub_policy_name": MoPropertyMeta("scrub_policy_name", "scrubPolicyName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "action": "action", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "qualifier": "qualifier", 
        "rn": "rn", 
        "sacl": "sacl", 
        "scrubPolicyName": "scrub_policy_name", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.action = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.qualifier = None
        self.sacl = None
        self.scrub_policy_name = None
        self.status = None

        ManagedObject.__init__(self, "ComputeBladeDiscPolicy", parent_mo_or_dn, **kwargs)

