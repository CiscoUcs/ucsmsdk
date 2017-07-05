"""This module contains the general information for EquipmentHostMgmtControllerCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentHostMgmtControllerCapConsts:
    COMM_METHOD_SERIAL = "serial"
    COMM_METHOD_UNKNOWN = "unknown"
    COMM_METHOD_USB_NIC = "usb-nic"


class EquipmentHostMgmtControllerCap(ManagedObject):
    """This is EquipmentHostMgmtControllerCap class."""

    consts = EquipmentHostMgmtControllerCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentHostMgmtControllerCap", "equipmentHostMgmtControllerCap", "host-mgmt-controller-cap", None, "InputOutput", 0x1f, [], ["read-only"], [u'equipmentBladeCapProvider', u'equipmentRackUnitCapProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "comm_method": MoPropertyMeta("comm_method", "commMethod", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["serial", "unknown", "usb-nic"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "commMethod": "comm_method", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.comm_method = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentHostMgmtControllerCap", parent_mo_or_dn, **kwargs)
