"""This module contains the general information for CallhomeTestAlert ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CallhomeTestAlertConsts:
    GROUP_DIAGNOSTIC = "diagnostic"
    GROUP_ENVIRONMENTAL = "environmental"
    GROUP_UNKNOWN = "unknown"
    LEVEL_CRITICAL = "critical"
    LEVEL_DEBUG = "debug"
    LEVEL_FATAL = "fatal"
    LEVEL_MAJOR = "major"
    LEVEL_MINOR = "minor"
    LEVEL_NORMAL = "normal"
    LEVEL_NOTIFY = "notify"
    LEVEL_UNKNOWN = "unknown"
    LEVEL_WARNING = "warning"
    MESSAGE_SUBTYPE_DELTA = "delta"
    MESSAGE_SUBTYPE_FULL = "full"
    MESSAGE_SUBTYPE_GOLDMAJOR = "goldmajor"
    MESSAGE_SUBTYPE_GOLDMINOR = "goldminor"
    MESSAGE_SUBTYPE_GOLDNORMAL = "goldnormal"
    MESSAGE_SUBTYPE_MAJOR = "major"
    MESSAGE_SUBTYPE_MINOR = "minor"
    MESSAGE_SUBTYPE_NOSUBTYPE = "nosubtype"
    MESSAGE_SUBTYPE_TEST = "test"
    MESSAGE_SUBTYPE_UNKNOWN = "unknown"
    MESSAGE_TYPE_CONF = "conf"
    MESSAGE_TYPE_DIAG = "diag"
    MESSAGE_TYPE_ENV = "env"
    MESSAGE_TYPE_INVENTORY = "inventory"
    MESSAGE_TYPE_SYSLOG = "syslog"
    MESSAGE_TYPE_TELEMETRY = "telemetry"
    MESSAGE_TYPE_TEST = "test"
    MESSAGE_TYPE_UNKNOWN = "unknown"
    SEND_NOW_FALSE = "false"
    SEND_NOW_NO = "no"
    SEND_NOW_TRUE = "true"
    SEND_NOW_YES = "yes"


class CallhomeTestAlert(ManagedObject):
    """This is CallhomeTestAlert class."""

    consts = CallhomeTestAlertConsts()
    naming_props = set([])

    mo_meta = MoMeta("CallhomeTestAlert", "callhomeTestAlert", "testalert", VersionMeta.Version101e, "InputOutput", 0x7ff, [], ["admin", "operations"], ['callhomeEp'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "group": MoPropertyMeta("group", "group", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["diagnostic", "environmental", "unknown"], []),
        "level": MoPropertyMeta("level", "level", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["critical", "debug", "fatal", "major", "minor", "normal", "notify", "unknown", "warning"], []),
        "message_subtype": MoPropertyMeta("message_subtype", "messageSubtype", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["delta", "full", "goldmajor", "goldminor", "goldnormal", "major", "minor", "nosubtype", "test", "unknown"], []),
        "message_type": MoPropertyMeta("message_type", "messageType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["conf", "diag", "env", "inventory", "syslog", "telemetry", "test", "unknown"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "send_now": MoPropertyMeta("send_now", "sendNow", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["false", "no", "true", "yes"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "description": "description", 
        "dn": "dn", 
        "group": "group", 
        "level": "level", 
        "messageSubtype": "message_subtype", 
        "messageType": "message_type", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sendNow": "send_now", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.description = None
        self.group = None
        self.level = None
        self.message_subtype = None
        self.message_type = None
        self.sacl = None
        self.send_now = None
        self.status = None

        ManagedObject.__init__(self, "CallhomeTestAlert", parent_mo_or_dn, **kwargs)
