"""This module contains the general information for SysdebugLogControlModule ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SysdebugLogControlModuleConsts:
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
    RESET_FALSE = "false"
    RESET_NO = "no"
    RESET_TRUE = "true"
    RESET_YES = "yes"


class SysdebugLogControlModule(ManagedObject):
    """This is SysdebugLogControlModule class."""

    consts = SysdebugLogControlModuleConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("SysdebugLogControlModule", "sysdebugLogControlModule", "module-[name]", VersionMeta.Version101e, "InputOutput", 0x1ff, [], ["admin", "operations"], ['sysdebugLogControlDomain'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "default_level": MoPropertyMeta("default_level", "defaultLevel", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["crit", "debug0", "debug1", "debug2", "debug3", "debug4", "info", "major", "minor", "warn"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "level": MoPropertyMeta("level", "level", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["crit", "debug0", "debug1", "debug2", "debug3", "debug4", "info", "major", "minor", "warn"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, 1, 510, None, [], []),
        "reset": MoPropertyMeta("reset", "reset", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "defaultLevel": "default_level", 
        "dn": "dn", 
        "level": "level", 
        "name": "name", 
        "reset": "reset", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.default_level = None
        self.level = None
        self.reset = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "SysdebugLogControlModule", parent_mo_or_dn, **kwargs)
