"""This module contains the general information for EquipmentRackUnitPsuStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentRackUnitPsuStatsHistConsts:
    AMBIENT_TEMP_NOT_APPLICABLE = "not-applicable"
    AMBIENT_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    AMBIENT_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    AMBIENT_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EquipmentRackUnitPsuStatsHist(ManagedObject):
    """This is EquipmentRackUnitPsuStatsHist class."""

    consts = EquipmentRackUnitPsuStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EquipmentRackUnitPsuStatsHist", "equipmentRackUnitPsuStatsHist", "[id]", VersionMeta.Version141i, "OutputOnly", 0xf, [], ["read-only"], ['equipmentRackUnitPsuStats'], [], ["Get"])

    prop_meta = {
        "ambient_temp": MoPropertyMeta("ambient_temp", "ambientTemp", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ambient_temp_avg": MoPropertyMeta("ambient_temp_avg", "ambientTempAvg", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ambient_temp_max": MoPropertyMeta("ambient_temp_max", "ambientTempMax", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "ambient_temp_min": MoPropertyMeta("ambient_temp_min", "ambientTempMin", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([\-]?)([123]?[1234]?)([0-9]{0,36})(([.])([0-9]{1,10}))?$""", ["not-applicable"], ["0-4294967295"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version141i, MoPropertyMeta.NAMING, None, None, None, None, [], []),
        "input_power": MoPropertyMeta("input_power", "inputPower", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "input_power_avg": MoPropertyMeta("input_power_avg", "inputPowerAvg", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "input_power_max": MoPropertyMeta("input_power_max", "inputPowerMax", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "input_power_min": MoPropertyMeta("input_power_min", "inputPowerMin", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "input_voltage": MoPropertyMeta("input_voltage", "inputVoltage", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "input_voltage_avg": MoPropertyMeta("input_voltage_avg", "inputVoltageAvg", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "input_voltage_max": MoPropertyMeta("input_voltage_max", "inputVoltageMax", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "input_voltage_min": MoPropertyMeta("input_voltage_min", "inputVoltageMin", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "output_current": MoPropertyMeta("output_current", "outputCurrent", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "output_current_avg": MoPropertyMeta("output_current_avg", "outputCurrentAvg", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "output_current_max": MoPropertyMeta("output_current_max", "outputCurrentMax", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "output_current_min": MoPropertyMeta("output_current_min", "outputCurrentMin", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "output_power": MoPropertyMeta("output_power", "outputPower", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "output_power_avg": MoPropertyMeta("output_power_avg", "outputPowerAvg", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "output_power_max": MoPropertyMeta("output_power_max", "outputPowerMax", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "output_power_min": MoPropertyMeta("output_power_min", "outputPowerMin", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "output_voltage": MoPropertyMeta("output_voltage", "outputVoltage", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "output_voltage_avg": MoPropertyMeta("output_voltage_avg", "outputVoltageAvg", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "output_voltage_max": MoPropertyMeta("output_voltage_max", "outputVoltageMax", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "output_voltage_min": MoPropertyMeta("output_voltage_min", "outputVoltageMin", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
    }

    prop_map = {
        "ambientTemp": "ambient_temp", 
        "ambientTempAvg": "ambient_temp_avg", 
        "ambientTempMax": "ambient_temp_max", 
        "ambientTempMin": "ambient_temp_min", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "inputPower": "input_power", 
        "inputPowerAvg": "input_power_avg", 
        "inputPowerMax": "input_power_max", 
        "inputPowerMin": "input_power_min", 
        "inputVoltage": "input_voltage", 
        "inputVoltageAvg": "input_voltage_avg", 
        "inputVoltageMax": "input_voltage_max", 
        "inputVoltageMin": "input_voltage_min", 
        "mostRecent": "most_recent", 
        "outputCurrent": "output_current", 
        "outputCurrentAvg": "output_current_avg", 
        "outputCurrentMax": "output_current_max", 
        "outputCurrentMin": "output_current_min", 
        "outputPower": "output_power", 
        "outputPowerAvg": "output_power_avg", 
        "outputPowerMax": "output_power_max", 
        "outputPowerMin": "output_power_min", 
        "outputVoltage": "output_voltage", 
        "outputVoltageAvg": "output_voltage_avg", 
        "outputVoltageMax": "output_voltage_max", 
        "outputVoltageMin": "output_voltage_min", 
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
        self.ambient_temp = None
        self.ambient_temp_avg = None
        self.ambient_temp_max = None
        self.ambient_temp_min = None
        self.child_action = None
        self.input_power = None
        self.input_power_avg = None
        self.input_power_max = None
        self.input_power_min = None
        self.input_voltage = None
        self.input_voltage_avg = None
        self.input_voltage_max = None
        self.input_voltage_min = None
        self.most_recent = None
        self.output_current = None
        self.output_current_avg = None
        self.output_current_max = None
        self.output_current_min = None
        self.output_power = None
        self.output_power_avg = None
        self.output_power_max = None
        self.output_power_min = None
        self.output_voltage = None
        self.output_voltage_avg = None
        self.output_voltage_max = None
        self.output_voltage_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "EquipmentRackUnitPsuStatsHist", parent_mo_or_dn, **kwargs)
