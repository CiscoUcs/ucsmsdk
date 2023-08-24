"""This module contains the general information for AdaptorCapSpec ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorCapSpecConsts:
    FW_VERSION_OPR_GT = "gt"
    FW_VERSION_OPR_LT = "lt"
    FW_VERSION_OPR_NONE = "none"
    FW_VERSION_OPR_RANGE = "range"
    MAXIMUM_UNSPECIFIED = "unspecified"
    RETIMER_SUPPORT_NO = "no"
    RETIMER_SUPPORT_YES = "yes"
    TYPE_CDN_SUPPORT = "cdn-support"
    TYPE_ETH_FLOW_MONITORING_NETFLOW = "eth-flow-monitoring-netflow"
    TYPE_ETH_NVGRE = "eth-nvgre"
    TYPE_ETH_NVGRE_ROCEV2 = "eth-nvgre-rocev2"
    TYPE_ETH_NVGRE_VMQ = "eth-nvgre-vmq"
    TYPE_ETH_PTP = "eth-ptp"
    TYPE_ETH_ROCE = "eth-roce"
    TYPE_ETH_ROCE_V2 = "eth-roce-v2"
    TYPE_ETH_VXLAN = "eth-vxlan"
    TYPE_ETH_VXLAN_ROCEV2 = "eth-vxlan-rocev2"
    TYPE_ETH_VXLAN_VMQ = "eth-vxlan-vmq"
    TYPE_FCOE = "fcoe"
    TYPE_NON_VIRTUALIZED_ETH_IF = "non-virtualized-eth-if"
    TYPE_NON_VIRTUALIZED_FC_IF = "non-virtualized-fc-if"
    TYPE_ORACLE_RAC_SUPPORT = "oracle-rac-support"
    TYPE_PATH_ENCAP_CONSOLIDATED = "path-encap-consolidated"
    TYPE_PATH_ENCAP_VIRTUAL = "path-encap-virtual"
    TYPE_PATH_ENCAP_VIRTUAL_CE = "path-encap-virtual-ce"
    TYPE_PROTECTED_ETH_IF = "protected-eth-if"
    TYPE_PROTECTED_FC_IF = "protected-fc-if"
    TYPE_PROTECTED_FCOE = "protected-fcoe"
    TYPE_PXEBOOT_CONFIG_SUPPORT = "pxeboot-config-support"
    TYPE_UPLINK_AGGREGATION = "uplink-aggregation"
    TYPE_VIRTUALIZED_CE_ETH_IF = "virtualized-ce-eth-if"
    TYPE_VIRTUALIZED_ETH_IF = "virtualized-eth-if"
    TYPE_VIRTUALIZED_ETH_SRIOV = "virtualized-eth-sriov"
    TYPE_VIRTUALIZED_ETH_SRIOV_USNIC = "virtualized-eth-sriov-usnic"
    TYPE_VIRTUALIZED_ETH_VMMQ = "virtualized-eth-vmmq"
    TYPE_VIRTUALIZED_ETH_VMQ = "virtualized-eth-vmq"
    TYPE_VIRTUALIZED_FC_IF = "virtualized-fc-if"
    TYPE_VIRTUALIZED_FC_SRIOV = "virtualized-fc-sriov"
    TYPE_VIRTUALIZED_SCSI_IF = "virtualized-scsi-if"


class AdaptorCapSpec(ManagedObject):
    """This is AdaptorCapSpec class."""

    consts = AdaptorCapSpecConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("AdaptorCapSpec", "adaptorCapSpec", "cap-[type]", VersionMeta.Version101e, "InputOutput", 0x3f, [], ["admin", "pn-policy"], ['adaptorFruCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "fw_version_hi": MoPropertyMeta("fw_version_hi", "fwVersionHi", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "fw_version_lo": MoPropertyMeta("fw_version_lo", "fwVersionLo", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "fw_version_opr": MoPropertyMeta("fw_version_opr", "fwVersionOpr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["gt", "lt", "none", "range"], []),
        "maximum": MoPropertyMeta("maximum", "maximum", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
        "nf_version_lo": MoPropertyMeta("nf_version_lo", "nfVersionLo", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "retimer_support": MoPropertyMeta("retimer_support", "retimerSupport", "string", VersionMeta.Version432b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, None, None, None, ["cdn-support", "eth-flow-monitoring-netflow", "eth-nvgre", "eth-nvgre-rocev2", "eth-nvgre-vmq", "eth-ptp", "eth-roce", "eth-roce-v2", "eth-vxlan", "eth-vxlan-rocev2", "eth-vxlan-vmq", "fcoe", "non-virtualized-eth-if", "non-virtualized-fc-if", "oracle-rac-support", "path-encap-consolidated", "path-encap-virtual", "path-encap-virtual-ce", "protected-eth-if", "protected-fc-if", "protected-fcoe", "pxeboot-config-support", "uplink-aggregation", "virtualized-ce-eth-if", "virtualized-eth-if", "virtualized-eth-sriov", "virtualized-eth-sriov-usnic", "virtualized-eth-vmmq", "virtualized-eth-vmq", "virtualized-fc-if", "virtualized-fc-sriov", "virtualized-scsi-if"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fwVersionHi": "fw_version_hi", 
        "fwVersionLo": "fw_version_lo", 
        "fwVersionOpr": "fw_version_opr", 
        "maximum": "maximum", 
        "nfVersionLo": "nf_version_lo", 
        "retimerSupport": "retimer_support", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.fw_version_hi = None
        self.fw_version_lo = None
        self.fw_version_opr = None
        self.maximum = None
        self.nf_version_lo = None
        self.retimer_support = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorCapSpec", parent_mo_or_dn, **kwargs)
