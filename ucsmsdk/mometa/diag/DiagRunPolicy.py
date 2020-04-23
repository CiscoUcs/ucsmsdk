"""This module contains the general information for DiagRunPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class DiagRunPolicyConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class DiagRunPolicy(ManagedObject):
    """This is DiagRunPolicy class."""

    consts = DiagRunPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("DiagRunPolicy", "diagRunPolicy", "diag-policy-[name]", VersionMeta.Version131c, "InputOutput", 0x3ff, [], ["admin", "pn-policy"], ['diagSrvCtrl', 'orgOrg'], ['diagMemoryTest'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "failure_action": MoPropertyMeta("failure_action", "failureAction", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((defaultValue|nothing|tech-support|wait-debug|skip-remaining),){0,4}(defaultValue|nothing|tech-support|wait-debug|skip-remaining){0,1}""", [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131c, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "success_action": MoPropertyMeta("success_action", "successAction", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((defaultValue|nothing|tech-support|wait-debug),){0,3}(defaultValue|nothing|tech-support|wait-debug){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "failureAction": "failure_action", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "successAction": "success_action", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.failure_action = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.success_action = None

        ManagedObject.__init__(self, "DiagRunPolicy", parent_mo_or_dn, **kwargs)
