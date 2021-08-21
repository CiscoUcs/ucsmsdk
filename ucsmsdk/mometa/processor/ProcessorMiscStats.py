"""This module contains the general information for ProcessorMiscStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ProcessorMiscStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ProcessorMiscStats(ManagedObject):
    """This is ProcessorMiscStats class."""

    consts = ProcessorMiscStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcessorMiscStats", "processorMiscStats", "misc-stats", VersionMeta.Version412a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['processorUnit'], [], [None])

    prop_meta = {
        "coherent_slave_correctable_errors": MoPropertyMeta("coherent_slave_correctable_errors", "CoherentSlaveCorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_correctable_errors15_min": MoPropertyMeta("coherent_slave_correctable_errors15_min", "CoherentSlaveCorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_correctable_errors15_min_h": MoPropertyMeta("coherent_slave_correctable_errors15_min_h", "CoherentSlaveCorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_correctable_errors1_day": MoPropertyMeta("coherent_slave_correctable_errors1_day", "CoherentSlaveCorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_correctable_errors1_day_h": MoPropertyMeta("coherent_slave_correctable_errors1_day_h", "CoherentSlaveCorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_correctable_errors1_hour": MoPropertyMeta("coherent_slave_correctable_errors1_hour", "CoherentSlaveCorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_correctable_errors1_hour_h": MoPropertyMeta("coherent_slave_correctable_errors1_hour_h", "CoherentSlaveCorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_correctable_errors1_week": MoPropertyMeta("coherent_slave_correctable_errors1_week", "CoherentSlaveCorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_correctable_errors1_week_h": MoPropertyMeta("coherent_slave_correctable_errors1_week_h", "CoherentSlaveCorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_correctable_errors2_weeks": MoPropertyMeta("coherent_slave_correctable_errors2_weeks", "CoherentSlaveCorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_correctable_errors2_weeks_h": MoPropertyMeta("coherent_slave_correctable_errors2_weeks_h", "CoherentSlaveCorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_uncorrectable_errors": MoPropertyMeta("coherent_slave_uncorrectable_errors", "CoherentSlaveUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_uncorrectable_errors15_min": MoPropertyMeta("coherent_slave_uncorrectable_errors15_min", "CoherentSlaveUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_uncorrectable_errors15_min_h": MoPropertyMeta("coherent_slave_uncorrectable_errors15_min_h", "CoherentSlaveUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_uncorrectable_errors1_day": MoPropertyMeta("coherent_slave_uncorrectable_errors1_day", "CoherentSlaveUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_uncorrectable_errors1_day_h": MoPropertyMeta("coherent_slave_uncorrectable_errors1_day_h", "CoherentSlaveUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_uncorrectable_errors1_hour": MoPropertyMeta("coherent_slave_uncorrectable_errors1_hour", "CoherentSlaveUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_uncorrectable_errors1_hour_h": MoPropertyMeta("coherent_slave_uncorrectable_errors1_hour_h", "CoherentSlaveUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_uncorrectable_errors1_week": MoPropertyMeta("coherent_slave_uncorrectable_errors1_week", "CoherentSlaveUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_uncorrectable_errors1_week_h": MoPropertyMeta("coherent_slave_uncorrectable_errors1_week_h", "CoherentSlaveUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_uncorrectable_errors2_weeks": MoPropertyMeta("coherent_slave_uncorrectable_errors2_weeks", "CoherentSlaveUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "coherent_slave_uncorrectable_errors2_weeks_h": MoPropertyMeta("coherent_slave_uncorrectable_errors2_weeks_h", "CoherentSlaveUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_correctable_errors": MoPropertyMeta("floating_point_unit_correctable_errors", "FloatingPointUnitCorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_correctable_errors15_min": MoPropertyMeta("floating_point_unit_correctable_errors15_min", "FloatingPointUnitCorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_correctable_errors15_min_h": MoPropertyMeta("floating_point_unit_correctable_errors15_min_h", "FloatingPointUnitCorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_correctable_errors1_day": MoPropertyMeta("floating_point_unit_correctable_errors1_day", "FloatingPointUnitCorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_correctable_errors1_day_h": MoPropertyMeta("floating_point_unit_correctable_errors1_day_h", "FloatingPointUnitCorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_correctable_errors1_hour": MoPropertyMeta("floating_point_unit_correctable_errors1_hour", "FloatingPointUnitCorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_correctable_errors1_hour_h": MoPropertyMeta("floating_point_unit_correctable_errors1_hour_h", "FloatingPointUnitCorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_correctable_errors1_week": MoPropertyMeta("floating_point_unit_correctable_errors1_week", "FloatingPointUnitCorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_correctable_errors1_week_h": MoPropertyMeta("floating_point_unit_correctable_errors1_week_h", "FloatingPointUnitCorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_correctable_errors2_weeks": MoPropertyMeta("floating_point_unit_correctable_errors2_weeks", "FloatingPointUnitCorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_correctable_errors2_weeks_h": MoPropertyMeta("floating_point_unit_correctable_errors2_weeks_h", "FloatingPointUnitCorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_uncorrectable_errors": MoPropertyMeta("floating_point_unit_uncorrectable_errors", "FloatingPointUnitUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_uncorrectable_errors15_min": MoPropertyMeta("floating_point_unit_uncorrectable_errors15_min", "FloatingPointUnitUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_uncorrectable_errors15_min_h": MoPropertyMeta("floating_point_unit_uncorrectable_errors15_min_h", "FloatingPointUnitUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_uncorrectable_errors1_day": MoPropertyMeta("floating_point_unit_uncorrectable_errors1_day", "FloatingPointUnitUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_uncorrectable_errors1_day_h": MoPropertyMeta("floating_point_unit_uncorrectable_errors1_day_h", "FloatingPointUnitUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_uncorrectable_errors1_hour": MoPropertyMeta("floating_point_unit_uncorrectable_errors1_hour", "FloatingPointUnitUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_uncorrectable_errors1_hour_h": MoPropertyMeta("floating_point_unit_uncorrectable_errors1_hour_h", "FloatingPointUnitUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_uncorrectable_errors1_week": MoPropertyMeta("floating_point_unit_uncorrectable_errors1_week", "FloatingPointUnitUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_uncorrectable_errors1_week_h": MoPropertyMeta("floating_point_unit_uncorrectable_errors1_week_h", "FloatingPointUnitUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_uncorrectable_errors2_weeks": MoPropertyMeta("floating_point_unit_uncorrectable_errors2_weeks", "FloatingPointUnitUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "floating_point_unit_uncorrectable_errors2_weeks_h": MoPropertyMeta("floating_point_unit_uncorrectable_errors2_weeks_h", "FloatingPointUnitUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_correctable_errors": MoPropertyMeta("mp_mgmnt_controller_correctable_errors", "MPMgmntControllerCorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_correctable_errors15_min": MoPropertyMeta("mp_mgmnt_controller_correctable_errors15_min", "MPMgmntControllerCorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_correctable_errors15_min_h": MoPropertyMeta("mp_mgmnt_controller_correctable_errors15_min_h", "MPMgmntControllerCorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_correctable_errors1_day": MoPropertyMeta("mp_mgmnt_controller_correctable_errors1_day", "MPMgmntControllerCorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_correctable_errors1_day_h": MoPropertyMeta("mp_mgmnt_controller_correctable_errors1_day_h", "MPMgmntControllerCorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_correctable_errors1_hour": MoPropertyMeta("mp_mgmnt_controller_correctable_errors1_hour", "MPMgmntControllerCorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_correctable_errors1_hour_h": MoPropertyMeta("mp_mgmnt_controller_correctable_errors1_hour_h", "MPMgmntControllerCorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_correctable_errors1_week": MoPropertyMeta("mp_mgmnt_controller_correctable_errors1_week", "MPMgmntControllerCorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_correctable_errors1_week_h": MoPropertyMeta("mp_mgmnt_controller_correctable_errors1_week_h", "MPMgmntControllerCorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_correctable_errors2_weeks": MoPropertyMeta("mp_mgmnt_controller_correctable_errors2_weeks", "MPMgmntControllerCorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_correctable_errors2_weeks_h": MoPropertyMeta("mp_mgmnt_controller_correctable_errors2_weeks_h", "MPMgmntControllerCorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_uncorrectable_errors": MoPropertyMeta("mp_mgmnt_controller_uncorrectable_errors", "MPMgmntControllerUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_uncorrectable_errors15_min": MoPropertyMeta("mp_mgmnt_controller_uncorrectable_errors15_min", "MPMgmntControllerUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_uncorrectable_errors15_min_h": MoPropertyMeta("mp_mgmnt_controller_uncorrectable_errors15_min_h", "MPMgmntControllerUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_uncorrectable_errors1_day": MoPropertyMeta("mp_mgmnt_controller_uncorrectable_errors1_day", "MPMgmntControllerUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_uncorrectable_errors1_day_h": MoPropertyMeta("mp_mgmnt_controller_uncorrectable_errors1_day_h", "MPMgmntControllerUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_uncorrectable_errors1_hour": MoPropertyMeta("mp_mgmnt_controller_uncorrectable_errors1_hour", "MPMgmntControllerUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_uncorrectable_errors1_hour_h": MoPropertyMeta("mp_mgmnt_controller_uncorrectable_errors1_hour_h", "MPMgmntControllerUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_uncorrectable_errors1_week": MoPropertyMeta("mp_mgmnt_controller_uncorrectable_errors1_week", "MPMgmntControllerUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_uncorrectable_errors1_week_h": MoPropertyMeta("mp_mgmnt_controller_uncorrectable_errors1_week_h", "MPMgmntControllerUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_uncorrectable_errors2_weeks": MoPropertyMeta("mp_mgmnt_controller_uncorrectable_errors2_weeks", "MPMgmntControllerUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mp_mgmnt_controller_uncorrectable_errors2_weeks_h": MoPropertyMeta("mp_mgmnt_controller_uncorrectable_errors2_weeks_h", "MPMgmntControllerUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_correctable_errors": MoPropertyMeta("parameter_block_correctable_errors", "ParameterBlockCorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_correctable_errors15_min": MoPropertyMeta("parameter_block_correctable_errors15_min", "ParameterBlockCorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_correctable_errors15_min_h": MoPropertyMeta("parameter_block_correctable_errors15_min_h", "ParameterBlockCorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_correctable_errors1_day": MoPropertyMeta("parameter_block_correctable_errors1_day", "ParameterBlockCorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_correctable_errors1_day_h": MoPropertyMeta("parameter_block_correctable_errors1_day_h", "ParameterBlockCorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_correctable_errors1_hour": MoPropertyMeta("parameter_block_correctable_errors1_hour", "ParameterBlockCorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_correctable_errors1_hour_h": MoPropertyMeta("parameter_block_correctable_errors1_hour_h", "ParameterBlockCorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_correctable_errors1_week": MoPropertyMeta("parameter_block_correctable_errors1_week", "ParameterBlockCorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_correctable_errors1_week_h": MoPropertyMeta("parameter_block_correctable_errors1_week_h", "ParameterBlockCorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_correctable_errors2_weeks": MoPropertyMeta("parameter_block_correctable_errors2_weeks", "ParameterBlockCorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_correctable_errors2_weeks_h": MoPropertyMeta("parameter_block_correctable_errors2_weeks_h", "ParameterBlockCorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_uncorrectable_errors": MoPropertyMeta("parameter_block_uncorrectable_errors", "ParameterBlockUncorrectableErrors", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_uncorrectable_errors15_min": MoPropertyMeta("parameter_block_uncorrectable_errors15_min", "ParameterBlockUncorrectableErrors15Min", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_uncorrectable_errors15_min_h": MoPropertyMeta("parameter_block_uncorrectable_errors15_min_h", "ParameterBlockUncorrectableErrors15MinH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_uncorrectable_errors1_day": MoPropertyMeta("parameter_block_uncorrectable_errors1_day", "ParameterBlockUncorrectableErrors1Day", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_uncorrectable_errors1_day_h": MoPropertyMeta("parameter_block_uncorrectable_errors1_day_h", "ParameterBlockUncorrectableErrors1DayH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_uncorrectable_errors1_hour": MoPropertyMeta("parameter_block_uncorrectable_errors1_hour", "ParameterBlockUncorrectableErrors1Hour", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_uncorrectable_errors1_hour_h": MoPropertyMeta("parameter_block_uncorrectable_errors1_hour_h", "ParameterBlockUncorrectableErrors1HourH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_uncorrectable_errors1_week": MoPropertyMeta("parameter_block_uncorrectable_errors1_week", "ParameterBlockUncorrectableErrors1Week", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_uncorrectable_errors1_week_h": MoPropertyMeta("parameter_block_uncorrectable_errors1_week_h", "ParameterBlockUncorrectableErrors1WeekH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_uncorrectable_errors2_weeks": MoPropertyMeta("parameter_block_uncorrectable_errors2_weeks", "ParameterBlockUncorrectableErrors2Weeks", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "parameter_block_uncorrectable_errors2_weeks_h": MoPropertyMeta("parameter_block_uncorrectable_errors2_weeks_h", "ParameterBlockUncorrectableErrors2WeeksH", "uint", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
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
        "CoherentSlaveCorrectableErrors": "coherent_slave_correctable_errors", 
        "CoherentSlaveCorrectableErrors15Min": "coherent_slave_correctable_errors15_min", 
        "CoherentSlaveCorrectableErrors15MinH": "coherent_slave_correctable_errors15_min_h", 
        "CoherentSlaveCorrectableErrors1Day": "coherent_slave_correctable_errors1_day", 
        "CoherentSlaveCorrectableErrors1DayH": "coherent_slave_correctable_errors1_day_h", 
        "CoherentSlaveCorrectableErrors1Hour": "coherent_slave_correctable_errors1_hour", 
        "CoherentSlaveCorrectableErrors1HourH": "coherent_slave_correctable_errors1_hour_h", 
        "CoherentSlaveCorrectableErrors1Week": "coherent_slave_correctable_errors1_week", 
        "CoherentSlaveCorrectableErrors1WeekH": "coherent_slave_correctable_errors1_week_h", 
        "CoherentSlaveCorrectableErrors2Weeks": "coherent_slave_correctable_errors2_weeks", 
        "CoherentSlaveCorrectableErrors2WeeksH": "coherent_slave_correctable_errors2_weeks_h", 
        "CoherentSlaveUncorrectableErrors": "coherent_slave_uncorrectable_errors", 
        "CoherentSlaveUncorrectableErrors15Min": "coherent_slave_uncorrectable_errors15_min", 
        "CoherentSlaveUncorrectableErrors15MinH": "coherent_slave_uncorrectable_errors15_min_h", 
        "CoherentSlaveUncorrectableErrors1Day": "coherent_slave_uncorrectable_errors1_day", 
        "CoherentSlaveUncorrectableErrors1DayH": "coherent_slave_uncorrectable_errors1_day_h", 
        "CoherentSlaveUncorrectableErrors1Hour": "coherent_slave_uncorrectable_errors1_hour", 
        "CoherentSlaveUncorrectableErrors1HourH": "coherent_slave_uncorrectable_errors1_hour_h", 
        "CoherentSlaveUncorrectableErrors1Week": "coherent_slave_uncorrectable_errors1_week", 
        "CoherentSlaveUncorrectableErrors1WeekH": "coherent_slave_uncorrectable_errors1_week_h", 
        "CoherentSlaveUncorrectableErrors2Weeks": "coherent_slave_uncorrectable_errors2_weeks", 
        "CoherentSlaveUncorrectableErrors2WeeksH": "coherent_slave_uncorrectable_errors2_weeks_h", 
        "FloatingPointUnitCorrectableErrors": "floating_point_unit_correctable_errors", 
        "FloatingPointUnitCorrectableErrors15Min": "floating_point_unit_correctable_errors15_min", 
        "FloatingPointUnitCorrectableErrors15MinH": "floating_point_unit_correctable_errors15_min_h", 
        "FloatingPointUnitCorrectableErrors1Day": "floating_point_unit_correctable_errors1_day", 
        "FloatingPointUnitCorrectableErrors1DayH": "floating_point_unit_correctable_errors1_day_h", 
        "FloatingPointUnitCorrectableErrors1Hour": "floating_point_unit_correctable_errors1_hour", 
        "FloatingPointUnitCorrectableErrors1HourH": "floating_point_unit_correctable_errors1_hour_h", 
        "FloatingPointUnitCorrectableErrors1Week": "floating_point_unit_correctable_errors1_week", 
        "FloatingPointUnitCorrectableErrors1WeekH": "floating_point_unit_correctable_errors1_week_h", 
        "FloatingPointUnitCorrectableErrors2Weeks": "floating_point_unit_correctable_errors2_weeks", 
        "FloatingPointUnitCorrectableErrors2WeeksH": "floating_point_unit_correctable_errors2_weeks_h", 
        "FloatingPointUnitUncorrectableErrors": "floating_point_unit_uncorrectable_errors", 
        "FloatingPointUnitUncorrectableErrors15Min": "floating_point_unit_uncorrectable_errors15_min", 
        "FloatingPointUnitUncorrectableErrors15MinH": "floating_point_unit_uncorrectable_errors15_min_h", 
        "FloatingPointUnitUncorrectableErrors1Day": "floating_point_unit_uncorrectable_errors1_day", 
        "FloatingPointUnitUncorrectableErrors1DayH": "floating_point_unit_uncorrectable_errors1_day_h", 
        "FloatingPointUnitUncorrectableErrors1Hour": "floating_point_unit_uncorrectable_errors1_hour", 
        "FloatingPointUnitUncorrectableErrors1HourH": "floating_point_unit_uncorrectable_errors1_hour_h", 
        "FloatingPointUnitUncorrectableErrors1Week": "floating_point_unit_uncorrectable_errors1_week", 
        "FloatingPointUnitUncorrectableErrors1WeekH": "floating_point_unit_uncorrectable_errors1_week_h", 
        "FloatingPointUnitUncorrectableErrors2Weeks": "floating_point_unit_uncorrectable_errors2_weeks", 
        "FloatingPointUnitUncorrectableErrors2WeeksH": "floating_point_unit_uncorrectable_errors2_weeks_h", 
        "MPMgmntControllerCorrectableErrors": "mp_mgmnt_controller_correctable_errors", 
        "MPMgmntControllerCorrectableErrors15Min": "mp_mgmnt_controller_correctable_errors15_min", 
        "MPMgmntControllerCorrectableErrors15MinH": "mp_mgmnt_controller_correctable_errors15_min_h", 
        "MPMgmntControllerCorrectableErrors1Day": "mp_mgmnt_controller_correctable_errors1_day", 
        "MPMgmntControllerCorrectableErrors1DayH": "mp_mgmnt_controller_correctable_errors1_day_h", 
        "MPMgmntControllerCorrectableErrors1Hour": "mp_mgmnt_controller_correctable_errors1_hour", 
        "MPMgmntControllerCorrectableErrors1HourH": "mp_mgmnt_controller_correctable_errors1_hour_h", 
        "MPMgmntControllerCorrectableErrors1Week": "mp_mgmnt_controller_correctable_errors1_week", 
        "MPMgmntControllerCorrectableErrors1WeekH": "mp_mgmnt_controller_correctable_errors1_week_h", 
        "MPMgmntControllerCorrectableErrors2Weeks": "mp_mgmnt_controller_correctable_errors2_weeks", 
        "MPMgmntControllerCorrectableErrors2WeeksH": "mp_mgmnt_controller_correctable_errors2_weeks_h", 
        "MPMgmntControllerUncorrectableErrors": "mp_mgmnt_controller_uncorrectable_errors", 
        "MPMgmntControllerUncorrectableErrors15Min": "mp_mgmnt_controller_uncorrectable_errors15_min", 
        "MPMgmntControllerUncorrectableErrors15MinH": "mp_mgmnt_controller_uncorrectable_errors15_min_h", 
        "MPMgmntControllerUncorrectableErrors1Day": "mp_mgmnt_controller_uncorrectable_errors1_day", 
        "MPMgmntControllerUncorrectableErrors1DayH": "mp_mgmnt_controller_uncorrectable_errors1_day_h", 
        "MPMgmntControllerUncorrectableErrors1Hour": "mp_mgmnt_controller_uncorrectable_errors1_hour", 
        "MPMgmntControllerUncorrectableErrors1HourH": "mp_mgmnt_controller_uncorrectable_errors1_hour_h", 
        "MPMgmntControllerUncorrectableErrors1Week": "mp_mgmnt_controller_uncorrectable_errors1_week", 
        "MPMgmntControllerUncorrectableErrors1WeekH": "mp_mgmnt_controller_uncorrectable_errors1_week_h", 
        "MPMgmntControllerUncorrectableErrors2Weeks": "mp_mgmnt_controller_uncorrectable_errors2_weeks", 
        "MPMgmntControllerUncorrectableErrors2WeeksH": "mp_mgmnt_controller_uncorrectable_errors2_weeks_h", 
        "ParameterBlockCorrectableErrors": "parameter_block_correctable_errors", 
        "ParameterBlockCorrectableErrors15Min": "parameter_block_correctable_errors15_min", 
        "ParameterBlockCorrectableErrors15MinH": "parameter_block_correctable_errors15_min_h", 
        "ParameterBlockCorrectableErrors1Day": "parameter_block_correctable_errors1_day", 
        "ParameterBlockCorrectableErrors1DayH": "parameter_block_correctable_errors1_day_h", 
        "ParameterBlockCorrectableErrors1Hour": "parameter_block_correctable_errors1_hour", 
        "ParameterBlockCorrectableErrors1HourH": "parameter_block_correctable_errors1_hour_h", 
        "ParameterBlockCorrectableErrors1Week": "parameter_block_correctable_errors1_week", 
        "ParameterBlockCorrectableErrors1WeekH": "parameter_block_correctable_errors1_week_h", 
        "ParameterBlockCorrectableErrors2Weeks": "parameter_block_correctable_errors2_weeks", 
        "ParameterBlockCorrectableErrors2WeeksH": "parameter_block_correctable_errors2_weeks_h", 
        "ParameterBlockUncorrectableErrors": "parameter_block_uncorrectable_errors", 
        "ParameterBlockUncorrectableErrors15Min": "parameter_block_uncorrectable_errors15_min", 
        "ParameterBlockUncorrectableErrors15MinH": "parameter_block_uncorrectable_errors15_min_h", 
        "ParameterBlockUncorrectableErrors1Day": "parameter_block_uncorrectable_errors1_day", 
        "ParameterBlockUncorrectableErrors1DayH": "parameter_block_uncorrectable_errors1_day_h", 
        "ParameterBlockUncorrectableErrors1Hour": "parameter_block_uncorrectable_errors1_hour", 
        "ParameterBlockUncorrectableErrors1HourH": "parameter_block_uncorrectable_errors1_hour_h", 
        "ParameterBlockUncorrectableErrors1Week": "parameter_block_uncorrectable_errors1_week", 
        "ParameterBlockUncorrectableErrors1WeekH": "parameter_block_uncorrectable_errors1_week_h", 
        "ParameterBlockUncorrectableErrors2Weeks": "parameter_block_uncorrectable_errors2_weeks", 
        "ParameterBlockUncorrectableErrors2WeeksH": "parameter_block_uncorrectable_errors2_weeks_h", 
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
        self.coherent_slave_correctable_errors = None
        self.coherent_slave_correctable_errors15_min = None
        self.coherent_slave_correctable_errors15_min_h = None
        self.coherent_slave_correctable_errors1_day = None
        self.coherent_slave_correctable_errors1_day_h = None
        self.coherent_slave_correctable_errors1_hour = None
        self.coherent_slave_correctable_errors1_hour_h = None
        self.coherent_slave_correctable_errors1_week = None
        self.coherent_slave_correctable_errors1_week_h = None
        self.coherent_slave_correctable_errors2_weeks = None
        self.coherent_slave_correctable_errors2_weeks_h = None
        self.coherent_slave_uncorrectable_errors = None
        self.coherent_slave_uncorrectable_errors15_min = None
        self.coherent_slave_uncorrectable_errors15_min_h = None
        self.coherent_slave_uncorrectable_errors1_day = None
        self.coherent_slave_uncorrectable_errors1_day_h = None
        self.coherent_slave_uncorrectable_errors1_hour = None
        self.coherent_slave_uncorrectable_errors1_hour_h = None
        self.coherent_slave_uncorrectable_errors1_week = None
        self.coherent_slave_uncorrectable_errors1_week_h = None
        self.coherent_slave_uncorrectable_errors2_weeks = None
        self.coherent_slave_uncorrectable_errors2_weeks_h = None
        self.floating_point_unit_correctable_errors = None
        self.floating_point_unit_correctable_errors15_min = None
        self.floating_point_unit_correctable_errors15_min_h = None
        self.floating_point_unit_correctable_errors1_day = None
        self.floating_point_unit_correctable_errors1_day_h = None
        self.floating_point_unit_correctable_errors1_hour = None
        self.floating_point_unit_correctable_errors1_hour_h = None
        self.floating_point_unit_correctable_errors1_week = None
        self.floating_point_unit_correctable_errors1_week_h = None
        self.floating_point_unit_correctable_errors2_weeks = None
        self.floating_point_unit_correctable_errors2_weeks_h = None
        self.floating_point_unit_uncorrectable_errors = None
        self.floating_point_unit_uncorrectable_errors15_min = None
        self.floating_point_unit_uncorrectable_errors15_min_h = None
        self.floating_point_unit_uncorrectable_errors1_day = None
        self.floating_point_unit_uncorrectable_errors1_day_h = None
        self.floating_point_unit_uncorrectable_errors1_hour = None
        self.floating_point_unit_uncorrectable_errors1_hour_h = None
        self.floating_point_unit_uncorrectable_errors1_week = None
        self.floating_point_unit_uncorrectable_errors1_week_h = None
        self.floating_point_unit_uncorrectable_errors2_weeks = None
        self.floating_point_unit_uncorrectable_errors2_weeks_h = None
        self.mp_mgmnt_controller_correctable_errors = None
        self.mp_mgmnt_controller_correctable_errors15_min = None
        self.mp_mgmnt_controller_correctable_errors15_min_h = None
        self.mp_mgmnt_controller_correctable_errors1_day = None
        self.mp_mgmnt_controller_correctable_errors1_day_h = None
        self.mp_mgmnt_controller_correctable_errors1_hour = None
        self.mp_mgmnt_controller_correctable_errors1_hour_h = None
        self.mp_mgmnt_controller_correctable_errors1_week = None
        self.mp_mgmnt_controller_correctable_errors1_week_h = None
        self.mp_mgmnt_controller_correctable_errors2_weeks = None
        self.mp_mgmnt_controller_correctable_errors2_weeks_h = None
        self.mp_mgmnt_controller_uncorrectable_errors = None
        self.mp_mgmnt_controller_uncorrectable_errors15_min = None
        self.mp_mgmnt_controller_uncorrectable_errors15_min_h = None
        self.mp_mgmnt_controller_uncorrectable_errors1_day = None
        self.mp_mgmnt_controller_uncorrectable_errors1_day_h = None
        self.mp_mgmnt_controller_uncorrectable_errors1_hour = None
        self.mp_mgmnt_controller_uncorrectable_errors1_hour_h = None
        self.mp_mgmnt_controller_uncorrectable_errors1_week = None
        self.mp_mgmnt_controller_uncorrectable_errors1_week_h = None
        self.mp_mgmnt_controller_uncorrectable_errors2_weeks = None
        self.mp_mgmnt_controller_uncorrectable_errors2_weeks_h = None
        self.parameter_block_correctable_errors = None
        self.parameter_block_correctable_errors15_min = None
        self.parameter_block_correctable_errors15_min_h = None
        self.parameter_block_correctable_errors1_day = None
        self.parameter_block_correctable_errors1_day_h = None
        self.parameter_block_correctable_errors1_hour = None
        self.parameter_block_correctable_errors1_hour_h = None
        self.parameter_block_correctable_errors1_week = None
        self.parameter_block_correctable_errors1_week_h = None
        self.parameter_block_correctable_errors2_weeks = None
        self.parameter_block_correctable_errors2_weeks_h = None
        self.parameter_block_uncorrectable_errors = None
        self.parameter_block_uncorrectable_errors15_min = None
        self.parameter_block_uncorrectable_errors15_min_h = None
        self.parameter_block_uncorrectable_errors1_day = None
        self.parameter_block_uncorrectable_errors1_day_h = None
        self.parameter_block_uncorrectable_errors1_hour = None
        self.parameter_block_uncorrectable_errors1_hour_h = None
        self.parameter_block_uncorrectable_errors1_week = None
        self.parameter_block_uncorrectable_errors1_week_h = None
        self.parameter_block_uncorrectable_errors2_weeks = None
        self.parameter_block_uncorrectable_errors2_weeks_h = None
        self.child_action = None
        self.intervals = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "ProcessorMiscStats", parent_mo_or_dn, **kwargs)
