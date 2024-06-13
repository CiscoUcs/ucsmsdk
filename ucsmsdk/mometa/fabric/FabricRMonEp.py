"""This module contains the general information for FabricRMonEp ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricRMonEpConsts:
    IS_CONFIG_SUCCESS_FALSE = "false"
    IS_CONFIG_SUCCESS_NO = "no"
    IS_CONFIG_SUCCESS_TRUE = "true"
    IS_CONFIG_SUCCESS_YES = "yes"


class FabricRMonEp(ManagedObject):
    """This is FabricRMonEp class."""

    consts = FabricRMonEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("FabricRMonEp", "fabricRMonEp", "remote-traffic-mon", VersionMeta.Version434a, "InputOutput", 0x3f, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricEp'], ['fabricMonOriginSVI'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_fail_reason": MoPropertyMeta("config_fail_reason", "configFailReason", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "is_config_success": MoPropertyMeta("is_config_success", "isConfigSuccess", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "configFailReason": "config_fail_reason", 
        "dn": "dn", 
        "isConfigSuccess": "is_config_success", 
        "name": "name", 
        "peerDn": "peer_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.config_fail_reason = None
        self.is_config_success = None
        self.name = None
        self.peer_dn = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FabricRMonEp", parent_mo_or_dn, **kwargs)
