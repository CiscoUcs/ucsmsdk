"""This module contains the general information for FirmwareChassisPack ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareChassisPackConsts:
    FORCE_DEPLOY_FALSE = "false"
    FORCE_DEPLOY_NO = "no"
    FORCE_DEPLOY_TRUE = "true"
    FORCE_DEPLOY_YES = "yes"
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


class FirmwareChassisPack(ManagedObject):
    """This is FirmwareChassisPack class."""

    consts = FirmwareChassisPackConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FirmwareChassisPack", "firmwareChassisPack", "fw-chassis-pack-[name]", VersionMeta.Version312b, "InputOutput", 0x7fff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['orgOrg'], ['firmwareBackupVersionHolder', 'firmwareExcludeChassisComponent', 'firmwarePackItem'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "chassis_bundle_name": MoPropertyMeta("chassis_bundle_name", "chassisBundleName", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "chassis_bundle_version": MoPropertyMeta("chassis_bundle_version", "chassisBundleVersion", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "force_deploy": MoPropertyMeta("force_deploy", "forceDeploy", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["one-shot", "staged"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "override_default_exclusion": MoPropertyMeta("override_default_exclusion", "overrideDefaultExclusion", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["false", "no", "true", "yes"], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "service_pack_bundle_name": MoPropertyMeta("service_pack_bundle_name", "servicePackBundleName", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "service_pack_bundle_version": MoPropertyMeta("service_pack_bundle_version", "servicePackBundleVersion", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x800, 0, 510, None, [], []),
        "stage_size": MoPropertyMeta("stage_size", "stageSize", "ushort", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "update_trigger": MoPropertyMeta("update_trigger", "updateTrigger", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["immediate"], []),
    }

    prop_map = {
        "chassisBundleName": "chassis_bundle_name", 
        "chassisBundleVersion": "chassis_bundle_version", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "forceDeploy": "force_deploy", 
        "intId": "int_id", 
        "mode": "mode", 
        "name": "name", 
        "overrideDefaultExclusion": "override_default_exclusion", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
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
        self.chassis_bundle_name = None
        self.chassis_bundle_version = None
        self.child_action = None
        self.descr = None
        self.force_deploy = None
        self.int_id = None
        self.mode = None
        self.override_default_exclusion = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.service_pack_bundle_name = None
        self.service_pack_bundle_version = None
        self.stage_size = None
        self.status = None
        self.update_trigger = None

        ManagedObject.__init__(self, "FirmwareChassisPack", parent_mo_or_dn, **kwargs)
