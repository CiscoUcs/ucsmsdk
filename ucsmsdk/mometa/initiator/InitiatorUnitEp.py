"""This module contains the general information for InitiatorUnitEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class InitiatorUnitEpConsts:
    BOOT_FALSE = "false"
    BOOT_NO = "no"
    BOOT_TRUE = "true"
    BOOT_YES = "yes"
    ID_UNSPECIFIED = "unspecified"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    PHY_ID_UNSPECIFIED = "unspecified"
    PROT_DERIVED = "derived"
    PROT_FC = "fc"
    PROT_ISCSI = "iscsi"


class InitiatorUnitEp(ManagedObject):
    """This is InitiatorUnitEp class."""

    consts = InitiatorUnitEpConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("InitiatorUnitEp", "initiatorUnitEp", "unit-[id]", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["read-only"], ['initiatorRequestorGrpEp'], [], [None])

    prop_meta = {
        "boot": MoPropertyMeta("boot", "boot", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "ha": MoPropertyMeta("ha", "ha", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|initiator|target|fabric),){0,4}(defaultValue|none|initiator|target|fabric){0,1}""", [], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8, None, None, None, ["unspecified"], ["0-4294967295"]),
        "item_dn": MoPropertyMeta("item_dn", "itemDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []),
        "phy_id": MoPropertyMeta("phy_id", "phyId", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
        "prot": MoPropertyMeta("prot", "prot", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["derived", "fc", "iscsi"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "boot": "boot", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "ha": "ha", 
        "id": "id", 
        "itemDn": "item_dn", 
        "lc": "lc", 
        "phyId": "phy_id", 
        "prot": "prot", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.boot = None
        self.child_action = None
        self.ep_dn = None
        self.ha = None
        self.item_dn = None
        self.lc = None
        self.phy_id = None
        self.prot = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "InitiatorUnitEp", parent_mo_or_dn, **kwargs)
