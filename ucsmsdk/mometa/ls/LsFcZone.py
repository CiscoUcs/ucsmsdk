"""This module contains the general information for LsFcZone ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LsFcZoneConsts:
    ADMIN_STATE_ACTIVE = "active"
    ADMIN_STATE_APPLIED = "applied"
    ADMIN_STATE_APPLY_PENDING = "apply-pending"
    ADMIN_STATE_APPLYING = "applying"
    ADMIN_STATE_CREATE_FAILED = "create-failed"
    ADMIN_STATE_CREATED = "created"
    ADMIN_STATE_DELETED = "deleted"
    ADMIN_STATE_NOT_ACTIVE = "not-active"
    ADMIN_STATE_NOT_APPLIED = "not-applied"
    ADMIN_STATE_ZONE_MERGE_FAILURE = "zone-merge-failure"
    OPER_STATE_ACTIVE = "active"
    OPER_STATE_APPLIED = "applied"
    OPER_STATE_APPLY_PENDING = "apply-pending"
    OPER_STATE_APPLYING = "applying"
    OPER_STATE_CREATE_FAILED = "create-failed"
    OPER_STATE_CREATED = "created"
    OPER_STATE_DELETED = "deleted"
    OPER_STATE_NOT_ACTIVE = "not-active"
    OPER_STATE_NOT_APPLIED = "not-applied"
    OPER_STATE_ZONE_MERGE_FAILURE = "zone-merge-failure"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    ZONING_TYPE_NONE = "none"
    ZONING_TYPE_SIMT = "simt"
    ZONING_TYPE_SIST = "sist"


class LsFcZone(ManagedObject):
    """This is LsFcZone class."""

    consts = LsFcZoneConsts()
    naming_props = set(['identity'])

    mo_meta = MoMeta("LsFcZone", "lsFcZone", "zone-[identity]", VersionMeta.Version211a, "InputOutput", 0x7f, [], ["admin", "ls-storage"], ['lsZoneInitiatorMember'], ['lsZoneTargetMember'], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "applied", "apply-pending", "applying", "create-failed", "created", "deleted", "not-active", "not-applied", "zone-merge-failure"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "identity": MoPropertyMeta("identity", "identity", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "ini_name": MoPropertyMeta("ini_name", "iniName", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{1,64}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "applied", "apply-pending", "applying", "create-failed", "created", "deleted", "not-active", "not-applied", "zone-merge-failure"], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []),
        "vnet_id": MoPropertyMeta("vnet_id", "vnetId", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4093"]),
        "zoning_type": MoPropertyMeta("zoning_type", "zoningType", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none", "simt", "sist"], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "identity": "identity", 
        "iniName": "ini_name", 
        "name": "name", 
        "operState": "oper_state", 
        "peerDn": "peer_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
        "usrLbl": "usr_lbl", 
        "vnetId": "vnet_id", 
        "zoningType": "zoning_type", 
    }

    def __init__(self, parent_mo_or_dn, identity, **kwargs):
        self._dirty_mask = 0
        self.identity = identity
        self.admin_state = None
        self.child_action = None
        self.id = None
        self.ini_name = None
        self.name = None
        self.oper_state = None
        self.peer_dn = None
        self.sacl = None
        self.status = None
        self.switch_id = None
        self.usr_lbl = None
        self.vnet_id = None
        self.zoning_type = None

        ManagedObject.__init__(self, "LsFcZone", parent_mo_or_dn, **kwargs)
