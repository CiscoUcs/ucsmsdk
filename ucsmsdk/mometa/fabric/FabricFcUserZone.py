"""This module contains the general information for FabricFcUserZone ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricFcUserZoneConsts:
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_FAILED_TO_APPLY = "failed-to-apply"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    OPER_STATE_ACTIVE = "active"
    OPER_STATE_CREATE_FAILED = "create-failed"
    OPER_STATE_CREATED = "created"
    OPER_STATE_DELETED = "deleted"
    OPER_STATE_NOT_ACTIVE = "not-active"
    OPER_STATE_ZONE_MERGE_FAILURE = "zone-merge-failure"
    PATH_A = "A"
    PATH_B = "B"
    PATH_NONE = "NONE"


class FabricFcUserZone(ManagedObject):
    """This is FabricFcUserZone class."""

    consts = FabricFcUserZoneConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricFcUserZone", "fabricFcUserZone", "zone-[name]", VersionMeta.Version312b, "InputOutput", 0x7f, [], ["admin", "ext-san-config", "ext-san-policy"], ['fabricFcZoneProfile'], ['fabricFcEndpoint', 'faultInst', 'storageVsanRef'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|zone-limit),){0,2}(defaultValue|none|zone-limit){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "applying", "failed-to-apply", "not-applied"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version312b, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{2,16}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "create-failed", "created", "deleted", "not-active", "zone-merge-failure"], []),
        "path": MoPropertyMeta("path", "path", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["A", "B", "NONE"], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "zone_name": MoPropertyMeta("zone_name", "zoneName", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{1,64}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "configState": "config_state", 
        "dn": "dn", 
        "id": "id", 
        "name": "name", 
        "operState": "oper_state", 
        "path": "path", 
        "peerDn": "peer_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "zoneName": "zone_name", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.config_qualifier = None
        self.config_state = None
        self.id = None
        self.oper_state = None
        self.path = None
        self.peer_dn = None
        self.sacl = None
        self.status = None
        self.zone_name = None

        ManagedObject.__init__(self, "FabricFcUserZone", parent_mo_or_dn, **kwargs)
