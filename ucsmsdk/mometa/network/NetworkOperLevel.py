"""This module contains the general information for NetworkOperLevel ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class NetworkOperLevelConsts:
    ID_A = "A"
    ID_B = "B"
    ID_NONE = "NONE"
    PRIMARY_VLAN_COUNT_STATUS_ABOVE_LIMIT = "above-limit"
    PRIMARY_VLAN_COUNT_STATUS_ABOVE_THRESHOLD_LIMIT = "above-threshold-limit"
    PRIMARY_VLAN_COUNT_STATUS_WITHIN_LIMIT = "within-limit"
    SECONDARY_VLAN_COUNT_STATUS_ABOVE_LIMIT = "above-limit"
    SECONDARY_VLAN_COUNT_STATUS_ABOVE_THRESHOLD_LIMIT = "above-threshold-limit"
    SECONDARY_VLAN_COUNT_STATUS_WITHIN_LIMIT = "within-limit"
    VIF_COUNT_STATUS_ABOVE_LIMIT = "above-limit"
    VIF_COUNT_STATUS_ABOVE_THRESHOLD_LIMIT = "above-threshold-limit"
    VIF_COUNT_STATUS_WITHIN_LIMIT = "within-limit"


class NetworkOperLevel(ManagedObject):
    """This is NetworkOperLevel class."""

    consts = NetworkOperLevelConsts()
    naming_props = set([])

    mo_meta = MoMeta("NetworkOperLevel", "networkOperLevel", "oper-level", VersionMeta.Version212a, "InputOutput", 0x1f, [], ["admin", "ext-lan-config"], ['networkElement'], ['faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version212a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "max_primary_vlan_count": MoPropertyMeta("max_primary_vlan_count", "maxPrimaryVlanCount", "uint", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "max_sec_vlan_per_primary_vlan_count": MoPropertyMeta("max_sec_vlan_per_primary_vlan_count", "maxSecVlanPerPrimaryVlanCount", "uint", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "max_secondary_vlan_count": MoPropertyMeta("max_secondary_vlan_count", "maxSecondaryVlanCount", "uint", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "max_vif_count": MoPropertyMeta("max_vif_count", "maxVifCount", "uint", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "primary_vlan_count": MoPropertyMeta("primary_vlan_count", "primaryVlanCount", "uint", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "primary_vlan_count_status": MoPropertyMeta("primary_vlan_count_status", "primaryVlanCountStatus", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["above-limit", "above-threshold-limit", "within-limit"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "secondary_vlan_count": MoPropertyMeta("secondary_vlan_count", "secondaryVlanCount", "uint", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "secondary_vlan_count_status": MoPropertyMeta("secondary_vlan_count_status", "secondaryVlanCountStatus", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["above-limit", "above-threshold-limit", "within-limit"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vif_count": MoPropertyMeta("vif_count", "vifCount", "uint", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "vif_count_status": MoPropertyMeta("vif_count_status", "vifCountStatus", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["above-limit", "above-threshold-limit", "within-limit"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "maxPrimaryVlanCount": "max_primary_vlan_count", 
        "maxSecVlanPerPrimaryVlanCount": "max_sec_vlan_per_primary_vlan_count", 
        "maxSecondaryVlanCount": "max_secondary_vlan_count", 
        "maxVifCount": "max_vif_count", 
        "primaryVlanCount": "primary_vlan_count", 
        "primaryVlanCountStatus": "primary_vlan_count_status", 
        "rn": "rn", 
        "sacl": "sacl", 
        "secondaryVlanCount": "secondary_vlan_count", 
        "secondaryVlanCountStatus": "secondary_vlan_count_status", 
        "status": "status", 
        "vifCount": "vif_count", 
        "vifCountStatus": "vif_count_status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.id = None
        self.max_primary_vlan_count = None
        self.max_sec_vlan_per_primary_vlan_count = None
        self.max_secondary_vlan_count = None
        self.max_vif_count = None
        self.primary_vlan_count = None
        self.primary_vlan_count_status = None
        self.sacl = None
        self.secondary_vlan_count = None
        self.secondary_vlan_count_status = None
        self.status = None
        self.vif_count = None
        self.vif_count_status = None

        ManagedObject.__init__(self, "NetworkOperLevel", parent_mo_or_dn, **kwargs)
