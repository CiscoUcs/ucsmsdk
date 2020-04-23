"""This module contains the general information for PowerProfiledPower ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PowerProfiledPowerConsts:
    ABS_MIN_POST_POWER_UNBOUNDED = "unbounded"
    MAX_APP_POWER_UNBOUNDED = "unbounded"
    MAX_POST_POWER_UNBOUNDED = "unbounded"
    MIN_APP_POWER_UNBOUNDED = "unbounded"
    MIN_NORM_POST_POWER_UNBOUNDED = "unbounded"
    MIN_POST_POWER_UNBOUNDED = "unbounded"
    PRE_DISCOVERY_POWER_UNBOUNDED = "unbounded"
    PROFILED_BOOT_UNBOUNDED = "unbounded"
    PROFILED_MAX_UNBOUNDED = "unbounded"
    PROFILED_MIN_UNBOUNDED = "unbounded"
    SKIP_PROFILING_FALSE = "false"
    SKIP_PROFILING_NO = "no"
    SKIP_PROFILING_TRUE = "true"
    SKIP_PROFILING_YES = "yes"


class PowerProfiledPower(ManagedObject):
    """This is PowerProfiledPower class."""

    consts = PowerProfiledPowerConsts()
    naming_props = set([])

    mo_meta = MoMeta("PowerProfiledPower", "powerProfiledPower", "prof-power", VersionMeta.Version302c, "InputOutput", 0x1f, [], ["admin", "power-mgmt"], ['powerBudget'], [], ["Get"])

    prop_meta = {
        "abs_min_post_power": MoPropertyMeta("abs_min_post_power", "absMinPostPower", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "max_app_power": MoPropertyMeta("max_app_power", "maxAppPower", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
        "max_post_power": MoPropertyMeta("max_post_power", "maxPostPower", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
        "min_app_power": MoPropertyMeta("min_app_power", "minAppPower", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
        "min_norm_post_power": MoPropertyMeta("min_norm_post_power", "minNormPostPower", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
        "min_post_power": MoPropertyMeta("min_post_power", "minPostPower", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
        "pre_discovery_power": MoPropertyMeta("pre_discovery_power", "preDiscoveryPower", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
        "profile_run_time": MoPropertyMeta("profile_run_time", "profileRunTime", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "profiled_boot": MoPropertyMeta("profiled_boot", "profiledBoot", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
        "profiled_max": MoPropertyMeta("profiled_max", "profiledMax", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
        "profiled_min": MoPropertyMeta("profiled_min", "profiledMin", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "skip_profiling": MoPropertyMeta("skip_profiling", "skipProfiling", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "absMinPostPower": "abs_min_post_power", 
        "childAction": "child_action", 
        "dn": "dn", 
        "maxAppPower": "max_app_power", 
        "maxPostPower": "max_post_power", 
        "minAppPower": "min_app_power", 
        "minNormPostPower": "min_norm_post_power", 
        "minPostPower": "min_post_power", 
        "preDiscoveryPower": "pre_discovery_power", 
        "profileRunTime": "profile_run_time", 
        "profiledBoot": "profiled_boot", 
        "profiledMax": "profiled_max", 
        "profiledMin": "profiled_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "skipProfiling": "skip_profiling", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.abs_min_post_power = None
        self.child_action = None
        self.max_app_power = None
        self.max_post_power = None
        self.min_app_power = None
        self.min_norm_post_power = None
        self.min_post_power = None
        self.pre_discovery_power = None
        self.profile_run_time = None
        self.profiled_boot = None
        self.profiled_max = None
        self.profiled_min = None
        self.sacl = None
        self.skip_profiling = None
        self.status = None

        ManagedObject.__init__(self, "PowerProfiledPower", parent_mo_or_dn, **kwargs)
