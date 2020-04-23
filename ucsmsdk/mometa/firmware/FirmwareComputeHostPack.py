"""This module contains the general information for FirmwareComputeHostPack ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareComputeHostPackConsts:
    IGNORE_COMP_CHECK_FALSE = "false"
    IGNORE_COMP_CHECK_NO = "no"
    IGNORE_COMP_CHECK_TRUE = "true"
    IGNORE_COMP_CHECK_YES = "yes"
    INT_ID_NONE = "none"
    MODE_ONE_SHOT = "one-shot"
    MODE_STAGED = "staged"
    OVERRIDE_DEFAULT_EXCLUSION_FALSE = "false"
    OVERRIDE_DEFAULT_EXCLUSION_NO = "no"
    OVERRIDE_DEFAULT_EXCLUSION_TRUE = "true"
    OVERRIDE_DEFAULT_EXCLUSION_YES = "yes"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    UPDATE_TRIGGER_IMMEDIATE = "immediate"


class FirmwareComputeHostPack(ManagedObject):
    """This is FirmwareComputeHostPack class."""

    consts = FirmwareComputeHostPackConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FirmwareComputeHostPack", "firmwareComputeHostPack", "fw-host-pack-[name]", VersionMeta.Version101e, "InputOutput", 0xffff, [], ["admin", "ls-compute", "ls-config-policy", "ls-server-policy"], ['orgOrg'], ['firmwareBackupVersionHolder', 'firmwareExcludeServerComponent', 'firmwarePackItem'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "blade_bundle_name": MoPropertyMeta("blade_bundle_name", "bladeBundleName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "blade_bundle_version": MoPropertyMeta("blade_bundle_version", "bladeBundleVersion", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|no-config-issue|bios-image-not-selected),){0,2}(defaultValue|no-config-issue|bios-image-not-selected){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "ignore_comp_check": MoPropertyMeta("ignore_comp_check", "ignoreCompCheck", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["one-shot", "staged"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "override_default_exclusion": MoPropertyMeta("override_default_exclusion", "overrideDefaultExclusion", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["false", "no", "true", "yes"], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["local", "pending-policy", "policy"], []),
        "rack_bundle_name": MoPropertyMeta("rack_bundle_name", "rackBundleName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rack_bundle_version": MoPropertyMeta("rack_bundle_version", "rackBundleVersion", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x800, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "service_pack_bundle_name": MoPropertyMeta("service_pack_bundle_name", "servicePackBundleName", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "service_pack_bundle_version": MoPropertyMeta("service_pack_bundle_version", "servicePackBundleVersion", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x1000, 0, 510, None, [], []),
        "stage_size": MoPropertyMeta("stage_size", "stageSize", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "update_trigger": MoPropertyMeta("update_trigger", "updateTrigger", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["immediate"], []),
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
        "mode": "mode", 
        "name": "name", 
        "overrideDefaultExclusion": "override_default_exclusion", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rackBundleName": "rack_bundle_name", 
        "rackBundleVersion": "rack_bundle_version", 
        "rn": "rn", 
        "sacl": "sacl", 
        "servicePackBundleName": "service_pack_bundle_name", 
        "servicePackBundleVersion": "service_pack_bundle_version", 
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
        self.mode = None
        self.override_default_exclusion = None
        self.policy_level = None
        self.policy_owner = None
        self.rack_bundle_name = None
        self.rack_bundle_version = None
        self.sacl = None
        self.service_pack_bundle_name = None
        self.service_pack_bundle_version = None
        self.stage_size = None
        self.status = None
        self.update_trigger = None

        ManagedObject.__init__(self, "FirmwareComputeHostPack", parent_mo_or_dn, **kwargs)
