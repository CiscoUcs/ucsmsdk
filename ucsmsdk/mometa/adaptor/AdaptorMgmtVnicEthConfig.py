"""This module contains the general information for AdaptorMgmtVnicEthConfig ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class AdaptorMgmtVnicEthConfigConsts():
    pass


class AdaptorMgmtVnicEthConfig(ManagedObject):
    """This is AdaptorMgmtVnicEthConfig class."""

    consts = AdaptorMgmtVnicEthConfigConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorMgmtVnicEthConfig", "adaptorMgmtVnicEthConfig", "mgmt-vnic", VersionMeta.Version224a, "InputOutput", 0x7fL, [], ["read-only"], [u'adaptorFruCapProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "host_port_id": MoPropertyMeta("host_port_id", "hostPortId", "byte", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], []), 
        "mac_offset": MoPropertyMeta("mac_offset", "macOffset", "byte", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], []), 
        "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "byte", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "hostPortId": "host_port_id", 
        "macOffset": "mac_offset", 
        "pciSlot": "pci_slot", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.host_port_id = None
        self.mac_offset = None
        self.pci_slot = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorMgmtVnicEthConfig", parent_mo_or_dn, **kwargs)

