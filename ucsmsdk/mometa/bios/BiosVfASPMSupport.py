"""This module contains the general information for BiosVfASPMSupport ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class BiosVfASPMSupportConsts():
    VP_ASPMSUPPORT_AUTO = "auto"
    VP_ASPMSUPPORT_DISABLED = "disabled"
    VP_ASPMSUPPORT_FORCEL0 = "forcel0"
    VP_ASPMSUPPORT_PLATFORM_DEFAULT = "platform-default"
    VP_ASPMSUPPORT_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfASPMSupport(ManagedObject):
    """This is BiosVfASPMSupport class."""

    consts = BiosVfASPMSupportConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfASPMSupport", "biosVfASPMSupport", "ASPM-Support", VersionMeta.Version251a, "InputOutput", 0x1fL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosSettings', u'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vp_aspm_support": MoPropertyMeta("vp_aspm_support", "vpASPMSupport", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["auto", "disabled", "forcel0", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "vpASPMSupport": "vp_aspm_support", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_aspm_support = None

        ManagedObject.__init__(self, "BiosVfASPMSupport", parent_mo_or_dn, **kwargs)

