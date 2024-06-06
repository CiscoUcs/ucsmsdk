"""This module contains the general information for SwNetflowMonSession ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwNetflowMonSessionConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    HAS_LAST_DEST_FALSE = "false"
    HAS_LAST_DEST_NO = "no"
    HAS_LAST_DEST_TRUE = "true"
    HAS_LAST_DEST_YES = "yes"
    LIFE_CYCLE_DELETED = "deleted"
    LIFE_CYCLE_NEW = "new"
    LIFE_CYCLE_NORMAL = "normal"
    PROTOCOL_NETFLOW = "netflow"
    SESSION_TYPE_ERSPAN_SOURCE = "erspan-source"
    SESSION_TYPE_SPAN_LOCAL = "span-local"
    SPAN_CTRL_PKTS_DISABLED = "disabled"
    SPAN_CTRL_PKTS_ENABLED = "enabled"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class SwNetflowMonSession(ManagedObject):
    """This is SwNetflowMonSession class."""

    consts = SwNetflowMonSessionConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("SwNetflowMonSession", "swNetflowMonSession", "flowmonsession-netflow-[name]", VersionMeta.Version221b, "InputOutput", 0x3ff, [], ["read-only"], ['swEthLanFlowMon'], ['swNetflowMonitor', 'swNetflowMonitorRef'], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "has_last_dest": MoPropertyMeta("has_last_dest", "hasLastDest", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "life_cycle": MoPropertyMeta("life_cycle", "lifeCycle", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deleted", "new", "normal"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["netflow"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "session": MoPropertyMeta("session", "session", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-255"]),
        "session_type": MoPropertyMeta("session_type", "sessionType", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["erspan-source", "span-local"], []),
        "span_ctrl_pkts": MoPropertyMeta("span_ctrl_pkts", "spanCtrlPkts", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["disabled", "enabled"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["A", "B", "NONE"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "hasLastDest": "has_last_dest", 
        "lifeCycle": "life_cycle", 
        "name": "name", 
        "peerDn": "peer_dn", 
        "protocol": "protocol", 
        "rn": "rn", 
        "sacl": "sacl", 
        "session": "session", 
        "sessionType": "session_type", 
        "spanCtrlPkts": "span_ctrl_pkts", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_state = None
        self.child_action = None
        self.has_last_dest = None
        self.life_cycle = None
        self.peer_dn = None
        self.protocol = None
        self.sacl = None
        self.session = None
        self.session_type = None
        self.span_ctrl_pkts = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "SwNetflowMonSession", parent_mo_or_dn, **kwargs)
