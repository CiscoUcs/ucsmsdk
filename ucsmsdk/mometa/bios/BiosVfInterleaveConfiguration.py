"""This module contains the general information for BiosVfInterleaveConfiguration ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfInterleaveConfigurationConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_CHANNEL_INTERLEAVING_1_WAY = "1-way"
    VP_CHANNEL_INTERLEAVING_2_WAY = "2-way"
    VP_CHANNEL_INTERLEAVING_3_WAY = "3-way"
    VP_CHANNEL_INTERLEAVING_4_WAY = "4-way"
    VP_CHANNEL_INTERLEAVING_AUTO = "auto"
    VP_CHANNEL_INTERLEAVING_PLATFORM_DEFAULT = "platform-default"
    VP_CHANNEL_INTERLEAVING_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_MEMORY_INTERLEAVING_2_WAY_NODE_INTERLEAVE = "2-way-node-interleave"
    VP_MEMORY_INTERLEAVING_4_WAY_NODE_INTERLEAVE = "4-way-node-interleave"
    VP_MEMORY_INTERLEAVING_8_WAY_INTERLEAVING_INTER_SOCKET = "8-way-interleaving-inter-socket"
    VP_MEMORY_INTERLEAVING_NUMA_1_WAY_NODE_INTERLEAVE = "numa---1-way-node-interleave"
    VP_MEMORY_INTERLEAVING_PLATFORM_DEFAULT = "platform-default"
    VP_MEMORY_INTERLEAVING_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_RANK_INTERLEAVING_1_WAY = "1-way"
    VP_RANK_INTERLEAVING_2_WAY = "2-way"
    VP_RANK_INTERLEAVING_4_WAY = "4-way"
    VP_RANK_INTERLEAVING_8_WAY = "8-way"
    VP_RANK_INTERLEAVING_AUTO = "auto"
    VP_RANK_INTERLEAVING_PLATFORM_DEFAULT = "platform-default"
    VP_RANK_INTERLEAVING_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfInterleaveConfiguration(ManagedObject):
    """This is BiosVfInterleaveConfiguration class."""

    consts = BiosVfInterleaveConfigurationConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfInterleaveConfiguration", "biosVfInterleaveConfiguration", "Interleave-Configuration", VersionMeta.Version222c, "InputOutput", 0xff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosSettings', 'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version222c, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version222c, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "vp_channel_interleaving": MoPropertyMeta("vp_channel_interleaving", "vpChannelInterleaving", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["1-way", "2-way", "3-way", "4-way", "auto", "platform-default", "platform-recommended"], []),
        "vp_memory_interleaving": MoPropertyMeta("vp_memory_interleaving", "vpMemoryInterleaving", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["2-way-node-interleave", "4-way-node-interleave", "8-way-interleaving-inter-socket", "numa---1-way-node-interleave", "platform-default", "platform-recommended"], []),
        "vp_rank_interleaving": MoPropertyMeta("vp_rank_interleaving", "vpRankInterleaving", "string", VersionMeta.Version222c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["1-way", "2-way", "4-way", "8-way", "auto", "platform-default", "platform-recommended"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpChannelInterleaving": "vp_channel_interleaving", 
        "vpMemoryInterleaving": "vp_memory_interleaving", 
        "vpRankInterleaving": "vp_rank_interleaving", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_channel_interleaving = None
        self.vp_memory_interleaving = None
        self.vp_rank_interleaving = None

        ManagedObject.__init__(self, "BiosVfInterleaveConfiguration", parent_mo_or_dn, **kwargs)
