"""This module contains the general information for AdaptorEthFailoverProfile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorEthFailoverProfileConsts:
    pass


class AdaptorEthFailoverProfile(ManagedObject):
    """This is AdaptorEthFailoverProfile class."""

    consts = AdaptorEthFailoverProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorEthFailoverProfile", "adaptorEthFailoverProfile", "eth-failover", VersionMeta.Version101e, "InputOutput", 0x3f, [], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"], ['adaptorHostEthIf', 'adaptorHostEthIfProfile', 'adaptorUsnicConnDef'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-600"]),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "timeout": "timeout", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.sacl = None
        self.status = None
        self.timeout = None

        ManagedObject.__init__(self, "AdaptorEthFailoverProfile", parent_mo_or_dn, **kwargs)
