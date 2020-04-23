"""This module contains the general information for BiosVfIOENVMe2OptionROM ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfIOENVMe2OptionROMConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_IOENVME2_OPTION_ROM_DISABLED = "disabled"
    VP_IOENVME2_OPTION_ROM_ENABLED = "enabled"
    VP_IOENVME2_OPTION_ROM_LEGACY_ONLY = "legacy-only"
    VP_IOENVME2_OPTION_ROM_PLATFORM_DEFAULT = "platform-default"
    VP_IOENVME2_OPTION_ROM_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_IOENVME2_OPTION_ROM_UEFI_ONLY = "uefi-only"


class BiosVfIOENVMe2OptionROM(ManagedObject):
    """This is BiosVfIOENVMe2OptionROM class."""

    consts = BiosVfIOENVMe2OptionROMConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfIOENVMe2OptionROM", "biosVfIOENVMe2OptionROM", "IOENVMe2-OptionROM", VersionMeta.Version312b, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosSettings', 'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version312b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version312b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "vp_ioenv_me2_option_rom": MoPropertyMeta("vp_ioenv_me2_option_rom", "vpIOENVMe2OptionROM", "string", VersionMeta.Version312b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpIOENVMe2OptionROM": "vp_ioenv_me2_option_rom", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_ioenv_me2_option_rom = None

        ManagedObject.__init__(self, "BiosVfIOENVMe2OptionROM", parent_mo_or_dn, **kwargs)
