"""This module contains the general information for BiosVfProcessorC7Report ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfProcessorC7ReportConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_PROCESSOR_C7_REPORT_C7 = "c7"
    VP_PROCESSOR_C7_REPORT_C7S = "c7s"
    VP_PROCESSOR_C7_REPORT_DISABLED = "disabled"
    VP_PROCESSOR_C7_REPORT_ENABLED = "enabled"
    VP_PROCESSOR_C7_REPORT_PLATFORM_DEFAULT = "platform-default"
    VP_PROCESSOR_C7_REPORT_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfProcessorC7Report(ManagedObject):
    """This is BiosVfProcessorC7Report class."""

    consts = BiosVfProcessorC7ReportConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfProcessorC7Report", "biosVfProcessorC7Report", "Processor-C7-Report", VersionMeta.Version202m, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosSettings', 'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202m, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "vp_processor_c7_report": MoPropertyMeta("vp_processor_c7_report", "vpProcessorC7Report", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["c7", "c7s", "disabled", "enabled", "platform-default", "platform-recommended"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpProcessorC7Report": "vp_processor_c7_report", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_processor_c7_report = None

        ManagedObject.__init__(self, "BiosVfProcessorC7Report", parent_mo_or_dn, **kwargs)
