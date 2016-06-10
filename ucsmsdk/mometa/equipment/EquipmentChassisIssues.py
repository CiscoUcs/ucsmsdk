"""This module contains the general information for EquipmentChassisIssues ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentChassisIssuesConsts:
    pass


class EquipmentChassisIssues(ManagedObject):
    """This is EquipmentChassisIssues class."""

    consts = EquipmentChassisIssuesConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentChassisIssues", "equipmentChassisIssues", "config-issue", VersionMeta.Version911z, "InputOutput", 0x1f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], [u'equipmentChassisProfile'], [u'faultInst'], [None])

    prop_meta = {
        "chassis_config_issues": MoPropertyMeta("chassis_config_issues", "chassisConfigIssues", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|chassis-profile-not-supported|migration|non-interrupt-fsm-running|insufficient-resources|physical-requirement|chassis-undiscovered|resource-ownership-conflict|chassis-unavailable|invalid-chassis-pack|missing-firmware-image|insufficient-power-budget),){0,12}(defaultValue|not-applicable|chassis-profile-not-supported|migration|non-interrupt-fsm-running|insufficient-resources|physical-requirement|chassis-undiscovered|resource-ownership-conflict|chassis-unavailable|invalid-chassis-pack|missing-firmware-image|insufficient-power-budget){0,1}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version911z, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_warnings": MoPropertyMeta("config_warnings", "configWarnings", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable),){0,1}(defaultValue|not-applicable){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version911z, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "storage_config_issues": MoPropertyMeta("storage_config_issues", "storageConfigIssues", "string", VersionMeta.Version911z, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|flexflash-metadata|unsupported-disk-controller-config|unsupported-expand-to-available|unsupported-use-remaining-disks|unsupported-strip-size-change|zone-capacity|duplicated-lun-name|unsupported-hotspare-change|unsupported-vd-modification|invalid-disk-slot-ownership|disk-role-mismatch|missing-raid-key|orphaned-lun-ref-missing|virtual-drive-access-denied|unsupported-disk-slot-zoning|destructive-local-disk-config|storage-feature-capability-mismatch|insufficient-disks|conflicting-lun-config|unsupported-global-hotspares|drive-cache-not-supported|unsupported-chassis-disk-zoning|flexflash-controller|unsupported-controller|invalid-storage-profile-binding|lun-in-use|disk-sharing-not-supported|incompatible-disk-types|storage-path-configuration-error|disk-type-mismatch|orphaned-lun-ref-access-denied|virtual-drive-deletion-in-progress|unsupported-partial-disk-group-zoning|virtual-drive-hidden-or-transport-ready|unsupported-raid-level|incomplete-lun-config|unsupported-order|embedded-controller-not-supported|unsupported-io-policy|incompatible-number-of-local-disks|flexflash-card|unsupported-destructive-change|invalid-local-lun-disk-policy-reference|set-proper-order|unsupported-chassis-spare-controller|wwnn-assignment|unsupported-orphan-lun-modification|unsupported-lun-map-modification|unsupported-write-cache-policy|invalid-zoning-virtual-drive-state|insufficient-storage-space|order-should-be-unique|virtual-drive-capacity|incompatible-raid-level|invalid-dzp-reference),){0,56}(defaultValue|not-applicable|flexflash-metadata|unsupported-disk-controller-config|unsupported-expand-to-available|unsupported-use-remaining-disks|unsupported-strip-size-change|zone-capacity|duplicated-lun-name|unsupported-hotspare-change|unsupported-vd-modification|invalid-disk-slot-ownership|disk-role-mismatch|missing-raid-key|orphaned-lun-ref-missing|virtual-drive-access-denied|unsupported-disk-slot-zoning|destructive-local-disk-config|storage-feature-capability-mismatch|insufficient-disks|conflicting-lun-config|unsupported-global-hotspares|drive-cache-not-supported|unsupported-chassis-disk-zoning|flexflash-controller|unsupported-controller|invalid-storage-profile-binding|lun-in-use|disk-sharing-not-supported|incompatible-disk-types|storage-path-configuration-error|disk-type-mismatch|orphaned-lun-ref-access-denied|virtual-drive-deletion-in-progress|unsupported-partial-disk-group-zoning|virtual-drive-hidden-or-transport-ready|unsupported-raid-level|incomplete-lun-config|unsupported-order|embedded-controller-not-supported|unsupported-io-policy|incompatible-number-of-local-disks|flexflash-card|unsupported-destructive-change|invalid-local-lun-disk-policy-reference|set-proper-order|unsupported-chassis-spare-controller|wwnn-assignment|unsupported-orphan-lun-modification|unsupported-lun-map-modification|unsupported-write-cache-policy|invalid-zoning-virtual-drive-state|insufficient-storage-space|order-should-be-unique|virtual-drive-capacity|incompatible-raid-level|invalid-dzp-reference){0,1}""", [], []), 
    }

    prop_map = {
        "chassisConfigIssues": "chassis_config_issues", 
        "childAction": "child_action", 
        "configWarnings": "config_warnings", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "storageConfigIssues": "storage_config_issues", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.chassis_config_issues = None
        self.child_action = None
        self.config_warnings = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.storage_config_issues = None

        ManagedObject.__init__(self, "EquipmentChassisIssues", parent_mo_or_dn, **kwargs)
