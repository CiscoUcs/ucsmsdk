"""This module contains the general information for EquipmentFexEnvStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentFexEnvStatsHistConsts:
    DIE1_N_A = "N/A"
    DIE1_AVG_N_A = "N/A"
    DIE1_MAX_N_A = "N/A"
    DIE1_MIN_N_A = "N/A"
    INLET_N_A = "N/A"
    INLET1_N_A = "N/A"
    INLET1_AVG_N_A = "N/A"
    INLET1_MAX_N_A = "N/A"
    INLET1_MIN_N_A = "N/A"
    INLET_AVG_N_A = "N/A"
    INLET_MAX_N_A = "N/A"
    INLET_MIN_N_A = "N/A"
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    OUTLET1_N_A = "N/A"
    OUTLET1_AVG_N_A = "N/A"
    OUTLET1_MAX_N_A = "N/A"
    OUTLET1_MIN_N_A = "N/A"
    OUTLET2_N_A = "N/A"
    OUTLET2_AVG_N_A = "N/A"
    OUTLET2_MAX_N_A = "N/A"
    OUTLET2_MIN_N_A = "N/A"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EquipmentFexEnvStatsHist(ManagedObject):
    """This is EquipmentFexEnvStatsHist class."""

    consts = EquipmentFexEnvStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EquipmentFexEnvStatsHist", "equipmentFexEnvStatsHist", "[id]", VersionMeta.Version141i, "OutputOnly", 0xf, [], ["read-only"], ['equipmentFexEnvStats'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "die1": MoPropertyMeta("die1", "die1", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "die1_avg": MoPropertyMeta("die1_avg", "die1Avg", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "die1_max": MoPropertyMeta("die1_max", "die1Max", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "die1_min": MoPropertyMeta("die1_min", "die1Min", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version141i, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "inlet": MoPropertyMeta("inlet", "inlet", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "inlet1": MoPropertyMeta("inlet1", "inlet1", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "inlet1_avg": MoPropertyMeta("inlet1_avg", "inlet1Avg", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "inlet1_max": MoPropertyMeta("inlet1_max", "inlet1Max", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "inlet1_min": MoPropertyMeta("inlet1_min", "inlet1Min", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "inlet_avg": MoPropertyMeta("inlet_avg", "inletAvg", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "inlet_max": MoPropertyMeta("inlet_max", "inletMax", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "inlet_min": MoPropertyMeta("inlet_min", "inletMin", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "outlet1": MoPropertyMeta("outlet1", "outlet1", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "outlet1_avg": MoPropertyMeta("outlet1_avg", "outlet1Avg", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "outlet1_max": MoPropertyMeta("outlet1_max", "outlet1Max", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "outlet1_min": MoPropertyMeta("outlet1_min", "outlet1Min", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "outlet2": MoPropertyMeta("outlet2", "outlet2", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "outlet2_avg": MoPropertyMeta("outlet2_avg", "outlet2Avg", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "outlet2_max": MoPropertyMeta("outlet2_max", "outlet2Max", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "outlet2_min": MoPropertyMeta("outlet2_min", "outlet2Min", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["N/A"], ["0-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "die1": "die1", 
        "die1Avg": "die1_avg", 
        "die1Max": "die1_max", 
        "die1Min": "die1_min", 
        "dn": "dn", 
        "id": "id", 
        "inlet": "inlet", 
        "inlet1": "inlet1", 
        "inlet1Avg": "inlet1_avg", 
        "inlet1Max": "inlet1_max", 
        "inlet1Min": "inlet1_min", 
        "inletAvg": "inlet_avg", 
        "inletMax": "inlet_max", 
        "inletMin": "inlet_min", 
        "mostRecent": "most_recent", 
        "outlet1": "outlet1", 
        "outlet1Avg": "outlet1_avg", 
        "outlet1Max": "outlet1_max", 
        "outlet1Min": "outlet1_min", 
        "outlet2": "outlet2", 
        "outlet2Avg": "outlet2_avg", 
        "outlet2Max": "outlet2_max", 
        "outlet2Min": "outlet2_min", 
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
        self.child_action = None
        self.die1 = None
        self.die1_avg = None
        self.die1_max = None
        self.die1_min = None
        self.inlet = None
        self.inlet1 = None
        self.inlet1_avg = None
        self.inlet1_max = None
        self.inlet1_min = None
        self.inlet_avg = None
        self.inlet_max = None
        self.inlet_min = None
        self.most_recent = None
        self.outlet1 = None
        self.outlet1_avg = None
        self.outlet1_max = None
        self.outlet1_min = None
        self.outlet2 = None
        self.outlet2_avg = None
        self.outlet2_max = None
        self.outlet2_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "EquipmentFexEnvStatsHist", parent_mo_or_dn, **kwargs)
