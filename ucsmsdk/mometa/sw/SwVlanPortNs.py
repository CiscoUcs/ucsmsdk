"""This module contains the general information for SwVlanPortNs ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwVlanPortNsConsts:
    ALLOC_STATUS_AVAILABLE = "available"
    ALLOC_STATUS_EXCEEDED = "exceeded"
    COMPRESSED_OPTIMIZATION_SETS_NA = "NA"
    COMPRESSED_VLAN_PORT_COUNT_NA = "NA"
    CONFIG_STATUS_NO_VLAN_COMP = "no-vlan-comp"
    CONFIG_STATUS_NONE = "none"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    TOTAL_OPTIMIZATION_SETS_NA = "NA"
    UNCOMPRESSED_VLAN_PORT_COUNT_NA = "NA"


class SwVlanPortNs(ManagedObject):
    """This is SwVlanPortNs class."""

    consts = SwVlanPortNsConsts()
    naming_props = set([])

    mo_meta = MoMeta("SwVlanPortNs", "swVlanPortNs", "vlan-port-ns", VersionMeta.Version131c, "InputOutput", 0x1f, [], ["read-only"], ['networkElement'], ['faultInst'], ["Get"])

    prop_meta = {
        "access_vlan_port_count": MoPropertyMeta("access_vlan_port_count", "accessVlanPortCount", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "alloc_status": MoPropertyMeta("alloc_status", "allocStatus", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["available", "exceeded"], []),
        "border_vlan_port_count": MoPropertyMeta("border_vlan_port_count", "borderVlanPortCount", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "compressed_optimization_sets": MoPropertyMeta("compressed_optimization_sets", "compressedOptimizationSets", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]),
        "compressed_vlan_port_count": MoPropertyMeta("compressed_vlan_port_count", "compressedVlanPortCount", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]),
        "config_status": MoPropertyMeta("config_status", "configStatus", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no-vlan-comp", "none"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "limit": MoPropertyMeta("limit", "limit", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "total_optimization_sets": MoPropertyMeta("total_optimization_sets", "totalOptimizationSets", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]),
        "total_vlan_port_count": MoPropertyMeta("total_vlan_port_count", "totalVlanPortCount", "uint", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "uncompressed_vlan_port_count": MoPropertyMeta("uncompressed_vlan_port_count", "uncompressedVlanPortCount", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]),
        "vlan_comp_off_limit": MoPropertyMeta("vlan_comp_off_limit", "vlanCompOffLimit", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "vlan_comp_on_limit": MoPropertyMeta("vlan_comp_on_limit", "vlanCompOnLimit", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
    }

    prop_map = {
        "accessVlanPortCount": "access_vlan_port_count", 
        "allocStatus": "alloc_status", 
        "borderVlanPortCount": "border_vlan_port_count", 
        "childAction": "child_action", 
        "compressedOptimizationSets": "compressed_optimization_sets", 
        "compressedVlanPortCount": "compressed_vlan_port_count", 
        "configStatus": "config_status", 
        "dn": "dn", 
        "limit": "limit", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
        "totalOptimizationSets": "total_optimization_sets", 
        "totalVlanPortCount": "total_vlan_port_count", 
        "uncompressedVlanPortCount": "uncompressed_vlan_port_count", 
        "vlanCompOffLimit": "vlan_comp_off_limit", 
        "vlanCompOnLimit": "vlan_comp_on_limit", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.access_vlan_port_count = None
        self.alloc_status = None
        self.border_vlan_port_count = None
        self.child_action = None
        self.compressed_optimization_sets = None
        self.compressed_vlan_port_count = None
        self.config_status = None
        self.limit = None
        self.sacl = None
        self.status = None
        self.switch_id = None
        self.total_optimization_sets = None
        self.total_vlan_port_count = None
        self.uncompressed_vlan_port_count = None
        self.vlan_comp_off_limit = None
        self.vlan_comp_on_limit = None

        ManagedObject.__init__(self, "SwVlanPortNs", parent_mo_or_dn, **kwargs)
