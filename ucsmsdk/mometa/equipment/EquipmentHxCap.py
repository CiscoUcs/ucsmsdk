"""This module contains the general information for EquipmentHxCap ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentHxCapConsts:
    IS_SED_SUPPORTED_NO = "no"
    IS_SED_SUPPORTED_YES = "yes"
    IS_USB_NIC_SUPPORTED_NO = "no"
    IS_USB_NIC_SUPPORTED_YES = "yes"


class EquipmentHxCap(ManagedObject):
    """This is EquipmentHxCap class."""

    consts = EquipmentHxCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentHxCap", "equipmentHxCap", "hx-cap", VersionMeta.Version321d, "InputOutput", 0x1f, [], ["read-only"], ['equipmentRackUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "is_sed_supported": MoPropertyMeta("is_sed_supported", "isSedSupported", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "is_usb_nic_supported": MoPropertyMeta("is_usb_nic_supported", "isUsbNicSupported", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "isSedSupported": "is_sed_supported", 
        "isUsbNicSupported": "is_usb_nic_supported", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.is_sed_supported = None
        self.is_usb_nic_supported = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentHxCap", parent_mo_or_dn, **kwargs)
