"""This module contains the general information for BiosVfCoreMultiProcessing ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class BiosVfCoreMultiProcessingConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_CORE_MULTI_PROCESSING_1 = "1"
    VP_CORE_MULTI_PROCESSING_10 = "10"
    VP_CORE_MULTI_PROCESSING_11 = "11"
    VP_CORE_MULTI_PROCESSING_12 = "12"
    VP_CORE_MULTI_PROCESSING_13 = "13"
    VP_CORE_MULTI_PROCESSING_14 = "14"
    VP_CORE_MULTI_PROCESSING_15 = "15"
    VP_CORE_MULTI_PROCESSING_16 = "16"
    VP_CORE_MULTI_PROCESSING_17 = "17"
    VP_CORE_MULTI_PROCESSING_18 = "18"
    VP_CORE_MULTI_PROCESSING_2 = "2"
    VP_CORE_MULTI_PROCESSING_3 = "3"
    VP_CORE_MULTI_PROCESSING_4 = "4"
    VP_CORE_MULTI_PROCESSING_5 = "5"
    VP_CORE_MULTI_PROCESSING_6 = "6"
    VP_CORE_MULTI_PROCESSING_7 = "7"
    VP_CORE_MULTI_PROCESSING_8 = "8"
    VP_CORE_MULTI_PROCESSING_9 = "9"
    VP_CORE_MULTI_PROCESSING_ALL = "all"
    VP_CORE_MULTI_PROCESSING_PLATFORM_DEFAULT = "platform-default"
    VP_CORE_MULTI_PROCESSING_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfCoreMultiProcessing(ManagedObject):
    """This is BiosVfCoreMultiProcessing class."""

    consts = BiosVfCoreMultiProcessingConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfCoreMultiProcessing", "biosVfCoreMultiProcessing", "Core-MultiProcessing", VersionMeta.Version111j, "InputOutput", 0x3fL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosSettings', u'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_core_multi_processing": MoPropertyMeta("vp_core_multi_processing", "vpCoreMultiProcessing", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["1", "10", "11", "12", "13", "14", "15", "16", "17", "18", "2", "3", "4", "5", "6", "7", "8", "9", "all", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpCoreMultiProcessing": "vp_core_multi_processing", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_core_multi_processing = None

        ManagedObject.__init__(self, "BiosVfCoreMultiProcessing", parent_mo_or_dn, **kwargs)

