"""This module contains the general information for BiosVfIntelEntrySASRAIDModule ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfIntelEntrySASRAIDModuleConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_SASRAID_DISABLED = "disabled"
    VP_SASRAID_ENABLED = "enabled"
    VP_SASRAID_PLATFORM_DEFAULT = "platform-default"
    VP_SASRAID_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_SASRAIDMODULE_INTEL_ESRTII = "intel-esrtii"
    VP_SASRAIDMODULE_IT_IR_RAID = "it-ir-raid"
    VP_SASRAIDMODULE_PLATFORM_DEFAULT = "platform-default"
    VP_SASRAIDMODULE_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfIntelEntrySASRAIDModule(ManagedObject):
    """This is BiosVfIntelEntrySASRAIDModule class."""

    consts = BiosVfIntelEntrySASRAIDModuleConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfIntelEntrySASRAIDModule", "biosVfIntelEntrySASRAIDModule", "Intel-entry-SAS-RAID-module", VersionMeta.Version111j, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosSettings', 'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "vp_sasraid": MoPropertyMeta("vp_sasraid", "vpSASRAID", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []),
        "vp_sasraid_module": MoPropertyMeta("vp_sasraid_module", "vpSASRAIDModule", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["intel-esrtii", "it-ir-raid", "platform-default", "platform-recommended"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpSASRAID": "vp_sasraid", 
        "vpSASRAIDModule": "vp_sasraid_module", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_sasraid = None
        self.vp_sasraid_module = None

        ManagedObject.__init__(self, "BiosVfIntelEntrySASRAIDModule", parent_mo_or_dn, **kwargs)
