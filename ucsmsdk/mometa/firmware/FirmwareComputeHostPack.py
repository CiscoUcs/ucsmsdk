"""This module contains the general information for FirmwareComputeHostPack ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FirmwareComputeHostPackConsts():
    IGNORE_COMP_CHECK_FALSE = "false"
    IGNORE_COMP_CHECK_NO = "no"
    IGNORE_COMP_CHECK_TRUE = "true"
    IGNORE_COMP_CHECK_YES = "yes"
    INT_ID_NONE = "none"
    MODE_ONE_SHOT = "one-shot"
    MODE_STAGED = "staged"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    UPDATE_TRIGGER_IMMEDIATE = "immediate"


class FirmwareComputeHostPack(ManagedObject):
    """This is FirmwareComputeHostPack class."""

    consts = FirmwareComputeHostPackConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("FirmwareComputeHostPack", "firmwareComputeHostPack", "fw-host-pack-[name]", VersionMeta.Version101e, "InputOutput", 0x7fffL, [], ["admin", "ls-compute", "ls-config-policy", "ls-server-policy"], [u'orgOrg'], [u'firmwareExcludeServerComponent', u'firmwarePackItem'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "blade_bundle_name": MoPropertyMeta("blade_bundle_name", "bladeBundleName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "blade_bundle_version": MoPropertyMeta("blade_bundle_version", "bladeBundleVersion", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x2L, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|no-config-issue|bios-image-not-selected),){0,2}(defaultValue|no-config-issue|bios-image-not-selected){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "ignore_comp_check": MoPropertyMeta("ignore_comp_check", "ignoreCompCheck", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["false", "no", "true", "yes"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "m_series_bundle_name": MoPropertyMeta("m_series_bundle_name", "mSeriesBundleName", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "m_series_bundle_version": MoPropertyMeta("m_series_bundle_version", "mSeriesBundleVersion", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x40L, 0, 510, None, [], []), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["one-shot", "staged"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x100L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rack_bundle_name": MoPropertyMeta("rack_bundle_name", "rackBundleName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rack_bundle_version": MoPropertyMeta("rack_bundle_version", "rackBundleVersion", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x400L, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x800L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "stage_size": MoPropertyMeta("stage_size", "stageSize", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "update_trigger": MoPropertyMeta("update_trigger", "updateTrigger", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["immediate"], []), 
    }

    prop_map = {
        "bladeBundleName": "blade_bundle_name", 
        "bladeBundleVersion": "blade_bundle_version", 
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "descr": "descr", 
        "dn": "dn", 
        "ignoreCompCheck": "ignore_comp_check", 
        "intId": "int_id", 
        "mSeriesBundleName": "m_series_bundle_name", 
        "mSeriesBundleVersion": "m_series_bundle_version", 
        "mode": "mode", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "propAcl": "prop_acl", 
        "rackBundleName": "rack_bundle_name", 
        "rackBundleVersion": "rack_bundle_version", 
        "rn": "rn", 
        "sacl": "sacl", 
        "stageSize": "stage_size", 
        "status": "status", 
        "updateTrigger": "update_trigger", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.blade_bundle_name = None
        self.blade_bundle_version = None
        self.child_action = None
        self.config_qualifier = None
        self.descr = None
        self.ignore_comp_check = None
        self.int_id = None
        self.m_series_bundle_name = None
        self.m_series_bundle_version = None
        self.mode = None
        self.policy_level = None
        self.policy_owner = None
        self.prop_acl = None
        self.rack_bundle_name = None
        self.rack_bundle_version = None
        self.sacl = None
        self.stage_size = None
        self.status = None
        self.update_trigger = None

        ManagedObject.__init__(self, "FirmwareComputeHostPack", parent_mo_or_dn, **kwargs)

