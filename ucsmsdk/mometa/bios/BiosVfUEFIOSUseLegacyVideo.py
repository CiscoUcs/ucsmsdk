"""This module contains the general information for BiosVfUEFIOSUseLegacyVideo ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfUEFIOSUseLegacyVideoConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_UEFIOSUSE_LEGACY_VIDEO_DISABLED = "disabled"
    VP_UEFIOSUSE_LEGACY_VIDEO_ENABLED = "enabled"
    VP_UEFIOSUSE_LEGACY_VIDEO_PLATFORM_DEFAULT = "platform-default"
    VP_UEFIOSUSE_LEGACY_VIDEO_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfUEFIOSUseLegacyVideo(ManagedObject):
    """This is BiosVfUEFIOSUseLegacyVideo class."""

    consts = BiosVfUEFIOSUseLegacyVideoConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfUEFIOSUseLegacyVideo", "biosVfUEFIOSUseLegacyVideo", "UEFI-OS-use-legacy-video", VersionMeta.Version141i, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosSettings', 'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "vp_uefios_use_legacy_video": MoPropertyMeta("vp_uefios_use_legacy_video", "vpUEFIOSUseLegacyVideo", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpUEFIOSUseLegacyVideo": "vp_uefios_use_legacy_video", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_uefios_use_legacy_video = None

        ManagedObject.__init__(self, "BiosVfUEFIOSUseLegacyVideo", parent_mo_or_dn, **kwargs)
