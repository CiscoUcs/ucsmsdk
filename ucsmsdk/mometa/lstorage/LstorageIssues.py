"""This module contains the general information for LstorageIssues ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageIssuesConsts():
    pass


class LstorageIssues(ManagedObject):
    """This is LstorageIssues class."""

    consts = LstorageIssuesConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageIssues", "lstorageIssues", "sa-config-issue", VersionMeta.Version302c, "InputOutput", 0x1fL, [], ["admin", "ls-storage"], [u'lstorageProcessor'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "network_config_issues": MoPropertyMeta("network_config_issues", "networkConfigIssues", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|invalid-config|invalid-iscsi-vlan|unsupported-vlan-capability|invalid-ip-address),){0,5}(defaultValue|not-applicable|invalid-config|invalid-iscsi-vlan|unsupported-vlan-capability|invalid-ip-address){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "server_config_issues": MoPropertyMeta("server_config_issues", "serverConfigIssues", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|invalid-dp-interface-switch-id|compute-inoperable|invalid-profile-references|invalid-config|invalid-iscsi-interface-switch-id|compute-degraded|processor-cardinality|invalid-number-of-iscsi-interfaces|missing-firmware-image|unsupported-storage-server|invalid-number-of-dp-interfaces|compute-unavailable|insufficient-resources|local-remote-policy-conflict),){0,15}(defaultValue|not-applicable|invalid-dp-interface-switch-id|compute-inoperable|invalid-profile-references|invalid-config|invalid-iscsi-interface-switch-id|compute-degraded|processor-cardinality|invalid-number-of-iscsi-interfaces|missing-firmware-image|unsupported-storage-server|invalid-number-of-dp-interfaces|compute-unavailable|insufficient-resources|local-remote-policy-conflict){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "storage_config_issues": MoPropertyMeta("storage_config_issues", "storageConfigIssues", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|invalid-config|missing-firmware-image|invalid-iqn-format),){0,4}(defaultValue|not-applicable|invalid-config|missing-firmware-image|invalid-iqn-format){0,1}""", [], []), 
        "vnic_config_issues": MoPropertyMeta("vnic_config_issues", "vnicConfigIssues", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-vxlan-vmq|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig),){0,50}(defaultValue|not-applicable|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-vxlan-vmq|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "networkConfigIssues": "network_config_issues", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serverConfigIssues": "server_config_issues", 
        "status": "status", 
        "storageConfigIssues": "storage_config_issues", 
        "vnicConfigIssues": "vnic_config_issues", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.network_config_issues = None
        self.sacl = None
        self.server_config_issues = None
        self.status = None
        self.storage_config_issues = None
        self.vnic_config_issues = None

        ManagedObject.__init__(self, "LstorageIssues", parent_mo_or_dn, **kwargs)

