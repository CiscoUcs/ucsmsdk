"""This module contains the general information for FcpoolBootTarget ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FcpoolBootTargetConsts:
    LUN_UNSPECIFIED = "unspecified"
    TYPE_PRIMARY = "primary"
    TYPE_SECONDARY = "secondary"


class FcpoolBootTarget(ManagedObject):
    """This is FcpoolBootTarget class."""

    consts = FcpoolBootTargetConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("FcpoolBootTarget", "fcpoolBootTarget", "target-[type]", VersionMeta.Version101e, "InputOutput", 0xff, [], ["admin", "ls-storage-policy"], ['fcpoolBlock', 'fcpoolInitiator'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "lun": MoPropertyMeta("lun", "lun", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["unspecified"], ["0-4294967295"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40, None, None, None, ["primary", "secondary"], []),
        "wwn": MoPropertyMeta("wwn", "wwn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "lun": "lun", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
        "wwn": "wwn", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.lun = None
        self.sacl = None
        self.status = None
        self.wwn = None

        ManagedObject.__init__(self, "FcpoolBootTarget", parent_mo_or_dn, **kwargs)
