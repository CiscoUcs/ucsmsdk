"""This module contains the general information for MgmtPmonEntry ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtPmonEntryConsts:
    STATE_ERROR = "error"
    STATE_EXIT_PENDING = "exit_pending"
    STATE_FAILED = "failed"
    STATE_IDLE = "idle"
    STATE_KILLED = "killed"
    STATE_PENDING = "pending"
    STATE_RUNNING = "running"
    STATE_TERMINATED = "terminated"
    STATE_UNKNOWN = "unknown"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class MgmtPmonEntry(ManagedObject):
    """This is MgmtPmonEntry class."""

    consts = MgmtPmonEntryConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("MgmtPmonEntry", "mgmtPmonEntry", "[name]", VersionMeta.Version201m, "InputOutput", 0x3f, [], ["read-only"], ['mgmtEntity'], ['faultInst'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "exit_signal": MoPropertyMeta("exit_signal", "exitSignal", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "full_pathname": MoPropertyMeta("full_pathname", "fullPathname", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "heap_size": MoPropertyMeta("heap_size", "heapSize", "ulong", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "heap_size16_gb": MoPropertyMeta("heap_size16_gb", "heapSize16Gb", "ulong", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "last_exit_code": MoPropertyMeta("last_exit_code", "lastExitCode", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "max_retries": MoPropertyMeta("max_retries", "maxRetries", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "retries": MoPropertyMeta("retries", "retries", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "spurious_retries": MoPropertyMeta("spurious_retries", "spuriousRetries", "uint", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["error", "exit_pending", "failed", "idle", "killed", "pending", "running", "terminated", "unknown"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "working_directory": MoPropertyMeta("working_directory", "workingDirectory", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "exitSignal": "exit_signal", 
        "fullPathname": "full_pathname", 
        "heapSize": "heap_size", 
        "heapSize16Gb": "heap_size16_gb", 
        "lastExitCode": "last_exit_code", 
        "maxRetries": "max_retries", 
        "name": "name", 
        "retries": "retries", 
        "rn": "rn", 
        "sacl": "sacl", 
        "spuriousRetries": "spurious_retries", 
        "state": "state", 
        "status": "status", 
        "switchId": "switch_id", 
        "workingDirectory": "working_directory", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.exit_signal = None
        self.full_pathname = None
        self.heap_size = None
        self.heap_size16_gb = None
        self.last_exit_code = None
        self.max_retries = None
        self.retries = None
        self.sacl = None
        self.spurious_retries = None
        self.state = None
        self.status = None
        self.switch_id = None
        self.working_directory = None

        ManagedObject.__init__(self, "MgmtPmonEntry", parent_mo_or_dn, **kwargs)
