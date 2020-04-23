"""This module contains the general information for CpmaintMaintPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CpmaintMaintPolicyConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    UPTIME_DISR_UNSPECIFIED = "unspecified"
    UPTIME_DISR_USER_ACK = "user-ack"


class CpmaintMaintPolicy(ManagedObject):
    """This is CpmaintMaintPolicy class."""

    consts = CpmaintMaintPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("CpmaintMaintPolicy", "cpmaintMaintPolicy", "chassis-profile-maint-[name]", VersionMeta.Version312b, "InputOutput", 0x7ff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['orgOrg'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "oper_sched_name": MoPropertyMeta("oper_sched_name", "operSchedName", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sched_name": MoPropertyMeta("sched_name", "schedName", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "trigger_config": MoPropertyMeta("trigger_config", "triggerConfig", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((defaultValue|none|on-next-boot),){0,2}(defaultValue|none|on-next-boot){0,1}""", [], []),
        "uptime_disr": MoPropertyMeta("uptime_disr", "uptimeDisr", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["unspecified", "user-ack"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "operSchedName": "oper_sched_name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "schedName": "sched_name", 
        "status": "status", 
        "triggerConfig": "trigger_config", 
        "uptimeDisr": "uptime_disr", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.oper_sched_name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.sched_name = None
        self.status = None
        self.trigger_config = None
        self.uptime_disr = None

        ManagedObject.__init__(self, "CpmaintMaintPolicy", parent_mo_or_dn, **kwargs)
