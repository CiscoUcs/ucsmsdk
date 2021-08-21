"""This module contains the general information for FirmwareSecureFPGA ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FirmwareSecureFPGAConsts:
    FPGAIMAGE_STATUS_ACTIVATION_FAILED = "Activation Failed"
    FPGAIMAGE_STATUS_ACTIVATION_IN_PROGRESS = "Activation In Progress"
    FPGAIMAGE_STATUS_READY = "Ready"
    SECURED_FALSE = "false"
    SECURED_NO = "no"
    SECURED_TRUE = "true"
    SECURED_YES = "yes"


class FirmwareSecureFPGA(ManagedObject):
    """This is FirmwareSecureFPGA class."""

    consts = FirmwareSecureFPGAConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareSecureFPGA", "firmwareSecureFPGA", "fw-secure-fpga", VersionMeta.Version413a, "InputOutput", 0x7f, [], ["admin"], ['networkElement'], ['faultInst'], [None])

    prop_meta = {
        "fpga_image_status": MoPropertyMeta("fpga_image_status", "FPGAImageStatus", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Activation Failed", "Activation In Progress", "Ready"], []),
        "secured": MoPropertyMeta("secured", "Secured", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["false", "no", "true", "yes"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, 0x8, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version413a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "FPGAImageStatus": "fpga_image_status", 
        "Secured": "secured", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.fpga_image_status = None
        self.secured = None
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareSecureFPGA", parent_mo_or_dn, **kwargs)
