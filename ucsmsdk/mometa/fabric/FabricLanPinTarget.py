"""This module contains the general information for FabricLanPinTarget ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricLanPinTargetConsts:
    FABRIC_ID_A = "A"
    FABRIC_ID_B = "B"
    FABRIC_ID_NONE = "NONE"
    FABRIC_ID_DUAL = "dual"
    TARGET_STATUS_INVALID = "invalid"
    TARGET_STATUS_VALID = "valid"


class FabricLanPinTarget(ManagedObject):
    """This is FabricLanPinTarget class."""

    consts = FabricLanPinTargetConsts()
    naming_props = set(['fabricId'])

    mo_meta = MoMeta("FabricLanPinTarget", "fabricLanPinTarget", "target-[fabric_id]", VersionMeta.Version101e, "InputOutput", 0x3ff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricLanPinGroup'], ['faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "aggr_port_id": MoPropertyMeta("aggr_port_id", "aggrPortId", "uint", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-108"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, 0, 256, None, [], []),
        "fabric_id": MoPropertyMeta("fabric_id", "fabricId", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, None, None, None, ["A", "B", "NONE", "dual"], []),
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["0-4"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["0-2"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "target_status": MoPropertyMeta("target_status", "targetStatus", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["invalid", "valid"], []),
    }

    prop_map = {
        "aggrPortId": "aggr_port_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "fabricId": "fabric_id", 
        "portId": "port_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotId": "slot_id", 
        "status": "status", 
        "targetStatus": "target_status", 
    }

    def __init__(self, parent_mo_or_dn, fabric_id, **kwargs):
        self._dirty_mask = 0
        self.fabric_id = fabric_id
        self.aggr_port_id = None
        self.child_action = None
        self.ep_dn = None
        self.port_id = None
        self.sacl = None
        self.slot_id = None
        self.status = None
        self.target_status = None

        ManagedObject.__init__(self, "FabricLanPinTarget", parent_mo_or_dn, **kwargs)
