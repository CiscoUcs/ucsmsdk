"""This module contains the general information for BiosVfCPUHardwarePowerManagement ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class BiosVfCPUHardwarePowerManagementConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_CPUHARDWARE_POWER_MANAGEMENT_DISABLED = "disabled"
    VP_CPUHARDWARE_POWER_MANAGEMENT_HWPM_NATIVE_MODE = "hwpm-native-mode"
    VP_CPUHARDWARE_POWER_MANAGEMENT_HWPM_OOB_MODE = "hwpm-oob-mode"
    VP_CPUHARDWARE_POWER_MANAGEMENT_PLATFORM_DEFAULT = "platform-default"
    VP_CPUHARDWARE_POWER_MANAGEMENT_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfCPUHardwarePowerManagement(ManagedObject):
    """This is BiosVfCPUHardwarePowerManagement class."""

    consts = BiosVfCPUHardwarePowerManagementConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfCPUHardwarePowerManagement", "biosVfCPUHardwarePowerManagement", "CPU-Hardware-Power-Management", None, "InputOutput", 0x3fL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosSettings', u'biosVProfile'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_cpu_hardware_power_management": MoPropertyMeta("vp_cpu_hardware_power_management", "vpCPUHardwarePowerManagement", "string", None, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["disabled", "hwpm-native-mode", "hwpm-oob-mode", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpCPUHardwarePowerManagement": "vp_cpu_hardware_power_management", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_cpu_hardware_power_management = None

        ManagedObject.__init__(self, "BiosVfCPUHardwarePowerManagement", parent_mo_or_dn, **kwargs)

