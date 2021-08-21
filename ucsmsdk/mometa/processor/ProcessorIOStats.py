"""This module contains the general information for ProcessorIOStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ProcessorIOStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ProcessorIOStats(ManagedObject):
    """This is ProcessorIOStats class."""

    consts = ProcessorIOStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcessorIOStats", "processorIOStats", "io-stats", VersionMeta.Version412a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['processorUnit'], [], [None])

    prop_meta = {
        "pc_ie_bank_correctable_errors": MoPropertyMeta("pc_ie_bank_correctable_errors", "PCIeBankCorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_correctable_errors15_min": MoPropertyMeta("pc_ie_bank_correctable_errors15_min", "PCIeBankCorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_correctable_errors15_min_h": MoPropertyMeta("pc_ie_bank_correctable_errors15_min_h", "PCIeBankCorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_correctable_errors1_day": MoPropertyMeta("pc_ie_bank_correctable_errors1_day", "PCIeBankCorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_correctable_errors1_day_h": MoPropertyMeta("pc_ie_bank_correctable_errors1_day_h", "PCIeBankCorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_correctable_errors1_hour": MoPropertyMeta("pc_ie_bank_correctable_errors1_hour", "PCIeBankCorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_correctable_errors1_hour_h": MoPropertyMeta("pc_ie_bank_correctable_errors1_hour_h", "PCIeBankCorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_correctable_errors1_week": MoPropertyMeta("pc_ie_bank_correctable_errors1_week", "PCIeBankCorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_correctable_errors1_week_h": MoPropertyMeta("pc_ie_bank_correctable_errors1_week_h", "PCIeBankCorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_correctable_errors2_weeks": MoPropertyMeta("pc_ie_bank_correctable_errors2_weeks", "PCIeBankCorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_correctable_errors2_weeks_h": MoPropertyMeta("pc_ie_bank_correctable_errors2_weeks_h", "PCIeBankCorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_uncorrectable_errors": MoPropertyMeta("pc_ie_bank_uncorrectable_errors", "PCIeBankUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_uncorrectable_errors15_min": MoPropertyMeta("pc_ie_bank_uncorrectable_errors15_min", "PCIeBankUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_uncorrectable_errors15_min_h": MoPropertyMeta("pc_ie_bank_uncorrectable_errors15_min_h", "PCIeBankUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_uncorrectable_errors1_day": MoPropertyMeta("pc_ie_bank_uncorrectable_errors1_day", "PCIeBankUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_uncorrectable_errors1_day_h": MoPropertyMeta("pc_ie_bank_uncorrectable_errors1_day_h", "PCIeBankUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_uncorrectable_errors1_hour": MoPropertyMeta("pc_ie_bank_uncorrectable_errors1_hour", "PCIeBankUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_uncorrectable_errors1_hour_h": MoPropertyMeta("pc_ie_bank_uncorrectable_errors1_hour_h", "PCIeBankUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_uncorrectable_errors1_week": MoPropertyMeta("pc_ie_bank_uncorrectable_errors1_week", "PCIeBankUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_uncorrectable_errors1_week_h": MoPropertyMeta("pc_ie_bank_uncorrectable_errors1_week_h", "PCIeBankUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_uncorrectable_errors2_weeks": MoPropertyMeta("pc_ie_bank_uncorrectable_errors2_weeks", "PCIeBankUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "pc_ie_bank_uncorrectable_errors2_weeks_h": MoPropertyMeta("pc_ie_bank_uncorrectable_errors2_weeks_h", "PCIeBankUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sata_uncorrectable_errors": MoPropertyMeta("sata_uncorrectable_errors", "SATAUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sata_uncorrectable_errors15_min": MoPropertyMeta("sata_uncorrectable_errors15_min", "SATAUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sata_uncorrectable_errors15_min_h": MoPropertyMeta("sata_uncorrectable_errors15_min_h", "SATAUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sata_uncorrectable_errors1_day": MoPropertyMeta("sata_uncorrectable_errors1_day", "SATAUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sata_uncorrectable_errors1_day_h": MoPropertyMeta("sata_uncorrectable_errors1_day_h", "SATAUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sata_uncorrectable_errors1_hour": MoPropertyMeta("sata_uncorrectable_errors1_hour", "SATAUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sata_uncorrectable_errors1_hour_h": MoPropertyMeta("sata_uncorrectable_errors1_hour_h", "SATAUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sata_uncorrectable_errors1_week": MoPropertyMeta("sata_uncorrectable_errors1_week", "SATAUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sata_uncorrectable_errors1_week_h": MoPropertyMeta("sata_uncorrectable_errors1_week_h", "SATAUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sata_uncorrectable_errors2_weeks": MoPropertyMeta("sata_uncorrectable_errors2_weeks", "SATAUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sata_uncorrectable_errors2_weeks_h": MoPropertyMeta("sata_uncorrectable_errors2_weeks_h", "SATAUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sat_acorrectable_errors": MoPropertyMeta("sat_acorrectable_errors", "SATAcorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sat_acorrectable_errors15_min": MoPropertyMeta("sat_acorrectable_errors15_min", "SATAcorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sat_acorrectable_errors15_min_h": MoPropertyMeta("sat_acorrectable_errors15_min_h", "SATAcorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sat_acorrectable_errors1_day": MoPropertyMeta("sat_acorrectable_errors1_day", "SATAcorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sat_acorrectable_errors1_day_h": MoPropertyMeta("sat_acorrectable_errors1_day_h", "SATAcorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sat_acorrectable_errors1_hour": MoPropertyMeta("sat_acorrectable_errors1_hour", "SATAcorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sat_acorrectable_errors1_hour_h": MoPropertyMeta("sat_acorrectable_errors1_hour_h", "SATAcorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sat_acorrectable_errors1_week": MoPropertyMeta("sat_acorrectable_errors1_week", "SATAcorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sat_acorrectable_errors1_week_h": MoPropertyMeta("sat_acorrectable_errors1_week_h", "SATAcorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sat_acorrectable_errors2_weeks": MoPropertyMeta("sat_acorrectable_errors2_weeks", "SATAcorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sat_acorrectable_errors2_weeks_h": MoPropertyMeta("sat_acorrectable_errors2_weeks_h", "SATAcorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smn_uncorrectable_errors": MoPropertyMeta("smn_uncorrectable_errors", "SMNUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smn_uncorrectable_errors15_min": MoPropertyMeta("smn_uncorrectable_errors15_min", "SMNUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smn_uncorrectable_errors15_min_h": MoPropertyMeta("smn_uncorrectable_errors15_min_h", "SMNUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smn_uncorrectable_errors1_day": MoPropertyMeta("smn_uncorrectable_errors1_day", "SMNUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smn_uncorrectable_errors1_day_h": MoPropertyMeta("smn_uncorrectable_errors1_day_h", "SMNUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smn_uncorrectable_errors1_hour": MoPropertyMeta("smn_uncorrectable_errors1_hour", "SMNUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smn_uncorrectable_errors1_hour_h": MoPropertyMeta("smn_uncorrectable_errors1_hour_h", "SMNUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smn_uncorrectable_errors1_week": MoPropertyMeta("smn_uncorrectable_errors1_week", "SMNUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smn_uncorrectable_errors1_week_h": MoPropertyMeta("smn_uncorrectable_errors1_week_h", "SMNUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smn_uncorrectable_errors2_weeks": MoPropertyMeta("smn_uncorrectable_errors2_weeks", "SMNUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smn_uncorrectable_errors2_weeks_h": MoPropertyMeta("smn_uncorrectable_errors2_weeks_h", "SMNUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sm_ncorrectable_errors": MoPropertyMeta("sm_ncorrectable_errors", "SMNcorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sm_ncorrectable_errors15_min": MoPropertyMeta("sm_ncorrectable_errors15_min", "SMNcorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sm_ncorrectable_errors15_min_h": MoPropertyMeta("sm_ncorrectable_errors15_min_h", "SMNcorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sm_ncorrectable_errors1_day": MoPropertyMeta("sm_ncorrectable_errors1_day", "SMNcorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sm_ncorrectable_errors1_day_h": MoPropertyMeta("sm_ncorrectable_errors1_day_h", "SMNcorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sm_ncorrectable_errors1_hour": MoPropertyMeta("sm_ncorrectable_errors1_hour", "SMNcorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sm_ncorrectable_errors1_hour_h": MoPropertyMeta("sm_ncorrectable_errors1_hour_h", "SMNcorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sm_ncorrectable_errors1_week": MoPropertyMeta("sm_ncorrectable_errors1_week", "SMNcorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sm_ncorrectable_errors1_week_h": MoPropertyMeta("sm_ncorrectable_errors1_week_h", "SMNcorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sm_ncorrectable_errors2_weeks": MoPropertyMeta("sm_ncorrectable_errors2_weeks", "SMNcorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sm_ncorrectable_errors2_weeks_h": MoPropertyMeta("sm_ncorrectable_errors2_weeks_h", "SMNcorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "usb_uncorrectable_errors": MoPropertyMeta("usb_uncorrectable_errors", "USBUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "usb_uncorrectable_errors15_min": MoPropertyMeta("usb_uncorrectable_errors15_min", "USBUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "usb_uncorrectable_errors15_min_h": MoPropertyMeta("usb_uncorrectable_errors15_min_h", "USBUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "usb_uncorrectable_errors1_day": MoPropertyMeta("usb_uncorrectable_errors1_day", "USBUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "usb_uncorrectable_errors1_day_h": MoPropertyMeta("usb_uncorrectable_errors1_day_h", "USBUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "usb_uncorrectable_errors1_hour": MoPropertyMeta("usb_uncorrectable_errors1_hour", "USBUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "usb_uncorrectable_errors1_hour_h": MoPropertyMeta("usb_uncorrectable_errors1_hour_h", "USBUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "usb_uncorrectable_errors1_week": MoPropertyMeta("usb_uncorrectable_errors1_week", "USBUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "usb_uncorrectable_errors1_week_h": MoPropertyMeta("usb_uncorrectable_errors1_week_h", "USBUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "usb_uncorrectable_errors2_weeks": MoPropertyMeta("usb_uncorrectable_errors2_weeks", "USBUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "usb_uncorrectable_errors2_weeks_h": MoPropertyMeta("usb_uncorrectable_errors2_weeks_h", "USBUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "us_bcorrectable_errors": MoPropertyMeta("us_bcorrectable_errors", "USBcorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "us_bcorrectable_errors15_min": MoPropertyMeta("us_bcorrectable_errors15_min", "USBcorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "us_bcorrectable_errors15_min_h": MoPropertyMeta("us_bcorrectable_errors15_min_h", "USBcorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "us_bcorrectable_errors1_day": MoPropertyMeta("us_bcorrectable_errors1_day", "USBcorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "us_bcorrectable_errors1_day_h": MoPropertyMeta("us_bcorrectable_errors1_day_h", "USBcorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "us_bcorrectable_errors1_hour": MoPropertyMeta("us_bcorrectable_errors1_hour", "USBcorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "us_bcorrectable_errors1_hour_h": MoPropertyMeta("us_bcorrectable_errors1_hour_h", "USBcorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "us_bcorrectable_errors1_week": MoPropertyMeta("us_bcorrectable_errors1_week", "USBcorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "us_bcorrectable_errors1_week_h": MoPropertyMeta("us_bcorrectable_errors1_week_h", "USBcorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "us_bcorrectable_errors2_weeks": MoPropertyMeta("us_bcorrectable_errors2_weeks", "USBcorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "us_bcorrectable_errors2_weeks_h": MoPropertyMeta("us_bcorrectable_errors2_weeks_h", "USBcorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
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
        "PCIeBankCorrectableErrors": "pc_ie_bank_correctable_errors", 
        "PCIeBankCorrectableErrors15Min": "pc_ie_bank_correctable_errors15_min", 
        "PCIeBankCorrectableErrors15MinH": "pc_ie_bank_correctable_errors15_min_h", 
        "PCIeBankCorrectableErrors1Day": "pc_ie_bank_correctable_errors1_day", 
        "PCIeBankCorrectableErrors1DayH": "pc_ie_bank_correctable_errors1_day_h", 
        "PCIeBankCorrectableErrors1Hour": "pc_ie_bank_correctable_errors1_hour", 
        "PCIeBankCorrectableErrors1HourH": "pc_ie_bank_correctable_errors1_hour_h", 
        "PCIeBankCorrectableErrors1Week": "pc_ie_bank_correctable_errors1_week", 
        "PCIeBankCorrectableErrors1WeekH": "pc_ie_bank_correctable_errors1_week_h", 
        "PCIeBankCorrectableErrors2Weeks": "pc_ie_bank_correctable_errors2_weeks", 
        "PCIeBankCorrectableErrors2WeeksH": "pc_ie_bank_correctable_errors2_weeks_h", 
        "PCIeBankUncorrectableErrors": "pc_ie_bank_uncorrectable_errors", 
        "PCIeBankUncorrectableErrors15Min": "pc_ie_bank_uncorrectable_errors15_min", 
        "PCIeBankUncorrectableErrors15MinH": "pc_ie_bank_uncorrectable_errors15_min_h", 
        "PCIeBankUncorrectableErrors1Day": "pc_ie_bank_uncorrectable_errors1_day", 
        "PCIeBankUncorrectableErrors1DayH": "pc_ie_bank_uncorrectable_errors1_day_h", 
        "PCIeBankUncorrectableErrors1Hour": "pc_ie_bank_uncorrectable_errors1_hour", 
        "PCIeBankUncorrectableErrors1HourH": "pc_ie_bank_uncorrectable_errors1_hour_h", 
        "PCIeBankUncorrectableErrors1Week": "pc_ie_bank_uncorrectable_errors1_week", 
        "PCIeBankUncorrectableErrors1WeekH": "pc_ie_bank_uncorrectable_errors1_week_h", 
        "PCIeBankUncorrectableErrors2Weeks": "pc_ie_bank_uncorrectable_errors2_weeks", 
        "PCIeBankUncorrectableErrors2WeeksH": "pc_ie_bank_uncorrectable_errors2_weeks_h", 
        "SATAUncorrectableErrors": "sata_uncorrectable_errors", 
        "SATAUncorrectableErrors15Min": "sata_uncorrectable_errors15_min", 
        "SATAUncorrectableErrors15MinH": "sata_uncorrectable_errors15_min_h", 
        "SATAUncorrectableErrors1Day": "sata_uncorrectable_errors1_day", 
        "SATAUncorrectableErrors1DayH": "sata_uncorrectable_errors1_day_h", 
        "SATAUncorrectableErrors1Hour": "sata_uncorrectable_errors1_hour", 
        "SATAUncorrectableErrors1HourH": "sata_uncorrectable_errors1_hour_h", 
        "SATAUncorrectableErrors1Week": "sata_uncorrectable_errors1_week", 
        "SATAUncorrectableErrors1WeekH": "sata_uncorrectable_errors1_week_h", 
        "SATAUncorrectableErrors2Weeks": "sata_uncorrectable_errors2_weeks", 
        "SATAUncorrectableErrors2WeeksH": "sata_uncorrectable_errors2_weeks_h", 
        "SATAcorrectableErrors": "sat_acorrectable_errors", 
        "SATAcorrectableErrors15Min": "sat_acorrectable_errors15_min", 
        "SATAcorrectableErrors15MinH": "sat_acorrectable_errors15_min_h", 
        "SATAcorrectableErrors1Day": "sat_acorrectable_errors1_day", 
        "SATAcorrectableErrors1DayH": "sat_acorrectable_errors1_day_h", 
        "SATAcorrectableErrors1Hour": "sat_acorrectable_errors1_hour", 
        "SATAcorrectableErrors1HourH": "sat_acorrectable_errors1_hour_h", 
        "SATAcorrectableErrors1Week": "sat_acorrectable_errors1_week", 
        "SATAcorrectableErrors1WeekH": "sat_acorrectable_errors1_week_h", 
        "SATAcorrectableErrors2Weeks": "sat_acorrectable_errors2_weeks", 
        "SATAcorrectableErrors2WeeksH": "sat_acorrectable_errors2_weeks_h", 
        "SMNUncorrectableErrors": "smn_uncorrectable_errors", 
        "SMNUncorrectableErrors15Min": "smn_uncorrectable_errors15_min", 
        "SMNUncorrectableErrors15MinH": "smn_uncorrectable_errors15_min_h", 
        "SMNUncorrectableErrors1Day": "smn_uncorrectable_errors1_day", 
        "SMNUncorrectableErrors1DayH": "smn_uncorrectable_errors1_day_h", 
        "SMNUncorrectableErrors1Hour": "smn_uncorrectable_errors1_hour", 
        "SMNUncorrectableErrors1HourH": "smn_uncorrectable_errors1_hour_h", 
        "SMNUncorrectableErrors1Week": "smn_uncorrectable_errors1_week", 
        "SMNUncorrectableErrors1WeekH": "smn_uncorrectable_errors1_week_h", 
        "SMNUncorrectableErrors2Weeks": "smn_uncorrectable_errors2_weeks", 
        "SMNUncorrectableErrors2WeeksH": "smn_uncorrectable_errors2_weeks_h", 
        "SMNcorrectableErrors": "sm_ncorrectable_errors", 
        "SMNcorrectableErrors15Min": "sm_ncorrectable_errors15_min", 
        "SMNcorrectableErrors15MinH": "sm_ncorrectable_errors15_min_h", 
        "SMNcorrectableErrors1Day": "sm_ncorrectable_errors1_day", 
        "SMNcorrectableErrors1DayH": "sm_ncorrectable_errors1_day_h", 
        "SMNcorrectableErrors1Hour": "sm_ncorrectable_errors1_hour", 
        "SMNcorrectableErrors1HourH": "sm_ncorrectable_errors1_hour_h", 
        "SMNcorrectableErrors1Week": "sm_ncorrectable_errors1_week", 
        "SMNcorrectableErrors1WeekH": "sm_ncorrectable_errors1_week_h", 
        "SMNcorrectableErrors2Weeks": "sm_ncorrectable_errors2_weeks", 
        "SMNcorrectableErrors2WeeksH": "sm_ncorrectable_errors2_weeks_h", 
        "USBUncorrectableErrors": "usb_uncorrectable_errors", 
        "USBUncorrectableErrors15Min": "usb_uncorrectable_errors15_min", 
        "USBUncorrectableErrors15MinH": "usb_uncorrectable_errors15_min_h", 
        "USBUncorrectableErrors1Day": "usb_uncorrectable_errors1_day", 
        "USBUncorrectableErrors1DayH": "usb_uncorrectable_errors1_day_h", 
        "USBUncorrectableErrors1Hour": "usb_uncorrectable_errors1_hour", 
        "USBUncorrectableErrors1HourH": "usb_uncorrectable_errors1_hour_h", 
        "USBUncorrectableErrors1Week": "usb_uncorrectable_errors1_week", 
        "USBUncorrectableErrors1WeekH": "usb_uncorrectable_errors1_week_h", 
        "USBUncorrectableErrors2Weeks": "usb_uncorrectable_errors2_weeks", 
        "USBUncorrectableErrors2WeeksH": "usb_uncorrectable_errors2_weeks_h", 
        "USBcorrectableErrors": "us_bcorrectable_errors", 
        "USBcorrectableErrors15Min": "us_bcorrectable_errors15_min", 
        "USBcorrectableErrors15MinH": "us_bcorrectable_errors15_min_h", 
        "USBcorrectableErrors1Day": "us_bcorrectable_errors1_day", 
        "USBcorrectableErrors1DayH": "us_bcorrectable_errors1_day_h", 
        "USBcorrectableErrors1Hour": "us_bcorrectable_errors1_hour", 
        "USBcorrectableErrors1HourH": "us_bcorrectable_errors1_hour_h", 
        "USBcorrectableErrors1Week": "us_bcorrectable_errors1_week", 
        "USBcorrectableErrors1WeekH": "us_bcorrectable_errors1_week_h", 
        "USBcorrectableErrors2Weeks": "us_bcorrectable_errors2_weeks", 
        "USBcorrectableErrors2WeeksH": "us_bcorrectable_errors2_weeks_h", 
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
        self.pc_ie_bank_correctable_errors = None
        self.pc_ie_bank_correctable_errors15_min = None
        self.pc_ie_bank_correctable_errors15_min_h = None
        self.pc_ie_bank_correctable_errors1_day = None
        self.pc_ie_bank_correctable_errors1_day_h = None
        self.pc_ie_bank_correctable_errors1_hour = None
        self.pc_ie_bank_correctable_errors1_hour_h = None
        self.pc_ie_bank_correctable_errors1_week = None
        self.pc_ie_bank_correctable_errors1_week_h = None
        self.pc_ie_bank_correctable_errors2_weeks = None
        self.pc_ie_bank_correctable_errors2_weeks_h = None
        self.pc_ie_bank_uncorrectable_errors = None
        self.pc_ie_bank_uncorrectable_errors15_min = None
        self.pc_ie_bank_uncorrectable_errors15_min_h = None
        self.pc_ie_bank_uncorrectable_errors1_day = None
        self.pc_ie_bank_uncorrectable_errors1_day_h = None
        self.pc_ie_bank_uncorrectable_errors1_hour = None
        self.pc_ie_bank_uncorrectable_errors1_hour_h = None
        self.pc_ie_bank_uncorrectable_errors1_week = None
        self.pc_ie_bank_uncorrectable_errors1_week_h = None
        self.pc_ie_bank_uncorrectable_errors2_weeks = None
        self.pc_ie_bank_uncorrectable_errors2_weeks_h = None
        self.sata_uncorrectable_errors = None
        self.sata_uncorrectable_errors15_min = None
        self.sata_uncorrectable_errors15_min_h = None
        self.sata_uncorrectable_errors1_day = None
        self.sata_uncorrectable_errors1_day_h = None
        self.sata_uncorrectable_errors1_hour = None
        self.sata_uncorrectable_errors1_hour_h = None
        self.sata_uncorrectable_errors1_week = None
        self.sata_uncorrectable_errors1_week_h = None
        self.sata_uncorrectable_errors2_weeks = None
        self.sata_uncorrectable_errors2_weeks_h = None
        self.sat_acorrectable_errors = None
        self.sat_acorrectable_errors15_min = None
        self.sat_acorrectable_errors15_min_h = None
        self.sat_acorrectable_errors1_day = None
        self.sat_acorrectable_errors1_day_h = None
        self.sat_acorrectable_errors1_hour = None
        self.sat_acorrectable_errors1_hour_h = None
        self.sat_acorrectable_errors1_week = None
        self.sat_acorrectable_errors1_week_h = None
        self.sat_acorrectable_errors2_weeks = None
        self.sat_acorrectable_errors2_weeks_h = None
        self.smn_uncorrectable_errors = None
        self.smn_uncorrectable_errors15_min = None
        self.smn_uncorrectable_errors15_min_h = None
        self.smn_uncorrectable_errors1_day = None
        self.smn_uncorrectable_errors1_day_h = None
        self.smn_uncorrectable_errors1_hour = None
        self.smn_uncorrectable_errors1_hour_h = None
        self.smn_uncorrectable_errors1_week = None
        self.smn_uncorrectable_errors1_week_h = None
        self.smn_uncorrectable_errors2_weeks = None
        self.smn_uncorrectable_errors2_weeks_h = None
        self.sm_ncorrectable_errors = None
        self.sm_ncorrectable_errors15_min = None
        self.sm_ncorrectable_errors15_min_h = None
        self.sm_ncorrectable_errors1_day = None
        self.sm_ncorrectable_errors1_day_h = None
        self.sm_ncorrectable_errors1_hour = None
        self.sm_ncorrectable_errors1_hour_h = None
        self.sm_ncorrectable_errors1_week = None
        self.sm_ncorrectable_errors1_week_h = None
        self.sm_ncorrectable_errors2_weeks = None
        self.sm_ncorrectable_errors2_weeks_h = None
        self.usb_uncorrectable_errors = None
        self.usb_uncorrectable_errors15_min = None
        self.usb_uncorrectable_errors15_min_h = None
        self.usb_uncorrectable_errors1_day = None
        self.usb_uncorrectable_errors1_day_h = None
        self.usb_uncorrectable_errors1_hour = None
        self.usb_uncorrectable_errors1_hour_h = None
        self.usb_uncorrectable_errors1_week = None
        self.usb_uncorrectable_errors1_week_h = None
        self.usb_uncorrectable_errors2_weeks = None
        self.usb_uncorrectable_errors2_weeks_h = None
        self.us_bcorrectable_errors = None
        self.us_bcorrectable_errors15_min = None
        self.us_bcorrectable_errors15_min_h = None
        self.us_bcorrectable_errors1_day = None
        self.us_bcorrectable_errors1_day_h = None
        self.us_bcorrectable_errors1_hour = None
        self.us_bcorrectable_errors1_hour_h = None
        self.us_bcorrectable_errors1_week = None
        self.us_bcorrectable_errors1_week_h = None
        self.us_bcorrectable_errors2_weeks = None
        self.us_bcorrectable_errors2_weeks_h = None
        self.child_action = None
        self.intervals = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "ProcessorIOStats", parent_mo_or_dn, **kwargs)
