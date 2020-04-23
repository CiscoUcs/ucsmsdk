"""This module contains the general information for ComputeKvmMgmtPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeKvmMgmtPolicyConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    VMEDIA_ENCRYPTION_DISABLE = "disable"
    VMEDIA_ENCRYPTION_ENABLE = "enable"


class ComputeKvmMgmtPolicy(ManagedObject):
    """This is ComputeKvmMgmtPolicy class."""

    consts = ComputeKvmMgmtPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("ComputeKvmMgmtPolicy", "computeKvmMgmtPolicy", "kvm-mgmt-policy-[name]", VersionMeta.Version222c, "InputOutput", 0x3ff, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-ext-access", "ls-server", "ls-server-oper", "ls-server-policy"], ['computeBlade', 'computeRackUnit', 'computeServerUnit', 'orgOrg'], ['mgmtKvmCertificate'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "kvm_port": MoPropertyMeta("kvm_port", "kvmPort", "ushort", VersionMeta.Version404a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1024-49151"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version222c, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vmedia_encryption": MoPropertyMeta("vmedia_encryption", "vmediaEncryption", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["disable", "enable"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "kvmPort": "kvm_port", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "vmediaEncryption": "vmedia_encryption", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.kvm_port = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None
        self.vmedia_encryption = None

        ManagedObject.__init__(self, "ComputeKvmMgmtPolicy", parent_mo_or_dn, **kwargs)
