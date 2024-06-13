"""This module contains the general information for VnicIPv4If ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicIPv4IfConsts:
    OPER_STATE_DOWN = "down"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_INDETERMINATE = "indeterminate"
    OPER_STATE_UP = "up"
    OWNER_CONN_POLICY = "conn_policy"
    OWNER_INITIATOR_POLICY = "initiator_policy"
    OWNER_LOGICAL = "logical"
    OWNER_PHYSICAL = "physical"
    OWNER_POLICY = "policy"
    OWNER_UNKNOWN = "unknown"
    SHARING_COMMUNITY = "community"
    SHARING_ISOLATED = "isolated"
    SHARING_NONE = "none"
    SHARING_PRIMARY = "primary"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    TYPE_ETHER = "ether"
    TYPE_FC = "fc"
    TYPE_IPC = "ipc"
    TYPE_SCSI = "scsi"
    TYPE_UNKNOWN = "unknown"


class VnicIPv4If(ManagedObject):
    """This is VnicIPv4If class."""

    consts = VnicIPv4IfConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicIPv4If", "vnicIPv4If", "ipv4", VersionMeta.Version101e, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server", "ls-storage"], ['vnicEtherIf', 'vnicIScsiBootVnic', 'vnicVlan'], ['fabricMonOriginIP', 'fabricNetflowIPv4Addr', 'vnicIPv4Dhcp', 'vnicIPv4Dns', 'vnicIPv4IscsiAddr', 'vnicIPv4PooledIscsiAddr', 'vnicIPv4StaticRoute', 'vnicIpV4MgmtPooledAddr', 'vnicIpV4PooledAddr', 'vnicIpV4ProfDerivedAddr', 'vnicIpV4StaticAddr'], ["Add", "Get"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|unsupported-azurestackqos-geneve|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unsupported-adaptor-for-vnic-cdn|misconfigured-net-san-group|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|redundancy-vnicpair-not-in-sync|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|unsupported-roce-properties|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|duplicate-vnic-cdn-name|overlapping-vlans|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|unsupported-adaptor-for-vnic-oracle-rac|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unsupported-geneve-vmq-vmmq-arfs-roce-advfilters|soft-pinning-vlan-mismatch|unsupported-roce-sriov-vxlan|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|insufficient-roce-resources|unsupported-azurestackqos-vmmq-geneve-advfilters|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unsupported-roce-nvgre|unresolved-net-san-group|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-nvgre-vxlan-vmq|redundancy-vnic-not-in-pair|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig|unsupported-vmq-resources),){0,65}(defaultValue|not-applicable|unsupported-azurestackqos-geneve|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unsupported-adaptor-for-vnic-cdn|misconfigured-net-san-group|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|redundancy-vnicpair-not-in-sync|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|unsupported-roce-properties|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|duplicate-vnic-cdn-name|overlapping-vlans|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|unsupported-adaptor-for-vnic-oracle-rac|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unsupported-geneve-vmq-vmmq-arfs-roce-advfilters|soft-pinning-vlan-mismatch|unsupported-roce-sriov-vxlan|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|insufficient-roce-resources|unsupported-azurestackqos-vmmq-geneve-advfilters|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unsupported-roce-nvgre|unresolved-net-san-group|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-nvgre-vxlan-vmq|redundancy-vnic-not-in-pair|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig|unsupported-vmq-resources){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_primary_vnet_dn": MoPropertyMeta("oper_primary_vnet_dn", "operPrimaryVnetDn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_primary_vnet_name": MoPropertyMeta("oper_primary_vnet_name", "operPrimaryVnetName", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["down", "failed", "indeterminate", "up"], []),
        "oper_vnet_dn": MoPropertyMeta("oper_vnet_dn", "operVnetDn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_vnet_name": MoPropertyMeta("oper_vnet_name", "operVnetName", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conn_policy", "initiator_policy", "logical", "physical", "policy", "unknown"], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pub_nw_id": MoPropertyMeta("pub_nw_id", "pubNwId", "uint", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "sharing": MoPropertyMeta("sharing", "sharing", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["community", "isolated", "none", "primary"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ether", "fc", "ipc", "scsi", "unknown"], []),
        "vnet": MoPropertyMeta("vnet", "vnet", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4093"]),
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "dn": "dn", 
        "name": "name", 
        "operPrimaryVnetDn": "oper_primary_vnet_dn", 
        "operPrimaryVnetName": "oper_primary_vnet_name", 
        "operState": "oper_state", 
        "operVnetDn": "oper_vnet_dn", 
        "operVnetName": "oper_vnet_name", 
        "owner": "owner", 
        "propAcl": "prop_acl", 
        "pubNwId": "pub_nw_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sharing": "sharing", 
        "status": "status", 
        "switchId": "switch_id", 
        "type": "type", 
        "vnet": "vnet", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.addr = None
        self.child_action = None
        self.config_qualifier = None
        self.name = None
        self.oper_primary_vnet_dn = None
        self.oper_primary_vnet_name = None
        self.oper_state = None
        self.oper_vnet_dn = None
        self.oper_vnet_name = None
        self.owner = None
        self.prop_acl = None
        self.pub_nw_id = None
        self.sacl = None
        self.sharing = None
        self.status = None
        self.switch_id = None
        self.type = None
        self.vnet = None

        ManagedObject.__init__(self, "VnicIPv4If", parent_mo_or_dn, **kwargs)
