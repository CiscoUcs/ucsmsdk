"""This module contains the general information for EquipmentRequirement ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentRequirementConsts:
    OPER_STATE_FAILED_TO_APPLY = "failed-to-apply"
    OPER_STATE_UNUSED = "unused"
    OPER_STATE_USED = "used"
    RESTRICT_MIGRATION_FALSE = "false"
    RESTRICT_MIGRATION_NO = "no"
    RESTRICT_MIGRATION_TRUE = "true"
    RESTRICT_MIGRATION_YES = "yes"


class EquipmentRequirement(ManagedObject):
    """This is EquipmentRequirement class."""

    consts = EquipmentRequirementConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentRequirement", "equipmentRequirement", "chassis-req", VersionMeta.Version312b, "InputOutput", 0xff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy", "read-only"], ['equipmentChassisProfile'], ['faultInst'], [None])

    prop_meta = {
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "chassis_dn": MoPropertyMeta("chassis_dn", "chassisDn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "chassis_pool_dn": MoPropertyMeta("chassis_pool_dn", "chassisPoolDn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "issues": MoPropertyMeta("issues", "issues", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|chassis-profile-not-supported|single-path-not-supported|invalid-cmc-version|migration|single-path-unsupported-cmc-version|single-path-operation-not-supported|firmware-version-mismatch|invalid-sas-exp-config-policy-reference|non-interrupt-fsm-running|insufficient-resources|compute-conn-invalid-hw-config|connection-management-unsupported-cmc-version|physical-requirement|single-path-expander-inoperable|connection-management-feature-not-supported|chassis-undiscovered|chassis-feature-capability-mismatch|resource-ownership-conflict|unsupported-sas-exp-config-settings|compute-conn-unsupported-cmc-version|connection-management-expander-inoperable|chassis-unavailable|invalid-chassis-pack|single-path-invalid-configuration|connection-management-operation-not-supported|missing-firmware-image|chassis-feature-capability-mismatch-non-fatal|single-path-feature-not-supported|compute-second-controller-unsupported-cmc-version|connection-management-not-supported|insufficient-power-budget),){0,32}(defaultValue|not-applicable|chassis-profile-not-supported|single-path-not-supported|invalid-cmc-version|migration|single-path-unsupported-cmc-version|single-path-operation-not-supported|firmware-version-mismatch|invalid-sas-exp-config-policy-reference|non-interrupt-fsm-running|insufficient-resources|compute-conn-invalid-hw-config|connection-management-unsupported-cmc-version|physical-requirement|single-path-expander-inoperable|connection-management-feature-not-supported|chassis-undiscovered|chassis-feature-capability-mismatch|resource-ownership-conflict|unsupported-sas-exp-config-settings|compute-conn-unsupported-cmc-version|connection-management-expander-inoperable|chassis-unavailable|invalid-chassis-pack|single-path-invalid-configuration|connection-management-operation-not-supported|missing-firmware-image|chassis-feature-capability-mismatch-non-fatal|single-path-feature-not-supported|compute-second-controller-unsupported-cmc-version|connection-management-not-supported|insufficient-power-budget){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,32}""", [], []),
        "oper_name": MoPropertyMeta("oper_name", "operName", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed-to-apply", "unused", "used"], []),
        "qualifier": MoPropertyMeta("qualifier", "qualifier", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "restrict_migration": MoPropertyMeta("restrict_migration", "restrictMigration", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "assignedToDn": "assigned_to_dn", 
        "chassisDn": "chassis_dn", 
        "chassisPoolDn": "chassis_pool_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "issues": "issues", 
        "name": "name", 
        "operName": "oper_name", 
        "operState": "oper_state", 
        "qualifier": "qualifier", 
        "restrictMigration": "restrict_migration", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.assigned_to_dn = None
        self.chassis_dn = None
        self.chassis_pool_dn = None
        self.child_action = None
        self.issues = None
        self.name = None
        self.oper_name = None
        self.oper_state = None
        self.qualifier = None
        self.restrict_migration = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentRequirement", parent_mo_or_dn, **kwargs)
