"""This module contains the general information for SwNetflowMonitor ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwNetflowMonitorConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    IS_VALID_CONFIG_INCOMPLETE = "incomplete"
    IS_VALID_CONFIG_OK = "ok"
    LIFE_CYCLE_DELETED = "deleted"
    LIFE_CYCLE_NEW = "new"
    LIFE_CYCLE_NORMAL = "normal"
    PROTOCOL_NETFLOW = "netflow"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class SwNetflowMonitor(ManagedObject):
    """This is SwNetflowMonitor class."""

    consts = SwNetflowMonitorConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("SwNetflowMonitor", "swNetflowMonitor", "flowmonitor-netflow-[name]", VersionMeta.Version221b, "InputOutput", 0x7f, [], ["read-only"], ['swEthLanFlowMon', 'swNetflowMonSession'], ['swNFExporterRef'], [None])

    prop_meta = {
        "active_timeout": MoPropertyMeta("active_timeout", "activeTimeout", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "flow_record_def_name": MoPropertyMeta("flow_record_def_name", "flowRecordDefName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "inactive_timeout": MoPropertyMeta("inactive_timeout", "inactiveTimeout", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "is_valid_config": MoPropertyMeta("is_valid_config", "isValidConfig", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["incomplete", "ok"], []),
        "life_cycle": MoPropertyMeta("life_cycle", "lifeCycle", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deleted", "new", "normal"], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["netflow"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "activeTimeout": "active_timeout", 
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "flowRecordDefName": "flow_record_def_name", 
        "inactiveTimeout": "inactive_timeout", 
        "isValidConfig": "is_valid_config", 
        "lifeCycle": "life_cycle", 
        "name": "name", 
        "peerDn": "peer_dn", 
        "protocol": "protocol", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.active_timeout = None
        self.admin_state = None
        self.child_action = None
        self.flow_record_def_name = None
        self.inactive_timeout = None
        self.is_valid_config = None
        self.life_cycle = None
        self.peer_dn = None
        self.protocol = None
        self.sacl = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "SwNetflowMonitor", parent_mo_or_dn, **kwargs)
