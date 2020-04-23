"""This module contains the general information for SysdebugLogControlDestinationFile ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SysdebugLogControlDestinationFileConsts:
    DEFAULT_LEVEL_CRIT = "crit"
    DEFAULT_LEVEL_DEBUG0 = "debug0"
    DEFAULT_LEVEL_DEBUG1 = "debug1"
    DEFAULT_LEVEL_DEBUG2 = "debug2"
    DEFAULT_LEVEL_DEBUG3 = "debug3"
    DEFAULT_LEVEL_DEBUG4 = "debug4"
    DEFAULT_LEVEL_INFO = "info"
    DEFAULT_LEVEL_MAJOR = "major"
    DEFAULT_LEVEL_MINOR = "minor"
    DEFAULT_LEVEL_WARN = "warn"
    LEVEL_CRIT = "crit"
    LEVEL_DEBUG0 = "debug0"
    LEVEL_DEBUG1 = "debug1"
    LEVEL_DEBUG2 = "debug2"
    LEVEL_DEBUG3 = "debug3"
    LEVEL_DEBUG4 = "debug4"
    LEVEL_INFO = "info"
    LEVEL_MAJOR = "major"
    LEVEL_MINOR = "minor"
    LEVEL_WARN = "warn"


class SysdebugLogControlDestinationFile(ManagedObject):
    """This is SysdebugLogControlDestinationFile class."""

    consts = SysdebugLogControlDestinationFileConsts()
    naming_props = set([])

    mo_meta = MoMeta("SysdebugLogControlDestinationFile", "sysdebugLogControlDestinationFile", "file", VersionMeta.Version101e, "InputOutput", 0x3ff, [], ["admin", "operations"], ['sysdebugLogControlDomain'], [], ["Get"])

    prop_meta = {
        "backup_count": MoPropertyMeta("backup_count", "backupCount", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["1-9"]),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "default_level": MoPropertyMeta("default_level", "defaultLevel", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["crit", "debug0", "debug1", "debug2", "debug3", "debug4", "info", "major", "minor", "warn"], []),
        "default_size": MoPropertyMeta("default_size", "defaultSize", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1000000-20000000"]),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "level": MoPropertyMeta("level", "level", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["crit", "debug0", "debug1", "debug2", "debug3", "debug4", "info", "major", "minor", "warn"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "size": MoPropertyMeta("size", "size", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["1000000-20000000"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "backupCount": "backup_count", 
        "childAction": "child_action", 
        "defaultLevel": "default_level", 
        "defaultSize": "default_size", 
        "dn": "dn", 
        "level": "level", 
        "rn": "rn", 
        "sacl": "sacl", 
        "size": "size", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.backup_count = None
        self.child_action = None
        self.default_level = None
        self.default_size = None
        self.level = None
        self.sacl = None
        self.size = None
        self.status = None

        ManagedObject.__init__(self, "SysdebugLogControlDestinationFile", parent_mo_or_dn, **kwargs)
