"""This module contains the general information for ConfigImpact ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ConfigImpactConsts():
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_FAILED_TO_APPLY = "failed-to-apply"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    DEPLOYMENT_MODE_IMMEDIATE = "immediate"
    DEPLOYMENT_MODE_TIMER_AUTOMATIC = "timer-automatic"
    DEPLOYMENT_MODE_USER_ACK = "user-ack"
    REBOOT_REQUIRED_FALSE = "false"
    REBOOT_REQUIRED_NO = "no"
    REBOOT_REQUIRED_TRUE = "true"
    REBOOT_REQUIRED_YES = "yes"


class ConfigImpact(ManagedObject):
    """This is ConfigImpact class."""

    consts = ConfigImpactConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("ConfigImpact", "configImpact", "impact-[name]", VersionMeta.Version212a, "InputOutput", 0x3fL, [], ["read-only"], [u'configManagedEpImpactResponse'], [], [None])

    prop_meta = {
        "affected_obj": MoPropertyMeta("affected_obj", "affectedObj", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "affected_server": MoPropertyMeta("affected_server", "affectedServer", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "changes": MoPropertyMeta("changes", "changes", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|boot-order|server-assignment|operational-policies|storage-identity|server-identity|storage|networking|vnic-vhba-placement),){0,8}(defaultValue|boot-order|server-assignment|operational-policies|storage-identity|server-identity|storage|networking|vnic-vhba-placement){0,1}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version212a, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_issues": MoPropertyMeta("config_issues", "configIssues", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|boot-order-pxe|wwnn-derivation-from-vhba|migration|incompat-bios-for-sriov-vnics|iscsi-initiator-ip-address|remote-policy|wwnn-assignment|processor-requirement|physical-requirement|hostimg-policy-invalid|vif-resources-overprovisioned|pinning-invalid|incompatible-number-of-local-disks|mac-derivation-virtualized-port|switch-virtual-if-capacity|invalid-wwn|missing-raid-key|board-controller-update-unsupported|insufficient-resources|compute-undiscovered|boot-configuration-invalid|incompatible-bios-image|iscsi-config|storage-path-configuration-error|resource-ownership-conflict|system-uuid-assignment|server-position-requirement|destructive-local-disk-config|imgsec-policy-invalid|pinning-vlan-mismatch|non-interrupt-fsm-running|vnic-capacity|adaptor-requirement|mac-address-assignment|qos-policy-invalid|insufficient-power-budget|boot-order-iscsi|vnic-vcon-provisioning-change|adaptor-protected-eth-capability|connection-placement|incompatible-disk-types|vnic-not-ha-ready|zone-capacity|adaptor-out-of-vifs|duplicate-address-conflict|vhba-capacity|boot-order-san-image-path|compute-unavailable|power-group-requirement|provsrv-policy-invalid|vnic-vlan-assignment-error|missing-firmware-image|wwpn-assignment|memory-requirement|vlan-port-capacity|bootip-policy-invalid|vfc-vnic-pvlan-conflict|named-vlan-inaccessible|adaptor-fcoe-capability|wwpn-derivation-virtualized-port|incompatible-raid-level|missing-primary-vlan|fcoe-capacity|dynamic-vf-vnic),){0,65}(defaultValue|not-applicable|boot-order-pxe|wwnn-derivation-from-vhba|migration|incompat-bios-for-sriov-vnics|iscsi-initiator-ip-address|remote-policy|wwnn-assignment|processor-requirement|physical-requirement|hostimg-policy-invalid|vif-resources-overprovisioned|pinning-invalid|incompatible-number-of-local-disks|mac-derivation-virtualized-port|switch-virtual-if-capacity|invalid-wwn|missing-raid-key|board-controller-update-unsupported|insufficient-resources|compute-undiscovered|boot-configuration-invalid|incompatible-bios-image|iscsi-config|storage-path-configuration-error|resource-ownership-conflict|system-uuid-assignment|server-position-requirement|destructive-local-disk-config|imgsec-policy-invalid|pinning-vlan-mismatch|non-interrupt-fsm-running|vnic-capacity|adaptor-requirement|mac-address-assignment|qos-policy-invalid|insufficient-power-budget|boot-order-iscsi|vnic-vcon-provisioning-change|adaptor-protected-eth-capability|connection-placement|incompatible-disk-types|vnic-not-ha-ready|zone-capacity|adaptor-out-of-vifs|duplicate-address-conflict|vhba-capacity|boot-order-san-image-path|compute-unavailable|power-group-requirement|provsrv-policy-invalid|vnic-vlan-assignment-error|missing-firmware-image|wwpn-assignment|memory-requirement|vlan-port-capacity|bootip-policy-invalid|vfc-vnic-pvlan-conflict|named-vlan-inaccessible|adaptor-fcoe-capability|wwpn-derivation-virtualized-port|incompatible-raid-level|missing-primary-vlan|fcoe-capacity|dynamic-vf-vnic){0,1}""", [], []), 
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|boot-order-pxe|wwnn-derivation-from-vhba|migration|incompat-bios-for-sriov-vnics|iscsi-initiator-ip-address|remote-policy|wwnn-assignment|processor-requirement|physical-requirement|hostimg-policy-invalid|vif-resources-overprovisioned|pinning-invalid|incompatible-number-of-local-disks|mac-derivation-virtualized-port|switch-virtual-if-capacity|invalid-wwn|missing-raid-key|board-controller-update-unsupported|insufficient-resources|compute-undiscovered|boot-configuration-invalid|incompatible-bios-image|iscsi-config|storage-path-configuration-error|resource-ownership-conflict|system-uuid-assignment|server-position-requirement|destructive-local-disk-config|imgsec-policy-invalid|pinning-vlan-mismatch|non-interrupt-fsm-running|vnic-capacity|adaptor-requirement|mac-address-assignment|qos-policy-invalid|insufficient-power-budget|boot-order-iscsi|vnic-vcon-provisioning-change|adaptor-protected-eth-capability|connection-placement|incompatible-disk-types|vnic-not-ha-ready|zone-capacity|adaptor-out-of-vifs|duplicate-address-conflict|vhba-capacity|boot-order-san-image-path|compute-unavailable|power-group-requirement|provsrv-policy-invalid|vnic-vlan-assignment-error|missing-firmware-image|wwpn-assignment|memory-requirement|vlan-port-capacity|bootip-policy-invalid|vfc-vnic-pvlan-conflict|named-vlan-inaccessible|adaptor-fcoe-capability|wwpn-derivation-virtualized-port|incompatible-raid-level|missing-primary-vlan|fcoe-capacity|dynamic-vf-vnic),){0,65}(defaultValue|not-applicable|boot-order-pxe|wwnn-derivation-from-vhba|migration|incompat-bios-for-sriov-vnics|iscsi-initiator-ip-address|remote-policy|wwnn-assignment|processor-requirement|physical-requirement|hostimg-policy-invalid|vif-resources-overprovisioned|pinning-invalid|incompatible-number-of-local-disks|mac-derivation-virtualized-port|switch-virtual-if-capacity|invalid-wwn|missing-raid-key|board-controller-update-unsupported|insufficient-resources|compute-undiscovered|boot-configuration-invalid|incompatible-bios-image|iscsi-config|storage-path-configuration-error|resource-ownership-conflict|system-uuid-assignment|server-position-requirement|destructive-local-disk-config|imgsec-policy-invalid|pinning-vlan-mismatch|non-interrupt-fsm-running|vnic-capacity|adaptor-requirement|mac-address-assignment|qos-policy-invalid|insufficient-power-budget|boot-order-iscsi|vnic-vcon-provisioning-change|adaptor-protected-eth-capability|connection-placement|incompatible-disk-types|vnic-not-ha-ready|zone-capacity|adaptor-out-of-vifs|duplicate-address-conflict|vhba-capacity|boot-order-san-image-path|compute-unavailable|power-group-requirement|provsrv-policy-invalid|vnic-vlan-assignment-error|missing-firmware-image|wwpn-assignment|memory-requirement|vlan-port-capacity|bootip-policy-invalid|vfc-vnic-pvlan-conflict|named-vlan-inaccessible|adaptor-fcoe-capability|wwpn-derivation-virtualized-port|incompatible-raid-level|missing-primary-vlan|fcoe-capacity|dynamic-vf-vnic){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "applying", "failed-to-apply", "not-applied"], []), 
        "deployment_mode": MoPropertyMeta("deployment_mode", "deploymentMode", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["immediate", "timer-automatic", "user-ack"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version212a, MoPropertyMeta.NAMING, 0x8L, 1, 510, None, [], []), 
        "reboot_required": MoPropertyMeta("reboot_required", "rebootRequired", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "affectedObj": "affected_obj", 
        "affectedServer": "affected_server", 
        "changes": "changes", 
        "childAction": "child_action", 
        "configIssues": "config_issues", 
        "configQualifier": "config_qualifier", 
        "configState": "config_state", 
        "deploymentMode": "deployment_mode", 
        "dn": "dn", 
        "name": "name", 
        "rebootRequired": "reboot_required", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.affected_obj = None
        self.affected_server = None
        self.changes = None
        self.child_action = None
        self.config_issues = None
        self.config_qualifier = None
        self.config_state = None
        self.deployment_mode = None
        self.reboot_required = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ConfigImpact", parent_mo_or_dn, **kwargs)

