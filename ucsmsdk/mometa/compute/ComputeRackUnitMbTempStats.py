"""This module contains the general information for ComputeRackUnitMbTempStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeRackUnitMbTempStatsConsts:
    AMBIENT_TEMP_NOT_APPLICABLE = "not-applicable"
    AMBIENT_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    AMBIENT_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    AMBIENT_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    FRONT_TEMP_NOT_APPLICABLE = "not-applicable"
    FRONT_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    FRONT_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    FRONT_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    IOH1_TEMP_NOT_APPLICABLE = "not-applicable"
    IOH1_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    IOH1_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    IOH1_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    IOH2_TEMP_NOT_APPLICABLE = "not-applicable"
    IOH2_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    IOH2_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    IOH2_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    REAR_TEMP_NOT_APPLICABLE = "not-applicable"
    REAR_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    REAR_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    REAR_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ComputeRackUnitMbTempStats(ManagedObject):
    """This is ComputeRackUnitMbTempStats class."""

    consts = ComputeRackUnitMbTempStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeRackUnitMbTempStats", "computeRackUnitMbTempStats", "temp-stats", VersionMeta.Version141i, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['computeBoard'], ['computeRackUnitMbTempStatsHist'], ["Get"])

    prop_meta = {
        "ambient_temp": MoPropertyMeta("ambient_temp", "ambientTemp", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ambient_temp_avg": MoPropertyMeta("ambient_temp_avg", "ambientTempAvg", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ambient_temp_max": MoPropertyMeta("ambient_temp_max", "ambientTempMax", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ambient_temp_min": MoPropertyMeta("ambient_temp_min", "ambientTempMin", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "front_temp": MoPropertyMeta("front_temp", "frontTemp", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "front_temp_avg": MoPropertyMeta("front_temp_avg", "frontTempAvg", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "front_temp_max": MoPropertyMeta("front_temp_max", "frontTempMax", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "front_temp_min": MoPropertyMeta("front_temp_min", "frontTempMin", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ioh1_temp": MoPropertyMeta("ioh1_temp", "ioh1Temp", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ioh1_temp_avg": MoPropertyMeta("ioh1_temp_avg", "ioh1TempAvg", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ioh1_temp_max": MoPropertyMeta("ioh1_temp_max", "ioh1TempMax", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ioh1_temp_min": MoPropertyMeta("ioh1_temp_min", "ioh1TempMin", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ioh2_temp": MoPropertyMeta("ioh2_temp", "ioh2Temp", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ioh2_temp_avg": MoPropertyMeta("ioh2_temp_avg", "ioh2TempAvg", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ioh2_temp_max": MoPropertyMeta("ioh2_temp_max", "ioh2TempMax", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ioh2_temp_min": MoPropertyMeta("ioh2_temp_min", "ioh2TempMin", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "rear_temp": MoPropertyMeta("rear_temp", "rearTemp", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "rear_temp_avg": MoPropertyMeta("rear_temp_avg", "rearTempAvg", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "rear_temp_max": MoPropertyMeta("rear_temp_max", "rearTempMax", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "rear_temp_min": MoPropertyMeta("rear_temp_min", "rearTempMin", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "ambientTemp": "ambient_temp", 
        "ambientTempAvg": "ambient_temp_avg", 
        "ambientTempMax": "ambient_temp_max", 
        "ambientTempMin": "ambient_temp_min", 
        "childAction": "child_action", 
        "dn": "dn", 
        "frontTemp": "front_temp", 
        "frontTempAvg": "front_temp_avg", 
        "frontTempMax": "front_temp_max", 
        "frontTempMin": "front_temp_min", 
        "intervals": "intervals", 
        "ioh1Temp": "ioh1_temp", 
        "ioh1TempAvg": "ioh1_temp_avg", 
        "ioh1TempMax": "ioh1_temp_max", 
        "ioh1TempMin": "ioh1_temp_min", 
        "ioh2Temp": "ioh2_temp", 
        "ioh2TempAvg": "ioh2_temp_avg", 
        "ioh2TempMax": "ioh2_temp_max", 
        "ioh2TempMin": "ioh2_temp_min", 
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
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.ambient_temp = None
        self.ambient_temp_avg = None
        self.ambient_temp_max = None
        self.ambient_temp_min = None
        self.child_action = None
        self.front_temp = None
        self.front_temp_avg = None
        self.front_temp_max = None
        self.front_temp_min = None
        self.intervals = None
        self.ioh1_temp = None
        self.ioh1_temp_avg = None
        self.ioh1_temp_max = None
        self.ioh1_temp_min = None
        self.ioh2_temp = None
        self.ioh2_temp_avg = None
        self.ioh2_temp_max = None
        self.ioh2_temp_min = None
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

        ManagedObject.__init__(self, "ComputeRackUnitMbTempStats", parent_mo_or_dn, **kwargs)
