"""This module contains the general information for VnicVmqConPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicVmqConPolicyConsts:
    INT_ID_NONE = "none"
    MULTI_QUEUE_DISABLED = "disabled"
    MULTI_QUEUE_ENABLED = "enabled"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class VnicVmqConPolicy(ManagedObject):
    """This is VnicVmqConPolicy class."""

    consts = VnicVmqConPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("VnicVmqConPolicy", "vnicVmqConPolicy", "vmq-con-[name]", VersionMeta.Version221b, "InputOutput", 0x1fff, [], ["admin", "ls-compute", "ls-network", "ls-network-policy", "ls-server"], ['orgOrg'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "adaptor_profile_name": MoPropertyMeta("adaptor_profile_name", "adaptorProfileName", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "intr_count": MoPropertyMeta("intr_count", "intrCount", "ushort", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-128"]),
        "multi_queue": MoPropertyMeta("multi_queue", "multiQueue", "string", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["disabled", "enabled"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vmmq_sub_vnics": MoPropertyMeta("vmmq_sub_vnics", "vmmqSubVnics", "ushort", VersionMeta.Version323a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, [], ["1-256"]),
        "vmq_count": MoPropertyMeta("vmq_count", "vmqCount", "ushort", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], ["1-128"]),
    }

    prop_map = {
        "adaptorProfileName": "adaptor_profile_name", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "intrCount": "intr_count", 
        "multiQueue": "multi_queue", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vmmqSubVnics": "vmmq_sub_vnics", 
        "vmqCount": "vmq_count", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.adaptor_profile_name = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.intr_count = None
        self.multi_queue = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.vmmq_sub_vnics = None
        self.vmq_count = None

        ManagedObject.__init__(self, "VnicVmqConPolicy", parent_mo_or_dn, **kwargs)
