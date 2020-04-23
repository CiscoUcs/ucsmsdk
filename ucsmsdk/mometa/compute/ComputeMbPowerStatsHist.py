"""This module contains the general information for ComputeMbPowerStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeMbPowerStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ComputeMbPowerStatsHist(ManagedObject):
    """This is ComputeMbPowerStatsHist class."""

    consts = ComputeMbPowerStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ComputeMbPowerStatsHist", "computeMbPowerStatsHist", "[id]", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["read-only"], ['computeMbPowerStats'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "consumed_power": MoPropertyMeta("consumed_power", "consumedPower", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "consumed_power_avg": MoPropertyMeta("consumed_power_avg", "consumedPowerAvg", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "consumed_power_max": MoPropertyMeta("consumed_power_max", "consumedPowerMax", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "consumed_power_min": MoPropertyMeta("consumed_power_min", "consumedPowerMin", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111j, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "input_current": MoPropertyMeta("input_current", "inputCurrent", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "input_current_avg": MoPropertyMeta("input_current_avg", "inputCurrentAvg", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "input_current_max": MoPropertyMeta("input_current_max", "inputCurrentMax", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "input_current_min": MoPropertyMeta("input_current_min", "inputCurrentMin", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "input_voltage": MoPropertyMeta("input_voltage", "inputVoltage", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "input_voltage_avg": MoPropertyMeta("input_voltage_avg", "inputVoltageAvg", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "input_voltage_max": MoPropertyMeta("input_voltage_max", "inputVoltageMax", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "input_voltage_min": MoPropertyMeta("input_voltage_min", "inputVoltageMin", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "consumedPower": "consumed_power", 
        "consumedPowerAvg": "consumed_power_avg", 
        "consumedPowerMax": "consumed_power_max", 
        "consumedPowerMin": "consumed_power_min", 
        "dn": "dn", 
        "id": "id", 
        "inputCurrent": "input_current", 
        "inputCurrentAvg": "input_current_avg", 
        "inputCurrentMax": "input_current_max", 
        "inputCurrentMin": "input_current_min", 
        "inputVoltage": "input_voltage", 
        "inputVoltageAvg": "input_voltage_avg", 
        "inputVoltageMax": "input_voltage_max", 
        "inputVoltageMin": "input_voltage_min", 
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
        self.child_action = None
        self.consumed_power = None
        self.consumed_power_avg = None
        self.consumed_power_max = None
        self.consumed_power_min = None
        self.input_current = None
        self.input_current_avg = None
        self.input_current_max = None
        self.input_current_min = None
        self.input_voltage = None
        self.input_voltage_avg = None
        self.input_voltage_max = None
        self.input_voltage_min = None
        self.most_recent = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "ComputeMbPowerStatsHist", parent_mo_or_dn, **kwargs)
