"""This module contains the general information for BiosVfDramRefreshRate ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfDramRefreshRateConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_DRAM_REFRESH_RATE_1X = "1x"
    VP_DRAM_REFRESH_RATE_2X = "2x"
    VP_DRAM_REFRESH_RATE_3X = "3x"
    VP_DRAM_REFRESH_RATE_4X = "4x"
    VP_DRAM_REFRESH_RATE_AUTO = "auto"
    VP_DRAM_REFRESH_RATE_PLATFORM_DEFAULT = "platform-default"
    VP_DRAM_REFRESH_RATE_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfDramRefreshRate(ManagedObject):
    """This is BiosVfDramRefreshRate class."""

    consts = BiosVfDramRefreshRateConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfDramRefreshRate", "biosVfDramRefreshRate", "Dram-Refresh-Rate", VersionMeta.Version205a, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosSettings', 'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version205a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version205a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version205a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version205a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "vp_dram_refresh_rate": MoPropertyMeta("vp_dram_refresh_rate", "vpDramRefreshRate", "string", VersionMeta.Version205a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["1x", "2x", "3x", "4x", "auto", "platform-default", "platform-recommended"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpDramRefreshRate": "vp_dram_refresh_rate", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_dram_refresh_rate = None

        ManagedObject.__init__(self, "BiosVfDramRefreshRate", parent_mo_or_dn, **kwargs)
