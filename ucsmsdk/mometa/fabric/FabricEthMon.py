"""This module contains the general information for FabricEthMon ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricEthMonConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    ID_A = "A"
    ID_B = "B"
    ID_NONE = "NONE"
    IS_CONFIG_SUCCESS_FALSE = "false"
    IS_CONFIG_SUCCESS_NO = "no"
    IS_CONFIG_SUCCESS_TRUE = "true"
    IS_CONFIG_SUCCESS_YES = "yes"
    OPER_STATE_DOWN = "down"
    OPER_STATE_ERROR = "error"
    OPER_STATE_UNKNOWN = "unknown"
    OPER_STATE_UP = "up"
    OPER_STATE_REASON_ARP_NOT_RESOLVED = "ARP_Not_Resolved"
    OPER_STATE_REASON_ACTIVE = "Active"
    OPER_STATE_REASON_EGRESS_IF_NOT_RESOLVED = "Egress_If_Not_Resolved"
    OPER_STATE_REASON_GENERIC_ERROR = "Generic_Error"
    OPER_STATE_REASON_MULTI_DESTINATION_NOT_ALLOWED = "Multi_Destination_Not_Allowed"
    OPER_STATE_REASON_NO_DESTINATION_CONFIGURED = "No_Destination_Configured"
    OPER_STATE_REASON_NO_ERSPAN_ID = "No_Erspan_Id"
    OPER_STATE_REASON_NO_HARDWARE_RESOURCE = "No_Hardware_Resource"
    OPER_STATE_REASON_NO_OPERATIONAL_SRC_DST = "No_Operational_Src_Dst"
    OPER_STATE_REASON_NO_ROUTE_TO_DEST_IP = "No_Route_To_Dest_IP"
    OPER_STATE_REASON_NO_SOURCE_DESTINATION_CONFIGURED = "No_Source_Destination_Configured"
    OPER_STATE_REASON_NO_SOURCES_CONFIGURED = "No_Sources_Configured"
    OPER_STATE_REASON_NO_VALID_IP_ADDRESS = "No_Valid_IP_Address"
    OPER_STATE_REASON_NO_VALID_ORIGIN_IP = "No_Valid_Origin_IP"
    OPER_STATE_REASON_NO_VALID_VRF = "No_Valid_VRF"
    OPER_STATE_REASON_SVI_NOT_RETRIVED = "SVI_Not_Retrived"
    OPER_STATE_REASON_SESSION_ADMIN_SHUT = "Session_Admin_Shut"
    OPER_STATE_REASON_UNKNOWN = "Unknown"
    OPER_STATE_REASON_WRONG_DESTINATION_MODE = "Wrong_Destination_Mode"
    OPER_STATE_REASON_WRONG_SOURCE_MODE = "Wrong_Source_Mode"
    SESSION_TYPE_ERSPAN_SOURCE = "erspan-source"
    SESSION_TYPE_SPAN_LOCAL = "span-local"
    SPAN_CTRL_PKTS_DISABLED = "disabled"
    SPAN_CTRL_PKTS_ENABLED = "enabled"


class FabricEthMon(ManagedObject):
    """This is FabricEthMon class."""

    consts = FabricEthMonConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricEthMon", "fabricEthMon", "eth-mon-[name]", VersionMeta.Version141i, "InputOutput", 0x3ff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricEthMonLan'], ['fabricEthMonDestEp', 'fabricEthMonFiltRef', 'fabricEthMonSrcRef', 'fabricRemoteConfig', 'fabricSubGroup', 'faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_fail_reason": MoPropertyMeta("config_fail_reason", "configFailReason", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version141i, MoPropertyMeta.CREATE_ONLY, 0x10, None, None, None, ["A", "B", "NONE"], []),
        "is_config_success": MoPropertyMeta("is_config_success", "isConfigSuccess", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["down", "error", "unknown", "up"], []),
        "oper_state_reason": MoPropertyMeta("oper_state_reason", "operStateReason", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ARP_Not_Resolved", "Active", "Egress_If_Not_Resolved", "Generic_Error", "Multi_Destination_Not_Allowed", "No_Destination_Configured", "No_Erspan_Id", "No_Hardware_Resource", "No_Operational_Src_Dst", "No_Route_To_Dest_IP", "No_Source_Destination_Configured", "No_Sources_Configured", "No_Valid_IP_Address", "No_Valid_Origin_IP", "No_Valid_VRF", "SVI_Not_Retrived", "Session_Admin_Shut", "Unknown", "Wrong_Destination_Mode", "Wrong_Source_Mode"], []),
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "session": MoPropertyMeta("session", "session", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-255"]),
        "session_type": MoPropertyMeta("session_type", "sessionType", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["erspan-source", "span-local"], []),
        "span_ctrl_pkts": MoPropertyMeta("span_ctrl_pkts", "spanCtrlPkts", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["disabled", "enabled"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "configFailReason": "config_fail_reason", 
        "dn": "dn", 
        "id": "id", 
        "isConfigSuccess": "is_config_success", 
        "locale": "locale", 
        "name": "name", 
        "operState": "oper_state", 
        "operStateReason": "oper_state_reason", 
        "peerDn": "peer_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "session": "session", 
        "sessionType": "session_type", 
        "spanCtrlPkts": "span_ctrl_pkts", 
        "status": "status", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_state = None
        self.child_action = None
        self.config_fail_reason = None
        self.id = None
        self.is_config_success = None
        self.locale = None
        self.oper_state = None
        self.oper_state_reason = None
        self.peer_dn = None
        self.sacl = None
        self.session = None
        self.session_type = None
        self.span_ctrl_pkts = None
        self.status = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "FabricEthMon", parent_mo_or_dn, **kwargs)
