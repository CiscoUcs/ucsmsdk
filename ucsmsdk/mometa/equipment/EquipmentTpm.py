"""This module contains the general information for EquipmentTpm ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentTpmConsts:
    ACTIVE_STATUS_ACTIVATED = "activated"
    ACTIVE_STATUS_DEACTIVATED = "deactivated"
    ACTIVE_STATUS_UNKNOWN = "unknown"
    ADMIN_ACTION_CLEAR_CONFIG = "clear-config"
    ADMIN_ACTION_UNSPECIFIED = "unspecified"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLY_FAILED = "apply-failed"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    ENABLED_STATUS_DISABLED = "disabled"
    ENABLED_STATUS_ENABLED = "enabled"
    ENABLED_STATUS_UNKNOWN = "unknown"
    OWNERSHIP_OWNED = "owned"
    OWNERSHIP_UNKNOWN = "unknown"
    OWNERSHIP_UNOWNED = "unowned"
    PASSWORD_STATE_NOT_SET = "not-set"
    PASSWORD_STATE_SET = "set"
    PASSWORD_STATE_UNKNOWN = "unknown"
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
    PRESENCE_EQUIPPED_DEPRECATED = "equipped-deprecated"
    PRESENCE_EQUIPPED_DISC_ERROR = "equipped-disc-error"
    PRESENCE_EQUIPPED_DISC_IN_PROGRESS = "equipped-disc-in-progress"
    PRESENCE_EQUIPPED_DISC_NOT_STARTED = "equipped-disc-not-started"
    PRESENCE_EQUIPPED_DISC_UNKNOWN = "equipped-disc-unknown"
    PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    PRESENCE_EQUIPPED_SLAVE = "equipped-slave"
    PRESENCE_EQUIPPED_UNSUPPORTED = "equipped-unsupported"
    PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    PRESENCE_INACCESSIBLE = "inaccessible"
    PRESENCE_MISMATCH = "mismatch"
    PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    PRESENCE_MISMATCH_SLAVE = "mismatch-slave"
    PRESENCE_MISSING = "missing"
    PRESENCE_MISSING_SLAVE = "missing-slave"
    PRESENCE_NOT_SUPPORTED = "not-supported"
    PRESENCE_UNAUTHORIZED = "unauthorized"
    PRESENCE_UNKNOWN = "unknown"
    TYPE_PHYSICAL = "physical"
    TYPE_UNKNOWN = "unknown"
    TYPE_VIRTUAL = "virtual"


class EquipmentTpm(ManagedObject):
    """This is EquipmentTpm class."""

    consts = EquipmentTpmConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EquipmentTpm", "equipmentTpm", "Tpm-[id]", VersionMeta.Version221b, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], ['computeBoard'], ['faultInst'], ["Get"])

    prop_meta = {
        "active_status": MoPropertyMeta("active_status", "activeStatus", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activated", "deactivated", "unknown"], []),
        "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["clear-config", "unspecified"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "apply-failed", "applying", "not-applied"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "enabled_status": MoPropertyMeta("enabled_status", "enabledStatus", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled", "unknown"], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "ownership": MoPropertyMeta("ownership", "ownership", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["owned", "unknown", "unowned"], []),
        "password_state": MoPropertyMeta("password_state", "passwordState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-set", "set", "unknown"], []),
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-disc-error", "equipped-disc-in-progress", "equipped-disc-not-started", "equipped-disc-unknown", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "tpm_revision": MoPropertyMeta("tpm_revision", "tpmRevision", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["physical", "unknown", "virtual"], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "activeStatus": "active_status", 
        "adminAction": "admin_action", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "dn": "dn", 
        "enabledStatus": "enabled_status", 
        "id": "id", 
        "model": "model", 
        "ownership": "ownership", 
        "passwordState": "password_state", 
        "presence": "presence", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "status": "status", 
        "tpmRevision": "tpm_revision", 
        "type": "type", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.active_status = None
        self.admin_action = None
        self.child_action = None
        self.config_state = None
        self.enabled_status = None
        self.model = None
        self.ownership = None
        self.password_state = None
        self.presence = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.status = None
        self.tpm_revision = None
        self.type = None
        self.vendor = None

        ManagedObject.__init__(self, "EquipmentTpm", parent_mo_or_dn, **kwargs)
