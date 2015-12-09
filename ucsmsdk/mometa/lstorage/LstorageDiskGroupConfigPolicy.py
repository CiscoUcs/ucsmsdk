"""This module contains the general information for LstorageDiskGroupConfigPolicy ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageDiskGroupConfigPolicyConsts():
    DEPLOY_ON_UPDATE_FALSE = "false"
    DEPLOY_ON_UPDATE_NO = "no"
    DEPLOY_ON_UPDATE_TRUE = "true"
    DEPLOY_ON_UPDATE_YES = "yes"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    RAID_LEVEL_MIRROR = "mirror"
    RAID_LEVEL_MIRROR_STRIPE = "mirror-stripe"
    RAID_LEVEL_RAID = "raid"
    RAID_LEVEL_SIMPLE = "simple"
    RAID_LEVEL_STRIPE = "stripe"
    RAID_LEVEL_STRIPE_DUAL_PARITY = "stripe-dual-parity"
    RAID_LEVEL_STRIPE_DUAL_PARITY_STRIPE = "stripe-dual-parity-stripe"
    RAID_LEVEL_STRIPE_PARITY = "stripe-parity"
    RAID_LEVEL_STRIPE_PARITY_STRIPE = "stripe-parity-stripe"
    RAID_LEVEL_UNSPECIFIED = "unspecified"


class LstorageDiskGroupConfigPolicy(ManagedObject):
    """This is LstorageDiskGroupConfigPolicy class."""

    consts = LstorageDiskGroupConfigPolicyConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("LstorageDiskGroupConfigPolicy", "lstorageDiskGroupConfigPolicy", "disk-group-config-[name]", VersionMeta.Version224b, "InputOutput", 0x3ffL, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-storage", "ls-storage-policy"], [u'orgOrg'], [u'lstorageDiskGroupQualifier', u'lstorageLocalDiskConfigRef', u'lstorageVirtualDriveDef'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "deploy_on_update": MoPropertyMeta("deploy_on_update", "deployOnUpdate", "string", VersionMeta.Version251a, MoPropertyMeta.CREATE_ONLY, 0x4L, None, None, None, ["false", "no", "true", "yes"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version224b, MoPropertyMeta.NAMING, 0x20L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "raid_level": MoPropertyMeta("raid_level", "raidLevel", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["mirror", "mirror-stripe", "raid", "simple", "stripe", "stripe-dual-parity", "stripe-dual-parity-stripe", "stripe-parity", "stripe-parity-stripe", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x100L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x200L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "deployOnUpdate": "deploy_on_update", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "raidLevel": "raid_level", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.deploy_on_update = None
        self.descr = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.raid_level = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageDiskGroupConfigPolicy", parent_mo_or_dn, **kwargs)
