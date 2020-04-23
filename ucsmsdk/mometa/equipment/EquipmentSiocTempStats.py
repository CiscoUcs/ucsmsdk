"""This module contains the general information for EquipmentSiocTempStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentSiocTempStatsConsts:
    CMC_TEMP_NOT_APPLICABLE = "not-applicable"
    CMC_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    CMC_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    CMC_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    FRONT_TEMP_NOT_APPLICABLE = "not-applicable"
    FRONT_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    FRONT_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    FRONT_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    MID_TEMP_NOT_APPLICABLE = "not-applicable"
    MID_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    MID_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    MID_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    REAR_TEMP_NOT_APPLICABLE = "not-applicable"
    REAR_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    REAR_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    REAR_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"
    VIC_TEMP_NOT_APPLICABLE = "not-applicable"
    VIC_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    VIC_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    VIC_TEMP_MIN_NOT_APPLICABLE = "not-applicable"


class EquipmentSiocTempStats(ManagedObject):
    """This is EquipmentSiocTempStats class."""

    consts = EquipmentSiocTempStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentSiocTempStats", "equipmentSiocTempStats", "temp-stats", VersionMeta.Version312b, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['equipmentSystemIOController'], ['equipmentSiocTempStatsHist'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "cmc_temp": MoPropertyMeta("cmc_temp", "cmcTemp", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "cmc_temp_avg": MoPropertyMeta("cmc_temp_avg", "cmcTempAvg", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "cmc_temp_max": MoPropertyMeta("cmc_temp_max", "cmcTempMax", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "cmc_temp_min": MoPropertyMeta("cmc_temp_min", "cmcTempMin", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "front_temp": MoPropertyMeta("front_temp", "frontTemp", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "front_temp_avg": MoPropertyMeta("front_temp_avg", "frontTempAvg", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "front_temp_max": MoPropertyMeta("front_temp_max", "frontTempMax", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "front_temp_min": MoPropertyMeta("front_temp_min", "frontTempMin", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mid_temp": MoPropertyMeta("mid_temp", "midTemp", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "mid_temp_avg": MoPropertyMeta("mid_temp_avg", "midTempAvg", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "mid_temp_max": MoPropertyMeta("mid_temp_max", "midTempMax", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "mid_temp_min": MoPropertyMeta("mid_temp_min", "midTempMin", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "rear_temp": MoPropertyMeta("rear_temp", "rearTemp", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "rear_temp_avg": MoPropertyMeta("rear_temp_avg", "rearTempAvg", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "rear_temp_max": MoPropertyMeta("rear_temp_max", "rearTempMax", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "rear_temp_min": MoPropertyMeta("rear_temp_min", "rearTempMin", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "vic_temp": MoPropertyMeta("vic_temp", "vicTemp", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "vic_temp_avg": MoPropertyMeta("vic_temp_avg", "vicTempAvg", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "vic_temp_max": MoPropertyMeta("vic_temp_max", "vicTempMax", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "vic_temp_min": MoPropertyMeta("vic_temp_min", "vicTempMin", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
    }

    prop_map = {
        "childAction": "child_action", 
        "cmcTemp": "cmc_temp", 
        "cmcTempAvg": "cmc_temp_avg", 
        "cmcTempMax": "cmc_temp_max", 
        "cmcTempMin": "cmc_temp_min", 
        "dn": "dn", 
        "frontTemp": "front_temp", 
        "frontTempAvg": "front_temp_avg", 
        "frontTempMax": "front_temp_max", 
        "frontTempMin": "front_temp_min", 
        "intervals": "intervals", 
        "midTemp": "mid_temp", 
        "midTempAvg": "mid_temp_avg", 
        "midTempMax": "mid_temp_max", 
        "midTempMin": "mid_temp_min", 
        "rearTemp": "rear_temp", 
        "rearTempAvg": "rear_temp_avg", 
        "rearTempMax": "rear_temp_max", 
        "rearTempMin": "rear_temp_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
        "vicTemp": "vic_temp", 
        "vicTempAvg": "vic_temp_avg", 
        "vicTempMax": "vic_temp_max", 
        "vicTempMin": "vic_temp_min", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.cmc_temp = None
        self.cmc_temp_avg = None
        self.cmc_temp_max = None
        self.cmc_temp_min = None
        self.front_temp = None
        self.front_temp_avg = None
        self.front_temp_max = None
        self.front_temp_min = None
        self.intervals = None
        self.mid_temp = None
        self.mid_temp_avg = None
        self.mid_temp_max = None
        self.mid_temp_min = None
        self.rear_temp = None
        self.rear_temp_avg = None
        self.rear_temp_max = None
        self.rear_temp_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None
        self.vic_temp = None
        self.vic_temp_avg = None
        self.vic_temp_max = None
        self.vic_temp_min = None

        ManagedObject.__init__(self, "EquipmentSiocTempStats", parent_mo_or_dn, **kwargs)
