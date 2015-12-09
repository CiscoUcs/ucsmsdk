"""This module contains the general information for EquipmentChassisStats ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentChassisStatsConsts():
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EquipmentChassisStats(ManagedObject):
    """This is EquipmentChassisStats class."""

    consts = EquipmentChassisStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentChassisStats", "equipmentChassisStats", "stats", VersionMeta.Version111j, "OutputOnly", 0xfL, [], ["admin", "operations", "read-only"], [u'equipmentChassis'], [u'equipmentChassisStatsHist'], ["Get"])

    prop_meta = {
        "chassis_i2_c_errors": MoPropertyMeta("chassis_i2_c_errors", "ChassisI2CErrors", "ulong", VersionMeta.Version226a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "chassis_i2_c_errors_delta": MoPropertyMeta("chassis_i2_c_errors_delta", "ChassisI2CErrorsDelta", "ulong", VersionMeta.Version226a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "chassis_i2_c_errors_delta_avg": MoPropertyMeta("chassis_i2_c_errors_delta_avg", "ChassisI2CErrorsDeltaAvg", "ulong", VersionMeta.Version226a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "chassis_i2_c_errors_delta_max": MoPropertyMeta("chassis_i2_c_errors_delta_max", "ChassisI2CErrorsDeltaMax", "ulong", VersionMeta.Version226a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "chassis_i2_c_errors_delta_min": MoPropertyMeta("chassis_i2_c_errors_delta_min", "ChassisI2CErrorsDeltaMin", "ulong", VersionMeta.Version226a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "input_power": MoPropertyMeta("input_power", "inputPower", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "input_power_avg": MoPropertyMeta("input_power_avg", "inputPowerAvg", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "input_power_max": MoPropertyMeta("input_power_max", "inputPowerMax", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "input_power_min": MoPropertyMeta("input_power_min", "inputPowerMin", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "output_power": MoPropertyMeta("output_power", "outputPower", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "output_power_avg": MoPropertyMeta("output_power_avg", "outputPowerAvg", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "output_power_max": MoPropertyMeta("output_power_max", "outputPowerMax", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "output_power_min": MoPropertyMeta("output_power_min", "outputPowerMin", "float", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "ChassisI2CErrors": "chassis_i2_c_errors", 
        "ChassisI2CErrorsDelta": "chassis_i2_c_errors_delta", 
        "ChassisI2CErrorsDeltaAvg": "chassis_i2_c_errors_delta_avg", 
        "ChassisI2CErrorsDeltaMax": "chassis_i2_c_errors_delta_max", 
        "ChassisI2CErrorsDeltaMin": "chassis_i2_c_errors_delta_min", 
        "childAction": "child_action", 
        "dn": "dn", 
        "inputPower": "input_power", 
        "inputPowerAvg": "input_power_avg", 
        "inputPowerMax": "input_power_max", 
        "inputPowerMin": "input_power_min", 
        "intervals": "intervals", 
        "outputPower": "output_power", 
        "outputPowerAvg": "output_power_avg", 
        "outputPowerMax": "output_power_max", 
        "outputPowerMin": "output_power_min", 
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
        self.chassis_i2_c_errors = None
        self.chassis_i2_c_errors_delta = None
        self.chassis_i2_c_errors_delta_avg = None
        self.chassis_i2_c_errors_delta_max = None
        self.chassis_i2_c_errors_delta_min = None
        self.child_action = None
        self.input_power = None
        self.input_power_avg = None
        self.input_power_max = None
        self.input_power_min = None
        self.intervals = None
        self.output_power = None
        self.output_power_avg = None
        self.output_power_max = None
        self.output_power_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "EquipmentChassisStats", parent_mo_or_dn, **kwargs)

