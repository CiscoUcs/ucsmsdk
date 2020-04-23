"""This module contains the general information for EquipmentIOCardStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentIOCardStatsHistConsts:
    AMBIENT_TEMP_NOT_APPLICABLE = "not-applicable"
    AMBIENT_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    AMBIENT_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    AMBIENT_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    DIMM_TEMP_NOT_APPLICABLE = "not-applicable"
    DIMM_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    DIMM_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    DIMM_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    PROC_TEMP_NOT_APPLICABLE = "not-applicable"
    PROC_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    PROC_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    PROC_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"
    TEMP_NOT_APPLICABLE = "not-applicable"
    TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    TEMP_MIN_NOT_APPLICABLE = "not-applicable"


class EquipmentIOCardStatsHist(ManagedObject):
    """This is EquipmentIOCardStatsHist class."""

    consts = EquipmentIOCardStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EquipmentIOCardStatsHist", "equipmentIOCardStatsHist", "[id]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["read-only"], ['equipmentIOCardStats'], [], ["Get"])

    prop_meta = {
        "iom_i2_c_errors": MoPropertyMeta("iom_i2_c_errors", "IomI2CErrors", "ulong", VersionMeta.Version226c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "iom_i2_c_errors_avg": MoPropertyMeta("iom_i2_c_errors_avg", "IomI2CErrorsAvg", "ulong", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "iom_i2_c_errors_max": MoPropertyMeta("iom_i2_c_errors_max", "IomI2CErrorsMax", "ulong", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "iom_i2_c_errors_min": MoPropertyMeta("iom_i2_c_errors_min", "IomI2CErrorsMin", "ulong", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ambient_temp": MoPropertyMeta("ambient_temp", "ambientTemp", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ambient_temp_avg": MoPropertyMeta("ambient_temp_avg", "ambientTempAvg", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ambient_temp_max": MoPropertyMeta("ambient_temp_max", "ambientTempMax", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ambient_temp_min": MoPropertyMeta("ambient_temp_min", "ambientTempMin", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dimm_temp": MoPropertyMeta("dimm_temp", "dimmTemp", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "dimm_temp_avg": MoPropertyMeta("dimm_temp_avg", "dimmTempAvg", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "dimm_temp_max": MoPropertyMeta("dimm_temp_max", "dimmTempMax", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "dimm_temp_min": MoPropertyMeta("dimm_temp_min", "dimmTempMin", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "proc_temp": MoPropertyMeta("proc_temp", "procTemp", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "proc_temp_avg": MoPropertyMeta("proc_temp_avg", "procTempAvg", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "proc_temp_max": MoPropertyMeta("proc_temp_max", "procTempMax", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "proc_temp_min": MoPropertyMeta("proc_temp_min", "procTempMin", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "temp": MoPropertyMeta("temp", "temp", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "temp_avg": MoPropertyMeta("temp_avg", "tempAvg", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "temp_max": MoPropertyMeta("temp_max", "tempMax", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "temp_min": MoPropertyMeta("temp_min", "tempMin", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
    }

    prop_map = {
        "IomI2CErrors": "iom_i2_c_errors", 
        "IomI2CErrorsAvg": "iom_i2_c_errors_avg", 
        "IomI2CErrorsMax": "iom_i2_c_errors_max", 
        "IomI2CErrorsMin": "iom_i2_c_errors_min", 
        "ambientTemp": "ambient_temp", 
        "ambientTempAvg": "ambient_temp_avg", 
        "ambientTempMax": "ambient_temp_max", 
        "ambientTempMin": "ambient_temp_min", 
        "childAction": "child_action", 
        "dimmTemp": "dimm_temp", 
        "dimmTempAvg": "dimm_temp_avg", 
        "dimmTempMax": "dimm_temp_max", 
        "dimmTempMin": "dimm_temp_min", 
        "dn": "dn", 
        "id": "id", 
        "mostRecent": "most_recent", 
        "procTemp": "proc_temp", 
        "procTempAvg": "proc_temp_avg", 
        "procTempMax": "proc_temp_max", 
        "procTempMin": "proc_temp_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "temp": "temp", 
        "tempAvg": "temp_avg", 
        "tempMax": "temp_max", 
        "tempMin": "temp_min", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.iom_i2_c_errors = None
        self.iom_i2_c_errors_avg = None
        self.iom_i2_c_errors_max = None
        self.iom_i2_c_errors_min = None
        self.ambient_temp = None
        self.ambient_temp_avg = None
        self.ambient_temp_max = None
        self.ambient_temp_min = None
        self.child_action = None
        self.dimm_temp = None
        self.dimm_temp_avg = None
        self.dimm_temp_max = None
        self.dimm_temp_min = None
        self.most_recent = None
        self.proc_temp = None
        self.proc_temp_avg = None
        self.proc_temp_max = None
        self.proc_temp_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.temp = None
        self.temp_avg = None
        self.temp_max = None
        self.temp_min = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "EquipmentIOCardStatsHist", parent_mo_or_dn, **kwargs)
