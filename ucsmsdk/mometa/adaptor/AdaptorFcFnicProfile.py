"""This module contains the general information for AdaptorFcFnicProfile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorFcFnicProfileConsts:
    pass


class AdaptorFcFnicProfile(ManagedObject):
    """This is AdaptorFcFnicProfile class."""

    consts = AdaptorFcFnicProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorFcFnicProfile", "adaptorFcFnicProfile", "fc-fnic", VersionMeta.Version312b, "InputOutput", 0x7f, [], ["admin", "ls-config-policy", "ls-server-policy", "ls-storage"], ['adaptorHostFcIf', 'adaptorHostFcIfProfile'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "io_retry_timeout": MoPropertyMeta("io_retry_timeout", "ioRetryTimeout", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-59"]),
        "lun_queue_depth": MoPropertyMeta("lun_queue_depth", "lunQueueDepth", "uint", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-254"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ioRetryTimeout": "io_retry_timeout", 
        "lunQueueDepth": "lun_queue_depth", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.io_retry_timeout = None
        self.lun_queue_depth = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorFcFnicProfile", parent_mo_or_dn, **kwargs)
