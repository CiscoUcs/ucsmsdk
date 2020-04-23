"""This module contains the general information for AdaptorHostMgmtCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorHostMgmtCapConsts:
    MODE_FULL = "full"
    MODE_PARTIAL = "partial"
    OPER_POWER_REQUIREMENT_FULL = "full"
    OPER_POWER_REQUIREMENT_NONE = "none"
    OPER_POWER_REQUIREMENT_STANDBY = "standby"
    PREBOOT_EFI = "EFI"
    PREBOOT_PNU_OS = "PnuOS"
    PREBOOT_NONE = "none"
    PRESENCE_CIMC = "cimc"
    PRESENCE_HOST = "host"
    PRESENCE_UNSPECIFIED = "unspecified"
    REBOOT_ACTION_ON_DESTRUCTIVE_ADAPTOR = "adaptor"
    REBOOT_ACTION_ON_DESTRUCTIVE_HOST = "host"
    REBOOT_ACTION_ON_DESTRUCTIVE_NONE = "none"


class AdaptorHostMgmtCap(ManagedObject):
    """This is AdaptorHostMgmtCap class."""

    consts = AdaptorHostMgmtCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorHostMgmtCap", "adaptorHostMgmtCap", "host-mgmt", VersionMeta.Version101e, "InputOutput", 0x3ff, [], ["read-only"], ['adaptorFruCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["full", "partial"], []),
        "oper_power_requirement": MoPropertyMeta("oper_power_requirement", "operPowerRequirement", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["full", "none", "standby"], []),
        "preboot": MoPropertyMeta("preboot", "preboot", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["EFI", "PnuOS", "none"], []),
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["cimc", "host", "unspecified"], []),
        "reboot_action_on_destructive": MoPropertyMeta("reboot_action_on_destructive", "rebootActionOnDestructive", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["adaptor", "host", "none"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "mode": "mode", 
        "operPowerRequirement": "oper_power_requirement", 
        "preboot": "preboot", 
        "presence": "presence", 
        "rebootActionOnDestructive": "reboot_action_on_destructive", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.mode = None
        self.oper_power_requirement = None
        self.preboot = None
        self.presence = None
        self.reboot_action_on_destructive = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorHostMgmtCap", parent_mo_or_dn, **kwargs)
