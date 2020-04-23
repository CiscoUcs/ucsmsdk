"""This module contains the general information for EquipmentFexPsuInputStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentFexPsuInputStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EquipmentFexPsuInputStats(ManagedObject):
    """This is EquipmentFexPsuInputStats class."""

    consts = EquipmentFexPsuInputStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentFexPsuInputStats", "equipmentFexPsuInputStats", "fex-psu-input-stats", VersionMeta.Version141i, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['equipmentFex', 'equipmentPsu'], ['equipmentFexPsuInputStatsHist'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "current": MoPropertyMeta("current", "current", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "current_avg": MoPropertyMeta("current_avg", "currentAvg", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "current_max": MoPropertyMeta("current_max", "currentMax", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "current_min": MoPropertyMeta("current_min", "currentMin", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "input_status": MoPropertyMeta("input_status", "inputStatus", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "power": MoPropertyMeta("power", "power", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "power_avg": MoPropertyMeta("power_avg", "powerAvg", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "power_max": MoPropertyMeta("power_max", "powerMax", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "power_min": MoPropertyMeta("power_min", "powerMin", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "voltage": MoPropertyMeta("voltage", "voltage", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "voltage_avg": MoPropertyMeta("voltage_avg", "voltageAvg", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "voltage_max": MoPropertyMeta("voltage_max", "voltageMax", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "voltage_min": MoPropertyMeta("voltage_min", "voltageMin", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "current": "current", 
        "currentAvg": "current_avg", 
        "currentMax": "current_max", 
        "currentMin": "current_min", 
        "dn": "dn", 
        "inputStatus": "input_status", 
        "intervals": "intervals", 
        "power": "power", 
        "powerAvg": "power_avg", 
        "powerMax": "power_max", 
        "powerMin": "power_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
        "voltage": "voltage", 
        "voltageAvg": "voltage_avg", 
        "voltageMax": "voltage_max", 
        "voltageMin": "voltage_min", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.current = None
        self.current_avg = None
        self.current_max = None
        self.current_min = None
        self.input_status = None
        self.intervals = None
        self.power = None
        self.power_avg = None
        self.power_max = None
        self.power_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None
        self.voltage = None
        self.voltage_avg = None
        self.voltage_max = None
        self.voltage_min = None

        ManagedObject.__init__(self, "EquipmentFexPsuInputStats", parent_mo_or_dn, **kwargs)
