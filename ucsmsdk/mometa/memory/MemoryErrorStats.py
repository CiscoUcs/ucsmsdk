"""This module contains the general information for MemoryErrorStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MemoryErrorStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class MemoryErrorStats(ManagedObject):
    """This is MemoryErrorStats class."""

    consts = MemoryErrorStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("MemoryErrorStats", "memoryErrorStats", "error-stats", VersionMeta.Version131c, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['memoryPersistentMemoryUnit', 'memoryUnit'], [], ["Get"])

    prop_meta = {
        "dram_write_data_correctable_crc_errors": MoPropertyMeta("dram_write_data_correctable_crc_errors", "DramWriteDataCorrectableCRCErrors", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_correctable_crc_errors15_min": MoPropertyMeta("dram_write_data_correctable_crc_errors15_min", "DramWriteDataCorrectableCRCErrors15Min", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_correctable_crc_errors15_min_h": MoPropertyMeta("dram_write_data_correctable_crc_errors15_min_h", "DramWriteDataCorrectableCRCErrors15MinH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_correctable_crc_errors1_day": MoPropertyMeta("dram_write_data_correctable_crc_errors1_day", "DramWriteDataCorrectableCRCErrors1Day", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_correctable_crc_errors1_day_h": MoPropertyMeta("dram_write_data_correctable_crc_errors1_day_h", "DramWriteDataCorrectableCRCErrors1DayH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_correctable_crc_errors1_hour": MoPropertyMeta("dram_write_data_correctable_crc_errors1_hour", "DramWriteDataCorrectableCRCErrors1Hour", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_correctable_crc_errors1_hour_h": MoPropertyMeta("dram_write_data_correctable_crc_errors1_hour_h", "DramWriteDataCorrectableCRCErrors1HourH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_correctable_crc_errors1_week": MoPropertyMeta("dram_write_data_correctable_crc_errors1_week", "DramWriteDataCorrectableCRCErrors1Week", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_correctable_crc_errors1_week_h": MoPropertyMeta("dram_write_data_correctable_crc_errors1_week_h", "DramWriteDataCorrectableCRCErrors1WeekH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_correctable_crc_errors2_weeks": MoPropertyMeta("dram_write_data_correctable_crc_errors2_weeks", "DramWriteDataCorrectableCRCErrors2Weeks", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_correctable_crc_errors2_weeks_h": MoPropertyMeta("dram_write_data_correctable_crc_errors2_weeks_h", "DramWriteDataCorrectableCRCErrors2WeeksH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_un_correctable_crc_errors": MoPropertyMeta("dram_write_data_un_correctable_crc_errors", "DramWriteDataUnCorrectableCRCErrors", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_un_correctable_crc_errors15_min": MoPropertyMeta("dram_write_data_un_correctable_crc_errors15_min", "DramWriteDataUnCorrectableCRCErrors15Min", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_un_correctable_crc_errors15_min_h": MoPropertyMeta("dram_write_data_un_correctable_crc_errors15_min_h", "DramWriteDataUnCorrectableCRCErrors15MinH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_un_correctable_crc_errors1_day": MoPropertyMeta("dram_write_data_un_correctable_crc_errors1_day", "DramWriteDataUnCorrectableCRCErrors1Day", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_un_correctable_crc_errors1_day_h": MoPropertyMeta("dram_write_data_un_correctable_crc_errors1_day_h", "DramWriteDataUnCorrectableCRCErrors1DayH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_un_correctable_crc_errors1_hour": MoPropertyMeta("dram_write_data_un_correctable_crc_errors1_hour", "DramWriteDataUnCorrectableCRCErrors1Hour", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_un_correctable_crc_errors1_hour_h": MoPropertyMeta("dram_write_data_un_correctable_crc_errors1_hour_h", "DramWriteDataUnCorrectableCRCErrors1HourH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_un_correctable_crc_errors1_week": MoPropertyMeta("dram_write_data_un_correctable_crc_errors1_week", "DramWriteDataUnCorrectableCRCErrors1Week", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_un_correctable_crc_errors1_week_h": MoPropertyMeta("dram_write_data_un_correctable_crc_errors1_week_h", "DramWriteDataUnCorrectableCRCErrors1WeekH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_un_correctable_crc_errors2_weeks": MoPropertyMeta("dram_write_data_un_correctable_crc_errors2_weeks", "DramWriteDataUnCorrectableCRCErrors2Weeks", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dram_write_data_un_correctable_crc_errors2_weeks_h": MoPropertyMeta("dram_write_data_un_correctable_crc_errors2_weeks_h", "DramWriteDataUnCorrectableCRCErrors2WeeksH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors": MoPropertyMeta("address_parity_errors", "addressParityErrors", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors15_min": MoPropertyMeta("address_parity_errors15_min", "addressParityErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors15_min_h": MoPropertyMeta("address_parity_errors15_min_h", "addressParityErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors1_day": MoPropertyMeta("address_parity_errors1_day", "addressParityErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors1_day_h": MoPropertyMeta("address_parity_errors1_day_h", "addressParityErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors1_hour": MoPropertyMeta("address_parity_errors1_hour", "addressParityErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors1_hour_h": MoPropertyMeta("address_parity_errors1_hour_h", "addressParityErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors1_week": MoPropertyMeta("address_parity_errors1_week", "addressParityErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors1_week_h": MoPropertyMeta("address_parity_errors1_week_h", "addressParityErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors2_weeks": MoPropertyMeta("address_parity_errors2_weeks", "addressParityErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors2_weeks_h": MoPropertyMeta("address_parity_errors2_weeks_h", "addressParityErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_correctable": MoPropertyMeta("address_parity_errors_correctable", "addressParityErrorsCorrectable", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_correctable15_min": MoPropertyMeta("address_parity_errors_correctable15_min", "addressParityErrorsCorrectable15Min", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_correctable15_min_h": MoPropertyMeta("address_parity_errors_correctable15_min_h", "addressParityErrorsCorrectable15MinH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_correctable1_day": MoPropertyMeta("address_parity_errors_correctable1_day", "addressParityErrorsCorrectable1Day", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_correctable1_day_h": MoPropertyMeta("address_parity_errors_correctable1_day_h", "addressParityErrorsCorrectable1DayH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_correctable1_hour": MoPropertyMeta("address_parity_errors_correctable1_hour", "addressParityErrorsCorrectable1Hour", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_correctable1_hour_h": MoPropertyMeta("address_parity_errors_correctable1_hour_h", "addressParityErrorsCorrectable1HourH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_correctable1_week": MoPropertyMeta("address_parity_errors_correctable1_week", "addressParityErrorsCorrectable1Week", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_correctable1_week_h": MoPropertyMeta("address_parity_errors_correctable1_week_h", "addressParityErrorsCorrectable1WeekH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_correctable2_weeks": MoPropertyMeta("address_parity_errors_correctable2_weeks", "addressParityErrorsCorrectable2Weeks", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_correctable2_weeks_h": MoPropertyMeta("address_parity_errors_correctable2_weeks_h", "addressParityErrorsCorrectable2WeeksH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_un_correctable": MoPropertyMeta("address_parity_errors_un_correctable", "addressParityErrorsUnCorrectable", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_un_correctable15_min": MoPropertyMeta("address_parity_errors_un_correctable15_min", "addressParityErrorsUnCorrectable15Min", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_un_correctable15_min_h": MoPropertyMeta("address_parity_errors_un_correctable15_min_h", "addressParityErrorsUnCorrectable15MinH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_un_correctable1_day": MoPropertyMeta("address_parity_errors_un_correctable1_day", "addressParityErrorsUnCorrectable1Day", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_un_correctable1_day_h": MoPropertyMeta("address_parity_errors_un_correctable1_day_h", "addressParityErrorsUnCorrectable1DayH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_un_correctable1_hour": MoPropertyMeta("address_parity_errors_un_correctable1_hour", "addressParityErrorsUnCorrectable1Hour", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_un_correctable1_hour_h": MoPropertyMeta("address_parity_errors_un_correctable1_hour_h", "addressParityErrorsUnCorrectable1HourH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_un_correctable1_week": MoPropertyMeta("address_parity_errors_un_correctable1_week", "addressParityErrorsUnCorrectable1Week", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_un_correctable1_week_h": MoPropertyMeta("address_parity_errors_un_correctable1_week_h", "addressParityErrorsUnCorrectable1WeekH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_un_correctable2_weeks": MoPropertyMeta("address_parity_errors_un_correctable2_weeks", "addressParityErrorsUnCorrectable2Weeks", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "address_parity_errors_un_correctable2_weeks_h": MoPropertyMeta("address_parity_errors_un_correctable2_weeks_h", "addressParityErrorsUnCorrectable2WeeksH", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "ecc_multibit_errors": MoPropertyMeta("ecc_multibit_errors", "eccMultibitErrors", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_multibit_errors15_min": MoPropertyMeta("ecc_multibit_errors15_min", "eccMultibitErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_multibit_errors15_min_h": MoPropertyMeta("ecc_multibit_errors15_min_h", "eccMultibitErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_multibit_errors1_day": MoPropertyMeta("ecc_multibit_errors1_day", "eccMultibitErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_multibit_errors1_day_h": MoPropertyMeta("ecc_multibit_errors1_day_h", "eccMultibitErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_multibit_errors1_hour": MoPropertyMeta("ecc_multibit_errors1_hour", "eccMultibitErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_multibit_errors1_hour_h": MoPropertyMeta("ecc_multibit_errors1_hour_h", "eccMultibitErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_multibit_errors1_week": MoPropertyMeta("ecc_multibit_errors1_week", "eccMultibitErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_multibit_errors1_week_h": MoPropertyMeta("ecc_multibit_errors1_week_h", "eccMultibitErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_multibit_errors2_weeks": MoPropertyMeta("ecc_multibit_errors2_weeks", "eccMultibitErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_multibit_errors2_weeks_h": MoPropertyMeta("ecc_multibit_errors2_weeks_h", "eccMultibitErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_singlebit_errors": MoPropertyMeta("ecc_singlebit_errors", "eccSinglebitErrors", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_singlebit_errors15_min": MoPropertyMeta("ecc_singlebit_errors15_min", "eccSinglebitErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_singlebit_errors15_min_h": MoPropertyMeta("ecc_singlebit_errors15_min_h", "eccSinglebitErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_singlebit_errors1_day": MoPropertyMeta("ecc_singlebit_errors1_day", "eccSinglebitErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_singlebit_errors1_day_h": MoPropertyMeta("ecc_singlebit_errors1_day_h", "eccSinglebitErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_singlebit_errors1_hour": MoPropertyMeta("ecc_singlebit_errors1_hour", "eccSinglebitErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_singlebit_errors1_hour_h": MoPropertyMeta("ecc_singlebit_errors1_hour_h", "eccSinglebitErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_singlebit_errors1_week": MoPropertyMeta("ecc_singlebit_errors1_week", "eccSinglebitErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_singlebit_errors1_week_h": MoPropertyMeta("ecc_singlebit_errors1_week_h", "eccSinglebitErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_singlebit_errors2_weeks": MoPropertyMeta("ecc_singlebit_errors2_weeks", "eccSinglebitErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ecc_singlebit_errors2_weeks_h": MoPropertyMeta("ecc_singlebit_errors2_weeks_h", "eccSinglebitErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mismatch_errors": MoPropertyMeta("mismatch_errors", "mismatchErrors", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mismatch_errors15_min": MoPropertyMeta("mismatch_errors15_min", "mismatchErrors15Min", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mismatch_errors15_min_h": MoPropertyMeta("mismatch_errors15_min_h", "mismatchErrors15MinH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mismatch_errors1_day": MoPropertyMeta("mismatch_errors1_day", "mismatchErrors1Day", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mismatch_errors1_day_h": MoPropertyMeta("mismatch_errors1_day_h", "mismatchErrors1DayH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mismatch_errors1_hour": MoPropertyMeta("mismatch_errors1_hour", "mismatchErrors1Hour", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mismatch_errors1_hour_h": MoPropertyMeta("mismatch_errors1_hour_h", "mismatchErrors1HourH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mismatch_errors1_week": MoPropertyMeta("mismatch_errors1_week", "mismatchErrors1Week", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mismatch_errors1_week_h": MoPropertyMeta("mismatch_errors1_week_h", "mismatchErrors1WeekH", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mismatch_errors2_weeks": MoPropertyMeta("mismatch_errors2_weeks", "mismatchErrors2Weeks", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mismatch_errors2_weeks_h": MoPropertyMeta("mismatch_errors2_weeks_h", "mismatchErrors2WeeksH", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "DramWriteDataCorrectableCRCErrors": "dram_write_data_correctable_crc_errors", 
        "DramWriteDataCorrectableCRCErrors15Min": "dram_write_data_correctable_crc_errors15_min", 
        "DramWriteDataCorrectableCRCErrors15MinH": "dram_write_data_correctable_crc_errors15_min_h", 
        "DramWriteDataCorrectableCRCErrors1Day": "dram_write_data_correctable_crc_errors1_day", 
        "DramWriteDataCorrectableCRCErrors1DayH": "dram_write_data_correctable_crc_errors1_day_h", 
        "DramWriteDataCorrectableCRCErrors1Hour": "dram_write_data_correctable_crc_errors1_hour", 
        "DramWriteDataCorrectableCRCErrors1HourH": "dram_write_data_correctable_crc_errors1_hour_h", 
        "DramWriteDataCorrectableCRCErrors1Week": "dram_write_data_correctable_crc_errors1_week", 
        "DramWriteDataCorrectableCRCErrors1WeekH": "dram_write_data_correctable_crc_errors1_week_h", 
        "DramWriteDataCorrectableCRCErrors2Weeks": "dram_write_data_correctable_crc_errors2_weeks", 
        "DramWriteDataCorrectableCRCErrors2WeeksH": "dram_write_data_correctable_crc_errors2_weeks_h", 
        "DramWriteDataUnCorrectableCRCErrors": "dram_write_data_un_correctable_crc_errors", 
        "DramWriteDataUnCorrectableCRCErrors15Min": "dram_write_data_un_correctable_crc_errors15_min", 
        "DramWriteDataUnCorrectableCRCErrors15MinH": "dram_write_data_un_correctable_crc_errors15_min_h", 
        "DramWriteDataUnCorrectableCRCErrors1Day": "dram_write_data_un_correctable_crc_errors1_day", 
        "DramWriteDataUnCorrectableCRCErrors1DayH": "dram_write_data_un_correctable_crc_errors1_day_h", 
        "DramWriteDataUnCorrectableCRCErrors1Hour": "dram_write_data_un_correctable_crc_errors1_hour", 
        "DramWriteDataUnCorrectableCRCErrors1HourH": "dram_write_data_un_correctable_crc_errors1_hour_h", 
        "DramWriteDataUnCorrectableCRCErrors1Week": "dram_write_data_un_correctable_crc_errors1_week", 
        "DramWriteDataUnCorrectableCRCErrors1WeekH": "dram_write_data_un_correctable_crc_errors1_week_h", 
        "DramWriteDataUnCorrectableCRCErrors2Weeks": "dram_write_data_un_correctable_crc_errors2_weeks", 
        "DramWriteDataUnCorrectableCRCErrors2WeeksH": "dram_write_data_un_correctable_crc_errors2_weeks_h", 
        "addressParityErrors": "address_parity_errors", 
        "addressParityErrors15Min": "address_parity_errors15_min", 
        "addressParityErrors15MinH": "address_parity_errors15_min_h", 
        "addressParityErrors1Day": "address_parity_errors1_day", 
        "addressParityErrors1DayH": "address_parity_errors1_day_h", 
        "addressParityErrors1Hour": "address_parity_errors1_hour", 
        "addressParityErrors1HourH": "address_parity_errors1_hour_h", 
        "addressParityErrors1Week": "address_parity_errors1_week", 
        "addressParityErrors1WeekH": "address_parity_errors1_week_h", 
        "addressParityErrors2Weeks": "address_parity_errors2_weeks", 
        "addressParityErrors2WeeksH": "address_parity_errors2_weeks_h", 
        "addressParityErrorsCorrectable": "address_parity_errors_correctable", 
        "addressParityErrorsCorrectable15Min": "address_parity_errors_correctable15_min", 
        "addressParityErrorsCorrectable15MinH": "address_parity_errors_correctable15_min_h", 
        "addressParityErrorsCorrectable1Day": "address_parity_errors_correctable1_day", 
        "addressParityErrorsCorrectable1DayH": "address_parity_errors_correctable1_day_h", 
        "addressParityErrorsCorrectable1Hour": "address_parity_errors_correctable1_hour", 
        "addressParityErrorsCorrectable1HourH": "address_parity_errors_correctable1_hour_h", 
        "addressParityErrorsCorrectable1Week": "address_parity_errors_correctable1_week", 
        "addressParityErrorsCorrectable1WeekH": "address_parity_errors_correctable1_week_h", 
        "addressParityErrorsCorrectable2Weeks": "address_parity_errors_correctable2_weeks", 
        "addressParityErrorsCorrectable2WeeksH": "address_parity_errors_correctable2_weeks_h", 
        "addressParityErrorsUnCorrectable": "address_parity_errors_un_correctable", 
        "addressParityErrorsUnCorrectable15Min": "address_parity_errors_un_correctable15_min", 
        "addressParityErrorsUnCorrectable15MinH": "address_parity_errors_un_correctable15_min_h", 
        "addressParityErrorsUnCorrectable1Day": "address_parity_errors_un_correctable1_day", 
        "addressParityErrorsUnCorrectable1DayH": "address_parity_errors_un_correctable1_day_h", 
        "addressParityErrorsUnCorrectable1Hour": "address_parity_errors_un_correctable1_hour", 
        "addressParityErrorsUnCorrectable1HourH": "address_parity_errors_un_correctable1_hour_h", 
        "addressParityErrorsUnCorrectable1Week": "address_parity_errors_un_correctable1_week", 
        "addressParityErrorsUnCorrectable1WeekH": "address_parity_errors_un_correctable1_week_h", 
        "addressParityErrorsUnCorrectable2Weeks": "address_parity_errors_un_correctable2_weeks", 
        "addressParityErrorsUnCorrectable2WeeksH": "address_parity_errors_un_correctable2_weeks_h", 
        "childAction": "child_action", 
        "dn": "dn", 
        "eccMultibitErrors": "ecc_multibit_errors", 
        "eccMultibitErrors15Min": "ecc_multibit_errors15_min", 
        "eccMultibitErrors15MinH": "ecc_multibit_errors15_min_h", 
        "eccMultibitErrors1Day": "ecc_multibit_errors1_day", 
        "eccMultibitErrors1DayH": "ecc_multibit_errors1_day_h", 
        "eccMultibitErrors1Hour": "ecc_multibit_errors1_hour", 
        "eccMultibitErrors1HourH": "ecc_multibit_errors1_hour_h", 
        "eccMultibitErrors1Week": "ecc_multibit_errors1_week", 
        "eccMultibitErrors1WeekH": "ecc_multibit_errors1_week_h", 
        "eccMultibitErrors2Weeks": "ecc_multibit_errors2_weeks", 
        "eccMultibitErrors2WeeksH": "ecc_multibit_errors2_weeks_h", 
        "eccSinglebitErrors": "ecc_singlebit_errors", 
        "eccSinglebitErrors15Min": "ecc_singlebit_errors15_min", 
        "eccSinglebitErrors15MinH": "ecc_singlebit_errors15_min_h", 
        "eccSinglebitErrors1Day": "ecc_singlebit_errors1_day", 
        "eccSinglebitErrors1DayH": "ecc_singlebit_errors1_day_h", 
        "eccSinglebitErrors1Hour": "ecc_singlebit_errors1_hour", 
        "eccSinglebitErrors1HourH": "ecc_singlebit_errors1_hour_h", 
        "eccSinglebitErrors1Week": "ecc_singlebit_errors1_week", 
        "eccSinglebitErrors1WeekH": "ecc_singlebit_errors1_week_h", 
        "eccSinglebitErrors2Weeks": "ecc_singlebit_errors2_weeks", 
        "eccSinglebitErrors2WeeksH": "ecc_singlebit_errors2_weeks_h", 
        "intervals": "intervals", 
        "mismatchErrors": "mismatch_errors", 
        "mismatchErrors15Min": "mismatch_errors15_min", 
        "mismatchErrors15MinH": "mismatch_errors15_min_h", 
        "mismatchErrors1Day": "mismatch_errors1_day", 
        "mismatchErrors1DayH": "mismatch_errors1_day_h", 
        "mismatchErrors1Hour": "mismatch_errors1_hour", 
        "mismatchErrors1HourH": "mismatch_errors1_hour_h", 
        "mismatchErrors1Week": "mismatch_errors1_week", 
        "mismatchErrors1WeekH": "mismatch_errors1_week_h", 
        "mismatchErrors2Weeks": "mismatch_errors2_weeks", 
        "mismatchErrors2WeeksH": "mismatch_errors2_weeks_h", 
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
        self.dram_write_data_correctable_crc_errors = None
        self.dram_write_data_correctable_crc_errors15_min = None
        self.dram_write_data_correctable_crc_errors15_min_h = None
        self.dram_write_data_correctable_crc_errors1_day = None
        self.dram_write_data_correctable_crc_errors1_day_h = None
        self.dram_write_data_correctable_crc_errors1_hour = None
        self.dram_write_data_correctable_crc_errors1_hour_h = None
        self.dram_write_data_correctable_crc_errors1_week = None
        self.dram_write_data_correctable_crc_errors1_week_h = None
        self.dram_write_data_correctable_crc_errors2_weeks = None
        self.dram_write_data_correctable_crc_errors2_weeks_h = None
        self.dram_write_data_un_correctable_crc_errors = None
        self.dram_write_data_un_correctable_crc_errors15_min = None
        self.dram_write_data_un_correctable_crc_errors15_min_h = None
        self.dram_write_data_un_correctable_crc_errors1_day = None
        self.dram_write_data_un_correctable_crc_errors1_day_h = None
        self.dram_write_data_un_correctable_crc_errors1_hour = None
        self.dram_write_data_un_correctable_crc_errors1_hour_h = None
        self.dram_write_data_un_correctable_crc_errors1_week = None
        self.dram_write_data_un_correctable_crc_errors1_week_h = None
        self.dram_write_data_un_correctable_crc_errors2_weeks = None
        self.dram_write_data_un_correctable_crc_errors2_weeks_h = None
        self.address_parity_errors = None
        self.address_parity_errors15_min = None
        self.address_parity_errors15_min_h = None
        self.address_parity_errors1_day = None
        self.address_parity_errors1_day_h = None
        self.address_parity_errors1_hour = None
        self.address_parity_errors1_hour_h = None
        self.address_parity_errors1_week = None
        self.address_parity_errors1_week_h = None
        self.address_parity_errors2_weeks = None
        self.address_parity_errors2_weeks_h = None
        self.address_parity_errors_correctable = None
        self.address_parity_errors_correctable15_min = None
        self.address_parity_errors_correctable15_min_h = None
        self.address_parity_errors_correctable1_day = None
        self.address_parity_errors_correctable1_day_h = None
        self.address_parity_errors_correctable1_hour = None
        self.address_parity_errors_correctable1_hour_h = None
        self.address_parity_errors_correctable1_week = None
        self.address_parity_errors_correctable1_week_h = None
        self.address_parity_errors_correctable2_weeks = None
        self.address_parity_errors_correctable2_weeks_h = None
        self.address_parity_errors_un_correctable = None
        self.address_parity_errors_un_correctable15_min = None
        self.address_parity_errors_un_correctable15_min_h = None
        self.address_parity_errors_un_correctable1_day = None
        self.address_parity_errors_un_correctable1_day_h = None
        self.address_parity_errors_un_correctable1_hour = None
        self.address_parity_errors_un_correctable1_hour_h = None
        self.address_parity_errors_un_correctable1_week = None
        self.address_parity_errors_un_correctable1_week_h = None
        self.address_parity_errors_un_correctable2_weeks = None
        self.address_parity_errors_un_correctable2_weeks_h = None
        self.child_action = None
        self.ecc_multibit_errors = None
        self.ecc_multibit_errors15_min = None
        self.ecc_multibit_errors15_min_h = None
        self.ecc_multibit_errors1_day = None
        self.ecc_multibit_errors1_day_h = None
        self.ecc_multibit_errors1_hour = None
        self.ecc_multibit_errors1_hour_h = None
        self.ecc_multibit_errors1_week = None
        self.ecc_multibit_errors1_week_h = None
        self.ecc_multibit_errors2_weeks = None
        self.ecc_multibit_errors2_weeks_h = None
        self.ecc_singlebit_errors = None
        self.ecc_singlebit_errors15_min = None
        self.ecc_singlebit_errors15_min_h = None
        self.ecc_singlebit_errors1_day = None
        self.ecc_singlebit_errors1_day_h = None
        self.ecc_singlebit_errors1_hour = None
        self.ecc_singlebit_errors1_hour_h = None
        self.ecc_singlebit_errors1_week = None
        self.ecc_singlebit_errors1_week_h = None
        self.ecc_singlebit_errors2_weeks = None
        self.ecc_singlebit_errors2_weeks_h = None
        self.intervals = None
        self.mismatch_errors = None
        self.mismatch_errors15_min = None
        self.mismatch_errors15_min_h = None
        self.mismatch_errors1_day = None
        self.mismatch_errors1_day_h = None
        self.mismatch_errors1_hour = None
        self.mismatch_errors1_hour_h = None
        self.mismatch_errors1_week = None
        self.mismatch_errors1_week_h = None
        self.mismatch_errors2_weeks = None
        self.mismatch_errors2_weeks_h = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "MemoryErrorStats", parent_mo_or_dn, **kwargs)
