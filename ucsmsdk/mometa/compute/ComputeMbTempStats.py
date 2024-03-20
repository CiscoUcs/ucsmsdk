"""This module contains the general information for ComputeMbTempStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeMbTempStatsConsts:
    FM_TEMP_SEN_FRONT_R_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_FRONT_RAVG_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_FRONT_RMAX_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_FRONT_RMIN_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_IO_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_IO_AVG_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_IO_MAX_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_IO_MIN_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_REAR_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_REAR_AVG_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_REAR_L_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_REAR_LAVG_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_REAR_LMAX_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_REAR_LMIN_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_REAR_MAX_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_REAR_MIN_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_REAR_R_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_REAR_RAVG_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_REAR_RMAX_NOT_APPLICABLE = "not-applicable"
    FM_TEMP_SEN_REAR_RMIN_NOT_APPLICABLE = "not-applicable"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ComputeMbTempStats(ManagedObject):
    """This is ComputeMbTempStats class."""

    consts = ComputeMbTempStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeMbTempStats", "computeMbTempStats", "temp-stats", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['computeBoard', 'computeExtBoard'], ['computeMbTempStatsHist'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "fm_temp_sen_front_r": MoPropertyMeta("fm_temp_sen_front_r", "fmTempSenFrontR", "string", VersionMeta.Version433a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_front_r_avg": MoPropertyMeta("fm_temp_sen_front_r_avg", "fmTempSenFrontRAvg", "string", VersionMeta.Version433a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_front_r_max": MoPropertyMeta("fm_temp_sen_front_r_max", "fmTempSenFrontRMax", "string", VersionMeta.Version433a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_front_r_min": MoPropertyMeta("fm_temp_sen_front_r_min", "fmTempSenFrontRMin", "string", VersionMeta.Version433a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_io": MoPropertyMeta("fm_temp_sen_io", "fmTempSenIo", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_io_avg": MoPropertyMeta("fm_temp_sen_io_avg", "fmTempSenIoAvg", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_io_max": MoPropertyMeta("fm_temp_sen_io_max", "fmTempSenIoMax", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_io_min": MoPropertyMeta("fm_temp_sen_io_min", "fmTempSenIoMin", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_rear": MoPropertyMeta("fm_temp_sen_rear", "fmTempSenRear", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_rear_avg": MoPropertyMeta("fm_temp_sen_rear_avg", "fmTempSenRearAvg", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_rear_l": MoPropertyMeta("fm_temp_sen_rear_l", "fmTempSenRearL", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_rear_l_avg": MoPropertyMeta("fm_temp_sen_rear_l_avg", "fmTempSenRearLAvg", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_rear_l_max": MoPropertyMeta("fm_temp_sen_rear_l_max", "fmTempSenRearLMax", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_rear_l_min": MoPropertyMeta("fm_temp_sen_rear_l_min", "fmTempSenRearLMin", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_rear_max": MoPropertyMeta("fm_temp_sen_rear_max", "fmTempSenRearMax", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_rear_min": MoPropertyMeta("fm_temp_sen_rear_min", "fmTempSenRearMin", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_rear_r": MoPropertyMeta("fm_temp_sen_rear_r", "fmTempSenRearR", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_rear_r_avg": MoPropertyMeta("fm_temp_sen_rear_r_avg", "fmTempSenRearRAvg", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_rear_r_max": MoPropertyMeta("fm_temp_sen_rear_r_max", "fmTempSenRearRMax", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "fm_temp_sen_rear_r_min": MoPropertyMeta("fm_temp_sen_rear_r_min", "fmTempSenRearRMin", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fmTempSenFrontR": "fm_temp_sen_front_r", 
        "fmTempSenFrontRAvg": "fm_temp_sen_front_r_avg", 
        "fmTempSenFrontRMax": "fm_temp_sen_front_r_max", 
        "fmTempSenFrontRMin": "fm_temp_sen_front_r_min", 
        "fmTempSenIo": "fm_temp_sen_io", 
        "fmTempSenIoAvg": "fm_temp_sen_io_avg", 
        "fmTempSenIoMax": "fm_temp_sen_io_max", 
        "fmTempSenIoMin": "fm_temp_sen_io_min", 
        "fmTempSenRear": "fm_temp_sen_rear", 
        "fmTempSenRearAvg": "fm_temp_sen_rear_avg", 
        "fmTempSenRearL": "fm_temp_sen_rear_l", 
        "fmTempSenRearLAvg": "fm_temp_sen_rear_l_avg", 
        "fmTempSenRearLMax": "fm_temp_sen_rear_l_max", 
        "fmTempSenRearLMin": "fm_temp_sen_rear_l_min", 
        "fmTempSenRearMax": "fm_temp_sen_rear_max", 
        "fmTempSenRearMin": "fm_temp_sen_rear_min", 
        "fmTempSenRearR": "fm_temp_sen_rear_r", 
        "fmTempSenRearRAvg": "fm_temp_sen_rear_r_avg", 
        "fmTempSenRearRMax": "fm_temp_sen_rear_r_max", 
        "fmTempSenRearRMin": "fm_temp_sen_rear_r_min", 
        "intervals": "intervals", 
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
        self.child_action = None
        self.fm_temp_sen_front_r = None
        self.fm_temp_sen_front_r_avg = None
        self.fm_temp_sen_front_r_max = None
        self.fm_temp_sen_front_r_min = None
        self.fm_temp_sen_io = None
        self.fm_temp_sen_io_avg = None
        self.fm_temp_sen_io_max = None
        self.fm_temp_sen_io_min = None
        self.fm_temp_sen_rear = None
        self.fm_temp_sen_rear_avg = None
        self.fm_temp_sen_rear_l = None
        self.fm_temp_sen_rear_l_avg = None
        self.fm_temp_sen_rear_l_max = None
        self.fm_temp_sen_rear_l_min = None
        self.fm_temp_sen_rear_max = None
        self.fm_temp_sen_rear_min = None
        self.fm_temp_sen_rear_r = None
        self.fm_temp_sen_rear_r_avg = None
        self.fm_temp_sen_rear_r_max = None
        self.fm_temp_sen_rear_r_min = None
        self.intervals = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "ComputeMbTempStats", parent_mo_or_dn, **kwargs)
