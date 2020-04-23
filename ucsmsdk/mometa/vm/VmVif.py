"""This module contains the general information for VmVif ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VmVifConsts:
    LINK_STATE_ADMIN_DOWN = "admin-down"
    LINK_STATE_DOWN = "down"
    LINK_STATE_ERROR = "error"
    LINK_STATE_OFFLINE = "offline"
    LINK_STATE_UNALLOCATED = "unallocated"
    LINK_STATE_UNAVAILABLE = "unavailable"
    LINK_STATE_UNKNOWN = "unknown"
    LINK_STATE_UP = "up"
    OPER_STATE_ACTIVE = "active"
    OPER_STATE_ADMIN_DOWN = "admin-down"
    OPER_STATE_ERROR = "error"
    OPER_STATE_LINK_DOWN = "link-down"
    OPER_STATE_PASSIVE = "passive"
    OPER_STATE_UNKNOWN = "unknown"
    PH_SWITCH_ID_A = "A"
    PH_SWITCH_ID_B = "B"
    PH_SWITCH_ID_NONE = "NONE"
    V_STATUS_OFFLINE = "offline"
    V_STATUS_ONLINE = "online"
    V_STATUS_UNKNOWN = "unknown"


class VmVif(ManagedObject):
    """This is VmVif class."""

    consts = VmVifConsts()
    naming_props = set(['phSwitchId', 'vifId'])

    mo_meta = MoMeta("VmVif", "vmVif", "sw-[ph_switch_id]vif-[vif_id]", VersionMeta.Version111j, "InputOutput", 0x7f, [], ["admin"], ['vmNic'], ['faultInst'], ["Get"])

    prop_meta = {
        "adp_vif_id": MoPropertyMeta("adp_vif_id", "adpVifId", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cookie": MoPropertyMeta("cookie", "cookie", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "link_state": MoPropertyMeta("link_state", "linkState", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["admin-down", "down", "error", "offline", "unallocated", "unavailable", "unknown", "up"], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "admin-down", "error", "link-down", "passive", "unknown"], []),
        "ph_switch_id": MoPropertyMeta("ph_switch_id", "phSwitchId", "string", VersionMeta.Version111j, MoPropertyMeta.NAMING, 0x8, None, None, None, ["A", "B", "NONE"], []),
        "phs_access_aggr_port_id": MoPropertyMeta("phs_access_aggr_port_id", "phsAccessAggrPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "phs_access_card_id": MoPropertyMeta("phs_access_card_id", "phsAccessCardId", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "phs_access_port_id": MoPropertyMeta("phs_access_port_id", "phsAccessPortId", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "phs_border_aggr_port_id": MoPropertyMeta("phs_border_aggr_port_id", "phsBorderAggrPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "phs_border_card_id": MoPropertyMeta("phs_border_card_id", "phsBorderCardId", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "phs_border_port_id": MoPropertyMeta("phs_border_port_id", "phsBorderPortId", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "state_qual": MoPropertyMeta("state_qual", "stateQual", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "status_change_ts": MoPropertyMeta("status_change_ts", "statusChangeTs", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "v_status": MoPropertyMeta("v_status", "vStatus", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["offline", "online", "unknown"], []),
        "vc_dn": MoPropertyMeta("vc_dn", "vcDn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "vif_id": MoPropertyMeta("vif_id", "vifId", "uint", VersionMeta.Version111j, MoPropertyMeta.NAMING, 0x40, None, None, None, [], []),
    }

    prop_map = {
        "adpVifId": "adp_vif_id", 
        "childAction": "child_action", 
        "cookie": "cookie", 
        "dn": "dn", 
        "linkState": "link_state", 
        "operState": "oper_state", 
        "phSwitchId": "ph_switch_id", 
        "phsAccessAggrPortId": "phs_access_aggr_port_id", 
        "phsAccessCardId": "phs_access_card_id", 
        "phsAccessPortId": "phs_access_port_id", 
        "phsBorderAggrPortId": "phs_border_aggr_port_id", 
        "phsBorderCardId": "phs_border_card_id", 
        "phsBorderPortId": "phs_border_port_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "stateQual": "state_qual", 
        "status": "status", 
        "statusChangeTs": "status_change_ts", 
        "vStatus": "v_status", 
        "vcDn": "vc_dn", 
        "vifId": "vif_id", 
    }

    def __init__(self, parent_mo_or_dn, ph_switch_id, vif_id, **kwargs):
        self._dirty_mask = 0
        self.ph_switch_id = ph_switch_id
        self.vif_id = vif_id
        self.adp_vif_id = None
        self.child_action = None
        self.cookie = None
        self.link_state = None
        self.oper_state = None
        self.phs_access_aggr_port_id = None
        self.phs_access_card_id = None
        self.phs_access_port_id = None
        self.phs_border_aggr_port_id = None
        self.phs_border_card_id = None
        self.phs_border_port_id = None
        self.sacl = None
        self.state_qual = None
        self.status = None
        self.status_change_ts = None
        self.v_status = None
        self.vc_dn = None

        ManagedObject.__init__(self, "VmVif", parent_mo_or_dn, **kwargs)
