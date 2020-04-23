"""This module contains the general information for AdaptorMgmtVnicEthConfig ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorMgmtVnicEthConfigConsts:
    pass


class AdaptorMgmtVnicEthConfig(ManagedObject):
    """This is AdaptorMgmtVnicEthConfig class."""

    consts = AdaptorMgmtVnicEthConfigConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorMgmtVnicEthConfig", "adaptorMgmtVnicEthConfig", "mgmt-vnic", VersionMeta.Version224b, "InputOutput", 0xff, [], ["read-only"], ['adaptorFruCapProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "host_port_id": MoPropertyMeta("host_port_id", "hostPortId", "byte", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-255"]),
        "mac_offset": MoPropertyMeta("mac_offset", "macOffset", "byte", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-255"]),
        "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "byte", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-255"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "hostPortId": "host_port_id", 
        "macOffset": "mac_offset", 
        "pciSlot": "pci_slot", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.host_port_id = None
        self.mac_offset = None
        self.pci_slot = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorMgmtVnicEthConfig", parent_mo_or_dn, **kwargs)
