"""This module contains the general information for SwCardEnvStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwCardEnvStatsHistConsts:
    SLOT_OUTLET1_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET1_AVG_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET1_MAX_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET1_MIN_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET2_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET2_AVG_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET2_MAX_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET2_MIN_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET3_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET3_AVG_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET3_MAX_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET3_MIN_NOT_APPLICABLE = "not-applicable"
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class SwCardEnvStatsHist(ManagedObject):
    """This is SwCardEnvStatsHist class."""

    consts = SwCardEnvStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("SwCardEnvStatsHist", "swCardEnvStatsHist", "[id]", VersionMeta.Version211a, "OutputOnly", 0xf, [], ["read-only"], ['swCardEnvStats'], [], ["Get"])

    prop_meta = {
        "slot_outlet1": MoPropertyMeta("slot_outlet1", "SlotOutlet1", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "slot_outlet1_avg": MoPropertyMeta("slot_outlet1_avg", "SlotOutlet1Avg", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "slot_outlet1_max": MoPropertyMeta("slot_outlet1_max", "SlotOutlet1Max", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "slot_outlet1_min": MoPropertyMeta("slot_outlet1_min", "SlotOutlet1Min", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "slot_outlet2": MoPropertyMeta("slot_outlet2", "SlotOutlet2", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "slot_outlet2_avg": MoPropertyMeta("slot_outlet2_avg", "SlotOutlet2Avg", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "slot_outlet2_max": MoPropertyMeta("slot_outlet2_max", "SlotOutlet2Max", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "slot_outlet2_min": MoPropertyMeta("slot_outlet2_min", "SlotOutlet2Min", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "slot_outlet3": MoPropertyMeta("slot_outlet3", "SlotOutlet3", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "slot_outlet3_avg": MoPropertyMeta("slot_outlet3_avg", "SlotOutlet3Avg", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "slot_outlet3_max": MoPropertyMeta("slot_outlet3_max", "SlotOutlet3Max", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "slot_outlet3_min": MoPropertyMeta("slot_outlet3_min", "SlotOutlet3Min", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version211a, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
    }

    prop_map = {
        "SlotOutlet1": "slot_outlet1", 
        "SlotOutlet1Avg": "slot_outlet1_avg", 
        "SlotOutlet1Max": "slot_outlet1_max", 
        "SlotOutlet1Min": "slot_outlet1_min", 
        "SlotOutlet2": "slot_outlet2", 
        "SlotOutlet2Avg": "slot_outlet2_avg", 
        "SlotOutlet2Max": "slot_outlet2_max", 
        "SlotOutlet2Min": "slot_outlet2_min", 
        "SlotOutlet3": "slot_outlet3", 
        "SlotOutlet3Avg": "slot_outlet3_avg", 
        "SlotOutlet3Max": "slot_outlet3_max", 
        "SlotOutlet3Min": "slot_outlet3_min", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.slot_outlet1 = None
        self.slot_outlet1_avg = None
        self.slot_outlet1_max = None
        self.slot_outlet1_min = None
        self.slot_outlet2 = None
        self.slot_outlet2_avg = None
        self.slot_outlet2_max = None
        self.slot_outlet2_min = None
        self.slot_outlet3 = None
        self.slot_outlet3_avg = None
        self.slot_outlet3_max = None
        self.slot_outlet3_min = None
        self.child_action = None
        self.most_recent = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "SwCardEnvStatsHist", parent_mo_or_dn, **kwargs)
