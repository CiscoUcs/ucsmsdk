"""This module contains the general information for ProcessorPCIBusStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ProcessorPCIBusStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ProcessorPCIBusStats(ManagedObject):
    """This is ProcessorPCIBusStats class."""

    consts = ProcessorPCIBusStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcessorPCIBusStats", "processorPCIBusStats", "pcibus-stats", VersionMeta.Version412a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['processorUnit'], [], [None])

    prop_meta = {
        "fch_uncorrectable_errors": MoPropertyMeta("fch_uncorrectable_errors", "FCHUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fch_uncorrectable_errors15_min": MoPropertyMeta("fch_uncorrectable_errors15_min", "FCHUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fch_uncorrectable_errors15_min_h": MoPropertyMeta("fch_uncorrectable_errors15_min_h", "FCHUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fch_uncorrectable_errors1_day": MoPropertyMeta("fch_uncorrectable_errors1_day", "FCHUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fch_uncorrectable_errors1_day_h": MoPropertyMeta("fch_uncorrectable_errors1_day_h", "FCHUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fch_uncorrectable_errors1_hour": MoPropertyMeta("fch_uncorrectable_errors1_hour", "FCHUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fch_uncorrectable_errors1_hour_h": MoPropertyMeta("fch_uncorrectable_errors1_hour_h", "FCHUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fch_uncorrectable_errors1_week": MoPropertyMeta("fch_uncorrectable_errors1_week", "FCHUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fch_uncorrectable_errors1_week_h": MoPropertyMeta("fch_uncorrectable_errors1_week_h", "FCHUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fch_uncorrectable_errors2_weeks": MoPropertyMeta("fch_uncorrectable_errors2_weeks", "FCHUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fch_uncorrectable_errors2_weeks_h": MoPropertyMeta("fch_uncorrectable_errors2_weeks_h", "FCHUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fc_hcorrectable_errors": MoPropertyMeta("fc_hcorrectable_errors", "FCHcorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fc_hcorrectable_errors15_min": MoPropertyMeta("fc_hcorrectable_errors15_min", "FCHcorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fc_hcorrectable_errors15_min_h": MoPropertyMeta("fc_hcorrectable_errors15_min_h", "FCHcorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fc_hcorrectable_errors1_day": MoPropertyMeta("fc_hcorrectable_errors1_day", "FCHcorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fc_hcorrectable_errors1_day_h": MoPropertyMeta("fc_hcorrectable_errors1_day_h", "FCHcorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fc_hcorrectable_errors1_hour": MoPropertyMeta("fc_hcorrectable_errors1_hour", "FCHcorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fc_hcorrectable_errors1_hour_h": MoPropertyMeta("fc_hcorrectable_errors1_hour_h", "FCHcorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fc_hcorrectable_errors1_week": MoPropertyMeta("fc_hcorrectable_errors1_week", "FCHcorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fc_hcorrectable_errors1_week_h": MoPropertyMeta("fc_hcorrectable_errors1_week_h", "FCHcorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fc_hcorrectable_errors2_weeks": MoPropertyMeta("fc_hcorrectable_errors2_weeks", "FCHcorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "fc_hcorrectable_errors2_weeks_h": MoPropertyMeta("fc_hcorrectable_errors2_weeks_h", "FCHcorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_correctable_errors": MoPropertyMeta("north_bridge_io_correctable_errors", "NorthBridgeIOCorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_correctable_errors15_min": MoPropertyMeta("north_bridge_io_correctable_errors15_min", "NorthBridgeIOCorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_correctable_errors15_min_h": MoPropertyMeta("north_bridge_io_correctable_errors15_min_h", "NorthBridgeIOCorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_correctable_errors1_day": MoPropertyMeta("north_bridge_io_correctable_errors1_day", "NorthBridgeIOCorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_correctable_errors1_day_h": MoPropertyMeta("north_bridge_io_correctable_errors1_day_h", "NorthBridgeIOCorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_correctable_errors1_hour": MoPropertyMeta("north_bridge_io_correctable_errors1_hour", "NorthBridgeIOCorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_correctable_errors1_hour_h": MoPropertyMeta("north_bridge_io_correctable_errors1_hour_h", "NorthBridgeIOCorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_correctable_errors1_week": MoPropertyMeta("north_bridge_io_correctable_errors1_week", "NorthBridgeIOCorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_correctable_errors1_week_h": MoPropertyMeta("north_bridge_io_correctable_errors1_week_h", "NorthBridgeIOCorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_correctable_errors2_weeks": MoPropertyMeta("north_bridge_io_correctable_errors2_weeks", "NorthBridgeIOCorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_correctable_errors2_weeks_h": MoPropertyMeta("north_bridge_io_correctable_errors2_weeks_h", "NorthBridgeIOCorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_uncorrectable_errors": MoPropertyMeta("north_bridge_io_uncorrectable_errors", "NorthBridgeIOUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_uncorrectable_errors15_min": MoPropertyMeta("north_bridge_io_uncorrectable_errors15_min", "NorthBridgeIOUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_uncorrectable_errors15_min_h": MoPropertyMeta("north_bridge_io_uncorrectable_errors15_min_h", "NorthBridgeIOUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_uncorrectable_errors1_day": MoPropertyMeta("north_bridge_io_uncorrectable_errors1_day", "NorthBridgeIOUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_uncorrectable_errors1_day_h": MoPropertyMeta("north_bridge_io_uncorrectable_errors1_day_h", "NorthBridgeIOUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_uncorrectable_errors1_hour": MoPropertyMeta("north_bridge_io_uncorrectable_errors1_hour", "NorthBridgeIOUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_uncorrectable_errors1_hour_h": MoPropertyMeta("north_bridge_io_uncorrectable_errors1_hour_h", "NorthBridgeIOUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_uncorrectable_errors1_week": MoPropertyMeta("north_bridge_io_uncorrectable_errors1_week", "NorthBridgeIOUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_uncorrectable_errors1_week_h": MoPropertyMeta("north_bridge_io_uncorrectable_errors1_week_h", "NorthBridgeIOUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_uncorrectable_errors2_weeks": MoPropertyMeta("north_bridge_io_uncorrectable_errors2_weeks", "NorthBridgeIOUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "north_bridge_io_uncorrectable_errors2_weeks_h": MoPropertyMeta("north_bridge_io_uncorrectable_errors2_weeks_h", "NorthBridgeIOUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "FCHUncorrectableErrors": "fch_uncorrectable_errors", 
        "FCHUncorrectableErrors15Min": "fch_uncorrectable_errors15_min", 
        "FCHUncorrectableErrors15MinH": "fch_uncorrectable_errors15_min_h", 
        "FCHUncorrectableErrors1Day": "fch_uncorrectable_errors1_day", 
        "FCHUncorrectableErrors1DayH": "fch_uncorrectable_errors1_day_h", 
        "FCHUncorrectableErrors1Hour": "fch_uncorrectable_errors1_hour", 
        "FCHUncorrectableErrors1HourH": "fch_uncorrectable_errors1_hour_h", 
        "FCHUncorrectableErrors1Week": "fch_uncorrectable_errors1_week", 
        "FCHUncorrectableErrors1WeekH": "fch_uncorrectable_errors1_week_h", 
        "FCHUncorrectableErrors2Weeks": "fch_uncorrectable_errors2_weeks", 
        "FCHUncorrectableErrors2WeeksH": "fch_uncorrectable_errors2_weeks_h", 
        "FCHcorrectableErrors": "fc_hcorrectable_errors", 
        "FCHcorrectableErrors15Min": "fc_hcorrectable_errors15_min", 
        "FCHcorrectableErrors15MinH": "fc_hcorrectable_errors15_min_h", 
        "FCHcorrectableErrors1Day": "fc_hcorrectable_errors1_day", 
        "FCHcorrectableErrors1DayH": "fc_hcorrectable_errors1_day_h", 
        "FCHcorrectableErrors1Hour": "fc_hcorrectable_errors1_hour", 
        "FCHcorrectableErrors1HourH": "fc_hcorrectable_errors1_hour_h", 
        "FCHcorrectableErrors1Week": "fc_hcorrectable_errors1_week", 
        "FCHcorrectableErrors1WeekH": "fc_hcorrectable_errors1_week_h", 
        "FCHcorrectableErrors2Weeks": "fc_hcorrectable_errors2_weeks", 
        "FCHcorrectableErrors2WeeksH": "fc_hcorrectable_errors2_weeks_h", 
        "NorthBridgeIOCorrectableErrors": "north_bridge_io_correctable_errors", 
        "NorthBridgeIOCorrectableErrors15Min": "north_bridge_io_correctable_errors15_min", 
        "NorthBridgeIOCorrectableErrors15MinH": "north_bridge_io_correctable_errors15_min_h", 
        "NorthBridgeIOCorrectableErrors1Day": "north_bridge_io_correctable_errors1_day", 
        "NorthBridgeIOCorrectableErrors1DayH": "north_bridge_io_correctable_errors1_day_h", 
        "NorthBridgeIOCorrectableErrors1Hour": "north_bridge_io_correctable_errors1_hour", 
        "NorthBridgeIOCorrectableErrors1HourH": "north_bridge_io_correctable_errors1_hour_h", 
        "NorthBridgeIOCorrectableErrors1Week": "north_bridge_io_correctable_errors1_week", 
        "NorthBridgeIOCorrectableErrors1WeekH": "north_bridge_io_correctable_errors1_week_h", 
        "NorthBridgeIOCorrectableErrors2Weeks": "north_bridge_io_correctable_errors2_weeks", 
        "NorthBridgeIOCorrectableErrors2WeeksH": "north_bridge_io_correctable_errors2_weeks_h", 
        "NorthBridgeIOUncorrectableErrors": "north_bridge_io_uncorrectable_errors", 
        "NorthBridgeIOUncorrectableErrors15Min": "north_bridge_io_uncorrectable_errors15_min", 
        "NorthBridgeIOUncorrectableErrors15MinH": "north_bridge_io_uncorrectable_errors15_min_h", 
        "NorthBridgeIOUncorrectableErrors1Day": "north_bridge_io_uncorrectable_errors1_day", 
        "NorthBridgeIOUncorrectableErrors1DayH": "north_bridge_io_uncorrectable_errors1_day_h", 
        "NorthBridgeIOUncorrectableErrors1Hour": "north_bridge_io_uncorrectable_errors1_hour", 
        "NorthBridgeIOUncorrectableErrors1HourH": "north_bridge_io_uncorrectable_errors1_hour_h", 
        "NorthBridgeIOUncorrectableErrors1Week": "north_bridge_io_uncorrectable_errors1_week", 
        "NorthBridgeIOUncorrectableErrors1WeekH": "north_bridge_io_uncorrectable_errors1_week_h", 
        "NorthBridgeIOUncorrectableErrors2Weeks": "north_bridge_io_uncorrectable_errors2_weeks", 
        "NorthBridgeIOUncorrectableErrors2WeeksH": "north_bridge_io_uncorrectable_errors2_weeks_h", 
        "childAction": "child_action", 
        "dn": "dn", 
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
        self.fch_uncorrectable_errors = None
        self.fch_uncorrectable_errors15_min = None
        self.fch_uncorrectable_errors15_min_h = None
        self.fch_uncorrectable_errors1_day = None
        self.fch_uncorrectable_errors1_day_h = None
        self.fch_uncorrectable_errors1_hour = None
        self.fch_uncorrectable_errors1_hour_h = None
        self.fch_uncorrectable_errors1_week = None
        self.fch_uncorrectable_errors1_week_h = None
        self.fch_uncorrectable_errors2_weeks = None
        self.fch_uncorrectable_errors2_weeks_h = None
        self.fc_hcorrectable_errors = None
        self.fc_hcorrectable_errors15_min = None
        self.fc_hcorrectable_errors15_min_h = None
        self.fc_hcorrectable_errors1_day = None
        self.fc_hcorrectable_errors1_day_h = None
        self.fc_hcorrectable_errors1_hour = None
        self.fc_hcorrectable_errors1_hour_h = None
        self.fc_hcorrectable_errors1_week = None
        self.fc_hcorrectable_errors1_week_h = None
        self.fc_hcorrectable_errors2_weeks = None
        self.fc_hcorrectable_errors2_weeks_h = None
        self.north_bridge_io_correctable_errors = None
        self.north_bridge_io_correctable_errors15_min = None
        self.north_bridge_io_correctable_errors15_min_h = None
        self.north_bridge_io_correctable_errors1_day = None
        self.north_bridge_io_correctable_errors1_day_h = None
        self.north_bridge_io_correctable_errors1_hour = None
        self.north_bridge_io_correctable_errors1_hour_h = None
        self.north_bridge_io_correctable_errors1_week = None
        self.north_bridge_io_correctable_errors1_week_h = None
        self.north_bridge_io_correctable_errors2_weeks = None
        self.north_bridge_io_correctable_errors2_weeks_h = None
        self.north_bridge_io_uncorrectable_errors = None
        self.north_bridge_io_uncorrectable_errors15_min = None
        self.north_bridge_io_uncorrectable_errors15_min_h = None
        self.north_bridge_io_uncorrectable_errors1_day = None
        self.north_bridge_io_uncorrectable_errors1_day_h = None
        self.north_bridge_io_uncorrectable_errors1_hour = None
        self.north_bridge_io_uncorrectable_errors1_hour_h = None
        self.north_bridge_io_uncorrectable_errors1_week = None
        self.north_bridge_io_uncorrectable_errors1_week_h = None
        self.north_bridge_io_uncorrectable_errors2_weeks = None
        self.north_bridge_io_uncorrectable_errors2_weeks_h = None
        self.child_action = None
        self.intervals = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "ProcessorPCIBusStats", parent_mo_or_dn, **kwargs)
