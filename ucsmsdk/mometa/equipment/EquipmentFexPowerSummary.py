"""This module contains the general information for EquipmentFexPowerSummary ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentFexPowerSummaryConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EquipmentFexPowerSummary(ManagedObject):
    """This is EquipmentFexPowerSummary class."""

    consts = EquipmentFexPowerSummaryConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentFexPowerSummary", "equipmentFexPowerSummary", "power-summary", VersionMeta.Version141i, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['equipmentFex'], ['equipmentFexPowerSummaryHist'], ["Get"])

    prop_meta = {
        "module_power": MoPropertyMeta("module_power", "ModulePower", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "module_power_avg": MoPropertyMeta("module_power_avg", "ModulePowerAvg", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "module_power_max": MoPropertyMeta("module_power_max", "ModulePowerMax", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "module_power_min": MoPropertyMeta("module_power_min", "ModulePowerMin", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "available_power": MoPropertyMeta("available_power", "availablePower", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "available_power_avg": MoPropertyMeta("available_power_avg", "availablePowerAvg", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "available_power_max": MoPropertyMeta("available_power_max", "availablePowerMax", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "available_power_min": MoPropertyMeta("available_power_min", "availablePowerMin", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "reserved_power": MoPropertyMeta("reserved_power", "reservedPower", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "reserved_power_avg": MoPropertyMeta("reserved_power_avg", "reservedPowerAvg", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "reserved_power_max": MoPropertyMeta("reserved_power_max", "reservedPowerMax", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "reserved_power_min": MoPropertyMeta("reserved_power_min", "reservedPowerMin", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "total_power": MoPropertyMeta("total_power", "totalPower", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total_power_avg": MoPropertyMeta("total_power_avg", "totalPowerAvg", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total_power_max": MoPropertyMeta("total_power_max", "totalPowerMax", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "total_power_min": MoPropertyMeta("total_power_min", "totalPowerMin", "float", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "ModulePower": "module_power", 
        "ModulePowerAvg": "module_power_avg", 
        "ModulePowerMax": "module_power_max", 
        "ModulePowerMin": "module_power_min", 
        "availablePower": "available_power", 
        "availablePowerAvg": "available_power_avg", 
        "availablePowerMax": "available_power_max", 
        "availablePowerMin": "available_power_min", 
        "childAction": "child_action", 
        "dn": "dn", 
        "intervals": "intervals", 
        "reservedPower": "reserved_power", 
        "reservedPowerAvg": "reserved_power_avg", 
        "reservedPowerMax": "reserved_power_max", 
        "reservedPowerMin": "reserved_power_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "totalPower": "total_power", 
        "totalPowerAvg": "total_power_avg", 
        "totalPowerMax": "total_power_max", 
        "totalPowerMin": "total_power_min", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.module_power = None
        self.module_power_avg = None
        self.module_power_max = None
        self.module_power_min = None
        self.available_power = None
        self.available_power_avg = None
        self.available_power_max = None
        self.available_power_min = None
        self.child_action = None
        self.intervals = None
        self.reserved_power = None
        self.reserved_power_avg = None
        self.reserved_power_max = None
        self.reserved_power_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.total_power = None
        self.total_power_avg = None
        self.total_power_max = None
        self.total_power_min = None
        self.update = None

        ManagedObject.__init__(self, "EquipmentFexPowerSummary", parent_mo_or_dn, **kwargs)
