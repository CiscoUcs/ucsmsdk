"""This module contains the general information for LsbootPolicy ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LsbootPolicyConsts:
    BOOT_MODE_LEGACY = "legacy"
    BOOT_MODE_UEFI = "uefi"
    ENFORCE_VNIC_NAME_FALSE = "false"
    ENFORCE_VNIC_NAME_NO = "no"
    ENFORCE_VNIC_NAME_TRUE = "true"
    ENFORCE_VNIC_NAME_YES = "yes"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PURPOSE_OPERATIONAL = "operational"
    PURPOSE_UTILITY = "utility"
    REBOOT_ON_UPDATE_FALSE = "false"
    REBOOT_ON_UPDATE_NO = "no"
    REBOOT_ON_UPDATE_TRUE = "true"
    REBOOT_ON_UPDATE_YES = "yes"


class LsbootPolicy(ManagedObject):
    """This is LsbootPolicy class."""

    consts = LsbootPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("LsbootPolicy", "lsbootPolicy", "boot-policy-[name]", VersionMeta.Version101e, "InputOutput", 0x7ff, [], ["admin", "ls-config-policy", "ls-server-policy", "ls-storage-policy"], ['orgOrg', 'policySystemEp'], ['lsbootBootSecurity', 'lsbootEFIShell', 'lsbootIScsi', 'lsbootLan', 'lsbootSan', 'lsbootStorage', 'lsbootVirtualMedia'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "boot_mode": MoPropertyMeta("boot_mode", "bootMode", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["legacy", "uefi"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "enforce_vnic_name": MoPropertyMeta("enforce_vnic_name", "enforceVnicName", "string", VersionMeta.Version102d, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["local", "pending-policy", "policy"], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "purpose": MoPropertyMeta("purpose", "purpose", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["operational", "utility"], []),
        "reboot_on_update": MoPropertyMeta("reboot_on_update", "rebootOnUpdate", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "bootMode": "boot_mode", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "enforceVnicName": "enforce_vnic_name", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "propAcl": "prop_acl", 
        "purpose": "purpose", 
        "rebootOnUpdate": "reboot_on_update", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.boot_mode = None
        self.child_action = None
        self.descr = None
        self.enforce_vnic_name = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.prop_acl = None
        self.purpose = None
        self.reboot_on_update = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LsbootPolicy", parent_mo_or_dn, **kwargs)
