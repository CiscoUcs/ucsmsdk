"""This module contains the general information for BiosVfProcessorEnergyConfiguration ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfProcessorEnergyConfigurationConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_ENERGY_PERFORMANCE_BALANCED_ENERGY = "balanced-energy"
    VP_ENERGY_PERFORMANCE_BALANCED_PERFORMANCE = "balanced-performance"
    VP_ENERGY_PERFORMANCE_ENERGY_EFFICIENT = "energy-efficient"
    VP_ENERGY_PERFORMANCE_PERFORMANCE = "performance"
    VP_ENERGY_PERFORMANCE_PLATFORM_DEFAULT = "platform-default"
    VP_ENERGY_PERFORMANCE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_POWER_TECHNOLOGY_CUSTOM = "custom"
    VP_POWER_TECHNOLOGY_DISABLED = "disabled"
    VP_POWER_TECHNOLOGY_ENERGY_EFFICIENT = "energy-efficient"
    VP_POWER_TECHNOLOGY_PERFORMANCE = "performance"
    VP_POWER_TECHNOLOGY_PLATFORM_DEFAULT = "platform-default"
    VP_POWER_TECHNOLOGY_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfProcessorEnergyConfiguration(ManagedObject):
    """This is BiosVfProcessorEnergyConfiguration class."""

    consts = BiosVfProcessorEnergyConfigurationConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfProcessorEnergyConfiguration", "biosVfProcessorEnergyConfiguration", "Processor-Energy-Configuration", VersionMeta.Version222c, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosSettings', 'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "vp_energy_performance": MoPropertyMeta("vp_energy_performance", "vpEnergyPerformance", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["balanced-energy", "balanced-performance", "energy-efficient", "performance", "platform-default", "platform-recommended"], []),
        "vp_power_technology": MoPropertyMeta("vp_power_technology", "vpPowerTechnology", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["custom", "disabled", "energy-efficient", "performance", "platform-default", "platform-recommended"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpEnergyPerformance": "vp_energy_performance", 
        "vpPowerTechnology": "vp_power_technology", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_energy_performance = None
        self.vp_power_technology = None

        ManagedObject.__init__(self, "BiosVfProcessorEnergyConfiguration", parent_mo_or_dn, **kwargs)
