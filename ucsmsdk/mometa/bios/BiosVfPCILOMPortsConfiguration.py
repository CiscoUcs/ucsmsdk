"""This module contains the general information for BiosVfPCILOMPortsConfiguration ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class BiosVfPCILOMPortsConfigurationConsts():
    VP_PCIE10_GLOM2_LINK_DISABLED = "disabled"
    VP_PCIE10_GLOM2_LINK_ENABLED = "enabled"
    VP_PCIE10_GLOM2_LINK_PLATFORM_DEFAULT = "platform-default"
    VP_PCIE10_GLOM2_LINK_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfPCILOMPortsConfiguration(ManagedObject):
    """This is BiosVfPCILOMPortsConfiguration class."""

    consts = BiosVfPCILOMPortsConfigurationConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfPCILOMPortsConfiguration", "biosVfPCILOMPortsConfiguration", "PCI-LOM-Ports-Configuration", VersionMeta.Version224a, "InputOutput", 0x1fL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosSettings', u'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vp_pc_ie10_glo_m2_link": MoPropertyMeta("vp_pc_ie10_glo_m2_link", "vpPCIe10GLOM2Link", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "vpPCIe10GLOM2Link": "vp_pc_ie10_glo_m2_link", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_pc_ie10_glo_m2_link = None

        ManagedObject.__init__(self, "BiosVfPCILOMPortsConfiguration", parent_mo_or_dn, **kwargs)

