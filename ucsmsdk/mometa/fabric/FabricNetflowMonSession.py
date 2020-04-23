"""This module contains the general information for FabricNetflowMonSession ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricNetflowMonSessionConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    ID_A = "A"
    ID_B = "B"
    ID_NONE = "NONE"
    IS_CONFIG_SUCCESS_FALSE = "false"
    IS_CONFIG_SUCCESS_NO = "no"
    IS_CONFIG_SUCCESS_TRUE = "true"
    IS_CONFIG_SUCCESS_YES = "yes"
    PROTOCOL_NETFLOW = "netflow"


class FabricNetflowMonSession(ManagedObject):
    """This is FabricNetflowMonSession class."""

    consts = FabricNetflowMonSessionConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricNetflowMonSession", "fabricNetflowMonSession", "netflow-mon-[name]", VersionMeta.Version221b, "InputOutput", 0x1ff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricEthLanFlowMonitoring'], ['fabricNetflowMonSrcRef', 'fabricNetflowMonitorRef', 'faultInst'], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "config_fail_reason": MoPropertyMeta("config_fail_reason", "configFailReason", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|record-unresolved|source-vlan-unresolved|monitor-unresolved|exporter-unresolved|exporter-profile-unresolved|collector-unresolved),){0,7}(defaultValue|not-applicable|record-unresolved|source-vlan-unresolved|monitor-unresolved|exporter-unresolved|exporter-profile-unresolved|collector-unresolved){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version221b, MoPropertyMeta.CREATE_ONLY, 0x20, None, None, None, ["A", "B", "NONE"], []),
        "is_config_success": MoPropertyMeta("is_config_success", "isConfigSuccess", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []),
        "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["netflow"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "session": MoPropertyMeta("session", "session", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-255"]),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "configFailReason": "config_fail_reason", 
        "configQualifier": "config_qualifier", 
        "descr": "descr", 
        "dn": "dn", 
        "id": "id", 
        "isConfigSuccess": "is_config_success", 
        "locale": "locale", 
        "name": "name", 
        "protocol": "protocol", 
        "rn": "rn", 
        "sacl": "sacl", 
        "session": "session", 
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
        self.config_qualifier = None
        self.descr = None
        self.id = None
        self.is_config_success = None
        self.locale = None
        self.protocol = None
        self.sacl = None
        self.session = None
        self.status = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "FabricNetflowMonSession", parent_mo_or_dn, **kwargs)
