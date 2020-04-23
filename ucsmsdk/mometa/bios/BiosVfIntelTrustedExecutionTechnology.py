"""This module contains the general information for BiosVfIntelTrustedExecutionTechnology ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfIntelTrustedExecutionTechnologyConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_INTEL_TRUSTED_EXECUTION_TECHNOLOGY_SUPPORT_DISABLED = "disabled"
    VP_INTEL_TRUSTED_EXECUTION_TECHNOLOGY_SUPPORT_ENABLED = "enabled"
    VP_INTEL_TRUSTED_EXECUTION_TECHNOLOGY_SUPPORT_PLATFORM_DEFAULT = "platform-default"
    VP_INTEL_TRUSTED_EXECUTION_TECHNOLOGY_SUPPORT_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfIntelTrustedExecutionTechnology(ManagedObject):
    """This is BiosVfIntelTrustedExecutionTechnology class."""

    consts = BiosVfIntelTrustedExecutionTechnologyConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfIntelTrustedExecutionTechnology", "biosVfIntelTrustedExecutionTechnology", "Intel-Trusted-Execution-Technology", VersionMeta.Version224b, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosSettings', 'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "vp_intel_trusted_execution_technology_support": MoPropertyMeta("vp_intel_trusted_execution_technology_support", "vpIntelTrustedExecutionTechnologySupport", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpIntelTrustedExecutionTechnologySupport": "vp_intel_trusted_execution_technology_support", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_intel_trusted_execution_technology_support = None

        ManagedObject.__init__(self, "BiosVfIntelTrustedExecutionTechnology", parent_mo_or_dn, **kwargs)
