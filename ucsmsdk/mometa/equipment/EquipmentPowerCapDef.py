"""This module contains the general information for EquipmentPowerCapDef ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentPowerCapDefConsts:
    IS_POWER_DEPLOYMENT_NEEDED_FALSE = "false"
    IS_POWER_DEPLOYMENT_NEEDED_NO = "no"
    IS_POWER_DEPLOYMENT_NEEDED_TRUE = "true"
    IS_POWER_DEPLOYMENT_NEEDED_YES = "yes"
    PROFILE_METHOD_DEFAULT = "default"
    PROFILE_METHOD_NODEMGR = "nodemgr"
    PROFILE_METHOD_PNUOS = "pnuos"
    PROFILE_METHOD_STATIC = "static"
    PROFILE_METHOD_UNKNOWN = "unknown"


class EquipmentPowerCapDef(ManagedObject):
    """This is EquipmentPowerCapDef class."""

    consts = EquipmentPowerCapDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentPowerCapDef", "equipmentPowerCapDef", "powercap", VersionMeta.Version302c, "InputOutput", 0x1f, [], [""], ['equipmentBladeCapProvider', 'equipmentChassisCapProvider', 'equipmentRackUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "is_power_deployment_needed": MoPropertyMeta("is_power_deployment_needed", "isPowerDeploymentNeeded", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "min_bios_version": MoPropertyMeta("min_bios_version", "minBiosVersion", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "min_cimc_version": MoPropertyMeta("min_cimc_version", "minCimcVersion", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "min_cmc_version": MoPropertyMeta("min_cmc_version", "minCmcVersion", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "profile_method": MoPropertyMeta("profile_method", "profileMethod", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["default", "nodemgr", "pnuos", "static", "unknown"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "isPowerDeploymentNeeded": "is_power_deployment_needed", 
        "minBiosVersion": "min_bios_version", 
        "minCimcVersion": "min_cimc_version", 
        "minCmcVersion": "min_cmc_version", 
        "profileMethod": "profile_method", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.is_power_deployment_needed = None
        self.min_bios_version = None
        self.min_cimc_version = None
        self.min_cmc_version = None
        self.profile_method = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPowerCapDef", parent_mo_or_dn, **kwargs)
