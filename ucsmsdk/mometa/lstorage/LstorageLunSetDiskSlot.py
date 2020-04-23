"""This module contains the general information for LstorageLunSetDiskSlot ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LstorageLunSetDiskSlotConsts:
    pass


class LstorageLunSetDiskSlot(ManagedObject):
    """This is LstorageLunSetDiskSlot class."""

    consts = LstorageLunSetDiskSlotConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("LstorageLunSetDiskSlot", "lstorageLunSetDiskSlot", "lun-set-disk-slot-[id]", VersionMeta.Version402a, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage", "ls-storage-policy"], ['lstorageLunSetConfig'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version402a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version402a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-60"]),
        "lun_name": MoPropertyMeta("lun_name", "lunName", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, None, 1, 32, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "size": MoPropertyMeta("size", "size", "ulong", VersionMeta.Version402a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version402a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "lunName": "lun_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "size": "size", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.lun_name = None
        self.sacl = None
        self.size = None
        self.status = None

        ManagedObject.__init__(self, "LstorageLunSetDiskSlot", parent_mo_or_dn, **kwargs)
