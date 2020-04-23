"""This module contains the general information for AdaptorFcVhbaTypeProfile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorFcVhbaTypeProfileConsts:
    MODE_FC_INITIATOR = "fc-initiator"
    MODE_FC_NVME_INITIATOR = "fc-nvme-initiator"
    MODE_FC_NVME_TARGET = "fc-nvme-target"
    MODE_FC_TARGET = "fc-target"


class AdaptorFcVhbaTypeProfile(ManagedObject):
    """This is AdaptorFcVhbaTypeProfile class."""

    consts = AdaptorFcVhbaTypeProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorFcVhbaTypeProfile", "adaptorFcVhbaTypeProfile", "fc-vhbatype", VersionMeta.Version402a, "InputOutput", 0x3f, [], ["admin", "ls-config-policy", "ls-server-policy", "ls-storage"], ['adaptorHostFcIf', 'adaptorHostFcIfProfile'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version402a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["fc-initiator", "fc-nvme-initiator", "fc-nvme-target", "fc-target"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "mode": "mode", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.mode = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorFcVhbaTypeProfile", parent_mo_or_dn, **kwargs)
