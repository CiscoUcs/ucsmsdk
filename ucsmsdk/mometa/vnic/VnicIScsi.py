"""This module contains the general information for VnicIScsi ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicIScsiConsts:
    ADDR_DERIVED = "derived"
    ADMIN_HOST_PORT_1 = "1"
    ADMIN_HOST_PORT_2 = "2"
    ADMIN_HOST_PORT_ANY = "ANY"
    ADMIN_HOST_PORT_NONE = "NONE"
    ADMIN_VCON_1 = "1"
    ADMIN_VCON_2 = "2"
    ADMIN_VCON_3 = "3"
    ADMIN_VCON_4 = "4"
    ADMIN_VCON_ANY = "any"
    BOOT_DEV_DISABLED = "disabled"
    BOOT_DEV_ENABLED = "enabled"
    CDN_PROP_IN_SYNC_FALSE = "false"
    CDN_PROP_IN_SYNC_NO = "no"
    CDN_PROP_IN_SYNC_TRUE = "true"
    CDN_PROP_IN_SYNC_YES = "yes"
    CDN_SOURCE_USER_DEFINED = "user-defined"
    CDN_SOURCE_VNIC_NAME = "vnic-name"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_FAILED_TO_APPLY = "failed-to-apply"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    EXT_IPSTATE_NONE = "none"
    EXT_IPSTATE_POOLED = "pooled"
    EXT_IPSTATE_STATIC = "static"
    INST_TYPE_DEFAULT = "default"
    INST_TYPE_DYNAMIC = "dynamic"
    INST_TYPE_DYNAMIC_VF = "dynamic-vf"
    INST_TYPE_MANUAL = "manual"
    OPER_HOST_PORT_1 = "1"
    OPER_HOST_PORT_2 = "2"
    OPER_HOST_PORT_ANY = "ANY"
    OPER_HOST_PORT_NONE = "NONE"
    OPER_ORDER_UNSPECIFIED = "unspecified"
    OPER_SPEED_LINE_RATE = "line-rate"
    OPER_VCON_1 = "1"
    OPER_VCON_2 = "2"
    OPER_VCON_3 = "3"
    OPER_VCON_4 = "4"
    OPER_VCON_ANY = "any"
    ORDER_UNSPECIFIED = "unspecified"
    OWNER_CONN_POLICY = "conn_policy"
    OWNER_INITIATOR_POLICY = "initiator_policy"
    OWNER_LOGICAL = "logical"
    OWNER_PHYSICAL = "physical"
    OWNER_POLICY = "policy"
    OWNER_UNKNOWN = "unknown"
    REDUNDANCY_PAIR_TYPE_NONE = "none"
    REDUNDANCY_PAIR_TYPE_PRIMARY = "primary"
    REDUNDANCY_PAIR_TYPE_SECONDARY = "secondary"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    TYPE_ETHER = "ether"
    TYPE_FC = "fc"
    TYPE_IPC = "ipc"
    TYPE_SCSI = "scsi"
    TYPE_UNKNOWN = "unknown"
    VNIC_DEF_TYPE_DYNAMIC_NW = "dynamic-nw"
    VNIC_DEF_TYPE_OPTION17 = "option17"
    VNIC_DEF_TYPE_OPTION43 = "option43"
    VNIC_DEF_TYPE_STATIC = "static"


class VnicIScsi(ManagedObject):
    """This is VnicIScsi class."""

    consts = VnicIScsiConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("VnicIScsi", "vnicIScsi", "iscsi-[name]", VersionMeta.Version201m, "InputOutput", 0x1ffffff, [], ["admin", "ls-config", "ls-network", "ls-server", "ls-storage"], ['lsServer'], ['fabricEthMonSrcEp', 'fabricFcMonSrcEp', 'fabricNetflowMonSrcEp', 'faultInst', 'vnicIPv4IscsiAddr', 'vnicIScsiAutoTargetIf', 'vnicIScsiStaticTargetIf', 'vnicIqnHistory', 'vnicMacHistory', 'vnicVlan'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "adaptor_profile_name": MoPropertyMeta("adaptor_profile_name", "adaptorProfileName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", ["derived"], []),
        "admin_cdn_name": MoPropertyMeta("admin_cdn_name", "adminCdnName", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "admin_host_port": MoPropertyMeta("admin_host_port", "adminHostPort", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1", "2", "ANY", "NONE"], []),
        "admin_vcon": MoPropertyMeta("admin_vcon", "adminVcon", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["1", "2", "3", "4", "any"], []),
        "auth_profile_name": MoPropertyMeta("auth_profile_name", "authProfileName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []),
        "boot_dev": MoPropertyMeta("boot_dev", "bootDev", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []),
        "cdn_prop_in_sync": MoPropertyMeta("cdn_prop_in_sync", "cdnPropInSync", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["false", "no", "true", "yes"], []),
        "cdn_source": MoPropertyMeta("cdn_source", "cdnSource", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["user-defined", "vnic-name"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x200, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|unsupported-azurestackqos-geneve|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unsupported-adaptor-for-vnic-cdn|misconfigured-net-san-group|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|redundancy-vnicpair-not-in-sync|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|unsupported-roce-properties|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|duplicate-vnic-cdn-name|overlapping-vlans|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|unsupported-adaptor-for-vnic-oracle-rac|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unsupported-geneve-vmq-vmmq-arfs-roce-advfilters|soft-pinning-vlan-mismatch|unsupported-roce-sriov-vxlan|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|insufficient-roce-resources|unsupported-azurestackqos-vmmq-geneve-advfilters|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unsupported-roce-nvgre|unresolved-net-san-group|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-nvgre-vxlan-vmq|redundancy-vnic-not-in-pair|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig|unsupported-vmq-resources),){0,65}(defaultValue|not-applicable|unsupported-azurestackqos-geneve|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unsupported-adaptor-for-vnic-cdn|misconfigured-net-san-group|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|redundancy-vnicpair-not-in-sync|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|unsupported-roce-properties|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|duplicate-vnic-cdn-name|overlapping-vlans|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|unsupported-adaptor-for-vnic-oracle-rac|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unsupported-geneve-vmq-vmmq-arfs-roce-advfilters|soft-pinning-vlan-mismatch|unsupported-roce-sriov-vxlan|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|insufficient-roce-resources|unsupported-azurestackqos-vmmq-geneve-advfilters|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unsupported-roce-nvgre|unresolved-net-san-group|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-nvgre-vxlan-vmq|redundancy-vnic-not-in-pair|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig|unsupported-vmq-resources){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "applying", "failed-to-apply", "not-applied"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []),
        "equipment_dn": MoPropertyMeta("equipment_dn", "equipmentDn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "eth_ep_dn": MoPropertyMeta("eth_ep_dn", "ethEpDn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "ext_ip_state": MoPropertyMeta("ext_ip_state", "extIPState", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["none", "pooled", "static"], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "ident_pool_name": MoPropertyMeta("ident_pool_name", "identPoolName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], []),
        "init_name_suffix": MoPropertyMeta("init_name_suffix", "initNameSuffix", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "initiator_name": MoPropertyMeta("initiator_name", "initiatorName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""[0-9a-zA-Z\.:-]{0,223}""", [], []),
        "inst_type": MoPropertyMeta("inst_type", "instType", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["default", "dynamic", "dynamic-vf", "manual"], []),
        "iqn_ident_pool_name": MoPropertyMeta("iqn_ident_pool_name", "iqnIdentPoolName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x8000, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "nw_templ_name": MoPropertyMeta("nw_templ_name", "nwTemplName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x10000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_adaptor_profile_name": MoPropertyMeta("oper_adaptor_profile_name", "operAdaptorProfileName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_auth_profile_name": MoPropertyMeta("oper_auth_profile_name", "operAuthProfileName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_cdn_name": MoPropertyMeta("oper_cdn_name", "operCdnName", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "oper_host_port": MoPropertyMeta("oper_host_port", "operHostPort", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "ANY", "NONE"], []),
        "oper_ident_pool_name": MoPropertyMeta("oper_ident_pool_name", "operIdentPoolName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_iqn_ident_pool_name": MoPropertyMeta("oper_iqn_ident_pool_name", "operIqnIdentPoolName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_order": MoPropertyMeta("oper_order", "operOrder", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-65535"]),
        "oper_speed": MoPropertyMeta("oper_speed", "operSpeed", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["line-rate"], ["8-100000000"]),
        "oper_stats_policy_name": MoPropertyMeta("oper_stats_policy_name", "operStatsPolicyName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "oper_vcon": MoPropertyMeta("oper_vcon", "operVcon", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "3", "4", "any"], []),
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, ["unspecified"], ["0-256"]),
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conn_policy", "initiator_policy", "logical", "physical", "policy", "unknown"], []),
        "pin_to_group_name": MoPropertyMeta("pin_to_group_name", "pinToGroupName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x40000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "qos_policy_name": MoPropertyMeta("qos_policy_name", "qosPolicyName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x80000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "redundancy_pair_type": MoPropertyMeta("redundancy_pair_type", "redundancyPairType", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none", "primary", "secondary"], []),
        "redundancy_peer": MoPropertyMeta("redundancy_peer", "redundancyPeer", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x100000, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "stats_policy_name": MoPropertyMeta("stats_policy_name", "statsPolicyName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x200000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x400000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x800000, None, None, None, ["A", "B", "NONE"], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ether", "fc", "ipc", "scsi", "unknown"], []),
        "vnic_def_type": MoPropertyMeta("vnic_def_type", "vnicDefType", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["dynamic-nw", "option17", "option43", "static"], []),
        "vnic_name": MoPropertyMeta("vnic_name", "vnicName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x1000000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
    }

    prop_map = {
        "adaptorProfileName": "adaptor_profile_name", 
        "addr": "addr", 
        "adminCdnName": "admin_cdn_name", 
        "adminHostPort": "admin_host_port", 
        "adminVcon": "admin_vcon", 
        "authProfileName": "auth_profile_name", 
        "bootDev": "boot_dev", 
        "cdnPropInSync": "cdn_prop_in_sync", 
        "cdnSource": "cdn_source", 
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "configState": "config_state", 
        "dn": "dn", 
        "equipmentDn": "equipment_dn", 
        "ethEpDn": "eth_ep_dn", 
        "extIPState": "ext_ip_state", 
        "fltAggr": "flt_aggr", 
        "identPoolName": "ident_pool_name", 
        "initNameSuffix": "init_name_suffix", 
        "initiatorName": "initiator_name", 
        "instType": "inst_type", 
        "iqnIdentPoolName": "iqn_ident_pool_name", 
        "name": "name", 
        "nwTemplName": "nw_templ_name", 
        "operAdaptorProfileName": "oper_adaptor_profile_name", 
        "operAuthProfileName": "oper_auth_profile_name", 
        "operCdnName": "oper_cdn_name", 
        "operHostPort": "oper_host_port", 
        "operIdentPoolName": "oper_ident_pool_name", 
        "operIqnIdentPoolName": "oper_iqn_ident_pool_name", 
        "operOrder": "oper_order", 
        "operSpeed": "oper_speed", 
        "operStatsPolicyName": "oper_stats_policy_name", 
        "operVcon": "oper_vcon", 
        "order": "order", 
        "owner": "owner", 
        "pinToGroupName": "pin_to_group_name", 
        "propAcl": "prop_acl", 
        "qosPolicyName": "qos_policy_name", 
        "redundancyPairType": "redundancy_pair_type", 
        "redundancyPeer": "redundancy_peer", 
        "rn": "rn", 
        "sacl": "sacl", 
        "statsPolicyName": "stats_policy_name", 
        "status": "status", 
        "switchId": "switch_id", 
        "type": "type", 
        "vnicDefType": "vnic_def_type", 
        "vnicName": "vnic_name", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.adaptor_profile_name = None
        self.addr = None
        self.admin_cdn_name = None
        self.admin_host_port = None
        self.admin_vcon = None
        self.auth_profile_name = None
        self.boot_dev = None
        self.cdn_prop_in_sync = None
        self.cdn_source = None
        self.child_action = None
        self.config_qualifier = None
        self.config_state = None
        self.equipment_dn = None
        self.eth_ep_dn = None
        self.ext_ip_state = None
        self.flt_aggr = None
        self.ident_pool_name = None
        self.init_name_suffix = None
        self.initiator_name = None
        self.inst_type = None
        self.iqn_ident_pool_name = None
        self.nw_templ_name = None
        self.oper_adaptor_profile_name = None
        self.oper_auth_profile_name = None
        self.oper_cdn_name = None
        self.oper_host_port = None
        self.oper_ident_pool_name = None
        self.oper_iqn_ident_pool_name = None
        self.oper_order = None
        self.oper_speed = None
        self.oper_stats_policy_name = None
        self.oper_vcon = None
        self.order = None
        self.owner = None
        self.pin_to_group_name = None
        self.prop_acl = None
        self.qos_policy_name = None
        self.redundancy_pair_type = None
        self.redundancy_peer = None
        self.sacl = None
        self.stats_policy_name = None
        self.status = None
        self.switch_id = None
        self.type = None
        self.vnic_def_type = None
        self.vnic_name = None

        ManagedObject.__init__(self, "VnicIScsi", parent_mo_or_dn, **kwargs)
