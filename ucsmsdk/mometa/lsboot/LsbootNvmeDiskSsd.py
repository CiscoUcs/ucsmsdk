"""This module contains the general information for LsbootNvmeDiskSsd ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LsbootNvmeDiskSsdConsts:
    TYPE_DISK_SSD = "disk-ssd"
    TYPE_PCI_SSD = "pci-ssd"


class LsbootNvmeDiskSsd(ManagedObject):
    """This is LsbootNvmeDiskSsd class."""

    consts = LsbootNvmeDiskSsdConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsbootNvmeDiskSsd", "lsbootNvmeDiskSsd", "nvme-disk-ssd", VersionMeta.Version321d, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], ['lsbootNvme'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-16"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_id": MoPropertyMeta("slot_id", "slotId", "ushort", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disk-ssd", "pci-ssd"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "order": "order", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotId": "slot_id", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.order = None
        self.sacl = None
        self.slot_id = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LsbootNvmeDiskSsd", parent_mo_or_dn, **kwargs)
