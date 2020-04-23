"""This module contains the general information for FabricChangedObjectRef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricChangedObjectRefConsts:
    REF_OBJ_STATUS_CREATED = "created"
    REF_OBJ_STATUS_DELETED = "deleted"
    REF_OBJ_STATUS_INTENT_DELETION = "intent-deletion"
    REF_OBJ_STATUS_MODIFIED = "modified"


class FabricChangedObjectRef(ManagedObject):
    """This is FabricChangedObjectRef class."""

    consts = FabricChangedObjectRefConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("FabricChangedObjectRef", "fabricChangedObjectRef", "ChangedObjectRef[id]", VersionMeta.Version212a, "InputOutput", 0x3f, [], ["read-only"], ['fabricVnetEpSyncEp'], [], [None])

    prop_meta = {
        "centrale_vnet_ep_dn": MoPropertyMeta("centrale_vnet_ep_dn", "centraleVnetEpDn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version212a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version212a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "old_centrale_vnet_ep_dn": MoPropertyMeta("old_centrale_vnet_ep_dn", "oldCentraleVnetEpDn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "ref_obj_status": MoPropertyMeta("ref_obj_status", "refObjStatus", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["created", "deleted", "intent-deletion", "modified"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version212a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "ucsm_vnet_ep_dn": MoPropertyMeta("ucsm_vnet_ep_dn", "ucsmVnetEpDn", "string", VersionMeta.Version212a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
    }

    prop_map = {
        "centraleVnetEpDn": "centrale_vnet_ep_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "oldCentraleVnetEpDn": "old_centrale_vnet_ep_dn", 
        "refObjStatus": "ref_obj_status", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "ucsmVnetEpDn": "ucsm_vnet_ep_dn", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.centrale_vnet_ep_dn = None
        self.child_action = None
        self.old_centrale_vnet_ep_dn = None
        self.ref_obj_status = None
        self.sacl = None
        self.status = None
        self.ucsm_vnet_ep_dn = None

        ManagedObject.__init__(self, "FabricChangedObjectRef", parent_mo_or_dn, **kwargs)
