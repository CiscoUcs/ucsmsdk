"""This module contains the general information for SwVlanPortNs ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class SwVlanPortNsConsts():
    ALLOC_STATUS_AVAILABLE = "available"
    ALLOC_STATUS_EXCEEDED = "exceeded"
    CONFIG_STATUS_NO_VLAN_COMP = "no-vlan-comp"
    CONFIG_STATUS_NONE = "none"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class SwVlanPortNs(ManagedObject):
    """This is SwVlanPortNs class."""

    consts = SwVlanPortNsConsts()
    naming_props = set([])

    mo_meta = MoMeta("SwVlanPortNs", "swVlanPortNs", "vlan-port-ns", VersionMeta.Version131c, "InputOutput", 0xfL, [], ["read-only"], [u'networkElement'], [u'faultInst'], ["Get"])

    prop_meta = {
        "access_vlan_port_count": MoPropertyMeta("access_vlan_port_count", "accessVlanPortCount", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "alloc_status": MoPropertyMeta("alloc_status", "allocStatus", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["available", "exceeded"], []), 
        "border_vlan_port_count": MoPropertyMeta("border_vlan_port_count", "borderVlanPortCount", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_status": MoPropertyMeta("config_status", "configStatus", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no-vlan-comp", "none"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "limit": MoPropertyMeta("limit", "limit", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []), 
        "total_vlan_port_count": MoPropertyMeta("total_vlan_port_count", "totalVlanPortCount", "uint", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "vlan_comp_off_limit": MoPropertyMeta("vlan_comp_off_limit", "vlanCompOffLimit", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "vlan_comp_on_limit": MoPropertyMeta("vlan_comp_on_limit", "vlanCompOnLimit", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "accessVlanPortCount": "access_vlan_port_count", 
        "allocStatus": "alloc_status", 
        "borderVlanPortCount": "border_vlan_port_count", 
        "childAction": "child_action", 
        "configStatus": "config_status", 
        "dn": "dn", 
        "limit": "limit", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
        "totalVlanPortCount": "total_vlan_port_count", 
        "vlanCompOffLimit": "vlan_comp_off_limit", 
        "vlanCompOnLimit": "vlan_comp_on_limit", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.access_vlan_port_count = None
        self.alloc_status = None
        self.border_vlan_port_count = None
        self.child_action = None
        self.config_status = None
        self.limit = None
        self.sacl = None
        self.status = None
        self.switch_id = None
        self.total_vlan_port_count = None
        self.vlan_comp_off_limit = None
        self.vlan_comp_on_limit = None

        ManagedObject.__init__(self, "SwVlanPortNs", parent_mo_or_dn, **kwargs)

