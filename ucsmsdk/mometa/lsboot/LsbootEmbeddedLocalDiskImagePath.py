"""This module contains the general information for LsbootEmbeddedLocalDiskImagePath ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class LsbootEmbeddedLocalDiskImagePathConsts:
    TYPE_PRIMARY = "primary"
    TYPE_SECONDARY = "secondary"


class LsbootEmbeddedLocalDiskImagePath(ManagedObject):
    """This is LsbootEmbeddedLocalDiskImagePath class."""

    consts = LsbootEmbeddedLocalDiskImagePathConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("LsbootEmbeddedLocalDiskImagePath", "lsbootEmbeddedLocalDiskImagePath", "diskimgpath-[type]", VersionMeta.Version227b, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], ['lsbootEmbeddedLocalDiskImage'], ['lsbootUEFIBootParam'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version227b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version227b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "slot_number": MoPropertyMeta("slot_number", "slotNumber", "ushort", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-254"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version227b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version227b, MoPropertyMeta.NAMING, 0x40, None, None, None, ["primary", "secondary"], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotNumber": "slot_number", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.sacl = None
        self.slot_number = None
        self.status = None

        ManagedObject.__init__(self, "LsbootEmbeddedLocalDiskImagePath", parent_mo_or_dn, **kwargs)
