"""This module contains the general information for LsbootNvme ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LsbootNvmeConsts:
    TYPE_EMBEDDED_LOCAL_JBOD = "embedded-local-jbod"
    TYPE_EMBEDDED_LOCAL_LUN = "embedded-local-lun"
    TYPE_LOCAL_ANY = "local-any"
    TYPE_LOCAL_JBOD = "local-jbod"
    TYPE_LOCAL_LUN = "local-lun"
    TYPE_NVME = "nvme"
    TYPE_SD_CARD = "sd-card"
    TYPE_USB_EXTERN = "usb-extern"
    TYPE_USB_INTERN = "usb-intern"


class LsbootNvme(ManagedObject):
    """This is LsbootNvme class."""

    consts = LsbootNvmeConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsbootNvme", "lsbootNvme", "nvme", VersionMeta.Version321d, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], ['lsbootLocalStorage'], ['lsbootNvmeDiskSsd', 'lsbootNvmePciSsd', 'lsbootUEFIBootParam'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-16"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["embedded-local-jbod", "embedded-local-lun", "local-any", "local-jbod", "local-lun", "nvme", "sd-card", "usb-extern", "usb-intern"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "order": "order", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.order = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LsbootNvme", parent_mo_or_dn, **kwargs)
