"""This module contains the general information for ExtmgmtIf ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ExtmgmtIfConsts:
    ID_A = "A"
    ID_B = "B"
    ID_NONE = "NONE"
    IF_ROLE_DIAG = "diag"
    IF_ROLE_FCOE_NAS_STORAGE = "fcoe-nas-storage"
    IF_ROLE_FCOE_STORAGE = "fcoe-storage"
    IF_ROLE_FCOE_UPLINK = "fcoe-uplink"
    IF_ROLE_MGMT = "mgmt"
    IF_ROLE_MONITOR = "monitor"
    IF_ROLE_NAS_STORAGE = "nas-storage"
    IF_ROLE_NETWORK = "network"
    IF_ROLE_NETWORK_FCOE_UPLINK = "network-fcoe-uplink"
    IF_ROLE_SERVER = "server"
    IF_ROLE_SERVICE = "service"
    IF_ROLE_STORAGE = "storage"
    IF_ROLE_UNKNOWN = "unknown"
    IF_TYPE_AGGREGATION = "aggregation"
    IF_TYPE_PHYSICAL = "physical"
    IF_TYPE_UNKNOWN = "unknown"
    IF_TYPE_VIRTUAL = "virtual"
    LAST_OPER_STATE_REPORT_DOWN = "down"
    LAST_OPER_STATE_REPORT_UNKNOWN = "unknown"
    LAST_OPER_STATE_REPORT_UP = "up"
    OPER_STATE_DOWN = "down"
    OPER_STATE_UNKNOWN = "unknown"
    OPER_STATE_UP = "up"


class ExtmgmtIf(ManagedObject):
    """This is ExtmgmtIf class."""

    consts = ExtmgmtIfConsts()
    naming_props = set([])

    mo_meta = MoMeta("ExtmgmtIf", "extmgmtIf", "extmgmt-intf", VersionMeta.Version141i, "InputOutput", 0x3ff, [], ["admin"], ['networkElement'], ['faultInst'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "fail_report_count": MoPropertyMeta("fail_report_count", "failReportCount", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["A", "B", "NONE"], []),
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []),
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []),
        "last_oper_state_report": MoPropertyMeta("last_oper_state_report", "lastOperStateReport", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["down", "unknown", "up"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["down", "unknown", "up"], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "failReportCount": "fail_report_count", 
        "fltAggr": "flt_aggr", 
        "id": "id", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "lastOperStateReport": "last_oper_state_report", 
        "locale": "locale", 
        "name": "name", 
        "operState": "oper_state", 
        "peerDn": "peer_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.ep_dn = None
        self.fail_report_count = None
        self.flt_aggr = None
        self.id = None
        self.if_role = None
        self.if_type = None
        self.last_oper_state_report = None
        self.locale = None
        self.name = None
        self.oper_state = None
        self.peer_dn = None
        self.sacl = None
        self.status = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "ExtmgmtIf", parent_mo_or_dn, **kwargs)
