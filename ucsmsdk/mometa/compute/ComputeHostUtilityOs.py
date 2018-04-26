"""This module contains the general information for ComputeHostUtilityOs ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeHostUtilityOsConsts:
    COMMUNICATION_TYPE_SERIAL_COM = "serial-com"
    COMMUNICATION_TYPE_USB_NIC = "usb-nic"


class ComputeHostUtilityOs(ManagedObject):
    """This is ComputeHostUtilityOs class."""

    consts = ComputeHostUtilityOsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeHostUtilityOs", "computeHostUtilityOs", "host-util-os-", None, "InputOutput", 0x1f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], [u'computeBlade', u'computeRackUnit', u'computeServerUnit'], [u'mgmtUsbNicMgmtIf'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "communication_type": MoPropertyMeta("communication_type", "communicationType", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["serial-com", "usb-nic"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "util_os_name": MoPropertyMeta("util_os_name", "utilOSName", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "communicationType": "communication_type", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "utilOSName": "util_os_name", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.communication_type = None
        self.sacl = None
        self.status = None
        self.util_os_name = None

        ManagedObject.__init__(self, "ComputeHostUtilityOs", parent_mo_or_dn, **kwargs)
