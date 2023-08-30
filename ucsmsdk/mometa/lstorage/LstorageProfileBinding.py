"""This module contains the general information for LstorageProfileBinding ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LstorageProfileBindingConsts:
    pass


class LstorageProfileBinding(ManagedObject):
    """This is LstorageProfileBinding class."""

    consts = LstorageProfileBindingConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageProfileBinding", "lstorageProfileBinding", "profile-binding", VersionMeta.Version224b, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-storage", "ls-storage-policy"], ['lsServer'], ['faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "issues": MoPropertyMeta("issues", "issues", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|boot-order-pxe|wwnn-derivation-from-vhba|migration|incompat-bios-for-sriov-vnics|iscsi-initiator-ip-address|remote-policy|wwnn-assignment|processor-requirement|physical-requirement|hostimg-policy-invalid|vif-resources-overprovisioned|pinning-invalid|incompatible-number-of-local-disks|mac-derivation-virtualized-port|switch-virtual-if-capacity|invalid-wwn|missing-raid-key|board-controller-update-unsupported|insufficient-resources|compute-undiscovered|boot-configuration-invalid|incompatible-bios-image|iscsi-config|storage-path-configuration-error|resource-ownership-conflict|system-uuid-assignment|server-position-requirement|destructive-local-disk-config|imgsec-policy-invalid|pinning-vlan-mismatch|non-interrupt-fsm-running|vnic-capacity|adaptor-requirement|mac-address-assignment|qos-policy-invalid|insufficient-power-budget|boot-order-iscsi|vnic-vcon-provisioning-change|adaptor-protected-eth-capability|connection-placement|incompatible-disk-types|vnic-not-ha-ready|zone-capacity|adaptor-out-of-vifs|duplicate-address-conflict|sb-adaptor-backup-version-unsupported|vhba-capacity|boot-order-san-image-path|compute-unavailable|power-group-requirement|provsrv-policy-invalid|vnic-vlan-assignment-error|missing-firmware-image|wwpn-assignment|memory-requirement|vlan-port-capacity|bootip-policy-invalid|vfc-vnic-pvlan-conflict|named-vlan-inaccessible|adaptor-fcoe-capability|wwpn-derivation-virtualized-port|incompatible-raid-level|missing-primary-vlan|fcoe-capacity|dynamic-vf-vnic),){0,66}(defaultValue|not-applicable|boot-order-pxe|wwnn-derivation-from-vhba|migration|incompat-bios-for-sriov-vnics|iscsi-initiator-ip-address|remote-policy|wwnn-assignment|processor-requirement|physical-requirement|hostimg-policy-invalid|vif-resources-overprovisioned|pinning-invalid|incompatible-number-of-local-disks|mac-derivation-virtualized-port|switch-virtual-if-capacity|invalid-wwn|missing-raid-key|board-controller-update-unsupported|insufficient-resources|compute-undiscovered|boot-configuration-invalid|incompatible-bios-image|iscsi-config|storage-path-configuration-error|resource-ownership-conflict|system-uuid-assignment|server-position-requirement|destructive-local-disk-config|imgsec-policy-invalid|pinning-vlan-mismatch|non-interrupt-fsm-running|vnic-capacity|adaptor-requirement|mac-address-assignment|qos-policy-invalid|insufficient-power-budget|boot-order-iscsi|vnic-vcon-provisioning-change|adaptor-protected-eth-capability|connection-placement|incompatible-disk-types|vnic-not-ha-ready|zone-capacity|adaptor-out-of-vifs|duplicate-address-conflict|sb-adaptor-backup-version-unsupported|vhba-capacity|boot-order-san-image-path|compute-unavailable|power-group-requirement|provsrv-policy-invalid|vnic-vlan-assignment-error|missing-firmware-image|wwpn-assignment|memory-requirement|vlan-port-capacity|bootip-policy-invalid|vfc-vnic-pvlan-conflict|named-vlan-inaccessible|adaptor-fcoe-capability|wwpn-derivation-virtualized-port|incompatible-raid-level|missing-primary-vlan|fcoe-capacity|dynamic-vf-vnic){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_storage_profile_name": MoPropertyMeta("oper_storage_profile_name", "operStorageProfileName", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "storage_profile_name": MoPropertyMeta("storage_profile_name", "storageProfileName", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
    }

    prop_map = {
        "assignedToDn": "assigned_to_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "issues": "issues", 
        "name": "name", 
        "operStorageProfileName": "oper_storage_profile_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "storageProfileName": "storage_profile_name", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.assigned_to_dn = None
        self.child_action = None
        self.issues = None
        self.name = None
        self.oper_storage_profile_name = None
        self.sacl = None
        self.status = None
        self.storage_profile_name = None

        ManagedObject.__init__(self, "LstorageProfileBinding", parent_mo_or_dn, **kwargs)
