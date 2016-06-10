"""This module contains the general information for BiosVfCPUPowerManagement ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfCPUPowerManagementConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_CPUPOWER_MANAGEMENT_CUSTOM = "custom"
    VP_CPUPOWER_MANAGEMENT_DISABLED = "disabled"
    VP_CPUPOWER_MANAGEMENT_ENERGY_EFFICIENT = "energy-efficient"
    VP_CPUPOWER_MANAGEMENT_PERFORMANCE = "performance"
    VP_CPUPOWER_MANAGEMENT_PLATFORM_DEFAULT = "platform-default"
    VP_CPUPOWER_MANAGEMENT_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfCPUPowerManagement(ManagedObject):
    """This is BiosVfCPUPowerManagement class."""

    consts = BiosVfCPUPowerManagementConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfCPUPowerManagement", "biosVfCPUPowerManagement", "CPU-Power-Management", VersionMeta.Version302a, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosSettings', u'biosVProfile'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_cpu_power_management": MoPropertyMeta("vp_cpu_power_management", "vpCPUPowerManagement", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["custom", "disabled", "energy-efficient", "performance", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpCPUPowerManagement": "vp_cpu_power_management", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_cpu_power_management = None

        ManagedObject.__init__(self, "BiosVfCPUPowerManagement", parent_mo_or_dn, **kwargs)
