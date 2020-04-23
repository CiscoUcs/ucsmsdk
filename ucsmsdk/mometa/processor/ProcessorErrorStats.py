"""This module contains the general information for ProcessorErrorStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ProcessorErrorStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ProcessorErrorStats(ManagedObject):
    """This is ProcessorErrorStats class."""

    consts = ProcessorErrorStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcessorErrorStats", "processorErrorStats", "error-stats", VersionMeta.Version131c, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['processorUnit'], [], ["Get"])

    prop_meta = {
        "correctable_link_crc_errors": MoPropertyMeta("correctable_link_crc_errors", "CorrectableLinkCRCErrors", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "correctable_link_crc_errors15_min": MoPropertyMeta("correctable_link_crc_errors15_min", "CorrectableLinkCRCErrors15Min", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "correctable_link_crc_errors15_min_h": MoPropertyMeta("correctable_link_crc_errors15_min_h", "CorrectableLinkCRCErrors15MinH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "correctable_link_crc_errors1_day": MoPropertyMeta("correctable_link_crc_errors1_day", "CorrectableLinkCRCErrors1Day", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "correctable_link_crc_errors1_day_h": MoPropertyMeta("correctable_link_crc_errors1_day_h", "CorrectableLinkCRCErrors1DayH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "correctable_link_crc_errors1_hour": MoPropertyMeta("correctable_link_crc_errors1_hour", "CorrectableLinkCRCErrors1Hour", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "correctable_link_crc_errors1_hour_h": MoPropertyMeta("correctable_link_crc_errors1_hour_h", "CorrectableLinkCRCErrors1HourH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "correctable_link_crc_errors1_week": MoPropertyMeta("correctable_link_crc_errors1_week", "CorrectableLinkCRCErrors1Week", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "correctable_link_crc_errors1_week_h": MoPropertyMeta("correctable_link_crc_errors1_week_h", "CorrectableLinkCRCErrors1WeekH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "correctable_link_crc_errors2_weeks": MoPropertyMeta("correctable_link_crc_errors2_weeks", "CorrectableLinkCRCErrors2Weeks", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "correctable_link_crc_errors2_weeks_h": MoPropertyMeta("correctable_link_crc_errors2_weeks_h", "CorrectableLinkCRCErrors2WeeksH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncorrectable_link_crc_errors": MoPropertyMeta("uncorrectable_link_crc_errors", "UncorrectableLinkCRCErrors", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncorrectable_link_crc_errors15_min": MoPropertyMeta("uncorrectable_link_crc_errors15_min", "UncorrectableLinkCRCErrors15Min", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncorrectable_link_crc_errors15_min_h": MoPropertyMeta("uncorrectable_link_crc_errors15_min_h", "UncorrectableLinkCRCErrors15MinH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncorrectable_link_crc_errors1_day": MoPropertyMeta("uncorrectable_link_crc_errors1_day", "UncorrectableLinkCRCErrors1Day", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncorrectable_link_crc_errors1_day_h": MoPropertyMeta("uncorrectable_link_crc_errors1_day_h", "UncorrectableLinkCRCErrors1DayH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncorrectable_link_crc_errors1_hour": MoPropertyMeta("uncorrectable_link_crc_errors1_hour", "UncorrectableLinkCRCErrors1Hour", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncorrectable_link_crc_errors1_hour_h": MoPropertyMeta("uncorrectable_link_crc_errors1_hour_h", "UncorrectableLinkCRCErrors1HourH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncorrectable_link_crc_errors1_week": MoPropertyMeta("uncorrectable_link_crc_errors1_week", "UncorrectableLinkCRCErrors1Week", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncorrectable_link_crc_errors1_week_h": MoPropertyMeta("uncorrectable_link_crc_errors1_week_h", "UncorrectableLinkCRCErrors1WeekH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncorrectable_link_crc_errors2_weeks": MoPropertyMeta("uncorrectable_link_crc_errors2_weeks", "UncorrectableLinkCRCErrors2Weeks", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "uncorrectable_link_crc_errors2_weeks_h": MoPropertyMeta("uncorrectable_link_crc_errors2_weeks_h", "UncorrectableLinkCRCErrors2WeeksH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_inter_sock_errors": MoPropertyMeta("mirroring_inter_sock_errors", "mirroringInterSockErrors", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_inter_sock_errors15_min": MoPropertyMeta("mirroring_inter_sock_errors15_min", "mirroringInterSockErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_inter_sock_errors15_min_h": MoPropertyMeta("mirroring_inter_sock_errors15_min_h", "mirroringInterSockErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_inter_sock_errors1_day": MoPropertyMeta("mirroring_inter_sock_errors1_day", "mirroringInterSockErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_inter_sock_errors1_day_h": MoPropertyMeta("mirroring_inter_sock_errors1_day_h", "mirroringInterSockErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_inter_sock_errors1_hour": MoPropertyMeta("mirroring_inter_sock_errors1_hour", "mirroringInterSockErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_inter_sock_errors1_hour_h": MoPropertyMeta("mirroring_inter_sock_errors1_hour_h", "mirroringInterSockErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_inter_sock_errors1_week": MoPropertyMeta("mirroring_inter_sock_errors1_week", "mirroringInterSockErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_inter_sock_errors1_week_h": MoPropertyMeta("mirroring_inter_sock_errors1_week_h", "mirroringInterSockErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_inter_sock_errors2_weeks": MoPropertyMeta("mirroring_inter_sock_errors2_weeks", "mirroringInterSockErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_inter_sock_errors2_weeks_h": MoPropertyMeta("mirroring_inter_sock_errors2_weeks_h", "mirroringInterSockErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_intra_sock_errors": MoPropertyMeta("mirroring_intra_sock_errors", "mirroringIntraSockErrors", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_intra_sock_errors15_min": MoPropertyMeta("mirroring_intra_sock_errors15_min", "mirroringIntraSockErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_intra_sock_errors15_min_h": MoPropertyMeta("mirroring_intra_sock_errors15_min_h", "mirroringIntraSockErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_intra_sock_errors1_day": MoPropertyMeta("mirroring_intra_sock_errors1_day", "mirroringIntraSockErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_intra_sock_errors1_day_h": MoPropertyMeta("mirroring_intra_sock_errors1_day_h", "mirroringIntraSockErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_intra_sock_errors1_hour": MoPropertyMeta("mirroring_intra_sock_errors1_hour", "mirroringIntraSockErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_intra_sock_errors1_hour_h": MoPropertyMeta("mirroring_intra_sock_errors1_hour_h", "mirroringIntraSockErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_intra_sock_errors1_week": MoPropertyMeta("mirroring_intra_sock_errors1_week", "mirroringIntraSockErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_intra_sock_errors1_week_h": MoPropertyMeta("mirroring_intra_sock_errors1_week_h", "mirroringIntraSockErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_intra_sock_errors2_weeks": MoPropertyMeta("mirroring_intra_sock_errors2_weeks", "mirroringIntraSockErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mirroring_intra_sock_errors2_weeks_h": MoPropertyMeta("mirroring_intra_sock_errors2_weeks_h", "mirroringIntraSockErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "smi_link_corr_errors": MoPropertyMeta("smi_link_corr_errors", "smiLinkCorrErrors", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_corr_errors15_min": MoPropertyMeta("smi_link_corr_errors15_min", "smiLinkCorrErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_corr_errors15_min_h": MoPropertyMeta("smi_link_corr_errors15_min_h", "smiLinkCorrErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_corr_errors1_day": MoPropertyMeta("smi_link_corr_errors1_day", "smiLinkCorrErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_corr_errors1_day_h": MoPropertyMeta("smi_link_corr_errors1_day_h", "smiLinkCorrErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_corr_errors1_hour": MoPropertyMeta("smi_link_corr_errors1_hour", "smiLinkCorrErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_corr_errors1_hour_h": MoPropertyMeta("smi_link_corr_errors1_hour_h", "smiLinkCorrErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_corr_errors1_week": MoPropertyMeta("smi_link_corr_errors1_week", "smiLinkCorrErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_corr_errors1_week_h": MoPropertyMeta("smi_link_corr_errors1_week_h", "smiLinkCorrErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_corr_errors2_weeks": MoPropertyMeta("smi_link_corr_errors2_weeks", "smiLinkCorrErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_corr_errors2_weeks_h": MoPropertyMeta("smi_link_corr_errors2_weeks_h", "smiLinkCorrErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_uncorr_errors": MoPropertyMeta("smi_link_uncorr_errors", "smiLinkUncorrErrors", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_uncorr_errors15_min": MoPropertyMeta("smi_link_uncorr_errors15_min", "smiLinkUncorrErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_uncorr_errors15_min_h": MoPropertyMeta("smi_link_uncorr_errors15_min_h", "smiLinkUncorrErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_uncorr_errors1_day": MoPropertyMeta("smi_link_uncorr_errors1_day", "smiLinkUncorrErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_uncorr_errors1_day_h": MoPropertyMeta("smi_link_uncorr_errors1_day_h", "smiLinkUncorrErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_uncorr_errors1_hour": MoPropertyMeta("smi_link_uncorr_errors1_hour", "smiLinkUncorrErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_uncorr_errors1_hour_h": MoPropertyMeta("smi_link_uncorr_errors1_hour_h", "smiLinkUncorrErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_uncorr_errors1_week": MoPropertyMeta("smi_link_uncorr_errors1_week", "smiLinkUncorrErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_uncorr_errors1_week_h": MoPropertyMeta("smi_link_uncorr_errors1_week_h", "smiLinkUncorrErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_uncorr_errors2_weeks": MoPropertyMeta("smi_link_uncorr_errors2_weeks", "smiLinkUncorrErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "smi_link_uncorr_errors2_weeks_h": MoPropertyMeta("smi_link_uncorr_errors2_weeks_h", "smiLinkUncorrErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sparing_errors": MoPropertyMeta("sparing_errors", "sparingErrors", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sparing_errors15_min": MoPropertyMeta("sparing_errors15_min", "sparingErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sparing_errors15_min_h": MoPropertyMeta("sparing_errors15_min_h", "sparingErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sparing_errors1_day": MoPropertyMeta("sparing_errors1_day", "sparingErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sparing_errors1_day_h": MoPropertyMeta("sparing_errors1_day_h", "sparingErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sparing_errors1_hour": MoPropertyMeta("sparing_errors1_hour", "sparingErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sparing_errors1_hour_h": MoPropertyMeta("sparing_errors1_hour_h", "sparingErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sparing_errors1_week": MoPropertyMeta("sparing_errors1_week", "sparingErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sparing_errors1_week_h": MoPropertyMeta("sparing_errors1_week_h", "sparingErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sparing_errors2_weeks": MoPropertyMeta("sparing_errors2_weeks", "sparingErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "sparing_errors2_weeks_h": MoPropertyMeta("sparing_errors2_weeks_h", "sparingErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "CorrectableLinkCRCErrors": "correctable_link_crc_errors", 
        "CorrectableLinkCRCErrors15Min": "correctable_link_crc_errors15_min", 
        "CorrectableLinkCRCErrors15MinH": "correctable_link_crc_errors15_min_h", 
        "CorrectableLinkCRCErrors1Day": "correctable_link_crc_errors1_day", 
        "CorrectableLinkCRCErrors1DayH": "correctable_link_crc_errors1_day_h", 
        "CorrectableLinkCRCErrors1Hour": "correctable_link_crc_errors1_hour", 
        "CorrectableLinkCRCErrors1HourH": "correctable_link_crc_errors1_hour_h", 
        "CorrectableLinkCRCErrors1Week": "correctable_link_crc_errors1_week", 
        "CorrectableLinkCRCErrors1WeekH": "correctable_link_crc_errors1_week_h", 
        "CorrectableLinkCRCErrors2Weeks": "correctable_link_crc_errors2_weeks", 
        "CorrectableLinkCRCErrors2WeeksH": "correctable_link_crc_errors2_weeks_h", 
        "UncorrectableLinkCRCErrors": "uncorrectable_link_crc_errors", 
        "UncorrectableLinkCRCErrors15Min": "uncorrectable_link_crc_errors15_min", 
        "UncorrectableLinkCRCErrors15MinH": "uncorrectable_link_crc_errors15_min_h", 
        "UncorrectableLinkCRCErrors1Day": "uncorrectable_link_crc_errors1_day", 
        "UncorrectableLinkCRCErrors1DayH": "uncorrectable_link_crc_errors1_day_h", 
        "UncorrectableLinkCRCErrors1Hour": "uncorrectable_link_crc_errors1_hour", 
        "UncorrectableLinkCRCErrors1HourH": "uncorrectable_link_crc_errors1_hour_h", 
        "UncorrectableLinkCRCErrors1Week": "uncorrectable_link_crc_errors1_week", 
        "UncorrectableLinkCRCErrors1WeekH": "uncorrectable_link_crc_errors1_week_h", 
        "UncorrectableLinkCRCErrors2Weeks": "uncorrectable_link_crc_errors2_weeks", 
        "UncorrectableLinkCRCErrors2WeeksH": "uncorrectable_link_crc_errors2_weeks_h", 
        "childAction": "child_action", 
        "dn": "dn", 
        "intervals": "intervals", 
        "mirroringInterSockErrors": "mirroring_inter_sock_errors", 
        "mirroringInterSockErrors15Min": "mirroring_inter_sock_errors15_min", 
        "mirroringInterSockErrors15MinH": "mirroring_inter_sock_errors15_min_h", 
        "mirroringInterSockErrors1Day": "mirroring_inter_sock_errors1_day", 
        "mirroringInterSockErrors1DayH": "mirroring_inter_sock_errors1_day_h", 
        "mirroringInterSockErrors1Hour": "mirroring_inter_sock_errors1_hour", 
        "mirroringInterSockErrors1HourH": "mirroring_inter_sock_errors1_hour_h", 
        "mirroringInterSockErrors1Week": "mirroring_inter_sock_errors1_week", 
        "mirroringInterSockErrors1WeekH": "mirroring_inter_sock_errors1_week_h", 
        "mirroringInterSockErrors2Weeks": "mirroring_inter_sock_errors2_weeks", 
        "mirroringInterSockErrors2WeeksH": "mirroring_inter_sock_errors2_weeks_h", 
        "mirroringIntraSockErrors": "mirroring_intra_sock_errors", 
        "mirroringIntraSockErrors15Min": "mirroring_intra_sock_errors15_min", 
        "mirroringIntraSockErrors15MinH": "mirroring_intra_sock_errors15_min_h", 
        "mirroringIntraSockErrors1Day": "mirroring_intra_sock_errors1_day", 
        "mirroringIntraSockErrors1DayH": "mirroring_intra_sock_errors1_day_h", 
        "mirroringIntraSockErrors1Hour": "mirroring_intra_sock_errors1_hour", 
        "mirroringIntraSockErrors1HourH": "mirroring_intra_sock_errors1_hour_h", 
        "mirroringIntraSockErrors1Week": "mirroring_intra_sock_errors1_week", 
        "mirroringIntraSockErrors1WeekH": "mirroring_intra_sock_errors1_week_h", 
        "mirroringIntraSockErrors2Weeks": "mirroring_intra_sock_errors2_weeks", 
        "mirroringIntraSockErrors2WeeksH": "mirroring_intra_sock_errors2_weeks_h", 
        "rn": "rn", 
        "sacl": "sacl", 
        "smiLinkCorrErrors": "smi_link_corr_errors", 
        "smiLinkCorrErrors15Min": "smi_link_corr_errors15_min", 
        "smiLinkCorrErrors15MinH": "smi_link_corr_errors15_min_h", 
        "smiLinkCorrErrors1Day": "smi_link_corr_errors1_day", 
        "smiLinkCorrErrors1DayH": "smi_link_corr_errors1_day_h", 
        "smiLinkCorrErrors1Hour": "smi_link_corr_errors1_hour", 
        "smiLinkCorrErrors1HourH": "smi_link_corr_errors1_hour_h", 
        "smiLinkCorrErrors1Week": "smi_link_corr_errors1_week", 
        "smiLinkCorrErrors1WeekH": "smi_link_corr_errors1_week_h", 
        "smiLinkCorrErrors2Weeks": "smi_link_corr_errors2_weeks", 
        "smiLinkCorrErrors2WeeksH": "smi_link_corr_errors2_weeks_h", 
        "smiLinkUncorrErrors": "smi_link_uncorr_errors", 
        "smiLinkUncorrErrors15Min": "smi_link_uncorr_errors15_min", 
        "smiLinkUncorrErrors15MinH": "smi_link_uncorr_errors15_min_h", 
        "smiLinkUncorrErrors1Day": "smi_link_uncorr_errors1_day", 
        "smiLinkUncorrErrors1DayH": "smi_link_uncorr_errors1_day_h", 
        "smiLinkUncorrErrors1Hour": "smi_link_uncorr_errors1_hour", 
        "smiLinkUncorrErrors1HourH": "smi_link_uncorr_errors1_hour_h", 
        "smiLinkUncorrErrors1Week": "smi_link_uncorr_errors1_week", 
        "smiLinkUncorrErrors1WeekH": "smi_link_uncorr_errors1_week_h", 
        "smiLinkUncorrErrors2Weeks": "smi_link_uncorr_errors2_weeks", 
        "smiLinkUncorrErrors2WeeksH": "smi_link_uncorr_errors2_weeks_h", 
        "sparingErrors": "sparing_errors", 
        "sparingErrors15Min": "sparing_errors15_min", 
        "sparingErrors15MinH": "sparing_errors15_min_h", 
        "sparingErrors1Day": "sparing_errors1_day", 
        "sparingErrors1DayH": "sparing_errors1_day_h", 
        "sparingErrors1Hour": "sparing_errors1_hour", 
        "sparingErrors1HourH": "sparing_errors1_hour_h", 
        "sparingErrors1Week": "sparing_errors1_week", 
        "sparingErrors1WeekH": "sparing_errors1_week_h", 
        "sparingErrors2Weeks": "sparing_errors2_weeks", 
        "sparingErrors2WeeksH": "sparing_errors2_weeks_h", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.correctable_link_crc_errors = None
        self.correctable_link_crc_errors15_min = None
        self.correctable_link_crc_errors15_min_h = None
        self.correctable_link_crc_errors1_day = None
        self.correctable_link_crc_errors1_day_h = None
        self.correctable_link_crc_errors1_hour = None
        self.correctable_link_crc_errors1_hour_h = None
        self.correctable_link_crc_errors1_week = None
        self.correctable_link_crc_errors1_week_h = None
        self.correctable_link_crc_errors2_weeks = None
        self.correctable_link_crc_errors2_weeks_h = None
        self.uncorrectable_link_crc_errors = None
        self.uncorrectable_link_crc_errors15_min = None
        self.uncorrectable_link_crc_errors15_min_h = None
        self.uncorrectable_link_crc_errors1_day = None
        self.uncorrectable_link_crc_errors1_day_h = None
        self.uncorrectable_link_crc_errors1_hour = None
        self.uncorrectable_link_crc_errors1_hour_h = None
        self.uncorrectable_link_crc_errors1_week = None
        self.uncorrectable_link_crc_errors1_week_h = None
        self.uncorrectable_link_crc_errors2_weeks = None
        self.uncorrectable_link_crc_errors2_weeks_h = None
        self.child_action = None
        self.intervals = None
        self.mirroring_inter_sock_errors = None
        self.mirroring_inter_sock_errors15_min = None
        self.mirroring_inter_sock_errors15_min_h = None
        self.mirroring_inter_sock_errors1_day = None
        self.mirroring_inter_sock_errors1_day_h = None
        self.mirroring_inter_sock_errors1_hour = None
        self.mirroring_inter_sock_errors1_hour_h = None
        self.mirroring_inter_sock_errors1_week = None
        self.mirroring_inter_sock_errors1_week_h = None
        self.mirroring_inter_sock_errors2_weeks = None
        self.mirroring_inter_sock_errors2_weeks_h = None
        self.mirroring_intra_sock_errors = None
        self.mirroring_intra_sock_errors15_min = None
        self.mirroring_intra_sock_errors15_min_h = None
        self.mirroring_intra_sock_errors1_day = None
        self.mirroring_intra_sock_errors1_day_h = None
        self.mirroring_intra_sock_errors1_hour = None
        self.mirroring_intra_sock_errors1_hour_h = None
        self.mirroring_intra_sock_errors1_week = None
        self.mirroring_intra_sock_errors1_week_h = None
        self.mirroring_intra_sock_errors2_weeks = None
        self.mirroring_intra_sock_errors2_weeks_h = None
        self.sacl = None
        self.smi_link_corr_errors = None
        self.smi_link_corr_errors15_min = None
        self.smi_link_corr_errors15_min_h = None
        self.smi_link_corr_errors1_day = None
        self.smi_link_corr_errors1_day_h = None
        self.smi_link_corr_errors1_hour = None
        self.smi_link_corr_errors1_hour_h = None
        self.smi_link_corr_errors1_week = None
        self.smi_link_corr_errors1_week_h = None
        self.smi_link_corr_errors2_weeks = None
        self.smi_link_corr_errors2_weeks_h = None
        self.smi_link_uncorr_errors = None
        self.smi_link_uncorr_errors15_min = None
        self.smi_link_uncorr_errors15_min_h = None
        self.smi_link_uncorr_errors1_day = None
        self.smi_link_uncorr_errors1_day_h = None
        self.smi_link_uncorr_errors1_hour = None
        self.smi_link_uncorr_errors1_hour_h = None
        self.smi_link_uncorr_errors1_week = None
        self.smi_link_uncorr_errors1_week_h = None
        self.smi_link_uncorr_errors2_weeks = None
        self.smi_link_uncorr_errors2_weeks_h = None
        self.sparing_errors = None
        self.sparing_errors15_min = None
        self.sparing_errors15_min_h = None
        self.sparing_errors1_day = None
        self.sparing_errors1_day_h = None
        self.sparing_errors1_hour = None
        self.sparing_errors1_hour_h = None
        self.sparing_errors1_week = None
        self.sparing_errors1_week_h = None
        self.sparing_errors2_weeks = None
        self.sparing_errors2_weeks_h = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "ProcessorErrorStats", parent_mo_or_dn, **kwargs)
