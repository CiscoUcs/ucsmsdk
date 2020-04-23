"""This module contains the general information for BiosVfProcessorPrefetchConfig ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfProcessorPrefetchConfigConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_ADJACENT_CACHE_LINE_PREFETCHER_DISABLED = "disabled"
    VP_ADJACENT_CACHE_LINE_PREFETCHER_ENABLED = "enabled"
    VP_ADJACENT_CACHE_LINE_PREFETCHER_PLATFORM_DEFAULT = "platform-default"
    VP_ADJACENT_CACHE_LINE_PREFETCHER_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_DCUIPPREFETCHER_DISABLED = "disabled"
    VP_DCUIPPREFETCHER_ENABLED = "enabled"
    VP_DCUIPPREFETCHER_PLATFORM_DEFAULT = "platform-default"
    VP_DCUIPPREFETCHER_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_DCUSTREAMER_PREFETCH_DISABLED = "disabled"
    VP_DCUSTREAMER_PREFETCH_ENABLED = "enabled"
    VP_DCUSTREAMER_PREFETCH_PLATFORM_DEFAULT = "platform-default"
    VP_DCUSTREAMER_PREFETCH_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_HARDWARE_PREFETCHER_DISABLED = "disabled"
    VP_HARDWARE_PREFETCHER_ENABLED = "enabled"
    VP_HARDWARE_PREFETCHER_PLATFORM_DEFAULT = "platform-default"
    VP_HARDWARE_PREFETCHER_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfProcessorPrefetchConfig(ManagedObject):
    """This is BiosVfProcessorPrefetchConfig class."""

    consts = BiosVfProcessorPrefetchConfigConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfProcessorPrefetchConfig", "biosVfProcessorPrefetchConfig", "Processor-Prefetch-Config", VersionMeta.Version222c, "InputOutput", 0x1ff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosSettings', 'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "vp_adjacent_cache_line_prefetcher": MoPropertyMeta("vp_adjacent_cache_line_prefetcher", "vpAdjacentCacheLinePrefetcher", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []),
        "vp_dcuip_prefetcher": MoPropertyMeta("vp_dcuip_prefetcher", "vpDCUIPPrefetcher", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []),
        "vp_dcu_streamer_prefetch": MoPropertyMeta("vp_dcu_streamer_prefetch", "vpDCUStreamerPrefetch", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []),
        "vp_hardware_prefetcher": MoPropertyMeta("vp_hardware_prefetcher", "vpHardwarePrefetcher", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpAdjacentCacheLinePrefetcher": "vp_adjacent_cache_line_prefetcher", 
        "vpDCUIPPrefetcher": "vp_dcuip_prefetcher", 
        "vpDCUStreamerPrefetch": "vp_dcu_streamer_prefetch", 
        "vpHardwarePrefetcher": "vp_hardware_prefetcher", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_adjacent_cache_line_prefetcher = None
        self.vp_dcuip_prefetcher = None
        self.vp_dcu_streamer_prefetch = None
        self.vp_hardware_prefetcher = None

        ManagedObject.__init__(self, "BiosVfProcessorPrefetchConfig", parent_mo_or_dn, **kwargs)
