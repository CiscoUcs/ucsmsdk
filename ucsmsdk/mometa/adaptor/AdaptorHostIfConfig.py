"""This module contains the general information for AdaptorHostIfConfig ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorHostIfConfigConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_DISABLED_ACTIVE = "disabled-active"
    ADMIN_STATE_DISABLED_PASSIVE = "disabled-passive"
    ADMIN_STATE_ENABLED = "enabled"
    ADMIN_STATE_ENABLED_ACTIVE = "enabled-active"
    ADMIN_STATE_ENABLED_PASSIVE = "enabled-passive"
    ADMIN_STATE_RESET_CONNECTIVITY = "reset-connectivity"
    ADMIN_STATE_RESET_CONNECTIVITY_ACTIVE = "reset-connectivity-active"
    ADMIN_STATE_RESET_CONNECTIVITY_PASSIVE = "reset-connectivity-passive"


class AdaptorHostIfConfig(ManagedObject):
    """This is AdaptorHostIfConfig class."""

    consts = AdaptorHostIfConfigConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorHostIfConfig", "adaptorHostIfConfig", "host-if-config-[id]", VersionMeta.Version227b, "InputOutput", 0x3f, [], ["read-only"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], [], ["Get"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "disabled-active", "disabled-passive", "enabled", "enabled-active", "enabled-passive", "reset-connectivity", "reset-connectivity-active", "reset-connectivity-passive"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version227b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version227b, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "transport": "transport", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_state = None
        self.child_action = None
        self.name = None
        self.sacl = None
        self.status = None
        self.transport = None

        ManagedObject.__init__(self, "AdaptorHostIfConfig", parent_mo_or_dn, **kwargs)
