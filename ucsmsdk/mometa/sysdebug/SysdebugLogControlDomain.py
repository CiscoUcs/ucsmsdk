"""This module contains the general information for SysdebugLogControlDomain ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SysdebugLogControlDomainConsts:
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
    LEVEL_FLAG_FALSE = "false"
    LEVEL_FLAG_NO = "no"
    LEVEL_FLAG_TRUE = "true"
    LEVEL_FLAG_YES = "yes"
    NAME_SYSMGMT = "sysmgmt"
    PERSIST_FALSE = "false"
    PERSIST_NO = "no"
    PERSIST_TRUE = "true"
    PERSIST_YES = "yes"
    RESET_FALSE = "false"
    RESET_NO = "no"
    RESET_TRUE = "true"
    RESET_YES = "yes"


class SysdebugLogControlDomain(ManagedObject):
    """This is SysdebugLogControlDomain class."""

    consts = SysdebugLogControlDomainConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("SysdebugLogControlDomain", "sysdebugLogControlDomain", "domain-[name]", VersionMeta.Version101e, "InputOutput", 0x3ff, [], ["admin", "operations"], ['sysdebugLogControlEp'], ['sysdebugLogControlDestinationFile', 'sysdebugLogControlDestinationSyslog', 'sysdebugLogControlModule'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "level": MoPropertyMeta("level", "level", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["crit", "debug0", "debug1", "debug2", "debug3", "debug4", "info", "major", "minor", "warn"], []),
        "level_flag": MoPropertyMeta("level_flag", "levelFlag", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20, None, None, None, ["sysmgmt"], []),
        "persist": MoPropertyMeta("persist", "persist", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["false", "no", "true", "yes"], []),
        "reset": MoPropertyMeta("reset", "reset", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["false", "no", "true", "yes"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "level": "level", 
        "levelFlag": "level_flag", 
        "name": "name", 
        "persist": "persist", 
        "reset": "reset", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.level = None
        self.level_flag = None
        self.persist = None
        self.reset = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "SysdebugLogControlDomain", parent_mo_or_dn, **kwargs)
