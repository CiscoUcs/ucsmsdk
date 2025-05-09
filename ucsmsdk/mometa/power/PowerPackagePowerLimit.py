"""This module contains the general information for PowerPackagePowerLimit ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class PowerPackagePowerLimitConsts:
    CONFIG_STATUS_FAILURE = "failure"
    CONFIG_STATUS_PENDING = "pending"
    CONFIG_STATUS_SUCCESS = "success"
    CONFIG_STATUS_UNKNOWN = "unknown"
    CONFIGURED_PPL_DEFAULT = "Default"
    CONFIGURED_PPL_MAX = "Max"
    CONFIGURED_PPL_MIN = "Min"
    POLICY_CONFIGURED_PPL_DEFAULT = "Default"
    POLICY_CONFIGURED_PPL_MAX = "Max"
    POLICY_CONFIGURED_PPL_MIN = "Min"


class PowerPackagePowerLimit(ManagedObject):
    """This is PowerPackagePowerLimit class."""

    consts = PowerPackagePowerLimitConsts()
    naming_props = set([])

    mo_meta = MoMeta("PowerPackagePowerLimit", "powerPackagePowerLimit", "ppl", VersionMeta.Version436a, "InputOutput", 0x1f, [], ["admin", "power-mgmt"], ['powerBudget'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version436a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_status": MoPropertyMeta("config_status", "configStatus", "string", VersionMeta.Version436a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failure", "pending", "success", "unknown"], []),
        "configured_ppl": MoPropertyMeta("configured_ppl", "configuredPpl", "string", VersionMeta.Version436a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Default", "Max", "Min"], []),
        "current_ppl": MoPropertyMeta("current_ppl", "currentPpl", "ushort", VersionMeta.Version436a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "default_ppl": MoPropertyMeta("default_ppl", "defaultPpl", "ushort", VersionMeta.Version436a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version436a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "max_ppl": MoPropertyMeta("max_ppl", "maxPpl", "ushort", VersionMeta.Version436a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "min_ppl": MoPropertyMeta("min_ppl", "minPpl", "ushort", VersionMeta.Version436a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "policy_configured_ppl": MoPropertyMeta("policy_configured_ppl", "policyConfiguredPpl", "string", VersionMeta.Version436a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Default", "Max", "Min"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version436a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version436a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version436a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configStatus": "config_status", 
        "configuredPpl": "configured_ppl", 
        "currentPpl": "current_ppl", 
        "defaultPpl": "default_ppl", 
        "dn": "dn", 
        "maxPpl": "max_ppl", 
        "minPpl": "min_ppl", 
        "policyConfiguredPpl": "policy_configured_ppl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.config_status = None
        self.configured_ppl = None
        self.current_ppl = None
        self.default_ppl = None
        self.max_ppl = None
        self.min_ppl = None
        self.policy_configured_ppl = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PowerPackagePowerLimit", parent_mo_or_dn, **kwargs)
