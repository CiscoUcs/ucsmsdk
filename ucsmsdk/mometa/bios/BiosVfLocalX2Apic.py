"""This module contains the general information for BiosVfLocalX2Apic ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfLocalX2ApicConsts:
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_LOCAL_X2_APIC_AUTO = "auto"
    VP_LOCAL_X2_APIC_PLATFORM_DEFAULT = "platform-default"
    VP_LOCAL_X2_APIC_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_LOCAL_X2_APIC_X2APIC = "x2apic"
    VP_LOCAL_X2_APIC_XAPIC = "xapic"


class BiosVfLocalX2Apic(ManagedObject):
    """This is BiosVfLocalX2Apic class."""

    consts = BiosVfLocalX2ApicConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfLocalX2Apic", "biosVfLocalX2Apic", "Local-X2-Apic", VersionMeta.Version213a, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosSettings', 'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version213a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version213a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "vp_local_x2_apic": MoPropertyMeta("vp_local_x2_apic", "vpLocalX2Apic", "string", VersionMeta.Version213a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["auto", "platform-default", "platform-recommended", "x2apic", "xapic"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpLocalX2Apic": "vp_local_x2_apic", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_local_x2_apic = None

        ManagedObject.__init__(self, "BiosVfLocalX2Apic", parent_mo_or_dn, **kwargs)
