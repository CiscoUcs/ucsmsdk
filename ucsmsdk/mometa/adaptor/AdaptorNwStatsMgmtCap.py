"""This module contains the general information for AdaptorNwStatsMgmtCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorNwStatsMgmtCapConsts:
    ENABLE_NW_STATS_COLLECTION_FALSE = "false"
    ENABLE_NW_STATS_COLLECTION_NO = "no"
    ENABLE_NW_STATS_COLLECTION_TRUE = "true"
    ENABLE_NW_STATS_COLLECTION_YES = "yes"
    MODE_FULL = "full"
    MODE_PARTIAL = "partial"
    OPER_POWER_REQUIREMENT_FULL = "full"
    OPER_POWER_REQUIREMENT_NONE = "none"
    OPER_POWER_REQUIREMENT_STANDBY = "standby"
    REBOOT_ACTION_ON_DESTRUCTIVE_ADAPTOR = "adaptor"
    REBOOT_ACTION_ON_DESTRUCTIVE_HOST = "host"
    REBOOT_ACTION_ON_DESTRUCTIVE_NONE = "none"


class AdaptorNwStatsMgmtCap(ManagedObject):
    """This is AdaptorNwStatsMgmtCap class."""

    consts = AdaptorNwStatsMgmtCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorNwStatsMgmtCap", "adaptorNwStatsMgmtCap", "nw-stats-mgmt", VersionMeta.Version302c, "InputOutput", 0x1ff, [], ["read-only"], ['adaptorFruCapProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "enable_nw_stats_collection": MoPropertyMeta("enable_nw_stats_collection", "enableNwStatsCollection", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["false", "no", "true", "yes"], []),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["full", "partial"], []),
        "oper_power_requirement": MoPropertyMeta("oper_power_requirement", "operPowerRequirement", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["full", "none", "standby"], []),
        "reboot_action_on_destructive": MoPropertyMeta("reboot_action_on_destructive", "rebootActionOnDestructive", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["adaptor", "host", "none"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "enableNwStatsCollection": "enable_nw_stats_collection", 
        "mode": "mode", 
        "operPowerRequirement": "oper_power_requirement", 
        "rebootActionOnDestructive": "reboot_action_on_destructive", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.enable_nw_stats_collection = None
        self.mode = None
        self.oper_power_requirement = None
        self.reboot_action_on_destructive = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorNwStatsMgmtCap", parent_mo_or_dn, **kwargs)
