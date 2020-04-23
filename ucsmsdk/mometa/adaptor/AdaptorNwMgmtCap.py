"""This module contains the general information for AdaptorNwMgmtCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorNwMgmtCapConsts:
    API_MENLO = "menlo"
    API_NONE = "none"
    API_PALO = "palo"
    MGMT_TRANSPORT_L2 = "L2"
    MGMT_TRANSPORT_L3 = "L3"
    MODE_FULL = "full"
    MODE_PARTIAL = "partial"
    OPER_POWER_REQUIREMENT_FULL = "full"
    OPER_POWER_REQUIREMENT_NONE = "none"
    OPER_POWER_REQUIREMENT_STANDBY = "standby"
    REBOOT_ACTION_ON_DESTRUCTIVE_ADAPTOR = "adaptor"
    REBOOT_ACTION_ON_DESTRUCTIVE_HOST = "host"
    REBOOT_ACTION_ON_DESTRUCTIVE_NONE = "none"


class AdaptorNwMgmtCap(ManagedObject):
    """This is AdaptorNwMgmtCap class."""

    consts = AdaptorNwMgmtCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorNwMgmtCap", "adaptorNwMgmtCap", "nw-mgmt", VersionMeta.Version101e, "InputOutput", 0x3ff, [], ["read-only"], ['adaptorFruCapProvider'], [], ["Get"])

    prop_meta = {
        "api": MoPropertyMeta("api", "api", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["menlo", "none", "palo"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "mgmt_transport": MoPropertyMeta("mgmt_transport", "mgmtTransport", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["L2", "L3"], []),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["full", "partial"], []),
        "oper_power_requirement": MoPropertyMeta("oper_power_requirement", "operPowerRequirement", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["full", "none", "standby"], []),
        "reboot_action_on_destructive": MoPropertyMeta("reboot_action_on_destructive", "rebootActionOnDestructive", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["adaptor", "host", "none"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "api": "api", 
        "childAction": "child_action", 
        "dn": "dn", 
        "mgmtTransport": "mgmt_transport", 
        "mode": "mode", 
        "operPowerRequirement": "oper_power_requirement", 
        "rebootActionOnDestructive": "reboot_action_on_destructive", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.api = None
        self.child_action = None
        self.mgmt_transport = None
        self.mode = None
        self.oper_power_requirement = None
        self.reboot_action_on_destructive = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorNwMgmtCap", parent_mo_or_dn, **kwargs)
