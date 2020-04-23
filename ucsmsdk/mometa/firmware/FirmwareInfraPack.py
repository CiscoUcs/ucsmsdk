"""This module contains the general information for FirmwareInfraPack ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareInfraPackConsts:
    EVACUATE_FALSE = "false"
    EVACUATE_NO = "no"
    EVACUATE_TRUE = "true"
    EVACUATE_YES = "yes"
    FORCE_DEPLOY_FALSE = "false"
    FORCE_DEPLOY_NO = "no"
    FORCE_DEPLOY_TRUE = "true"
    FORCE_DEPLOY_YES = "yes"
    INT_ID_NONE = "none"
    MODE_ONE_SHOT = "one-shot"
    MODE_STAGED = "staged"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SKIP_VALIDATION_FALSE = "false"
    SKIP_VALIDATION_NO = "no"
    SKIP_VALIDATION_TRUE = "true"
    SKIP_VALIDATION_YES = "yes"
    UPDATE_TRIGGER_IMMEDIATE = "immediate"


class FirmwareInfraPack(ManagedObject):
    """This is FirmwareInfraPack class."""

    consts = FirmwareInfraPackConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FirmwareInfraPack", "firmwareInfraPack", "fw-infra-pack-[name]", VersionMeta.Version211a, "InputOutput", 0x7fff, [], ["admin"], ['orgOrg'], ['firmwareBackupVersionHolder', 'firmwarePackItem'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "evacuate": MoPropertyMeta("evacuate", "evacuate", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []),
        "force_deploy": MoPropertyMeta("force_deploy", "forceDeploy", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []),
        "infra_bundle_name": MoPropertyMeta("infra_bundle_name", "infraBundleName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "infra_bundle_version": MoPropertyMeta("infra_bundle_version", "infraBundleVersion", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], []),
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["one-shot", "staged"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["local", "pending-policy", "policy"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "service_pack_bundle_name": MoPropertyMeta("service_pack_bundle_name", "servicePackBundleName", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "service_pack_bundle_version": MoPropertyMeta("service_pack_bundle_version", "servicePackBundleVersion", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x800, 0, 510, None, [], []),
        "skip_validation": MoPropertyMeta("skip_validation", "skipValidation", "string", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "stage_size": MoPropertyMeta("stage_size", "stageSize", "ushort", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "update_trigger": MoPropertyMeta("update_trigger", "updateTrigger", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["immediate"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "evacuate": "evacuate", 
        "forceDeploy": "force_deploy", 
        "infraBundleName": "infra_bundle_name", 
        "infraBundleVersion": "infra_bundle_version", 
        "intId": "int_id", 
        "mode": "mode", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "servicePackBundleName": "service_pack_bundle_name", 
        "servicePackBundleVersion": "service_pack_bundle_version", 
        "skipValidation": "skip_validation", 
        "stageSize": "stage_size", 
        "status": "status", 
        "updateTrigger": "update_trigger", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.evacuate = None
        self.force_deploy = None
        self.infra_bundle_name = None
        self.infra_bundle_version = None
        self.int_id = None
        self.mode = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.service_pack_bundle_name = None
        self.service_pack_bundle_version = None
        self.skip_validation = None
        self.stage_size = None
        self.status = None
        self.update_trigger = None

        ManagedObject.__init__(self, "FirmwareInfraPack", parent_mo_or_dn, **kwargs)
