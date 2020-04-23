"""This module contains the general information for AaaExtMgmtCutThruTkn ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AaaExtMgmtCutThruTknConsts:
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    REMOTE_FALSE = "false"
    REMOTE_NO = "no"
    REMOTE_TRUE = "true"
    REMOTE_YES = "yes"
    TYPE_KVM = "kvm"


class AaaExtMgmtCutThruTkn(ManagedObject):
    """This is AaaExtMgmtCutThruTkn class."""

    consts = AaaExtMgmtCutThruTknConsts()
    naming_props = set(['token'])

    mo_meta = MoMeta("AaaExtMgmtCutThruTkn", "aaaExtMgmtCutThruTkn", "-[token]", VersionMeta.Version102d, "InputOutput", 0x1ff, [], ["aaa", "admin"], ['aaaUserEp'], [], ["Get"])

    prop_meta = {
        "auth_domain": MoPropertyMeta("auth_domain", "authDomain", "string", VersionMeta.Version203a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "auth_user": MoPropertyMeta("auth_user", "authUser", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version102d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "creation_time": MoPropertyMeta("creation_time", "creationTime", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version102d, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version102d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version102d, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "locales": MoPropertyMeta("locales", "locales", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version102d, MoPropertyMeta.CREATE_ONLY, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "pn_dn": MoPropertyMeta("pn_dn", "pnDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["local", "pending-policy", "policy"], []),
        "priv": MoPropertyMeta("priv", "priv", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""((ext-lan-policy|pn-maintenance|ls-security-policy|pod-security|pn-equipment|ls-config-policy|ls-compute|ext-san-policy|ls-security|aaa|power-mgmt|read-only|ext-lan-security|ls-config|ls-server-policy|pod-qos|pn-policy|ls-storage-policy|org-management|admin|ext-san-security|pod-config|ls-server|ext-lan-qos|ls-storage|ls-qos-policy|operations|ext-lan-config|pn-security|ls-network-policy|pod-policy|ext-san-qos|ls-qos|ls-server-oper|ext-san-config|ls-network|ls-ext-access|fault),){0,37}(ext-lan-policy|pn-maintenance|ls-security-policy|pod-security|pn-equipment|ls-config-policy|ls-compute|ext-san-policy|ls-security|aaa|power-mgmt|read-only|ext-lan-security|ls-config|ls-server-policy|pod-qos|pn-policy|ls-storage-policy|org-management|admin|ext-san-security|pod-config|ls-server|ext-lan-qos|ls-storage|ls-qos-policy|operations|ext-lan-config|pn-security|ls-network-policy|pod-policy|ext-san-qos|ls-qos|ls-server-oper|ext-san-config|ls-network|ls-ext-access|fault){0,1}""", [], []),
        "remote": MoPropertyMeta("remote", "remote", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version102d, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version102d, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "token": MoPropertyMeta("token", "token", "string", VersionMeta.Version102d, MoPropertyMeta.NAMING, 0x100, 1, 510, None, [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version102d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["kvm"], []),
        "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version102d, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
    }

    prop_map = {
        "authDomain": "auth_domain", 
        "authUser": "auth_user", 
        "childAction": "child_action", 
        "creationTime": "creation_time", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "locales": "locales", 
        "name": "name", 
        "pnDn": "pn_dn", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "priv": "priv", 
        "remote": "remote", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "token": "token", 
        "type": "type", 
        "user": "user", 
    }

    def __init__(self, parent_mo_or_dn, token, **kwargs):
        self._dirty_mask = 0
        self.token = token
        self.auth_domain = None
        self.auth_user = None
        self.child_action = None
        self.creation_time = None
        self.descr = None
        self.int_id = None
        self.locales = None
        self.name = None
        self.pn_dn = None
        self.policy_level = None
        self.policy_owner = None
        self.priv = None
        self.remote = None
        self.sacl = None
        self.status = None
        self.type = None
        self.user = None

        ManagedObject.__init__(self, "AaaExtMgmtCutThruTkn", parent_mo_or_dn, **kwargs)
