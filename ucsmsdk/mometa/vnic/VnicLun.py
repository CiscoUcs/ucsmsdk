"""This module contains the general information for VnicLun ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicLunConsts:
    BOOTABLE_FALSE = "false"
    BOOTABLE_NO = "no"
    BOOTABLE_TRUE = "true"
    BOOTABLE_YES = "yes"


class VnicLun(ManagedObject):
    """This is VnicLun class."""

    consts = VnicLunConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicLun", "vnicLun", "lun", VersionMeta.Version201m, "InputOutput", 0x7f, [], ["admin", "ls-config", "ls-server", "ls-storage"], ['vnicIScsiStaticTargetIf'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "bootable": MoPropertyMeta("bootable", "bootable", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["false", "no", "true", "yes"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ushort", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-65535"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "bootable": "bootable", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.bootable = None
        self.child_action = None
        self.id = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "VnicLun", parent_mo_or_dn, **kwargs)
