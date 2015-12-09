"""This module contains the general information for SysdebugBackupBehavior ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class SysdebugBackupBehaviorConsts():
    CLEAR_ON_BACKUP_FALSE = "false"
    CLEAR_ON_BACKUP_NO = "no"
    CLEAR_ON_BACKUP_TRUE = "true"
    CLEAR_ON_BACKUP_YES = "yes"
    FORMAT_ASCII = "ascii"
    FORMAT_BINARY = "binary"
    INTERVAL_1HOUR = "1hour"
    INTERVAL_1MONTH = "1month"
    INTERVAL_1WEEK = "1week"
    INTERVAL_24HOURS = "24hours"
    INTERVAL_2HOURS = "2hours"
    INTERVAL_4HOURS = "4hours"
    INTERVAL_8HOURS = "8hours"
    INTERVAL_NEVER = "never"
    PROTO_FTP = "ftp"
    PROTO_HTTP = "http"
    PROTO_NFS_COPY = "nfs-copy"
    PROTO_NONE = "none"
    PROTO_SCP = "scp"
    PROTO_SFTP = "sftp"
    PROTO_TFTP = "tftp"


class SysdebugBackupBehavior(ManagedObject):
    """This is SysdebugBackupBehavior class."""

    consts = SysdebugBackupBehaviorConsts()
    naming_props = set([])

    mo_meta = MoMeta("SysdebugBackupBehavior", "sysdebugBackupBehavior", "backup", VersionMeta.Version111j, "InputOutput", 0x3fffL, [], ["admin", "operations"], [u'sysdebugMEpLogPolicy'], [], ["Get", "Set"])

    prop_meta = {
        "action": MoPropertyMeta("action", "action", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x2L, None, None, r"""((defaultValue|none|log-full|on-clear|timer|on-assoc-change),){0,5}(defaultValue|none|log-full|on-clear|timer|on-assoc-change){0,1}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "clear_on_backup": MoPropertyMeta("clear_on_backup", "clearOnBackup", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["false", "no", "true", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "format": MoPropertyMeta("format", "format", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["ascii", "binary"], []), 
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], []), 
        "interval": MoPropertyMeta("interval", "interval", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["1hour", "1month", "1week", "24hours", "2hours", "4hours", "8hours", "never"], []), 
        "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["ftp", "http", "nfs-copy", "none", "scp", "sftp", "tftp"], []), 
        "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x200L, 0, 64, None, [], []), 
        "remote_path": MoPropertyMeta("remote_path", "remotePath", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x400L, 1, 128, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x800L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x2000L, 0, 510, None, [], []), 
    }

    prop_map = {
        "action": "action", 
        "childAction": "child_action", 
        "clearOnBackup": "clear_on_backup", 
        "dn": "dn", 
        "format": "format", 
        "hostname": "hostname", 
        "interval": "interval", 
        "proto": "proto", 
        "pwd": "pwd", 
        "remotePath": "remote_path", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "user": "user", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.action = None
        self.child_action = None
        self.clear_on_backup = None
        self.format = None
        self.hostname = None
        self.interval = None
        self.proto = None
        self.pwd = None
        self.remote_path = None
        self.sacl = None
        self.status = None
        self.user = None

        ManagedObject.__init__(self, "SysdebugBackupBehavior", parent_mo_or_dn, **kwargs)

