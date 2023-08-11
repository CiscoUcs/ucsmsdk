"""This module contains the general information for EquipmentRackEnclosure ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentRackEnclosureConsts:
    MFG_TIME_NOT_APPLICABLE = "not-applicable"
    OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
    OPERABILITY_BACKPLANE_PORT_PROBLEM = "backplane-port-problem"
    OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPERABILITY_CHASSIS_INTRUSION = "chassis-intrusion"
    OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPERABILITY_CONFIG = "config"
    OPERABILITY_DECOMISSIONING = "decomissioning"
    OPERABILITY_DEGRADED = "degraded"
    OPERABILITY_DIMM_DISABLED = "dimm-disabled"
    OPERABILITY_DISABLED = "disabled"
    OPERABILITY_DISCOVERY = "discovery"
    OPERABILITY_DISCOVERY_FAILED = "discovery-failed"
    OPERABILITY_EQUIPMENT_PROBLEM = "equipment-problem"
    OPERABILITY_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    OPERABILITY_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    OPERABILITY_IDENTIFY = "identify"
    OPERABILITY_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    OPERABILITY_INOPERABLE = "inoperable"
    OPERABILITY_LINK_ACTIVATE_BLOCKED = "link-activate-blocked"
    OPERABILITY_MALFORMED_FRU = "malformed-fru"
    OPERABILITY_NON_OPTIMAL = "non-optimal"
    OPERABILITY_NON_OPTIMAL_SEVERE = "non-optimal-severe"
    OPERABILITY_NOT_SUPPORTED = "not-supported"
    OPERABILITY_OPERABLE = "operable"
    OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
    OPERABILITY_PEER_DIMM_DISABLED = "peer-dimm-disabled"
    OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
    OPERABILITY_POST_FAILURE = "post-failure"
    OPERABILITY_POWER_PROBLEM = "power-problem"
    OPERABILITY_POWERED_OFF = "powered-off"
    OPERABILITY_REMOVED = "removed"
    OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
    OPERABILITY_UNKNOWN = "unknown"
    OPERABILITY_UNSUPPORTED_CONFIG = "unsupported-config"
    OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
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


class EquipmentRackEnclosure(ManagedObject):
    """This is EquipmentRackEnclosure class."""

    consts = EquipmentRackEnclosureConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EquipmentRackEnclosure", "equipmentRackEnclosure", "rack-enclosure-[id]", VersionMeta.Version401a, "InputOutput", 0x3f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['topSystem'], ['equipmentFanModule', 'equipmentPsu', 'equipmentSlotEp'], [None])

    prop_meta = {
        "asset_tag": MoPropertyMeta("asset_tag", "assetTag", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version401a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "mfg_time": MoPropertyMeta("mfg_time", "mfgTime", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["not-applicable"], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-intrusion", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "dimm-disabled", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "non-optimal", "non-optimal-severe", "not-supported", "operable", "peer-comm-problem", "peer-dimm-disabled", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "unsupported-config", "upgrade-problem", "voltage-problem"], []),
        "part_number": MoPropertyMeta("part_number", "partNumber", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-deprecated", "equipped-disc-error", "equipped-disc-in-progress", "equipped-disc-not-started", "equipped-disc-unknown", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "vid": MoPropertyMeta("vid", "vid", "string", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "assetTag": "asset_tag", 
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "id": "id", 
        "mfgTime": "mfg_time", 
        "model": "model", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operability": "operability", 
        "partNumber": "part_number", 
        "presence": "presence", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "status": "status", 
        "vendor": "vendor", 
        "vid": "vid", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.asset_tag = None
        self.child_action = None
        self.flt_aggr = None
        self.mfg_time = None
        self.model = None
        self.oper_qualifier_reason = None
        self.operability = None
        self.part_number = None
        self.presence = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.status = None
        self.vendor = None
        self.vid = None

        ManagedObject.__init__(self, "EquipmentRackEnclosure", parent_mo_or_dn, **kwargs)
