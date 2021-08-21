"""This module contains the general information for ProcessorExecStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ProcessorExecStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ProcessorExecStats(ManagedObject):
    """This is ProcessorExecStats class."""

    consts = ProcessorExecStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcessorExecStats", "processorExecStats", "exec-stats", VersionMeta.Version412a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['processorUnit'], [], [None])

    prop_meta = {
        "decode_unit_correctable_errors": MoPropertyMeta("decode_unit_correctable_errors", "DecodeUnitCorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_correctable_errors15_min": MoPropertyMeta("decode_unit_correctable_errors15_min", "DecodeUnitCorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_correctable_errors15_min_h": MoPropertyMeta("decode_unit_correctable_errors15_min_h", "DecodeUnitCorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_correctable_errors1_day": MoPropertyMeta("decode_unit_correctable_errors1_day", "DecodeUnitCorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_correctable_errors1_day_h": MoPropertyMeta("decode_unit_correctable_errors1_day_h", "DecodeUnitCorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_correctable_errors1_hour": MoPropertyMeta("decode_unit_correctable_errors1_hour", "DecodeUnitCorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_correctable_errors1_hour_h": MoPropertyMeta("decode_unit_correctable_errors1_hour_h", "DecodeUnitCorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_correctable_errors1_week": MoPropertyMeta("decode_unit_correctable_errors1_week", "DecodeUnitCorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_correctable_errors1_week_h": MoPropertyMeta("decode_unit_correctable_errors1_week_h", "DecodeUnitCorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_correctable_errors2_weeks": MoPropertyMeta("decode_unit_correctable_errors2_weeks", "DecodeUnitCorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_correctable_errors2_weeks_h": MoPropertyMeta("decode_unit_correctable_errors2_weeks_h", "DecodeUnitCorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_uncorrectable_errors": MoPropertyMeta("decode_unit_uncorrectable_errors", "DecodeUnitUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_uncorrectable_errors15_min": MoPropertyMeta("decode_unit_uncorrectable_errors15_min", "DecodeUnitUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_uncorrectable_errors15_min_h": MoPropertyMeta("decode_unit_uncorrectable_errors15_min_h", "DecodeUnitUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_uncorrectable_errors1_day": MoPropertyMeta("decode_unit_uncorrectable_errors1_day", "DecodeUnitUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_uncorrectable_errors1_day_h": MoPropertyMeta("decode_unit_uncorrectable_errors1_day_h", "DecodeUnitUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_uncorrectable_errors1_hour": MoPropertyMeta("decode_unit_uncorrectable_errors1_hour", "DecodeUnitUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_uncorrectable_errors1_hour_h": MoPropertyMeta("decode_unit_uncorrectable_errors1_hour_h", "DecodeUnitUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_uncorrectable_errors1_week": MoPropertyMeta("decode_unit_uncorrectable_errors1_week", "DecodeUnitUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_uncorrectable_errors1_week_h": MoPropertyMeta("decode_unit_uncorrectable_errors1_week_h", "DecodeUnitUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_uncorrectable_errors2_weeks": MoPropertyMeta("decode_unit_uncorrectable_errors2_weeks", "DecodeUnitUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "decode_unit_uncorrectable_errors2_weeks_h": MoPropertyMeta("decode_unit_uncorrectable_errors2_weeks_h", "DecodeUnitUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_correctable_errors": MoPropertyMeta("execution_unit_correctable_errors", "ExecutionUnitCorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_correctable_errors15_min": MoPropertyMeta("execution_unit_correctable_errors15_min", "ExecutionUnitCorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_correctable_errors15_min_h": MoPropertyMeta("execution_unit_correctable_errors15_min_h", "ExecutionUnitCorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_correctable_errors1_day": MoPropertyMeta("execution_unit_correctable_errors1_day", "ExecutionUnitCorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_correctable_errors1_day_h": MoPropertyMeta("execution_unit_correctable_errors1_day_h", "ExecutionUnitCorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_correctable_errors1_hour": MoPropertyMeta("execution_unit_correctable_errors1_hour", "ExecutionUnitCorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_correctable_errors1_hour_h": MoPropertyMeta("execution_unit_correctable_errors1_hour_h", "ExecutionUnitCorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_correctable_errors1_week": MoPropertyMeta("execution_unit_correctable_errors1_week", "ExecutionUnitCorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_correctable_errors1_week_h": MoPropertyMeta("execution_unit_correctable_errors1_week_h", "ExecutionUnitCorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_correctable_errors2_weeks": MoPropertyMeta("execution_unit_correctable_errors2_weeks", "ExecutionUnitCorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_correctable_errors2_weeks_h": MoPropertyMeta("execution_unit_correctable_errors2_weeks_h", "ExecutionUnitCorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_uncorrectable_errors": MoPropertyMeta("execution_unit_uncorrectable_errors", "ExecutionUnitUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_uncorrectable_errors15_min": MoPropertyMeta("execution_unit_uncorrectable_errors15_min", "ExecutionUnitUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_uncorrectable_errors15_min_h": MoPropertyMeta("execution_unit_uncorrectable_errors15_min_h", "ExecutionUnitUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_uncorrectable_errors1_day": MoPropertyMeta("execution_unit_uncorrectable_errors1_day", "ExecutionUnitUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_uncorrectable_errors1_day_h": MoPropertyMeta("execution_unit_uncorrectable_errors1_day_h", "ExecutionUnitUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_uncorrectable_errors1_hour": MoPropertyMeta("execution_unit_uncorrectable_errors1_hour", "ExecutionUnitUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_uncorrectable_errors1_hour_h": MoPropertyMeta("execution_unit_uncorrectable_errors1_hour_h", "ExecutionUnitUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_uncorrectable_errors1_week": MoPropertyMeta("execution_unit_uncorrectable_errors1_week", "ExecutionUnitUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_uncorrectable_errors1_week_h": MoPropertyMeta("execution_unit_uncorrectable_errors1_week_h", "ExecutionUnitUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_uncorrectable_errors2_weeks": MoPropertyMeta("execution_unit_uncorrectable_errors2_weeks", "ExecutionUnitUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "execution_unit_uncorrectable_errors2_weeks_h": MoPropertyMeta("execution_unit_uncorrectable_errors2_weeks_h", "ExecutionUnitUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_correctable_errors": MoPropertyMeta("instruction_fetch_unit_correctable_errors", "InstructionFetchUnitCorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_correctable_errors15_min": MoPropertyMeta("instruction_fetch_unit_correctable_errors15_min", "InstructionFetchUnitCorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_correctable_errors15_min_h": MoPropertyMeta("instruction_fetch_unit_correctable_errors15_min_h", "InstructionFetchUnitCorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_correctable_errors1_day": MoPropertyMeta("instruction_fetch_unit_correctable_errors1_day", "InstructionFetchUnitCorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_correctable_errors1_day_h": MoPropertyMeta("instruction_fetch_unit_correctable_errors1_day_h", "InstructionFetchUnitCorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_correctable_errors1_hour": MoPropertyMeta("instruction_fetch_unit_correctable_errors1_hour", "InstructionFetchUnitCorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_correctable_errors1_hour_h": MoPropertyMeta("instruction_fetch_unit_correctable_errors1_hour_h", "InstructionFetchUnitCorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_correctable_errors1_week": MoPropertyMeta("instruction_fetch_unit_correctable_errors1_week", "InstructionFetchUnitCorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_correctable_errors1_week_h": MoPropertyMeta("instruction_fetch_unit_correctable_errors1_week_h", "InstructionFetchUnitCorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_correctable_errors2_weeks": MoPropertyMeta("instruction_fetch_unit_correctable_errors2_weeks", "InstructionFetchUnitCorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_correctable_errors2_weeks_h": MoPropertyMeta("instruction_fetch_unit_correctable_errors2_weeks_h", "InstructionFetchUnitCorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_uncorrectable_errors": MoPropertyMeta("instruction_fetch_unit_uncorrectable_errors", "InstructionFetchUnitUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_uncorrectable_errors15_min": MoPropertyMeta("instruction_fetch_unit_uncorrectable_errors15_min", "InstructionFetchUnitUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_uncorrectable_errors15_min_h": MoPropertyMeta("instruction_fetch_unit_uncorrectable_errors15_min_h", "InstructionFetchUnitUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_uncorrectable_errors1_day": MoPropertyMeta("instruction_fetch_unit_uncorrectable_errors1_day", "InstructionFetchUnitUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_uncorrectable_errors1_day_h": MoPropertyMeta("instruction_fetch_unit_uncorrectable_errors1_day_h", "InstructionFetchUnitUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_uncorrectable_errors1_hour": MoPropertyMeta("instruction_fetch_unit_uncorrectable_errors1_hour", "InstructionFetchUnitUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_uncorrectable_errors1_hour_h": MoPropertyMeta("instruction_fetch_unit_uncorrectable_errors1_hour_h", "InstructionFetchUnitUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_uncorrectable_errors1_week": MoPropertyMeta("instruction_fetch_unit_uncorrectable_errors1_week", "InstructionFetchUnitUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_uncorrectable_errors1_week_h": MoPropertyMeta("instruction_fetch_unit_uncorrectable_errors1_week_h", "InstructionFetchUnitUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_uncorrectable_errors2_weeks": MoPropertyMeta("instruction_fetch_unit_uncorrectable_errors2_weeks", "InstructionFetchUnitUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "instruction_fetch_unit_uncorrectable_errors2_weeks_h": MoPropertyMeta("instruction_fetch_unit_uncorrectable_errors2_weeks_h", "InstructionFetchUnitUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_correctable_errors": MoPropertyMeta("load_store_unit_correctable_errors", "LoadStoreUnitCorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_correctable_errors15_min": MoPropertyMeta("load_store_unit_correctable_errors15_min", "LoadStoreUnitCorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_correctable_errors15_min_h": MoPropertyMeta("load_store_unit_correctable_errors15_min_h", "LoadStoreUnitCorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_correctable_errors1_day": MoPropertyMeta("load_store_unit_correctable_errors1_day", "LoadStoreUnitCorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_correctable_errors1_day_h": MoPropertyMeta("load_store_unit_correctable_errors1_day_h", "LoadStoreUnitCorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_correctable_errors1_hour": MoPropertyMeta("load_store_unit_correctable_errors1_hour", "LoadStoreUnitCorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_correctable_errors1_hour_h": MoPropertyMeta("load_store_unit_correctable_errors1_hour_h", "LoadStoreUnitCorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_correctable_errors1_week": MoPropertyMeta("load_store_unit_correctable_errors1_week", "LoadStoreUnitCorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_correctable_errors1_week_h": MoPropertyMeta("load_store_unit_correctable_errors1_week_h", "LoadStoreUnitCorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_correctable_errors2_weeks": MoPropertyMeta("load_store_unit_correctable_errors2_weeks", "LoadStoreUnitCorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_correctable_errors2_weeks_h": MoPropertyMeta("load_store_unit_correctable_errors2_weeks_h", "LoadStoreUnitCorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_uncorrectable_errors": MoPropertyMeta("load_store_unit_uncorrectable_errors", "LoadStoreUnitUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_uncorrectable_errors15_min": MoPropertyMeta("load_store_unit_uncorrectable_errors15_min", "LoadStoreUnitUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_uncorrectable_errors15_min_h": MoPropertyMeta("load_store_unit_uncorrectable_errors15_min_h", "LoadStoreUnitUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_uncorrectable_errors1_day": MoPropertyMeta("load_store_unit_uncorrectable_errors1_day", "LoadStoreUnitUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_uncorrectable_errors1_day_h": MoPropertyMeta("load_store_unit_uncorrectable_errors1_day_h", "LoadStoreUnitUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_uncorrectable_errors1_hour": MoPropertyMeta("load_store_unit_uncorrectable_errors1_hour", "LoadStoreUnitUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_uncorrectable_errors1_hour_h": MoPropertyMeta("load_store_unit_uncorrectable_errors1_hour_h", "LoadStoreUnitUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_uncorrectable_errors1_week": MoPropertyMeta("load_store_unit_uncorrectable_errors1_week", "LoadStoreUnitUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_uncorrectable_errors1_week_h": MoPropertyMeta("load_store_unit_uncorrectable_errors1_week_h", "LoadStoreUnitUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_uncorrectable_errors2_weeks": MoPropertyMeta("load_store_unit_uncorrectable_errors2_weeks", "LoadStoreUnitUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_store_unit_uncorrectable_errors2_weeks_h": MoPropertyMeta("load_store_unit_uncorrectable_errors2_weeks_h", "LoadStoreUnitUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
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
        "DecodeUnitCorrectableErrors": "decode_unit_correctable_errors", 
        "DecodeUnitCorrectableErrors15Min": "decode_unit_correctable_errors15_min", 
        "DecodeUnitCorrectableErrors15MinH": "decode_unit_correctable_errors15_min_h", 
        "DecodeUnitCorrectableErrors1Day": "decode_unit_correctable_errors1_day", 
        "DecodeUnitCorrectableErrors1DayH": "decode_unit_correctable_errors1_day_h", 
        "DecodeUnitCorrectableErrors1Hour": "decode_unit_correctable_errors1_hour", 
        "DecodeUnitCorrectableErrors1HourH": "decode_unit_correctable_errors1_hour_h", 
        "DecodeUnitCorrectableErrors1Week": "decode_unit_correctable_errors1_week", 
        "DecodeUnitCorrectableErrors1WeekH": "decode_unit_correctable_errors1_week_h", 
        "DecodeUnitCorrectableErrors2Weeks": "decode_unit_correctable_errors2_weeks", 
        "DecodeUnitCorrectableErrors2WeeksH": "decode_unit_correctable_errors2_weeks_h", 
        "DecodeUnitUncorrectableErrors": "decode_unit_uncorrectable_errors", 
        "DecodeUnitUncorrectableErrors15Min": "decode_unit_uncorrectable_errors15_min", 
        "DecodeUnitUncorrectableErrors15MinH": "decode_unit_uncorrectable_errors15_min_h", 
        "DecodeUnitUncorrectableErrors1Day": "decode_unit_uncorrectable_errors1_day", 
        "DecodeUnitUncorrectableErrors1DayH": "decode_unit_uncorrectable_errors1_day_h", 
        "DecodeUnitUncorrectableErrors1Hour": "decode_unit_uncorrectable_errors1_hour", 
        "DecodeUnitUncorrectableErrors1HourH": "decode_unit_uncorrectable_errors1_hour_h", 
        "DecodeUnitUncorrectableErrors1Week": "decode_unit_uncorrectable_errors1_week", 
        "DecodeUnitUncorrectableErrors1WeekH": "decode_unit_uncorrectable_errors1_week_h", 
        "DecodeUnitUncorrectableErrors2Weeks": "decode_unit_uncorrectable_errors2_weeks", 
        "DecodeUnitUncorrectableErrors2WeeksH": "decode_unit_uncorrectable_errors2_weeks_h", 
        "ExecutionUnitCorrectableErrors": "execution_unit_correctable_errors", 
        "ExecutionUnitCorrectableErrors15Min": "execution_unit_correctable_errors15_min", 
        "ExecutionUnitCorrectableErrors15MinH": "execution_unit_correctable_errors15_min_h", 
        "ExecutionUnitCorrectableErrors1Day": "execution_unit_correctable_errors1_day", 
        "ExecutionUnitCorrectableErrors1DayH": "execution_unit_correctable_errors1_day_h", 
        "ExecutionUnitCorrectableErrors1Hour": "execution_unit_correctable_errors1_hour", 
        "ExecutionUnitCorrectableErrors1HourH": "execution_unit_correctable_errors1_hour_h", 
        "ExecutionUnitCorrectableErrors1Week": "execution_unit_correctable_errors1_week", 
        "ExecutionUnitCorrectableErrors1WeekH": "execution_unit_correctable_errors1_week_h", 
        "ExecutionUnitCorrectableErrors2Weeks": "execution_unit_correctable_errors2_weeks", 
        "ExecutionUnitCorrectableErrors2WeeksH": "execution_unit_correctable_errors2_weeks_h", 
        "ExecutionUnitUncorrectableErrors": "execution_unit_uncorrectable_errors", 
        "ExecutionUnitUncorrectableErrors15Min": "execution_unit_uncorrectable_errors15_min", 
        "ExecutionUnitUncorrectableErrors15MinH": "execution_unit_uncorrectable_errors15_min_h", 
        "ExecutionUnitUncorrectableErrors1Day": "execution_unit_uncorrectable_errors1_day", 
        "ExecutionUnitUncorrectableErrors1DayH": "execution_unit_uncorrectable_errors1_day_h", 
        "ExecutionUnitUncorrectableErrors1Hour": "execution_unit_uncorrectable_errors1_hour", 
        "ExecutionUnitUncorrectableErrors1HourH": "execution_unit_uncorrectable_errors1_hour_h", 
        "ExecutionUnitUncorrectableErrors1Week": "execution_unit_uncorrectable_errors1_week", 
        "ExecutionUnitUncorrectableErrors1WeekH": "execution_unit_uncorrectable_errors1_week_h", 
        "ExecutionUnitUncorrectableErrors2Weeks": "execution_unit_uncorrectable_errors2_weeks", 
        "ExecutionUnitUncorrectableErrors2WeeksH": "execution_unit_uncorrectable_errors2_weeks_h", 
        "InstructionFetchUnitCorrectableErrors": "instruction_fetch_unit_correctable_errors", 
        "InstructionFetchUnitCorrectableErrors15Min": "instruction_fetch_unit_correctable_errors15_min", 
        "InstructionFetchUnitCorrectableErrors15MinH": "instruction_fetch_unit_correctable_errors15_min_h", 
        "InstructionFetchUnitCorrectableErrors1Day": "instruction_fetch_unit_correctable_errors1_day", 
        "InstructionFetchUnitCorrectableErrors1DayH": "instruction_fetch_unit_correctable_errors1_day_h", 
        "InstructionFetchUnitCorrectableErrors1Hour": "instruction_fetch_unit_correctable_errors1_hour", 
        "InstructionFetchUnitCorrectableErrors1HourH": "instruction_fetch_unit_correctable_errors1_hour_h", 
        "InstructionFetchUnitCorrectableErrors1Week": "instruction_fetch_unit_correctable_errors1_week", 
        "InstructionFetchUnitCorrectableErrors1WeekH": "instruction_fetch_unit_correctable_errors1_week_h", 
        "InstructionFetchUnitCorrectableErrors2Weeks": "instruction_fetch_unit_correctable_errors2_weeks", 
        "InstructionFetchUnitCorrectableErrors2WeeksH": "instruction_fetch_unit_correctable_errors2_weeks_h", 
        "InstructionFetchUnitUncorrectableErrors": "instruction_fetch_unit_uncorrectable_errors", 
        "InstructionFetchUnitUncorrectableErrors15Min": "instruction_fetch_unit_uncorrectable_errors15_min", 
        "InstructionFetchUnitUncorrectableErrors15MinH": "instruction_fetch_unit_uncorrectable_errors15_min_h", 
        "InstructionFetchUnitUncorrectableErrors1Day": "instruction_fetch_unit_uncorrectable_errors1_day", 
        "InstructionFetchUnitUncorrectableErrors1DayH": "instruction_fetch_unit_uncorrectable_errors1_day_h", 
        "InstructionFetchUnitUncorrectableErrors1Hour": "instruction_fetch_unit_uncorrectable_errors1_hour", 
        "InstructionFetchUnitUncorrectableErrors1HourH": "instruction_fetch_unit_uncorrectable_errors1_hour_h", 
        "InstructionFetchUnitUncorrectableErrors1Week": "instruction_fetch_unit_uncorrectable_errors1_week", 
        "InstructionFetchUnitUncorrectableErrors1WeekH": "instruction_fetch_unit_uncorrectable_errors1_week_h", 
        "InstructionFetchUnitUncorrectableErrors2Weeks": "instruction_fetch_unit_uncorrectable_errors2_weeks", 
        "InstructionFetchUnitUncorrectableErrors2WeeksH": "instruction_fetch_unit_uncorrectable_errors2_weeks_h", 
        "LoadStoreUnitCorrectableErrors": "load_store_unit_correctable_errors", 
        "LoadStoreUnitCorrectableErrors15Min": "load_store_unit_correctable_errors15_min", 
        "LoadStoreUnitCorrectableErrors15MinH": "load_store_unit_correctable_errors15_min_h", 
        "LoadStoreUnitCorrectableErrors1Day": "load_store_unit_correctable_errors1_day", 
        "LoadStoreUnitCorrectableErrors1DayH": "load_store_unit_correctable_errors1_day_h", 
        "LoadStoreUnitCorrectableErrors1Hour": "load_store_unit_correctable_errors1_hour", 
        "LoadStoreUnitCorrectableErrors1HourH": "load_store_unit_correctable_errors1_hour_h", 
        "LoadStoreUnitCorrectableErrors1Week": "load_store_unit_correctable_errors1_week", 
        "LoadStoreUnitCorrectableErrors1WeekH": "load_store_unit_correctable_errors1_week_h", 
        "LoadStoreUnitCorrectableErrors2Weeks": "load_store_unit_correctable_errors2_weeks", 
        "LoadStoreUnitCorrectableErrors2WeeksH": "load_store_unit_correctable_errors2_weeks_h", 
        "LoadStoreUnitUncorrectableErrors": "load_store_unit_uncorrectable_errors", 
        "LoadStoreUnitUncorrectableErrors15Min": "load_store_unit_uncorrectable_errors15_min", 
        "LoadStoreUnitUncorrectableErrors15MinH": "load_store_unit_uncorrectable_errors15_min_h", 
        "LoadStoreUnitUncorrectableErrors1Day": "load_store_unit_uncorrectable_errors1_day", 
        "LoadStoreUnitUncorrectableErrors1DayH": "load_store_unit_uncorrectable_errors1_day_h", 
        "LoadStoreUnitUncorrectableErrors1Hour": "load_store_unit_uncorrectable_errors1_hour", 
        "LoadStoreUnitUncorrectableErrors1HourH": "load_store_unit_uncorrectable_errors1_hour_h", 
        "LoadStoreUnitUncorrectableErrors1Week": "load_store_unit_uncorrectable_errors1_week", 
        "LoadStoreUnitUncorrectableErrors1WeekH": "load_store_unit_uncorrectable_errors1_week_h", 
        "LoadStoreUnitUncorrectableErrors2Weeks": "load_store_unit_uncorrectable_errors2_weeks", 
        "LoadStoreUnitUncorrectableErrors2WeeksH": "load_store_unit_uncorrectable_errors2_weeks_h", 
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
        self.decode_unit_correctable_errors = None
        self.decode_unit_correctable_errors15_min = None
        self.decode_unit_correctable_errors15_min_h = None
        self.decode_unit_correctable_errors1_day = None
        self.decode_unit_correctable_errors1_day_h = None
        self.decode_unit_correctable_errors1_hour = None
        self.decode_unit_correctable_errors1_hour_h = None
        self.decode_unit_correctable_errors1_week = None
        self.decode_unit_correctable_errors1_week_h = None
        self.decode_unit_correctable_errors2_weeks = None
        self.decode_unit_correctable_errors2_weeks_h = None
        self.decode_unit_uncorrectable_errors = None
        self.decode_unit_uncorrectable_errors15_min = None
        self.decode_unit_uncorrectable_errors15_min_h = None
        self.decode_unit_uncorrectable_errors1_day = None
        self.decode_unit_uncorrectable_errors1_day_h = None
        self.decode_unit_uncorrectable_errors1_hour = None
        self.decode_unit_uncorrectable_errors1_hour_h = None
        self.decode_unit_uncorrectable_errors1_week = None
        self.decode_unit_uncorrectable_errors1_week_h = None
        self.decode_unit_uncorrectable_errors2_weeks = None
        self.decode_unit_uncorrectable_errors2_weeks_h = None
        self.execution_unit_correctable_errors = None
        self.execution_unit_correctable_errors15_min = None
        self.execution_unit_correctable_errors15_min_h = None
        self.execution_unit_correctable_errors1_day = None
        self.execution_unit_correctable_errors1_day_h = None
        self.execution_unit_correctable_errors1_hour = None
        self.execution_unit_correctable_errors1_hour_h = None
        self.execution_unit_correctable_errors1_week = None
        self.execution_unit_correctable_errors1_week_h = None
        self.execution_unit_correctable_errors2_weeks = None
        self.execution_unit_correctable_errors2_weeks_h = None
        self.execution_unit_uncorrectable_errors = None
        self.execution_unit_uncorrectable_errors15_min = None
        self.execution_unit_uncorrectable_errors15_min_h = None
        self.execution_unit_uncorrectable_errors1_day = None
        self.execution_unit_uncorrectable_errors1_day_h = None
        self.execution_unit_uncorrectable_errors1_hour = None
        self.execution_unit_uncorrectable_errors1_hour_h = None
        self.execution_unit_uncorrectable_errors1_week = None
        self.execution_unit_uncorrectable_errors1_week_h = None
        self.execution_unit_uncorrectable_errors2_weeks = None
        self.execution_unit_uncorrectable_errors2_weeks_h = None
        self.instruction_fetch_unit_correctable_errors = None
        self.instruction_fetch_unit_correctable_errors15_min = None
        self.instruction_fetch_unit_correctable_errors15_min_h = None
        self.instruction_fetch_unit_correctable_errors1_day = None
        self.instruction_fetch_unit_correctable_errors1_day_h = None
        self.instruction_fetch_unit_correctable_errors1_hour = None
        self.instruction_fetch_unit_correctable_errors1_hour_h = None
        self.instruction_fetch_unit_correctable_errors1_week = None
        self.instruction_fetch_unit_correctable_errors1_week_h = None
        self.instruction_fetch_unit_correctable_errors2_weeks = None
        self.instruction_fetch_unit_correctable_errors2_weeks_h = None
        self.instruction_fetch_unit_uncorrectable_errors = None
        self.instruction_fetch_unit_uncorrectable_errors15_min = None
        self.instruction_fetch_unit_uncorrectable_errors15_min_h = None
        self.instruction_fetch_unit_uncorrectable_errors1_day = None
        self.instruction_fetch_unit_uncorrectable_errors1_day_h = None
        self.instruction_fetch_unit_uncorrectable_errors1_hour = None
        self.instruction_fetch_unit_uncorrectable_errors1_hour_h = None
        self.instruction_fetch_unit_uncorrectable_errors1_week = None
        self.instruction_fetch_unit_uncorrectable_errors1_week_h = None
        self.instruction_fetch_unit_uncorrectable_errors2_weeks = None
        self.instruction_fetch_unit_uncorrectable_errors2_weeks_h = None
        self.load_store_unit_correctable_errors = None
        self.load_store_unit_correctable_errors15_min = None
        self.load_store_unit_correctable_errors15_min_h = None
        self.load_store_unit_correctable_errors1_day = None
        self.load_store_unit_correctable_errors1_day_h = None
        self.load_store_unit_correctable_errors1_hour = None
        self.load_store_unit_correctable_errors1_hour_h = None
        self.load_store_unit_correctable_errors1_week = None
        self.load_store_unit_correctable_errors1_week_h = None
        self.load_store_unit_correctable_errors2_weeks = None
        self.load_store_unit_correctable_errors2_weeks_h = None
        self.load_store_unit_uncorrectable_errors = None
        self.load_store_unit_uncorrectable_errors15_min = None
        self.load_store_unit_uncorrectable_errors15_min_h = None
        self.load_store_unit_uncorrectable_errors1_day = None
        self.load_store_unit_uncorrectable_errors1_day_h = None
        self.load_store_unit_uncorrectable_errors1_hour = None
        self.load_store_unit_uncorrectable_errors1_hour_h = None
        self.load_store_unit_uncorrectable_errors1_week = None
        self.load_store_unit_uncorrectable_errors1_week_h = None
        self.load_store_unit_uncorrectable_errors2_weeks = None
        self.load_store_unit_uncorrectable_errors2_weeks_h = None
        self.child_action = None
        self.intervals = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "ProcessorExecStats", parent_mo_or_dn, **kwargs)
