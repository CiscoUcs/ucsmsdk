"""This module contains the general information for SysdebugMEpLog ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SysdebugMEpLogConsts:
    ADMIN_STATE_BACKUP = "backup"
    ADMIN_STATE_CLEAR = "clear"
    ADMIN_STATE_POLICY = "policy"
    CAPACITY_AVAILABLE = "available"
    CAPACITY_FULL = "full"
    CAPACITY_LOW = "low"
    CAPACITY_UNKNOWN = "unknown"
    CAPACITY_VERY_LOW = "very-low"
    LAST_UPDATE_NEVER = "never"
    OPER_STATE_BMC_COMMUNICATION_ERROR = "bmc-communication-error"
    OPER_STATE_INTERNAL_UCSM_ERROR = "internal-ucsm-error"
    OPER_STATE_OK = "ok"
    OPER_STATE_PERMISSION_DENIED_ERROR = "permission-denied-error"
    OPER_STATE_REMOTE_COMMUNICATION_ERROR = "remote-communication-error"
    TYPE_OBFL = "OBFL"
    TYPE_SEL = "SEL"
    TYPE_SYSLOG = "Syslog"


class SysdebugMEpLog(ManagedObject):
    """This is SysdebugMEpLog class."""

    consts = SysdebugMEpLogConsts()
    naming_props = set(['type', 'id'])

    mo_meta = MoMeta("SysdebugMEpLog", "sysdebugMEpLog", "log-[type]-[id]", VersionMeta.Version101e, "InputOutput", 0xff, [], ["admin", "operations"], ['mgmtController'], ['faultInst'], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["backup", "clear", "policy"], []),
        "capacity": MoPropertyMeta("capacity", "capacity", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["available", "full", "low", "unknown", "very-low"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "byte", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["0-8"]),
        "last_update": MoPropertyMeta("last_update", "lastUpdate", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["bmc-communication-error", "internal-ucsm-error", "ok", "permission-denied-error", "remote-communication-error"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x80, None, None, None, ["OBFL", "SEL", "Syslog"], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "capacity": "capacity", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "lastUpdate": "last_update", 
        "operState": "oper_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, id, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.id = id
        self.admin_state = None
        self.capacity = None
        self.child_action = None
        self.last_update = None
        self.oper_state = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "SysdebugMEpLog", parent_mo_or_dn, **kwargs)
