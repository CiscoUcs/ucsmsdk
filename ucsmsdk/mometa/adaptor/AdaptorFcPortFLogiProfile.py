"""This module contains the general information for AdaptorFcPortFLogiProfile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorFcPortFLogiProfileConsts:
    RETRIES_INFINITE = "infinite"


class AdaptorFcPortFLogiProfile(ManagedObject):
    """This is AdaptorFcPortFLogiProfile class."""

    consts = AdaptorFcPortFLogiProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorFcPortFLogiProfile", "adaptorFcPortFLogiProfile", "fc-port-flogi", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["admin", "ls-config-policy", "ls-server-policy", "ls-storage"], ['adaptorHostFcIf', 'adaptorHostFcIfProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "retries": MoPropertyMeta("retries", "retries", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["infinite"], ["0-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1000-255000"]),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "retries": "retries", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "timeout": "timeout", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.retries = None
        self.sacl = None
        self.status = None
        self.timeout = None

        ManagedObject.__init__(self, "AdaptorFcPortFLogiProfile", parent_mo_or_dn, **kwargs)
