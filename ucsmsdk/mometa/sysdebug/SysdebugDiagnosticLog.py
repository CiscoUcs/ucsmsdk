"""This module contains the general information for SysdebugDiagnosticLog ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SysdebugDiagnosticLogConsts:
    OPER_STATE_ALLOCATED = "allocated"
    OPER_STATE_CREATED = "created"
    OPER_STATE_UNKNOWN = "unknown"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class SysdebugDiagnosticLog(ManagedObject):
    """This is SysdebugDiagnosticLog class."""

    consts = SysdebugDiagnosticLogConsts()
    naming_props = set(['name', 'switchId'])

    mo_meta = MoMeta("SysdebugDiagnosticLog", "sysdebugDiagnosticLog", "diag-log-[name]-[switch_id]", VersionMeta.Version321d, "InputOutput", 0xff, [], ["admin", "operations"], ['computeBlade', 'computeRackUnit', 'computeServerUnit', 'sysdebugDiagnosticLogRepository'], [], ["Get", "Set"])

    prop_meta = {
        "checksum": MoPropertyMeta("checksum", "checksum", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version321d, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x10, 1, 128, None, [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "created", "unknown"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "size": MoPropertyMeta("size", "size", "ulong", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version321d, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version321d, MoPropertyMeta.NAMING, 0x80, None, None, None, ["A", "B", "NONE"], []),
        "tftp_uri": MoPropertyMeta("tftp_uri", "tftpUri", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "ts": MoPropertyMeta("ts", "ts", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "uri": MoPropertyMeta("uri", "uri", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
    }

    prop_map = {
        "checksum": "checksum", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "ip": "ip", 
        "name": "name", 
        "operState": "oper_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "size": "size", 
        "status": "status", 
        "switchId": "switch_id", 
        "tftpUri": "tftp_uri", 
        "ts": "ts", 
        "uri": "uri", 
    }

    def __init__(self, parent_mo_or_dn, name, switch_id, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.switch_id = switch_id
        self.checksum = None
        self.child_action = None
        self.descr = None
        self.ip = None
        self.oper_state = None
        self.sacl = None
        self.size = None
        self.status = None
        self.tftp_uri = None
        self.ts = None
        self.uri = None

        ManagedObject.__init__(self, "SysdebugDiagnosticLog", parent_mo_or_dn, **kwargs)
